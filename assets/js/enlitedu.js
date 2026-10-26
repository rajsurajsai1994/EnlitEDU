/* EnlitEDU site behaviour. No jQuery needed; uses the template's Swiper + AOS. */
(function () {
  "use strict";
  var doc = document.documentElement;
  doc.classList.remove("no-js");
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- sticky header shadow + back-to-top ---------- */
  var header = document.querySelector(".site-header");
  var toTop = document.querySelector(".to-top");
  function onScroll() {
    var y = window.scrollY || 0;
    if (header) header.classList.toggle("scrolled", y > 10);
    if (toTop) toTop.classList.toggle("show", y > 700);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
  if (toTop) toTop.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: reduce ? "auto" : "smooth" }); });

  /* ---------- mega menu ---------- */
  var items = document.querySelectorAll(".nav-main > li.has-mega");
  function closeAll(except) {
    items.forEach(function (li) {
      if (li !== except) {
        li.classList.remove("open");
        var b = li.querySelector(":scope > button");
        if (b) b.setAttribute("aria-expanded", "false");
      }
    });
  }
  items.forEach(function (li) {
    var btn = li.querySelector(":scope > button");
    var timer;
    btn.addEventListener("click", function (e) {
      e.preventDefault();
      var open = !li.classList.contains("open");
      closeAll(li);
      li.classList.toggle("open", open);
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
    li.addEventListener("mouseenter", function () {
      if (window.innerWidth < 1061) return;
      clearTimeout(timer);
      closeAll(li);
      li.classList.add("open");
      btn.setAttribute("aria-expanded", "true");
    });
    li.addEventListener("mouseleave", function () {
      if (window.innerWidth < 1061) return;
      timer = setTimeout(function () {
        li.classList.remove("open");
        btn.setAttribute("aria-expanded", "false");
      }, 160);
    });
  });
  document.addEventListener("click", function (e) { if (!e.target.closest(".nav-main")) closeAll(); });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") { closeAll(); closeDrawer(); closeVideo(); }
  });

  /* ---------- scroll lock (drawer + video): pin the page so the background cannot scroll, incl. iOS ---------- */
  var lockY = 0, locks = 0;
  function lockScroll() {
    if (locks++) return;
    lockY = window.scrollY || 0;
    var b = document.body.style;
    b.position = "fixed"; b.top = -lockY + "px"; b.left = "0"; b.right = "0"; b.width = "100%"; b.overflow = "hidden";
    doc.classList.add("scroll-locked");
  }
  function unlockScroll() {
    if (!locks || --locks) return;
    var b = document.body.style;
    b.position = b.top = b.left = b.right = b.width = b.overflow = "";
    doc.classList.remove("scroll-locked");
    window.scrollTo(0, lockY);
  }

  /* ---------- "you are here": highlight the current page in the mega menus and the mobile menu ---------- */
  var here = location.pathname.replace(/index\.html$/, "");
  document.querySelectorAll(".mega a[href], .drawer a[href]").forEach(function (a) {
    var p = a.pathname ? a.pathname.replace(/index\.html$/, "") : "";
    if (p && p === here && !a.hash) {
      a.classList.add("is-current"); a.setAttribute("aria-current", "page");
      var det = a.closest("details"); if (det) { det.classList.add("has-current"); det.open = true; }
    }
  });

  /* ---------- mobile drawer ---------- */
  var drawer = document.querySelector(".drawer");
  var burger = document.querySelector(".burger");
  function openDrawer() {
    if (!drawer) return;
    drawer.classList.add("open");
    drawer.setAttribute("aria-hidden", "false");
    if (burger) burger.setAttribute("aria-expanded", "true");
    lockScroll();
    var c = drawer.querySelector(".close"); if (c) c.focus();
  }
  function closeDrawer() {
    if (!drawer || !drawer.classList.contains("open")) return;
    drawer.classList.remove("open");
    drawer.setAttribute("aria-hidden", "true");
    if (burger) { burger.setAttribute("aria-expanded", "false"); burger.focus(); }
    unlockScroll();
  }
  if (burger) burger.addEventListener("click", openDrawer);
  if (drawer) {
    drawer.querySelector(".scrim").addEventListener("click", closeDrawer);
    drawer.querySelector(".close").addEventListener("click", closeDrawer);
  }

  /* ---------- tabs ---------- */
  document.querySelectorAll("[data-tabs]").forEach(function (wrap) {
    var btns = wrap.querySelectorAll('[role="tab"]');
    var panels = wrap.querySelectorAll('[role="tabpanel"]');
    function select(i, focus) {
      btns.forEach(function (b, j) {
        var on = i === j;
        b.setAttribute("aria-selected", on ? "true" : "false");
        b.tabIndex = on ? 0 : -1;
        panels[j].classList.toggle("active", on);
        panels[j].hidden = !on;
      });
      if (focus) btns[i].focus();
    }
    btns.forEach(function (b, i) {
      b.addEventListener("click", function () { select(i); });
      b.addEventListener("keydown", function (e) {
        if (e.key === "ArrowRight") { e.preventDefault(); select((i + 1) % btns.length, true); }
        if (e.key === "ArrowLeft") { e.preventDefault(); select((i - 1 + btns.length) % btns.length, true); }
      });
    });
  });

  /* ---------- expanding tiles ---------- */
  document.querySelectorAll(".tiles").forEach(function (wrap) {
    var tiles = wrap.querySelectorAll(".tile");
    tiles.forEach(function (t) {
      function act() {
        tiles.forEach(function (x) { x.classList.remove("active"); x.setAttribute("aria-expanded", "false"); });
        t.classList.add("active"); t.setAttribute("aria-expanded", "true");
      }
      t.addEventListener("click", act);
      t.addEventListener("focus", act);
      t.addEventListener("mouseenter", function () { if (window.innerWidth > 991) act(); });
    });
  });

  /* ---------- FAQ accordion ---------- */
  document.querySelectorAll(".faq-item").forEach(function (item) {
    var q = item.querySelector(".faq-q");
    q.addEventListener("click", function () {
      var open = !item.classList.contains("open");
      var group = item.closest(".faq-wrap");
      if (group) group.querySelectorAll(".faq-item.open").forEach(function (o) {
        if (o !== item) { o.classList.remove("open"); o.querySelector(".faq-q").setAttribute("aria-expanded", "false"); }
      });
      item.classList.toggle("open", open);
      q.setAttribute("aria-expanded", open ? "true" : "false");
    });
  });

  /* ---------- counters ---------- */
  var counters = document.querySelectorAll("[data-count]");
  function runCounter(el) {
    var end = parseFloat(el.getAttribute("data-count"));
    var dec = (el.getAttribute("data-count").split(".")[1] || "").length;
    if (reduce) { el.textContent = end.toFixed(dec); return; }
    var start = null, dur = 1600;
    function step(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var v = end * (1 - Math.pow(1 - p, 3));
      el.textContent = v.toFixed(dec);
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { runCounter(en.target); io.unobserve(en.target); } });
    }, { threshold: 0.4 });
    counters.forEach(function (c) { io.observe(c); });
  }

  /* ---------- video modal (YouTube, privacy-enhanced) ---------- */
  var modal = document.querySelector(".vmodal");
  var lastFocus = null;
  function openVideo(id, start) {
    if (!modal) return;
    lastFocus = document.activeElement;
    var src = "https://www.youtube-nocookie.com/embed/" + encodeURIComponent(id) + "?autoplay=1&rel=0" + (start ? "&start=" + parseInt(start, 10) : "");
    modal.querySelector(".box").insertAdjacentHTML("beforeend", '<iframe src="' + src + '" title="Video" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe>');
    modal.classList.add("open");
    modal.querySelector(".x").focus();
    lockScroll();
  }
  function closeVideo() {
    if (!modal || !modal.classList.contains("open")) return;
    var f = modal.querySelector("iframe"); if (f) f.remove();
    modal.classList.remove("open");
    unlockScroll();
    if (lastFocus) lastFocus.focus();
  }
  document.addEventListener("click", function (e) {
    var t = e.target.closest("[data-video]");
    if (t) { e.preventDefault(); openVideo(t.getAttribute("data-video"), t.getAttribute("data-start")); }
  });
  if (modal) {
    modal.addEventListener("click", function (e) { if (e.target === modal) closeVideo(); });
    modal.querySelector(".x").addEventListener("click", closeVideo);
  }

  /* ---------- filters (blog, stories) ---------- */
  document.querySelectorAll("[data-filter-group]").forEach(function (bar) {
    var target = document.querySelector(bar.getAttribute("data-filter-group"));
    if (!target) return;
    bar.querySelectorAll("button").forEach(function (b) {
      b.addEventListener("click", function () {
        bar.querySelectorAll("button").forEach(function (x) { x.setAttribute("aria-pressed", "false"); });
        b.setAttribute("aria-pressed", "true");
        var f = b.getAttribute("data-filter");
        target.querySelectorAll("[data-tags]").forEach(function (card) {
          var show = f === "all" || (" " + card.getAttribute("data-tags") + " ").indexOf(" " + f + " ") > -1;
          card.hidden = !show;
        });
      });
    });
  });

  /* ---------- Swiper carousels ---------- */
  if (window.Swiper) {
    document.querySelectorAll("[data-swiper]").forEach(function (el) {
      var id = el.getAttribute("data-swiper");
      new window.Swiper(el, {
        slidesPerView: 1.1,
        spaceBetween: 18,
        grabCursor: true,
        navigation: { nextEl: '[data-next="' + id + '"]', prevEl: '[data-prev="' + id + '"]' },
        breakpoints: { 576: { slidesPerView: 2, spaceBetween: 20 }, 992: { slidesPerView: 3, spaceBetween: 24 }, 1200: { slidesPerView: parseInt(el.getAttribute("data-xl") || "4", 10), spaceBetween: 24 } }
      });
    });
  }

  /* ---------- AOS ---------- */
  if (window.AOS) {
    window.AOS.init({ duration: 800, easing: "ease-out-cubic", once: true, offset: 60, disable: reduce });
  }

  /* ---------- forms (Web3Forms) ---------- */
  var WEB3FORMS_KEY = "3cc27b4f-9a77-45ca-aa64-d9da669f720d";
  document.querySelectorAll("form[data-web3]").forEach(function (form) {
    form.addEventListener("submit", async function (e) {
      e.preventDefault();
      var msg = form.querySelector(".form-msg");
      var btn = form.querySelector('[type="submit"]');
      if (msg) { msg.className = "form-msg"; msg.textContent = ""; }
      if (!form.checkValidity()) { form.reportValidity(); return; }
      if (form.querySelector('[name="botcheck"]') && form.querySelector('[name="botcheck"]').checked) return;
      var data = new FormData(form);
      var mods = [].slice.call(form.querySelectorAll('input[name="modules"]:checked')).map(function (c) { return c.value; });
      data.delete("modules");
      if (mods.length) data.append("modules", mods.join(", "));
      data.append("access_key", form.getAttribute("data-key") || WEB3FORMS_KEY);  // a form can use its own Web3Forms key via data-key
      data.append("from_name", "EnlitEDU website");
      data.append("subject", form.getAttribute("data-subject") || "New enquiry from enlitedu.com");
      data.append("page", location.pathname);
      var label = btn ? btn.innerHTML : "";
      if (btn) { btn.disabled = true; btn.innerHTML = "Sending…"; }
      try {
        var res = await fetch("https://api.web3forms.com/submit", { method: "POST", body: data });
        var json = await res.json();
        if (!json.success) throw new Error(json.message || "Request failed");
        window.dataLayer = window.dataLayer || [];
        window.dataLayer.push({ event: "generate_lead", form: form.getAttribute("data-subject") || "form" });
        window.location.href = form.getAttribute("data-redirect") || "thank-you.html";
      } catch (err) {
        if (msg) {
          msg.className = "form-msg err";
          var to = form.getAttribute("data-email") || "info@enlitedu.com";
          msg.innerHTML = 'We couldn’t send that just now. Please email <a href="mailto:' + to + '">' + to + '</a> and we’ll reply within one business day.';
        }
        if (btn) { btn.disabled = false; btn.innerHTML = label; }
      }
    });
  });

  /* ---------- TBR announcement popup: opens on every homepage visit; after ✕ it stays closed for that visit ---------- */
  var pop = document.querySelector(".tbr-pop");
  if (pop) {
    var popLocked = false, popLast = null;
    var openPop = function () {
      popLast = document.activeElement;
      pop.hidden = false;
      void pop.offsetWidth; pop.classList.add("open");  // reflow first so the fade-in transition runs
      if (!window.matchMedia("(max-width: 767px)").matches) { lockScroll(); popLocked = true; }  // mobile: page stays scrollable
      var x = pop.querySelector(".tbr-pop-x"); if (x) x.focus({ preventScroll: true });
    };
    var closePop = function () {
      if (pop.hidden) return;
      try { sessionStorage.setItem("tbrPromoClosed", "1"); } catch (e) {}
      pop.classList.remove("open");
      if (popLocked) { unlockScroll(); popLocked = false; }
      setTimeout(function () { pop.hidden = true; }, 280);
      if (popLast && popLast.focus) popLast.focus({ preventScroll: true });
    };
    pop.querySelector(".tbr-pop-x").addEventListener("click", closePop);
    pop.querySelector(".tbr-pop-close2").addEventListener("click", closePop);
    pop.querySelector(".tbr-pop-scrim").addEventListener("click", closePop);
    pop.querySelector(".tbr-pop-card a").addEventListener("click", function () { if (popLocked) { unlockScroll(); popLocked = false; } });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") closePop(); });
    var closed = false; try { closed = sessionStorage.getItem("tbrPromoClosed") === "1"; } catch (e) {}
    var force = /[?&]tbr-popup\b/.test(location.search);
    if (force || (pop.getAttribute("data-auto") === "1" && !closed)) setTimeout(openPop, 700);
  }

  /* ---------- year ---------- */
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
