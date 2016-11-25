<metal:macro define-macro="portlet">

<dl class="box leading-large portlet portletEvents"
tal:define="events_path python: '/east/communication/events';
events python: context.getFolderContents(full_objects=True, contentFilter={'sort_on': 'start', 'path': {'query':events_path, 'depth':3}, 'portal_type':['Event', 'EEA Meeting']})">

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
</metal:macro>
