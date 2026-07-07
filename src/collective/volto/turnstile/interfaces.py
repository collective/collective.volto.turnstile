"""Module where all interfaces, events and exceptions live."""

from collective.volto.turnstile import _
from plone.restapi.controlpanels import IControlpanel
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ICloudflareTurnstileLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ICloudflareTurnstileSettingsControlpanel(IControlpanel):
    """Volto control panel for the Cloudflare Turnstile settings"""


class ICloudflareTurnstileSettings(Interface):
    """Cloudflare Turnstile connector configuration"""

    site_key = schema.TextLine(
        title=_("Site Key"),
        description=_("The Site Key of the Cloudflare Turnstile service."),
        required=True,
    )

    secret_key = schema.TextLine(
        title=_("Secret Key"),
        description=_("The Secret Key of the Cloudflare Turnstile service."),
        required=True,
    )
