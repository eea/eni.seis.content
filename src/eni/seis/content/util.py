from plone import api
from eni.seis.content.interfaces import IEniSeisEastContentLayer
from eni.seis.content.interfaces import IEniSeisSouthContentLayer


def is_east_website(request):
    return IEniSeisEastContentLayer.providedBy(request)


def is_south_website(request):
    return IEniSeisSouthContentLayer.providedBy(request)


def portal_absolute_url():
    return api.portal.get().absolute_url()
