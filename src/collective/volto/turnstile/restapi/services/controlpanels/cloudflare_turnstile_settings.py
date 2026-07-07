from plone.restapi.controlpanels import RegistryConfigletPanel
from collective.volto.turnstile.interfaces import ICloudflareTurnstileSettings
from collective.volto.turnstile.interfaces import ICloudflareTurnstileSettingsControlpanel
from zope.component import adapter
from zope.interface import implementer
from zope.interface import Interface


@adapter(Interface, Interface)
@implementer(ICloudflareTurnstileSettingsControlpanel)
class CloudflareTurnstileSettingsControlpanel(RegistryConfigletPanel):
    """Volto control panel for Cloudflare Turnstile settings."""

    schema = ICloudflareTurnstileSettings
    configlet_id = "CloudflareTurnstileSettings"
    configlet_category_id = "Products"
    schema_prefix = "cloudflare-turnstile"
