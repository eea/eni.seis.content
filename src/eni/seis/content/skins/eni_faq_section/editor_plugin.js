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

      jQuery(document).ready(function() {
        window.faq_behavior = (function eni_faq_sections() {
          // View mode
          $("div.eni-faq-answer").hide();
          $("div.eni-faq-question a").on("click", function(evt) {
            evt.preventDefault();
            $(this).parent().parent().find(".eni-faq-answer").toggle();
          });

          // Add edit button
          var $edit_btn = $('<input type="button" value="Edit" name="faq-edit" />');
          $edit_btn.insertAfter($(".eni-faq-wrapper"));

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
            result += "<button id='faq-save'>Save</button>";
            return result;
          }

          function html_edit_to_view($edit_dialog) {
            // Prepare the html for view mode based on updated items.
            // Return the html as used in a faq section.
            var result = "";
            $edit_dialog.find(".eni-faq-item").each(function() {
              $question = $(this).find("textarea.question");
              $answer = $(this).find("textarea.answer");
              result += "<div class='eni-faq-item'>";
              result += "<div class='eni-faq-question'><a href='#'>" + $question.val() + "</a></div>";
              result += "<div class='eni-faq-answer'>" + $answer.val() + "</div>";
              result += "</div>";
            });
            return result;
          }

          $edit_btn.on("click", function() {
            // Edit mode
            $edit_btn.remove();
            $faq_wrapper = $(".eni-faq-wrapper");
            $faq_items = $faq_wrapper.find(".eni-faq-item");
            var $edit_dialog = $(document.createElement('div'));
            $edit_dialog.html(html_view_to_edit($faq_items));
            $edit_dialog.dialog({dialogClass:'eni-faq-dialog'});

            $(document.body).on('click', 'button.eni-faq-delete-question', function(evt) {
              var result = confirm("Delete item: Are you sure?");
              if (result) {
                $(this).parent().remove();
              }
            });

            $(document.body).on('click', 'button.eni-faq-add-question', function(evt) {
              $(this).parent().after(faq_item("", "<p></p>"));
            });

            $("#faq-save").on("click", function(evt) {
              // Save
              evt.preventDefault();
              new_html = html_edit_to_view($edit_dialog);
              $faq_wrapper.html(new_html);

              // Clear
              $edit_dialog.dialog("close");
              $edit_dialog.dialog('destroy').remove();
              $(document.body).off('click', 'button.eni-faq-delete-question');
              $(document.body).off('click', 'button.eni-faq-add-question');

              // Reinit
              eni_faq_sections();
            });

          });
        }());

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
      var html_content = $("iframe").contents().find("#eni-faq-dialog").find("textarea").val();
      tinyMCE.activeEditor.selection.setContent(html_content);
    },

    _onEdit: function() {
      var $content = $("iframe").contents().find('div.eni-faq-wrapper').first();
      var $faq_items = $content.find("div.eni-faq-item");
      var $faq_dialog = $("iframe").contents().find("div#eni-faq-dialog");
      $faq_dialog.find("textarea").val($faq_items.html());
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
