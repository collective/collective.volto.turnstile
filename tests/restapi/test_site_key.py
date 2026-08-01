"""Tests for the Turnstile Site Key endpoint."""

from collective.volto.turnstile.testing import RESTAPI_TESTING
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.app.testing import TEST_USER_ID
from plone.restapi.testing import RelativeSession
from transaction import commit
from unittest import mock

import unittest


class TurnstileSiteKeyEndpointTest(unittest.TestCase):
    """Test the @cloudflare-turnstile-sitekey endpoint."""

    layer = RESTAPI_TESTING

    def setUp(self):
        """Set up the test."""
        self.app = self.layer["app"]
        self.portal = self.layer["portal"]
        self.portal_url = self.portal.absolute_url()
        self.endpoint_url = "/@cloudflare-turnstile-sitekey"

        self.api_session = RelativeSession(self.portal_url)
        self.api_session.headers.update({"Accept": "application/json"})
        self.api_session.auth = (SITE_OWNER_NAME, SITE_OWNER_PASSWORD)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

        self.page = api.content.create(
            container=self.portal, type="Document", title="Test Page"
        )
        commit()

    def tearDown(self):
        """Clean up after the test."""
        self.api_session.close()

    def test_endpoint_returns_site_key_from_registry(self):
        """Test that the endpoint returns the site key from the registry."""
        # Set a test site key in the registry
        test_site_key = "1x00000000000000000000BB"
        api.portal.set_registry_record(
            "cloudflare-turnstile.site_key",
            test_site_key,
        )
        commit()

        # Make request to the endpoint
        response = self.api_session.get(self.endpoint_url)

        # Verify response
        self.assertEqual(response.status_code, 200)
        self.assertIn("application/json", response.headers.get("Content-Type", ""))

        data = response.json()
        self.assertIn("@id", data)
        self.assertIn("site_key", data)
        self.assertEqual(data["site_key"], test_site_key)
        self.assertTrue(data["@id"].endswith(self.endpoint_url))

    def test_endpoint_accessible_to_anonymous_users(self):
        """Test that the endpoint is accessible to anonymous users."""
        # Create an anonymous session (no authentication)
        anon_session = RelativeSession(self.portal_url)
        anon_session.headers.update({"Accept": "application/json"})

        # Set a site key for testing
        test_site_key = "1x00000000000000000000CC"
        api.portal.set_registry_record(
            "cloudflare-turnstile.site_key",
            test_site_key,
        )
        commit()

        try:
            # Make request without authentication
            response = anon_session.get(self.endpoint_url)

            # Verify that anonymous users can access the endpoint
            self.assertEqual(response.status_code, 200)
            data = response.json()
            self.assertIn("site_key", data)
            self.assertEqual(data["site_key"], test_site_key)
        finally:
            anon_session.close()

    def test_endpoint_handles_exceptions(self):
        """Test that the endpoint handles exceptions gracefully."""
        # Mock api.portal.get_registry_record to raise an exception
        with mock.patch(
            "collective.volto.turnstile.restapi.services.turnstile.site_key.api.portal.get_registry_record"
        ) as mock_get_record:
            mock_get_record.side_effect = Exception("Registry error")

            # Make request to the endpoint
            response = self.api_session.get(self.endpoint_url)

            # Verify response - should still return 200 with default key
            self.assertEqual(response.status_code, 200)
            data = response.json()
            self.assertIn("site_key", data)
            self.assertIn("error", data)
            # Should return the default test key even on error
            self.assertEqual(data["site_key"], "1x00000000000000000000AA")
            self.assertEqual(data["error"], "Registry error")

    def test_endpoint_response_structure(self):
        """Test that the endpoint response has the correct structure."""
        # Set a site key
        api.portal.set_registry_record(
            "cloudflare-turnstile.site_key",
            "test-key-123",
        )
        commit()

        # Make request
        response = self.api_session.get(self.endpoint_url)
        data = response.json()

        # Verify structure
        self.assertIsInstance(data, dict)
        self.assertIn("@id", data)
        self.assertIn("site_key", data)
        self.assertIsInstance(data["@id"], str)
        self.assertIsInstance(data["site_key"], str)
