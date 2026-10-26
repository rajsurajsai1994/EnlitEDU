# -*- coding: utf-8 -*-
"""Deployment files generated from ONE redirect map, so every host behaves the same:
   vercel.json + .vercelignore (Vercel, the GitHub-connected deployment),
   cloudfront-function-redirects.js (AWS S3 + CloudFront, the current live host),
   _redirects + _headers (Netlify / Cloudflare Pages) and .htaccess (Apache).
Also writes manifest.json and keeps the Google Search Console verification file."""
import os, json, shutil

HOST = "www.enlitedu.com"
IMG = "/assets/img/enlitedu/"

# 301 exact-path redirects: old site URLs, short links, renamed modules, folder URLs without an index page
EXACT = {
    # renamed modules (Oct 2026)
    "/articulate.html": "/transfer-credit-intelligence.html", "/articulate": "/transfer-credit-intelligence.html",
    "/transfer-credit": "/transfer-credit-intelligence.html", "/transfer-credit-evaluation": "/transfer-credit-intelligence.html",
    "/assess.html": "/freshman-intelligence.html", "/assess": "/freshman-intelligence.html",
    "/gpa-standardization": "/freshman-intelligence.html", "/freshman": "/freshman-intelligence.html",
    # marketing short links from the old site
    "/prior-learning": "/prior-learning-assessment.html", "/pla.html": "/prior-learning-assessment.html", "/pla": "/prior-learning-assessment.html", "/jst": "/veterans.html", "/athletics": "/athletics.html",
    "/demo": "/request-demo.html", "/book-a-demo": "/request-demo.html", "/dupmerge": "/contact.html",
    "/products": "/platform.html", "/products/": "/platform.html",
    # folders that have no index page of their own
    "/solutions": "/platform.html", "/solutions/": "/platform.html",
    "/who-we-serve": "/who-we-serve/community-colleges.html", "/who-we-serve/": "/who-we-serve/community-colleges.html",
    "/news": "/news/tennessee-board-of-regents-selects-lioraai.html", "/news/": "/news/tennessee-board-of-regents-selects-lioraai.html", "/tbr": "/news/tennessee-board-of-regents-selects-lioraai.html",
    "/case-studies/": "/case-studies.html", "/georgia/": "/georgia.html", "/blog/": "/blog.html", "/careers/": "/careers.html", "/jobs": "/careers.html", "/jobs/": "/careers.html",
    "/feed": "/blog.html", "/feed/": "/blog.html",
    # legacy WordPress posts
    "/uncategorized/data-integration-for-improving-academic-performance-tracking/": "/mobility.html",
    "/uncategorized/how-data-integration-improves-institutional-decision-making/": "/mobility.html",
    # browsers ask for this automatically
    "/favicon.ico": IMG + "favicon-32.png",
}
# 301 prefix redirects (legacy WordPress structure)
PREFIX = [("/uncategorized/", "/blog.html"), ("/category/", "/blog.html"), ("/tag/", "/blog.html"), ("/author/", "/about.html"),
          ("/2023/", "/blog.html"), ("/2024/", "/blog.html"), ("/2025/", "/blog.html")]
# paths that should simply 404 (WordPress probes)
GONE = ["/wp-admin/", "/wp-content/", "/wp-includes/", "/wp-login.php", "/xmlrpc.php"]

SEC_HEADERS = [("X-Content-Type-Options", "nosniff"), ("X-Frame-Options", "SAMEORIGIN"), ("Referrer-Policy", "strict-origin-when-cross-origin"),
               ("Permissions-Policy", "camera=(), microphone=(), geolocation=(), interest-cohort=()"),
               ("Strict-Transport-Security", "max-age=31536000; includeSubDomains; preload")]

def image_redirects(out, old_images_dir):
    """Old site served images from /images/; the same files now live in /assets/img/. Map each one that exists."""
    m = {}
    if not os.path.isdir(old_images_dir):
        return m
    index = {}
    for root, _, fs in os.walk(os.path.join(out, "assets", "img")):
        for f in fs:
            index.setdefault(f, "/" + os.path.relpath(os.path.join(root, f), out).replace(os.sep, "/"))
    for root, _, fs in os.walk(old_images_dir):
        for f in fs:
            old = "/images/" + os.path.relpath(os.path.join(root, f), old_images_dir).replace(os.sep, "/")
            m[old] = index.get(f, IMG + "favicon-192.png" if f.startswith("favicon") else IMG + "og-lioraai.jpg")
    return m

