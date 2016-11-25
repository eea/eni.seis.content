<metal:macro define-macro="portlet">

<tal:def tal:on-error="nothing" tal:define="
vocab context/event_countries_vocab;
events python: [b.getObject() for b in context.portal_catalog.searchResults(portal_type=['Event', 'EEA Meeting'], review_state='published', sort_on='start')];
events python: [ev for ev in events if vocab[context.Title()] in (ev.countries or [])][:5];
">
<dl class="box leading-large portlet portletEvents" tal:condition="events">
<dt>Events</dt>
<dd>
<div tal:repeat="event events">


        <a href="" tal:attributes="href event/absolute_url" class="tile" title="" tal:content="event/Title">
            An event related to ENI-SEIS East
        </a>

        <span class="portletItemDetails">
            <span tal:replace="python:event.get_event_dates(event=event)" />
            <span tal:replace="python:event.get_event_year(event=event)" />
            <span class="location"> —
                <span tal:replace="event/location">Bucharest</span>
            </span>
        </span>

          </div>
</dd>
</dl>
</tal:def>
</metal:macro>
