# -*- coding: utf-8 -*-
"""Deep structured-data + head audit.  python _build/schema_audit.py
Checks every JSON-LD node against Google / schema.org required and recommended properties,
@id references, breadcrumb URLs, FAQ text parity, speakable selectors, head tags and llms.txt links."""
import os, re, json, glob, html, collections, datetime

os.chdir(os.path.join(os.path.dirname(__file__), ".."))
BASE = "https://www.enlitedu.com"
files = sorted(f.replace(os.sep, "/") for f in glob.glob("**/*.html", recursive=True) if not f.startswith(("assets", "_build", "google")))
issues, warns, types = collections.defaultdict(list), collections.defaultdict(list), collections.Counter()

REQ = {  # required (error) / recommended (warning)
    "Organization": (["name", "url", "logo"], ["sameAs", "description", "address", "email", "contactPoint"]),
    "WebSite": (["name", "url"], ["publisher", "inLanguage"]),
    "WebPage": (["url", "name"], ["description", "isPartOf"]),
    "CollectionPage": (["url", "name"], ["description"]),
    "AboutPage": (["url", "name"], []), "ContactPage": (["url", "name"], []), "FAQPage": (["mainEntity"], []),
    "BreadcrumbList": (["itemListElement"], []),
    "BlogPosting": (["headline", "image", "datePublished", "author", "publisher"], ["dateModified", "description", "mainEntityOfPage"]),
    "Article": (["headline", "image", "datePublished", "author", "publisher"], ["dateModified", "description"]),
    "SoftwareApplication": (["name", "applicationCategory"], ["operatingSystem", "offers", "description"]),
    "Service": (["name", "provider"], ["areaServed", "serviceType", "description"]),
    "HowTo": (["name", "step"], ["description"]),
    "VideoObject": (["name", "description", "thumbnailUrl", "uploadDate"], ["embedUrl", "contentUrl", "duration"]),
    "DefinedTermSet": (["name", "hasDefinedTerm"], []), "Blog": (["name", "url"], []),
    "ItemList": (["itemListElement"], []),
    "JobPosting": (["title", "description", "datePosted", "hiringOrganization"], ["validThrough", "employmentType", "applicantLocationRequirements", "directApply", "identifier"]),
}

def nodes_of(g):
    out = []
    def walk(x):
        if isinstance(x, dict):
            out.append(x); [walk(v) for v in x.values()]
        elif isinstance(x, list):
            [walk(v) for v in x]
    walk(g); return out

def local(url):
    if not url.startswith(BASE): return None
    p = url[len(BASE):].split("#")[0].lstrip("/")
    return p or "index.html"

def iso(s):
    try: datetime.date.fromisoformat(s[:10]); return True
    except Exception: return False

