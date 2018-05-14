// Imported by upgrade step in: /portal_tinymce/@@tinymce-controlpanel - Resource Types - Custom Plugins:
// eni_faq_section|portal_skins/eni_faq_section/editor_plugin.js
(function() {
  // Load plugin specific language pack
  tinymce.PluginManager.requireLangPack('eni_faq_section');

  tinymce.create('tinymce.plugins.ENIFAQSectionPlugin', {
    /**
     * Initializes the plugin, this will be executed after the plugin has been created.
     * This call is done before the editor instance has finished it's initialization so use the onInit event
     * of the editor instance to intercept that event.
     *
     * @param {tinymce.Editor} ed Editor instance that the plugin is initialized in.
     * @param {string} url Absolute URL to where the plugin is located.
     */
    init : function(ed, url) {
      // Register the command so that it can be invoked by using tinyMCE.activeEditor.execCommand('mceENIFAQSection');
      ed.addCommand('mceENIFAQSection', function() {
        ed.windowManager.open({
          file : url + '/eni_faq_section.html',
          width : 900 + ed.getLang('eni_faq_section.delta_width', 0),
          height : 700 + ed.getLang('eni_faq_section.delta_height', 0),
          inline : 1
        }, {
          plugin_url : url, // Plugin absolute URL
        });
      });

      // Register eni_faq_section button
      ed.addButton('eni_faq_section', {
        title : 'ENI FAQ Section',
        cmd : 'mceENIFAQSection',
        image : url + '/img/eni_faq_section.png'
      });

      // Add a node change handler, selects the button in the UI when a child of .eni-faq-wrapper is selected
      ed.onNodeChange.add(function(ed, cm, n) {
        cm.setActive('eni_faq_section', $(n).closest(".eni-faq-wrapper").length);
      });
    },

    /**
     * Creates control instances based in the incomming name. This method is normally not
     * needed since the addButton method of the tinymce.Editor class is a more easy way of adding buttons
     * but you sometimes need to create more complex controls like listboxes, split buttons etc then this
     * method can be used to create those.
     *
     * @param {String} n Name of the control to create.
     * @param {tinymce.ControlManager} cm Control manager to use inorder to create new control.
     * @return {tinymce.ui.Control} New control instance or null if no control was created.
     */
    createControl : function(n, cm) {
      return null;
    },

    _onSave: function() {
      function html_edit_to_view($edit_dialog) {
        // Prepare the html for view mode based on updated items.
        // Return the html as used in a faq section.
        var result = "<div class='eni-faq-wrapper'>";
        $edit_dialog.find(".eni-faq-item").each(function() {
          $question = $(this).find("textarea.question");
          $answer = $(this).find("textarea.answer");
          result += "<div class='eni-faq-item'>";
          result += "<div class='eni-faq-question'><a href='#'>" + $question.val() + "</a></div>";
          result += "<div class='eni-faq-answer'>" + $answer.val() + "</div>";
          result += "</div>";
        });

        result += "</div>"
        return result;
      }

      var $edit_dialog = $("iframe").contents().find("#eni-faq-dialog");
      var html_content = html_edit_to_view($edit_dialog);
      var $old_section = $("iframe").contents().find('div.eni-faq-wrapper').first();
      $old_section.replaceWith(html_content);
    },

    // TODO:
    // - option: delete all section
    // - option: insert section
    // - clear code in theme
    // - add styles for dialog
    // - clear styles in theme

    _onEdit: function() {
      function faq_item(question_text, answer_html) {
        // Return a faq item as used in edit mode
        var result = "";
        $textarea_question = '<textarea class="question" rows="5">' + question_text + '</textarea>';
        $textarea_answer = '<textarea class="answer" rows="5">' + answer_html + '</textarea>';
        result += "<div class='eni-faq-item'>";
        result += "<h3>FAQ question:</h3>";
        result += $textarea_question;
        result += "<h3>FAQ answer:</h3>";
        result += $textarea_answer;
        result += "<button class='eni-faq-delete-question'>Delete</button>";
        result += "<button class='eni-faq-add-question'>Add</button>";
        result += "</div>";
        return result;
      }

      function html_view_to_edit($faq_items) {
        // Prepare edit mode for existing questions.
        // Return the html used in edit dialog.
        var result = "";
        $faq_items.each(function() {
          $question = $(this).find(".eni-faq-question");
          $answer = $(this).find(".eni-faq-answer");
          result += faq_item($question.text(), $answer.html());
        });
        if($faq_items.length == 0) {
          result += faq_item("", "<p></p>");
        }
        result += "<button class='eni-faq-delete-all'>Delete all</button>";
        return result;
      }

      $(document).ready(function() {
        // Delete item
        $("iframe").contents().on('click', 'button.eni-faq-delete-question', function(evt) {
          evt.preventDefault();
          var result = confirm("Delete item: Are you sure?");
          if (result) {
            $(this).parent().remove();
          }
        });

        // Add item
        $("iframe").contents().on('click', 'button.eni-faq-add-question', function(evt) {
          evt.preventDefault();
          $(this).parent().after(faq_item("", "<p></p>"));
        });

        // Delete all items
        $("iframe").contents().on('click', 'button.eni-faq-delete-all', function(evt) {
          evt.preventDefault();
          var result = confirm("Delete ALL items: Are you sure?");
          if (result) {
            $(this).parent().html("");
          }
        });
      });

      var $content = $("iframe").contents().find('div.eni-faq-wrapper').first();
      var $faq_items = $content.find("div.eni-faq-item");
      var $faq_dialog = $("iframe").contents().find("div#eni-faq-dialog");
      var html_result = html_view_to_edit($faq_items);
      $faq_dialog.html(html_result);
    },

    /**
     * Returns information about the plugin as a name/value array.
     * The current keys are longname, author, authorurl, infourl and version.
     *
     * @return {Object} Name/value array containing information about the plugin.
     */
    getInfo : function() {
      return {
        longname : 'ENIFAQSection plugin',
        author : 'Ghiță Bizău',
        authorurl : 'https://github.com/GhitaB',
        infourl : '',
        version : "1.0"
      };
    }
  });

  // Register plugin
  tinymce.PluginManager.add('eni_faq_section', tinymce.plugins.ENIFAQSectionPlugin);
})();
