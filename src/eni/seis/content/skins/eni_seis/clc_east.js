$(function() {
  $("#eni-accordion").accordion({
    active: false,
    collapsible: true,
    heightStyle: "content"
  });
});

$(document).ready(function() {
  $("tr.more-info").hide();

  $(".btn-more-info.fa-plus").on("click", function() {
    var data_id = $(this).parent().attr("data-btn-id");
    $("tr[data-tr-id=" + data_id + "]").show();
    $(this).removeClass("fa-plus");
    $(this).addClass("fa-minus");
  });

  $(".btn-more-info.fa-minus").on("click", function() {
    var data_id = $(this).parent().attr("data-btn-id");
    $("tr[data-tr-id=" + data_id + "]").hide();
    $(this).removeClass("fa-minus");
    $(this).addClass("fa-plus");
  });
});
