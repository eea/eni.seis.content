# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import eni.seis.content


class EniSeisContentLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=eni.seis.content)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'eni.seis.content:default')


ENI_SEIS_CONTENT_FIXTURE = EniSeisContentLayer()


ENI_SEIS_CONTENT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ENI_SEIS_CONTENT_FIXTURE,),
    name='EniSeisContentLayer:IntegrationTesting'
)


ENI_SEIS_CONTENT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ENI_SEIS_CONTENT_FIXTURE,),
    name='EniSeisContentLayer:FunctionalTesting'
)


ENI_SEIS_CONTENT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ENI_SEIS_CONTENT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='EniSeisContentLayer:AcceptanceTesting'
)
