if(window.eeatinymceplugins === undefined){
  var eeatinymceplugins = {
    "name": "EEA TinyMCE Plugins",
    "settings": {}
  };
}

jQuery.getJSON("tinymceplugins.json", function( data ) {
    eeatinymceplugins.settings = data;
});
