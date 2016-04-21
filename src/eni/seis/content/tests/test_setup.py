# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from eni.seis.content.testing import ENI_SEIS_CONTENT_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that eni.seis.content is properly installed."""

    layer = ENI_SEIS_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if eni.seis.content is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'eni.seis.content'))

    def test_browserlayer(self):
        """Test that IEniSeisContentLayer is registered."""
        from eni.seis.content.interfaces import (
            IEniSeisContentLayer)
        from plone.browserlayer import utils
        self.assertIn(IEniSeisContentLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = ENI_SEIS_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['eni.seis.content'])

    def test_product_uninstalled(self):
        """Test if eni.seis.content is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'eni.seis.content'))

    def test_browserlayer_removed(self):
        """Test that IEniSeisContentLayer is removed."""
        from eni.seis.content.interfaces import IEniSeisContentLayer
        from plone.browserlayer import utils
        self.assertNotIn(IEniSeisContentLayer, utils.registered_layers())
