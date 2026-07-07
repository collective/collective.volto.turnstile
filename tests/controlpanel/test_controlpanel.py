"""Tests for the CloudflareTurnstileEditForm controlpanel."""

from collective.volto.turnstile.controlpanels.cloudflare_turnstile_settings import (
    CloudflareTurnstileControlPanel,
)
from collective.volto.turnstile.controlpanels.cloudflare_turnstile_settings import (
    CloudflareTurnstileEditForm,
)
from unittest.mock import patch


class TestCloudflareTurnstileEditForm:
    def test_update_fields_delegates_to_super(self):
        with patch.object(
            CloudflareTurnstileEditForm.__bases__[0], "updateFields"
        ) as mock_uf:
            form = object.__new__(CloudflareTurnstileEditForm)
            form.updateFields()
        mock_uf.assert_called_once()

    def test_update_widgets_delegates_to_super(self):
        with patch.object(
            CloudflareTurnstileEditForm.__bases__[0], "updateWidgets"
        ) as mock_uw:
            form = object.__new__(CloudflareTurnstileEditForm)
            form.updateWidgets()
        mock_uw.assert_called_once()

    def test_control_panel_uses_edit_form(self):
        assert CloudflareTurnstileControlPanel.form is CloudflareTurnstileEditForm
