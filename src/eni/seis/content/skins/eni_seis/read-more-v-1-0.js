// https://cdn.rawgit.com/GhitaB/read-more/master/read-more-v-1-0.js
$(document).ready(function() {
  var add_readmore_links = function() {
    $("span.read-more").after("<a href='#' class='read-more-link'><span class='read-more-link-text'>Read more</span></a>");
  };

  var toggle_text = function(text) {
    if(text == "Read more") {
      return "Read less";
    } else {
      return "Read more";
    }
  };

  var toggle_sections_visibility_on_click = function() {
    $(".read-more-link").on("click", function() {
      $(this).prev().slideToggle();
      var $span_readmore_link = $(this).find("span.read-more-link-text");
      $span_readmore_link.text(toggle_text($span_readmore_link.text()));
      return false;
    });
  };

  var hide_all = function() {
    $("span.read-more").hide();
  };

  var init_readmore = function() {
    add_readmore_links();
    hide_all();
    toggle_sections_visibility_on_click();
  };

  init_readmore();
});
