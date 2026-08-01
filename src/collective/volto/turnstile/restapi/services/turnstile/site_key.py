"""Public endpoint to get Cloudflare Turnstile site key.

This endpoint is public (no authentication required) because the site key
must be accessible to anonymous users for the Turnstile widget to work.
"""

from plone import api
from plone.restapi.services import Service


class TurnstileSiteKeyGet(Service):
    """Get the Cloudflare Turnstile site key (public endpoint)."""

    def reply(self):
        """Return the site key from registry settings."""
        try:
            # Get the site key from plone.app.registry
            site_key = api.portal.get_registry_record(
                "cloudflare-turnstile.site_key",
                default="1x00000000000000000000AA",
            )

            return {
                "@id": f"{self.context.absolute_url()}/@cloudflare-turnstile-sitekey",
                "site_key": site_key,
            }
        except Exception as e:
            # Log the error but return a default test key
            # to prevent the widget from breaking
            return {
                "@id": f"{self.context.absolute_url()}/@cloudflare-turnstile-sitekey",
                "site_key": "1x00000000000000000000AA",
                "error": str(e),
            }
