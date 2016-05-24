from Products.Five.browser import BrowserView
from eni.seis.content.util import portal_absolute_url
from eni.seis.content.util import is_east_website
from eni.seis.content.util import is_south_website


class WebsiteTitleHtmlView(BrowserView):
    """ A view used to prepare html website title
        <h1 class="east">
            <a href="">ENI SEIS II <strong>East</strong></a>
        </h1>

        or

        <h1 class="south">
            <a href="">ENI SEIS II <strong>South</strong></a>
        </h1>
    """

    def __call__(self):
        if is_east_website(self.request):
            html_title = "<h1 class='east'><a href='" + \
                portal_absolute_url() + \
                "'>ENI SEIS II <strong>East</strong></a></h1>"
        elif is_south_website(self.request):
            html_title = "<h1 class='south'><a href='" + \
                portal_absolute_url() + \
                "'>ENI SEIS II <strong>South</strong></a></h1>"
        else:
            html_title = "Website config missing."
        return html_title
