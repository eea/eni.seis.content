<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en"
      xmlns:tal="http://xml.zope.org/namespaces/tal"
      xmlns:metal="http://xml.zope.org/namespaces/metal"
      xmlns:i18n="http://xml.zope.org/namespaces/i18n"
      lang="en"
      metal:use-macro="context/main_template/macros/master"
      i18n:domain="plone">

<body>

<metal:content-core fill-slot="content-core">
<metal:block define-macro="content-core"
                    tal:define="kssClassesView context/@@kss_field_decorator_view;
                                getKssClasses nocall:kssClassesView/getKssClassesInlineEditable;
                                templateId template/getId;">
<metal:slot define-slot="long_description">
<div tal:replace="structure context/long_description | nothing" tal:on-error="nothing"></div>
</metal:slot>

    <metal:listingmacro define-macro="listing">

    <tal:foldercontents define="contentFilter contentFilter|request/contentFilter|nothing;
                        contentFilter python:contentFilter and dict(contentFilter) or {};
                        limit_display limit_display|request/limit_display|nothing;
                        limit_display python:limit_display and int(limit_display) or None;
                        more_url more_url|request/more_url|string:folder_contents;
                        is_a_topic python:context.portal_type=='Topic';
                        folderContents folderContents|nothing; folderContents python:folderContents or is_a_topic and context.queryCatalog(batch=True, **contentFilter) or context.getFolderContents(contentFilter, batch=True, b_size=limit_display or 100);
                        site_properties context/portal_properties/site_properties;
                        use_view_action site_properties/typesUseViewActionInListings|python:();
                        Batch python:modules['Products.CMFPlone'].Batch;
                        b_start python:request.get('b_start', 0);
                        batch python:folderContents if isinstance(folderContents, Batch) else Batch(folderContents, limit_display or 100, int(b_start), orphan=1);
                        isAnon context/@@plone_portal_state/anonymous;
                        normalizeString nocall: context/plone_utils/normalizeString;
                        toLocalizedTime nocall: context/@@plone/toLocalizedTime;
                        show_about python:not isAnon or site_properties.allowAnonymousViewAbout;
                        navigation_root_url context/@@plone_portal_state/navigation_root_url;
                        pas_member context/@@pas_member;
                        plone_view context/@@plone;">
    <tal:listing condition="batch">

        <dl metal:define-slot="entries">
            <tal:entry tal:repeat="item python:[b for b in batch]" metal:define-macro="entries">
            <tal:block tal:define="item_url item/getURL|item/absolute_url;
                                   item_id item/getId|item/id;
                                   item_title_or_id item/pretty_title_or_id;
                                   item_description item/Description;
                                   item_type item/portal_type;
                                   item_type_title item/Type;
                                   item_modified item/ModificationDate;
                                   item_created item/CreationDate;
                                   item_icon python:plone_view.getIcon(item);
                                   item_type_class python:'contenttype-' + normalizeString(item_type);
                                   item_wf_state item/review_state|python: context.portal_workflow.getInfoFor(item, 'review_state', '');
                                   item_wf_state_class python:'state-' + normalizeString(item_wf_state);
                                   item_creator item/Creator;
                                   item_start item/start|item/StartDate|nothing;
                                   item_end item/end|item/EndDate|nothing;
                                   item_sametime python: item_start == item_end;
                                   item_samedate python: (item_end - item_start &lt; 1) if item_type == 'Event' else False">
                <metal:block define-slot="entry">
                <dt metal:define-macro="listitem"
                    tal:attributes="class python:test(item_type == 'Event', 'vevent', '')">

                    <span class="summary">
                        <img tal:replace="structure item_icon/html_tag" />
                        <a href="#"
                           tal:attributes="href python:test(item_type in use_view_action, item_url+'/view', item_url);
                                           class string:$item_type_class $item_wf_state_class url"
                           tal:content="item_title_or_id">
                            Item Title
                        </a>
                    </span>

                    <span class="documentByLine">
                        <span tal:condition="python: item_type == 'Event' and item_sametime"
                              i18n:translate="label_event_byline_onlyfrom">
                             <abbr class="dtstart"
                                   tal:attributes="title python:item_start"
                                   tal:content="python:toLocalizedTime(item_start,long_format=1)"
                                   i18n:name="start">from date</abbr>
                        </span>
                        <span tal:condition="python: item_type == 'Event' and item_samedate and not item_sametime"
                              i18n:translate="label_event_byline_samedate">
                             <abbr class="dtstart"
                                   tal:attributes="title python:item_start"
                                   tal:content="python:toLocalizedTime(item_start)"
                                   i18n:name="start">from date</abbr> from
                             <abbr class="dtstart"
                                   tal:attributes="title python:item_start"
                                   tal:content="python:toLocalizedTime(item_start,time_only=1)"
                                   i18n:name="starttime">from time</abbr> to
                             <abbr class="dtend"
                                   tal:attributes="title python:item_end"
                                   tal:content="python:toLocalizedTime(item_end,time_only=1)"
                                   i18n:name="end">to time</abbr>
                        </span>
                        <span tal:condition="python: item_type == 'Event' and not item_samedate and not item_sametime"
                              i18n:translate="label_event_byline">
                              from
                                   <abbr class="dtstart"
                                   tal:attributes="title python:item_start"
                                   tal:content="python:toLocalizedTime(item_start,long_format=1)"
                                   i18n:name="start">from date</abbr> to
                             <abbr class="dtend"
                                   tal:attributes="title python:item_end"
                                   tal:content="python:toLocalizedTime(item_end,long_format=1)"
                                   i18n:name="end">to date</abbr>
                        </span>
                         <span tal:condition="python: item_type == 'Event' and item.location"
                              i18n:translate="label_event_byline_location">&mdash;
                             <span tal:content="string:${item/location}"
                                   class="location"
                                   i18n:name="location">Oslo</span>,
                        </span>
                        <tal:byline condition="show_about">
                            &mdash;

                            <tal:name tal:condition="item_creator"
                                tal:define="author python:pas_member.info(item_creator);
                                            creator_short_form author/username;
                                            creator_long_form string:?author=${author/username};
                                            creator_is_openid python:'/' in creator_short_form;
                                            creator_id python:(creator_short_form, creator_long_form)[creator_is_openid];">
                              <span i18n:translate="label_by_author">
                                by
                              <a href="#"
                                 tal:attributes="href string:${navigation_root_url}/author/${item_creator}"
                                 tal:content="author/name_or_id"
                                 tal:omit-tag="not:author"
                                 i18n:name="author">
                                Bob Dobalina
                              </a>
                              </span>

                            </tal:name>

                            <tal:modified condition="python: item_type != 'Event'">
                                &mdash;
                                <tal:mod i18n:translate="box_last_modified">
                                  last modified
                                </tal:mod>
                                <span tal:replace="python:toLocalizedTime(item_modified,long_format=1)">
                                  August 16, 2001 at 23:35:59
                                </span>
                            </tal:modified>

                            <metal:description define-slot="description_slot">
                                <tal:comment replace="nothing">
                                    Place custom listing info for custom types here
                                </tal:comment>
                            </metal:description>
                        </tal:byline>
                    </span>

                </dt>

                <dd>
                    <span class="description"
                        tal:condition="item_description"
                        tal:content="item_description">
                        Description
                    </span>
                </dd>
            </metal:block>
            </tal:block>
            </tal:entry>
        </dl>

        <div metal:use-macro="context/batch_macros/macros/navigation" />

    </tal:listing>
    <metal:empty metal:define-slot="no_items_in_listing">
        <p class="discreet"
           tal:condition="not: folderContents"
           i18n:translate="description_no_items_in_folder">

        </p>
    </metal:empty>

    </tal:foldercontents>
    </metal:listingmacro>

</metal:block>
</metal:content-core>

</body>
</html>
