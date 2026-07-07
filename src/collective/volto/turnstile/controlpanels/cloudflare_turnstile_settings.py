from collective.volto.turnstile import _
from collective.volto.turnstile.interfaces import ICloudflareTurnstileSettings
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm


class CloudflareTurnstileEditForm(RegistryEditForm):
    schema = ICloudflareTurnstileSettings
    schema_prefix = "cloudflare-turnstile"
    label = _("Cloudflare Turnstile Settings")
    description = _("Define the credentials parameters for Cloudflare Turnstile.")

    def updateFields(self):
        super().updateFields()

    def updateWidgets(self):
        super().updateWidgets()


class CloudflareTurnstileControlPanel(ControlPanelFormWrapper):
    form = CloudflareTurnstileEditForm
