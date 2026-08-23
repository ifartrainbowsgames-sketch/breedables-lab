/* Collapsible primary sidebar.
 *
 * Material only folds the navigation away below its desktop breakpoint. This
 * wiki is deep enough that the tree is worth keeping open most of the time and
 * worth reclaiming the width from when you are reading a long lesson, so the
 * reader gets an explicit toggle. The choice is remembered between pages.
 */
(function () {
  var KEY = "wiki-nav-collapsed";
  var CLASS = "wiki-nav-collapsed";

  function isCollapsed() {
    try {
      return localStorage.getItem(KEY) === "1";
    } catch (e) {
      return false;
    }
  }

  function apply(collapsed, button) {
    document.body.classList.toggle(CLASS, collapsed);
    if (button) {
      button.setAttribute("aria-expanded", String(!collapsed));
      button.setAttribute(
        "title",
        collapsed ? "Show navigation" : "Hide navigation"
      );
    }
  }

  function mount() {
    var existing = document.querySelector(".wiki-nav-toggle");
    if (existing) {
      apply(isCollapsed(), existing);
      return;
    }

    var header = document.querySelector(".md-header__inner");
    if (!header) return;

    var button = document.createElement("button");
    button.type = "button";
    button.className = "wiki-nav-toggle";
    button.setAttribute("aria-label", "Toggle navigation");
    button.innerHTML =
      '<svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true">' +
      '<path fill="currentColor" d="M3 6h18v2H3V6m0 5h18v2H3v-2m0 5h18v2H3v-2Z"/></svg>';

    button.addEventListener("click", function () {
      var next = !document.body.classList.contains(CLASS);
      try {
        localStorage.setItem(KEY, next ? "1" : "0");
      } catch (e) {
        /* private mode — the toggle still works for this page */
      }
      apply(next, button);
    });

    // Sits immediately after the hamburger so it reads as a nav control.
    header.insertBefore(button, header.children[1] || null);
    apply(isCollapsed(), button);
  }

  mount();
  document.addEventListener("DOMContentLoaded", mount);

  // navigation.instant replaces the page body without a reload.
  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(mount);
  }
})();
