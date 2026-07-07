from plone.restapi.interfaces import ISerializeToJson
from plone.restapi.serializer.controlpanels import ControlpanelSerializeToJson
from sevilla.imd.website.interfaces import ICloudflareTurnstileSettingsControlpanel
from zope.component import adapter
from zope.interface import implementer

import logging


logger = logging.getLogger(__name__)


@implementer(ISerializeToJson)
@adapter(ICloudflareTurnstileSettingsControlpanel)
class CloudflareTurnstileSettingsSerializeToJson(ControlpanelSerializeToJson):
    def __call__(self):
        json_data = super().__call__()
        return json_data
