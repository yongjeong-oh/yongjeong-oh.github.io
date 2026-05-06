---
layout: page
permalink: /publications/
title: publications
description: A complete list of my publications, organized by category. * indicates corresponding author. Names appearing in <strong>bold</strong> are mine.
nav: true
nav_order: 2
nav_icon: fa-solid fa-book
toc:
  sidebar: left
_styles: >
  .post .post-header { display: none; }
  body > .container[role="main"] { max-width: 1080px; }
  nav.navbar > .container { max-width: 1080px; }
  #toc-sidebar .nav-link { white-space: nowrap; }
  .toc-sticky-wrap { margin-left: -0.5rem; }
---

<!-- _pages/publications.md -->

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

<div class="publications">

<div class="card mt-3 p-3">
  <h3 class="card-title font-weight-medium" id="preprints">Preprints</h3>
  <div>
    {% bibliography --group_by none --query @*[keywords=submitted]* %}
  </div>
</div>

<div class="card mt-3 p-3">
  <h3 class="card-title font-weight-medium" id="international-journal-papers" data-toc-text="Int. J. Papers">International Journal Papers</h3>
  <div>
    {% bibliography --group_by none --query @*[keywords=intl_journal]* %}
  </div>
</div>

<div class="card mt-3 p-3">
  <h3 class="card-title font-weight-medium" id="international-conference-papers" data-toc-text="Int. Conf. Papers">International Conference Papers</h3>
  <div>
    {% bibliography --group_by none --query @*[keywords=intl_conf]* %}
  </div>
</div>

<div class="card mt-3 p-3">
  <h3 class="card-title font-weight-medium" id="domestic-journal-papers" data-toc-text="Dom. J. Papers">Domestic Journal Papers</h3>
  <div>
    {% bibliography --group_by none --query @*[keywords=dom_journal]* %}
  </div>
</div>

<div class="card mt-3 p-3">
  <h3 class="card-title font-weight-medium" id="domestic-conference-papers" data-toc-text="Dom. Conf. Papers">Domestic Conference Papers</h3>
  <div>
    {% bibliography --group_by none --query @*[keywords=dom_conf]* %}
  </div>
</div>

<div class="card mt-3 p-3">
  <h3 class="card-title font-weight-medium" id="patents">Patents</h3>
  <div>
    {% bibliography --group_by none --query @*[keywords=patent]* %}
  </div>
</div>

</div>

<script>
  // Reverse-number each section: top item gets the largest number.
  // Also move the bib-search input into the TOC sidebar.
  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".publications .card ol.bibliography").forEach(function (ol) {
      var items = ol.querySelectorAll(":scope > li");
      var total = items.length;
      items.forEach(function (li, i) {
        li.style.setProperty("--pub-num", '"' + (total - i) + '"');
      });
    });

    var search = document.getElementById("bibsearch");
    var wrap = search ? search.closest(".bibsearch-wrap") : null;
    var toc = document.getElementById("toc-sidebar");
    if (wrap && toc && toc.parentNode) {
      // Move sticky behaviour from nav to a shared wrapper so nav + search
      // can be visually separated while still sticking together.
      toc.classList.remove("sticky-top");
      var stickyWrap = document.createElement("div");
      stickyWrap.className = "toc-sticky-wrap sticky-top";
      toc.parentNode.insertBefore(stickyWrap, toc);
      stickyWrap.appendChild(toc);
      stickyWrap.appendChild(wrap);
    }

    // After bootstrap-toc has populated the sidebar, force the first link
    // (Preprints) to be active on page load, and re-arm scrollspy so the
    // next section becomes active once its header reaches mid-viewport.
    setTimeout(function () {
      var firstLink = document.querySelector("#toc-sidebar .nav-link");
      if (firstLink && !document.querySelector("#toc-sidebar .nav-link.active")) {
        firstLink.classList.add("active");
      }
      if (window.jQuery) {
        try {
          window.jQuery(document.body).scrollspy("dispose");
        } catch (e) {}
        window.jQuery(document.body).scrollspy({
          target: "#toc-sidebar",
          offset: Math.floor(window.innerHeight * 0.55),
        });
      }

      // When a TOC link is clicked, mark it active immediately and keep it
      // active briefly so the smooth-scroll lands on the correct section.
      document.querySelectorAll("#toc-sidebar .nav-link").forEach(function (link) {
        link.addEventListener("click", function () {
          document
            .querySelectorAll("#toc-sidebar .nav-link.active")
            .forEach(function (l) {
              l.classList.remove("active");
            });
          this.classList.add("active");
        });
      });
    }, 300);

    // When the user scrolls back to the very top, force Preprints active
    // (bootstrap-toc sometimes lags at the top of the page).
    window.addEventListener("scroll", function () {
      if (window.scrollY < 120) {
        var links = document.querySelectorAll("#toc-sidebar .nav-link");
        links.forEach(function (l, i) {
          if (i === 0) {
            l.classList.add("active");
          } else {
            l.classList.remove("active");
          }
        });
      }
    }, { passive: true });
  });
</script>
