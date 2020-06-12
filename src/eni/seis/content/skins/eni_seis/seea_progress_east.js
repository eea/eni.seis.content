  $(function() {
    $("#eni-accordion").accordion({
      active: false,
      collapsible: true,
      heightStyle: "content"
    });

    $("div.page-body").addClass("page-main");  // Apply styles & skip diazo issues
  });
