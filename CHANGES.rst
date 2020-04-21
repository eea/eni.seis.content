Changelog
=========

1.3.0 (unreleased)
------------------
- Fix: Add image caption in photo gallery.
  [GhitaB #116711]
- Fix: Remove expandable text in events listing - Land section.
- Improve: Add more categories for product item.
- Improve: Update Land products tab titles.
- Fix: Hide footer sections in Areas of work / Data.
  [GhitaB #116290]

1.2.9 (2020-04-15)
------------------
- Feature: expandable texts in events listing.
  [GhitaB #116290]

1.2.8 (2020-04-13)
------------------
- Feature: Land section.
  Manual step: create section (folder). Set template (clc_east).
  Manual step: Fix order in folder_contents of Areas of work. Land after
  Indicators and Assesments.
  Manual step: Add bullet for Land after ‘Indicators and Assessment’
  /homepage-section-aow-slider.
  [GhitaB #116290]
- Improve: Include new fields and content types to be checked by script.
  [GhitaB #108137]

1.2.7 (2020-04-03)
------------------
- Improve: ProductItem listing - set view url to download file in case it
  has one.
  [GhitaB #114456]
- Improve: script to check broken links in body text of eea.meeting objects.
  [GhitaB #108137]

1.2.6 (2020-04-01)
------------------
- Improve: Editable sections in Access to env.
  Manual step: create sections (as folders) used by this custom template.
- Fix: Set active tabs in Access to environmental listings.
- Improve: change sections order (K. resources, Partners).
- Improve: update Products tabs titles and table listings.
  [GhitaB #114456]
- Feature: show photo credits in folder gallery view when an image title
  starts with @.
  [GhitaB #116119]
- Improve: update photos in Results section (East). Fix links.
- Fix: Use larger image in news listing.
  [GhitaB #107342]

1.2.5 (2020-03-20)
------------------
- Fix: meetings order in Events list (Access to environmental - Deliverables).
- Fix: product items listing in case no country is selected.
- Improve: Collapse all the accordion tabs by default.
- Improve: Move body text before accordion.
  [GhitaB #114456]

1.2.4 (2020-03-18)
------------------
- Improve: Access to environmental - add listings with tabs (Events, Products).
- Feature: new content type Product Item.
  Manual step: /east/areas-of-work/work-plans - exclude from navigation.
  Manual step: /east/homepage-section-aow-slider/edit - remove Work plans.
  Manual step: create folder
  /east/areas-of-work/access-to-environmental-information/products/
  Manual step: /east/dexterity-types/productitem/@@behaviors - add Countries
  Manual step: edit Access, add text in bottom of the page.
  [GhitaB #114456]

1.2.3 (2020-03-12)
------------------
- Feature: add country events in country view - East.
  [GhitaB #115573]
- Fix: reports order by position in folder, in country view - East.
  [GhitaB #115563]

1.2.2 (2020-03-05)
------------------
- Feature: Editable good practice reports section
  Manual step: add folder Good practice reports.
  [GhitaB #114456]
- Improve: Access to environmental - national reports listing.
  [GhitaB #114456]
- Feature: National reports (content type, updated templates for country view
  and Countries).
  [GhitaB #107340]

1.2.1 (2020-02-24)
------------------
- Fix: Set level class for national and regional meetings.
  [GhitaB #114456]

1.2.0 (2020-02-20)
------------------
- Feature: Add Access env section (East).
  Manual step: set template, rename item.
  [GhitaB #114456]

1.1.9 (2020-01-31)
------------------
- Fix: Skip daviz title in embeded chart and dashboard.
  [GhitaB #113379]
- Fix: Countries link in Results section.
  [GhitaB #107342]

1.1.8 (2020-01-23)
------------------
- Feature: add Testimonials demo template (East).
  Manual step: add page /east/governance/results/testimonials, use content
  from testimonials_demo template.
  Manual step: add folder /east/governance/results/photos, set display as
  photo gallery.
  Manual step: add folder /east/governance/results/case-studies, set display as
  news listing.
- Improve: Results section (East).
  [GhitaB #107342]

1.1.7 (2020-01-14)
------------------
- Feature: Settings for dashboards heights in indicatordata.
- Feature: Results page.
  Manual step: create /east/governance/results/ folder.
  Manual step: add results_root_east in
  /east/portal_types/Folder/manage_propertiesForm and set is as display mode
  for Results folder.
  [GhitaB #107342]

1.1.6 (2019-12-16)
------------------
- Improve: DaViz dashboard rendering in indicator view.
  [GhitaB #110823]

1.1.5 (2019-12-03)
------------------
- Improve: SEEA Progress table will be editable as page.
  [GhitaB #111804]
- Feature: Results section.
  [GhitaB #107342]

1.1.4 (2019-11-06)
------------------
- Improve: Update indicators search configuration. Manual step: import.
- Improve: move styles to theme.
  [GhitaB #110829]

1.1.3 (2019-10-31)
------------------
- Fix: Update SEEA Progress page table - value for Armenia 2.1.1.
  [GhitaB #107341]

1.1.2 (2019-10-22)
------------------
- Improve: Update SEEA Progress page table section.
  [GhitaB #107341]
- Improve: update links for tags and topics in indicatordata view to use
  faceted search for indicators section.
- Improve: update configuration for indicators search.
- Improve: add new indexes in portal_catalog for indicatordata.
  Manual step: run upgrade step, reindex indexes.
  [GhitaB #108504]

1.1.1 (2019-10-17)
------------------
- Improve: In meetings table view describe webinar's location as 'Webinar'
  instead of empty field.
  [GhitaB #110353]
- Feature: SEEA Progress section template.
  Manual step: add seea-progress_root as display type for Folder.
  [GhitaB #107341]
- Improve: Move styles to theme.
  [GhitaB #108504]
- Fix: lead image listing for indicators in search page.
  Manual step: delete template customization in production website (East).
  [GhitaB #110078]

1.1.0 (2019-10-01)
------------------
- Improve: add style for custom tables in indicator view.
- Fix: error when fields are empty.
- Feature: custom indicators listing for search section.
- Manual step: disable portlets for indicators folder. Else the styles are
  broken because main.page-main instead of div.page-main.
  [GhitaB #108504]

1.0.9 (2019-09-24)
------------------
- Feature: Indicators search (faceted). Manual step: import config.
- Fix: links for topics and tags in indicatordata view.
  [GhitaB #108504]

1.0.8 (2019-09-19)
------------------
- Feature: Add IndicatorData content type.
  Manual step: /dexterity-types/indicatordata/@@behaviors - add Countries Field
  [GhitaB #108504]

1.0.7 (2019-08-28)
------------------
- Feature: Prepare a demo template to preview the new indicator view layout.
  [GhitaB #108504]

1.0.6 (2019-08-26)
------------------
- Improve: Show last update info in broken-links view.
  [GhitaB #108137]

1.0.5 (2019-08-07)
------------------
- Fix: script for South.
  [GhitaB #108137]

1.0.4 (2019-08-07)
------------------
- Feature: implement broken-links view and script.
  [GhitaB #108137]

1.0.3 (2019-08-02)
------------------
- Fix: Update folder custom listing to have direct links in case of images.
  Useful in some cases of No blob file error for images.
  [GhitaB #108137]

1.0.2 (2019-07-18)
------------------
- Feature: Add main_template customization. Add sentry config in main_template.
  [GhitaB #107647]

1.0.1 (2019-01-16)
------------------
- Improve: Add icon class for Key docs tab in country view - South.
  [GhitaB #101533]

1.0 (2018-12-07)
----------------
- Improve: add disclaimer privacy statement checkbox in meeting register.
- Improve: add request_data_deletion field for subscriber. Update subscriber
  view to include its value.

- Fix: eea.versions warning by reverting to original CanonicalURL viewlet.
  [GhitaB #96598]

- Subscriber view: add request_data_deletion field.
  [GhitaB #96598]

- Subscriber: add request_data_deletion field.
  [GhitaB #96598]

- Fix privacy statement url to work for both websites.
  [GhitaB #96598]

- Add disclaimer checkbox in meeting register.
  [GhitaB #96598]

- Fix eea.versions warning by reverting to original Canon
  [GhitaB #96598]

- News item: Remove listing in custom template.
  [GhitaB #96861]

- Add newsitem no listing view.
  [GhitaB #96861]

- Folder newsletters view template - include description
  [GhitaB #97716]

- Add Newsletter item content type.
  [GhitaB #97716]

- Add fixblobs scripts.
  [GhitaB #96597]

- South: country view - add icons for events, news sections.
  [GhitaB #93660]

- Add a div container for news image for better align.
  [GhitaB #94091]

- Add news images in news listing.
  [GhitaB #94091]

- Fix styles for Delete all button.
  [GhitaB #92274]

- Add styles.
  [GhitaB #92274]

- Fix delete all option to clean all faq section content.
  [GhitaB #92274]

- Add option for inserting new FAQ section.
  [GhitaB #92274]

- Replace all FAQ section with edited on save.
  [GhitaB #92274]

- Add option for deleting all section items.
  [GhitaB #92274]

- Fix html content on save, to use template.
  [GhitaB #92274]

- Countries view: change layout for country visits pages.
  [GhitaB #92269]

- Countries view: show missing reports, too.
  [GhitaB #92270]

- Use reports types vocabulary in report edit form.
  [GhitaB #92270]

- Upgrade step: delete deprecated reports, add new report
  [GhitaB #94287]

- Countries table: Get rid of Subnational environmental r
  [GhitaB #94287]

- Add upgrade step: delete deprecated reports.
  [GhitaB #94287]

- Add styles for FAQ sections in edit mode.
  [GhitaB #92274]

- Newsletters view - improve markup.
  [GhitaB #92252]

- Newsletters view - fix urls.
  [GhitaB #92252]

- South: use the same Newsletter view template.
  [GhitaB #92252]

- East: WIP Newsletter view template.
  [GhitaB #92252]

- Improve get_events_dates: eea.meeting objects to return
  [GhitaB #92650]

- Gallery view: use image description as caption.
  [GhitaB #93380]

- Add getFolderImages script.
  [GhitaB #93380]

- WIP Gallery view - add lightbox2.
  [GhitaB #93380]

- Improve pullquote styles.
  [GhitaB #92272]

- TinyMCE: custom theme styles for East / South.
  [GhitaB #92267]

- Remove EIONET texts: get rid of mail password form cust
  [GhitaB #88608]

- Update hover text based on Victoria's feedback.
  [GhitaB #91703]

- Update text for Waste section hover.
  [GhitaB #91703]

- Add Waste section in Areas of Work/Data.
  [GhitaB #91703]

- Fix error in bin/www1 adduser.
  [GhitaB #91703]

- Show only news items in news_listing_view.
  [GhitaB #82889]

- Use custom folder listing for new added folders.
  [GhitaB #82889]

- Add custom folder listing. (folder_listing is already u
  [GhitaB #82889]

- Fix typo in folder_listing template.
  [GhitaB #82889]

- Fix get_event_level script to show correct value in eve
  [GhitaB #82889]

- Document view: add child files listing (in eea.meeting
  [GhitaB #82889]

- Add custom document view.
  [GhitaB #82889]

- News item view: show child items.
  [GhitaB #82889]

- News item view: Back to old customization in skins; upd
  [GhitaB #82889]

- WIP Custom news item view.
  [GhitaB #82889]

- Event view: show child items.
  [GhitaB #82889]

- WIP Events, News, Documents lists to include folderish.
  [GhitaB #82889]

- WIP Events, News lists to include folderish.
  [GhitaB #82889]

- Update Create a new Event button to use folderish.
  [GhitaB #82889]

- WIP Update queries to inlude folderish objects.
  [GhitaB #82889]

- Prevent extending fields with long_description for fold
  [GhitaB #82889]

- Use default view for new added folderish event, news it
  [GhitaB #82889]

- Improve dialog styles.
  [GhitaB #82899]

- Update Position field description. Make it required in
  [GhitaB #89956]

- Update folder view custom templates.
  [GhitaB #82887]

- Login page - update form for use_email_as_login case.
  [GhitaB #88608]

- Improve text in mail password form template.
  [GhitaB #88608]

- Improve texts for Forgot your password? section in logi
  [GhitaB #88608]

- Subscriber view: set view permission.
  [GhitaB #88609]

- If a public video is not added as child (any level) of
  [GhitaB #88611]

- Add wildcard.media.
  [GhitaB #88611]

- Add message for eionet members in mail_password_form te
  [GhitaB #88608]

- Add override for mail_password_form (WIP).
  [GhitaB #88608]

- Fix double emails issue on Register to this meeting.
  [GhitaB #88593]

- Report: remove custom meta_type.
  [GhitaB #88495]

- Indicator: remove custom meta_type.
  [GhitaB #88495]

- nfp: remove custom meta_type.
  [GhitaB #88495]

- Improve NFPs table design.
  [GhitaB #87782]

- Improve NFPs table.
  [GhitaB #87782]

- East: improve nfps table design.
  [GhitaB #87782]

- East: nfps table optional.
  [GhitaB #87782]

- Improve nfps_listing_view markup.
  [GhitaB #87782]

- NFPs in country_view_east.
  [GhitaB #87782]

- South country view - exclude NFPs folder from tabs.
  [GhitaB #87782]

- Add nfp content type.
  [GhitaB #87782]

- Country view: show max 5 items for a category in a subtab.
  [GhitaB #87783]

- Country view: add icons definition.
  [GhitaB #87783]

- Add flag in country view.
  [GhitaB #87783]

- Make sure to abort the transaction.
  [david-batranu #87630]

- Areas of work root section as in homepage.
  [GhitaB #86208]

- WIP Areas of work - new look.
  [GhitaB #86208]

- Countries - country visits pages - sort on position in
  [GhitaB #86208]

- Force folder_listing as default layout for new created
  [GhitaB #86208]

- Add copyright info for images in Data.
  [GhitaB #86208]

- Cancel generating reports and indicators if the contain
  [GhitaB #86208]

- Countries view east - reports table.
  [GhitaB #86208]

- Countries view east - fix missing description.
  [GhitaB #86208]

- Indicators table in country view est - styles.
  [GhitaB #86208]

- Country view east: publications style.
  [GhitaB #86208]

- Indicators data utils view.
  [GhitaB #86208]

- Country view east - reports data.
  [GhitaB #86208]

- WIP template for root Countries section (countries_view
  [GhitaB #86208]

- Improve template using custom icons.
  [GhitaB #86208]

- WIP replace http with https.
  [GhitaB #86911]

- WIP Country view.
  [GhitaB #86208]

- Add country view for east.
  [GhitaB #86208]

- WIP Indicators and Assessments.
  [GhitaB #86208]

- Areas of work / Data - layout fixes (container fluid vs
  [GhitaB #86208]

- Communication and visibility - fix layout container flu
  [GhitaB #86208]

- WIP Communications and visibility - use icons.
  [GhitaB #86208]

- WIP Communications and visibility.
  [GhitaB #86208]

- Communications and visibility.
  [GhitaB #86208]

- WIP Communication and visibility.
  [GhitaB #86208]

- Add Communication and visibility.
  [GhitaB #86208]

- WIP Areas of work - Data.
  [GhitaB #86208]

- get_upcoming_events view.
  [GhitaB #86299]

- Fix getLocalEvents to work for sub-sections of a countr
  [GhitaB #84441]

- Fix getLocalNews to work for sub-sections of a country
  [GhitaB #84441]

- Meetings table view - update classes to have the design
  [GhitaB #84441]

- Meetings table view - use format used in events table v
  [GhitaB #84441]

- More edit buttons in country view.
  [GhitaB #84441]

- Data and statistics: editable content in right column.
  [GhitaB #84441]

- Data and statistics: use subfolders for left sections.
  [GhitaB #84441]

- Making fields mandatory.
  [david-batranu]

- Fixing user schema fields.
  [david-batranu]

- Updated Reimbursment field tooltip text
  [irina-botez]

- pdated post registration message
  [irina-botez]

- Fix border right as in mockup in Data and statistics.
  [GhitaB #84441]

- Country view: edit text button.
  [GhitaB #84441]

- Data and statistics.
  [GhitaB #84441]

- Added getLocalNews script
  [tiberiuichim]

- More links - get rid of fa icon.
  [GhitaB #84441]

- Adding tooltip for Eionet users.
  [GhitaB #83535]

- Handle no JS and split js and css.
  [david-batranu #83535]

- Country view: svg icons.
  [GhitaB #84441]

- Notify new subscriber event.
  [david-batranu #83535]

- Signup form implementation.
  [david-batranu #83535]

- Country view: tabs icons.
  [GhitaB #84441]

- Fixed fields for empty values on adding user.
  [GhitaB #83535]

- Redirect to login and back to meeting - register related.
  [GhitaB #83535]

- Prevent error by listing only Event objects in events t
  [GhitaB #83535]

- Prevent error by listing only eea.meeting objects in me
  [GhitaB #83535]

- Show register form in meetings table only of registrati
  [GhitaB #83535]

- Remove unused script.
  [GhitaB #83535]

- Fix typo.
  [GhitaB #83535]

- get_subscriber_roles view, to prevent Unautorized for a
  [GhitaB #83535]

- Use values from vocabulary in register form.
  [GhitaB #83535]

- Add form with role and reimbursed on register subscriber.
  [GhitaB #83535]

- Add subscriber_roles vocabulary.
  [GhitaB #83535]

- Fix Events portlet to filter by country in its subpages.
  [GhitaB #83042]

- Fix Events portlet to filter by country in its subpages.
  [GhitaB #83042]

- Fix News portlet to filter by country in its subpages.
  [GhitaB #83042]

- Update template for portlet_local_news with copy from E
  [GhitaB #83042]

- Fix upgrade step.
  [GhitaB #82545]

- Add new fields for user, register page, profile.
  [GhitaB #82545]

- long_description not primary. Fix error of collective.f
  [GhitaB #82889]

- Adding dependency to ATVocabularyManager.
  [david-batranu]

- Script was updated in portal_skins/custom.
  [david-batranu]

- added button menu for meetings
  [mihai-macaneata]

- Added tinymce themes override
  [tiberiuichim]

- Make countries field multivalued
  [tiberiuichim]

- Added ICountries behavior to match atschemaextender subtype
  [tiberiuichim]

- Add countries on News; Tabular view for news.
  [melish]

- Add Countries on Event and add custom view for Events listing
  [melish]

- Remove unused Events section in Homepage.
  [GhitaB #74679]

- Docs: how to disable diazo, use classic theme.
  [GhitaB #71544]

- Fix site description on banner in homepage.
  [GhitaB #71544]

- Fix broken design in events list.
  [GhitaB #71544]

- Docs: homepage text from sections.
  [GhitaB #71544]

- Solution for svg countries map. Update docs.
  [GhitaB #71544]

- Docs: fix portlets. Newsletter.
  [GhitaB #71544]

- Update docs: html_index.
  [GhitaB #71544]

- Fix eventh month show first 3 letters.
  [GhitaB #71544]

- Docs: add example configuration.
  [GhitaB #71544]

- Add views to check website type. Update docs.
  [GhitaB #71544]

- Update config details docs.
  [GhitaB #71544]

- Update events section.
  [GhitaB #71544]

- Move config to template for easy later customization.
  [GhitaB #71544]

- Use script for events in homepage.
  [GhitaB #71544]

- Website title based on website type.
  [GhitaB #71544]

- Fix typo.
  [GhitaB #71544]

- Fix homepage content using website configuration.
  [GhitaB #71544]

- East vs south website configuration.
  [GhitaB #71544]

- Fix Homepage sections urls.
  [GhitaB #71544]

- Fix events-calendar url in events section.
  [GhitaB #71544]

- Add sections content on Homepage.
  [GhitaB #71544]

- Add site structure for EAST and SOUTH.
  [GhitaB #71641]

- Use data-diazo attr to mark events section.
  [GhitaB #71544]

- Homepage: order events by start date, ascending.
  [GhitaB #71544]

- Homepage - Events section.
  [GhitaB #71544]

- Add site structure
  [david-batranu]

- Fix Generic setup profile
  [david-batranu]

- Initial release.
  [anton16]