for f in files:
    t = open(f, encoding="utf-8").read()
    head = t.split("</head>")[0]
    noidx = "noindex" in re.search(r'<meta name="robots" content="([^"]*)"', t).group(1)
    canon = re.search(r'<link rel="canonical" href="([^"]+)"', t).group(1)
    if '<html lang="en' not in t: issues[f].append("html lang missing")
    if 'name="viewport"' not in head: issues[f].append("no viewport")
    ogi = re.search(r'property="og:image" content="([^"]+)"', head)
    if ogi and "unsplash" in ogi.group(1) and not re.search(r"[?&]h=\d+", ogi.group(1)): warns[f].append("og:image not cropped to 1200x630")
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S)
    if not blocks and not noidx: issues[f].append("no JSON-LD")
    defined, refs = {}, []
    for b in blocks:
        g = json.loads(b)
        if g.get("@context") not in ("https://schema.org", "https://schema.org/"): issues[f].append("bad @context")
        for n in g.get("@graph", [g]):
            ty = n.get("@type"); tys = ty if isinstance(ty, list) else [ty]
            for x in tys: types[x] += 1
            if "@id" in n:
                if n["@id"] in defined and defined[n["@id"]] != tys: issues[f].append("conflicting @id " + n["@id"])
                defined[n["@id"]] = tys
            for x in tys:
                req, rec = REQ.get(x, ([], []))
                miss = [k for k in req if not n.get(k)]
                if miss: issues[f].append("%s missing %s" % (x, miss))
                missr = [k for k in rec if not n.get(k)]
                if missr: warns[f].append("%s lacks %s" % (x, missr))
            if "BreadcrumbList" in tys:
                els = n["itemListElement"]
                if [e["position"] for e in els] != list(range(1, len(els) + 1)): issues[f].append("breadcrumb positions")
                for e in els:
                    it = e.get("item"); it = it.get("@id") if isinstance(it, dict) else it
                    if it and local(it) and not os.path.exists(local(it)): issues[f].append("breadcrumb dead " + it)
                last = els[-1].get("item"); last = last.get("@id") if isinstance(last, dict) else last
                if last and last.split("#")[0] != canon: issues[f].append("breadcrumb last %s != canonical" % last)
            if "FAQPage" in tys:
                vis_q = [html.unescape(re.sub(r"<[^>]+>", "", q)).strip() for q in re.findall(r'class="faq-q"[^>]*>(.*?)<span class="pm"', t, re.S)]
                vis_q += [html.unescape(q).strip() for q in re.findall(r'<p class="q">(.*?)</p>', t, re.S)]
                for q in n["mainEntity"]:
                    if q.get("@type") != "Question" or not q.get("acceptedAnswer", {}).get("text"): issues[f].append("FAQ item malformed")
                    if html.unescape(q["name"]).strip() not in vis_q: issues[f].append("FAQ schema question not visible: " + q["name"][:60])
            if set(tys) & {"BlogPosting", "Article"}:
                if len(n.get("headline", "")) > 110: issues[f].append("headline > 110 chars")
                if not (iso(n.get("datePublished", "")) and iso(n.get("dateModified", n.get("datePublished", "")))): issues[f].append("bad dates")
                if n.get("dateModified", "") < n.get("datePublished", ""): issues[f].append("modified before published")
                if n.get("mainEntityOfPage") and n["mainEntityOfPage"] != canon: issues[f].append("mainEntityOfPage != canonical")
            sp = n.get("speakable", {}).get("cssSelector", []) if isinstance(n.get("speakable"), dict) else []
            for sel in sp:
                if sel.startswith(".") and not re.search(r'class="[^"]*\b%s\b' % re.escape(sel.split()[-1].lstrip(".")), t): issues[f].append("speakable selector absent " + sel)
        for x in nodes_of(g):
            if list(x.keys()) == ["@id"]: refs.append(x["@id"])
    for r in refs:
        if r not in defined and not r.endswith("/blog.html#blog"): issues[f].append("dangling @id ref " + r)
    for m in re.finditer(r'"(https://www\.enlitedu\.com/[^"#]*)', " ".join(blocks)):
        p = local(m.group(1))
        if p and not p.endswith((".png", ".jpg", ".webp", ".svg", ".txt", ".xml")) and not os.path.exists(p): issues[f].append("schema URL dead " + m.group(1))

# llms.txt links
for u in re.findall(r"\]\((https://www\.enlitedu\.com/[^)]+)\)", open("llms.txt", encoding="utf-8").read()):
    if not os.path.exists(local(u)): issues["llms.txt"].append("dead " + u)
# sitemap sanity
sm = open("sitemap.xml", encoding="utf-8").read()
for u in re.findall(r"<loc>([^<]+)</loc>", sm):
    if not os.path.exists(local(u)): issues["sitemap.xml"].append("dead " + u)
rb = open("robots.txt", encoding="utf-8").read()
for bot in ("GPTBot", "ClaudeBot", "PerplexityBot", "Google-Extended", "OAI-SearchBot", "Bingbot"):
    if "User-agent: %s\nAllow: /" % bot not in rb: issues["robots.txt"].append(bot + " not allowed")

print("SCHEMA TYPES (node count):", dict(types.most_common()))
print("\nERRORS:", "none" if not issues else "")
for f, v in issues.items(): print(" ", f, "->", sorted(set(v)))
print("\nWARNINGS (recommended properties):")
agg = collections.Counter(w for v in warns.values() for w in set(v))
for w, c in agg.most_common(): print("  %3d pages: %s" % (c, w))