def write_all(out, old_site_dir=None):
    exact = dict(EXACT)
    if old_site_dir:
        exact.update(image_redirects(out, os.path.join(old_site_dir, "images")))
        g = os.path.join(old_site_dir, "google6a18e45d8fd24580.html")
        if os.path.exists(g):
            shutil.copyfile(g, os.path.join(out, "google6a18e45d8fd24580.html"))
    for src, dst in exact.items():  # every redirect target must exist
        f = dst.split("#")[0].lstrip("/") or "index.html"
        assert os.path.exists(os.path.join(out, f)), "redirect target missing: %s -> %s" % (src, dst)

    def w(name, text):
        with open(os.path.join(out, name), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)

    # ---------------------------------------------------------------- Vercel
    redirects = [{"source": "/:path*", "has": [{"type": "host", "value": "enlitedu.com"}], "destination": "https://%s/:path*" % HOST, "permanent": True}]
    redirects += [{"source": s, "destination": d, "permanent": True} for s, d in exact.items()]
    redirects += [{"source": p + ":path*", "destination": d, "permanent": True} for p, d in PREFIX]
    vercel = {
        "$schema": "https://openapi.vercel.sh/vercel.json",
        "cleanUrls": False, "trailingSlash": False,
        "redirects": redirects,
        # missing paths (incl. WordPress probes in GONE) get Vercel's real 404 with /404.html; a rewrite would answer 200
        "headers": [
            {"source": "/(.*)", "headers": [{"key": k, "value": v} for k, v in SEC_HEADERS]},
            {"source": "/assets/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]},
            {"source": "/(.*)\\.html", "headers": [{"key": "Cache-Control", "value": "public, max-age=3600, must-revalidate"}]},
            # preview deployments (*.vercel.app) must never be indexed; only www.enlitedu.com is canonical
            {"source": "/(.*)", "has": [{"type": "host", "value": "(?<sub>.*)\\.vercel\\.app"}], "headers": [{"key": "X-Robots-Tag", "value": "noindex, nofollow"}]},
        ],
    }
    w("vercel.json", json.dumps(vercel, indent=2) + "\n")
    w(".vercelignore", "# never publish build scripts, docs or repo metadata\n_build/\nREADME.md\n.git/\n.gitignore\n")

    # ---------------------------------------------------------------- CloudFront Function (viewer-request)
    js = """/**
 * CloudFront Function (JavaScript runtime 2.0), viewer-request. Generated by _build/deploy.py: do not edit by hand.
 *   1. apex -> www (301)   2. old URLs, short links, renamed modules (301)   3. /path -> /path.html, /dir/ -> /dir/index.html
 * Distribution settings this file can't do on its own:
 *   Error pages: 403 -> /404.html (response code 404) and 404 -> /404.html (response code 404). S3 returns 403 for
 *   missing files when the bucket is private, so BOTH must be mapped. 401 is never produced by a public static site.
 *   Response headers policy: HSTS, nosniff, SAMEORIGIN, strict-origin-when-cross-origin, Permissions-Policy.
 */
var HOST = '%s';
var EXACT = %s;
var PREFIX = %s;
var GONE = %s;

function redirect(loc) {
  return { statusCode: 301, statusDescription: 'Moved Permanently', headers: { location: { value: loc }, 'cache-control': { value: 'max-age=3600' } } };
}
function qs(q) {
  var k = Object.keys(q || {});
  return k.length ? '?' + k.map(function (n) { return n + (q[n].value ? '=' + q[n].value : ''); }).join('&') : '';
}
function handler(event) {
  var req = event.request, uri = req.uri;
  var host = (req.headers.host && req.headers.host.value) || HOST;
  if (host !== HOST) return redirect('https://' + HOST + uri + qs(req.querystring));
  if (EXACT[uri]) return redirect('https://' + HOST + EXACT[uri]);
  for (var i = 0; i < PREFIX.length; i++) if (uri.indexOf(PREFIX[i][0]) === 0) return redirect('https://' + HOST + PREFIX[i][1]);
  for (var j = 0; j < GONE.length; j++) if (uri.indexOf(GONE[j]) === 0) { req.uri = '/404-not-found'; return req; }
  if (uri.endsWith('/')) req.uri = uri + 'index.html';
  else if (uri.lastIndexOf('.') < uri.lastIndexOf('/')) req.uri = uri + '.html';
  return req;
}
""" % (HOST, json.dumps(exact, indent=2), json.dumps(PREFIX), json.dumps(GONE))
    w("cloudfront-function-redirects.js", js)

    # ---------------------------------------------------------------- Netlify / Cloudflare Pages
    r = ["# Generated by _build/deploy.py. Netlify / Cloudflare Pages format.",
         "http://enlitedu.com/*      https://%s/:splat  301!" % HOST, "https://enlitedu.com/*     https://%s/:splat  301!" % HOST,
         "http://%s/*  https://%s/:splat  301!" % (HOST, HOST)]
    r += ["%-60s %s  301" % (s, d) for s, d in exact.items()]
    r += ["%-60s %s  301" % (p + "*", d) for p, d in PREFIX]
    r += ["%-60s /404.html  404" % (g + ("*" if g.endswith("/") else "")) for g in GONE]
    w("_redirects", "\n".join(r) + "\n")
    w("_headers", "/*\n" + "".join("  %s: %s\n" % kv for kv in SEC_HEADERS)
      + "\n/assets/*\n  Cache-Control: public, max-age=31536000, immutable\n\n/*.html\n  Cache-Control: public, max-age=3600, must-revalidate\n")

    # ---------------------------------------------------------------- Apache
    esc = lambda p: p.lstrip("/").replace(".", "\\.")
    ht = ["# Generated by _build/deploy.py. Apache only (S3/CloudFront and Vercel ignore this file).",
          "Options -Indexes", "ErrorDocument 404 /404.html", "ErrorDocument 403 /404.html", "",
          "<IfModule mod_headers.c>"] + ['  Header always set %s "%s"' % kv for kv in SEC_HEADERS] + [
          '  <FilesMatch "\\.(css|js|jpg|jpeg|png|gif|webp|avif|svg|woff2?|ico)$">', '    Header set Cache-Control "public, max-age=31536000, immutable"', "  </FilesMatch>",
          '  <FilesMatch "\\.html$">', '    Header set Cache-Control "public, max-age=3600, must-revalidate"', "  </FilesMatch>", "</IfModule>", "",
          "<IfModule mod_rewrite.c>", "  RewriteEngine On",
          "  RewriteCond %{HTTPS} off [OR]", "  RewriteCond %{HTTP_HOST} !^www\\. [NC]", "  RewriteRule ^(.*)$ https://" + HOST + "/$1 [L,R=301]",
          "  RewriteRule ^_build/ - [R=404,L]"]
    ht += ["  RewriteRule ^%s$ %s [L,R=301]" % (esc(s), d) for s, d in exact.items()]
    ht += ["  RewriteRule ^%s %s [L,R=301]" % (esc(p), d) for p, d in PREFIX]
    ht += ["  RewriteRule ^%s - [R=404,L]" % esc(g) for g in GONE]
    ht += ["  RewriteCond %{REQUEST_FILENAME} !-d", "  RewriteCond %{REQUEST_FILENAME}.html -f", "  RewriteRule ^(.*)$ $1.html [L]", "</IfModule>"]
    w(".htaccess", "\n".join(ht) + "\n")

    # ---------------------------------------------------------------- web app manifest
    w("manifest.json", json.dumps({
        "name": "EnlitEDU - LioraAI", "short_name": "EnlitEDU",
        "description": "LioraAI transcript and credit evaluation software for colleges and universities across the U.S.",
        "start_url": "/", "display": "browser", "background_color": "#ffffff", "theme_color": "#0a1d3a",
        "icons": [{"src": IMG + "favicon-192.png", "sizes": "192x192", "type": "image/png"},
                  {"src": IMG + "favicon-512.png", "sizes": "512x512", "type": "image/png"},
                  {"src": IMG + "apple-touch-icon.png", "sizes": "180x180", "type": "image/png"}]}, indent=2) + "\n")
    return exact
