/* Sticky quick-link bar on wiki hub pages (Outlands / Fandom pinned nav pattern) */
document.addEventListener("DOMContentLoaded", function () {
  var hub = document.querySelector(".wiki-hub");
  if (!hub) return;

  var bar = document.createElement("nav");
  bar.className = "wiki-quicknav";
  bar.setAttribute("aria-label", "Quick links");

  var links = [
    ["Main pages", "#main-pages"],
    ["Popular", "#popular-pages"],
    ["Browse", "#browse-by-topic"],
    ["Search", "#"],
  ];

  links.forEach(function (pair) {
    var a = document.createElement("a");
    a.href = pair[1];
    a.textContent = pair[0];
    if (pair[1] === "#") {
      a.addEventListener("click", function (e) {
        e.preventDefault();
        var search = document.querySelector('[data-md-component="search"] input, .md-search__input');
        if (search) search.focus();
      });
    }
    bar.appendChild(a);
  });

  hub.insertBefore(bar, hub.firstChild);

  var headings = hub.querySelectorAll("h2");
  headings.forEach(function (h) {
    var text = h.textContent || "";
    if (/main pages/i.test(text)) h.id = "main-pages";
    if (/popular pages/i.test(text)) h.id = "popular-pages";
    if (/browse by topic/i.test(text)) h.id = "browse-by-topic";
  });
});
