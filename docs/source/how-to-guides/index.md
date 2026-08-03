---
myst:
  html_meta:
    "description": "Cloudflare Turnstile integration with Plone how-to guides"
    "property=og:description": "Cloudflare Turnstile integration with Plone how-to guides"
    "property=og:title": "Cloudflare Turnstile integration with Plone how-to guides"
    "keywords": "Cloudflare, Turnstile, service, Plone, integration, documentation, how-to, guides"
---

# General information

This part of the documentation contains how-to guides, and including installation and usage.

## Features

- Control panel in {term}`Plone` registry to manage {term}`Cloudflare Turnstile Settings`.

- A Restricted RESTful API endpoint that exposes the {term}`Cloudflare Turnstile Settings` for {term}`Volto` _integration_.

- A Public RESTful API endpoint to get the {term}`Site key` from the {term}`Cloudflare Turnstile Settings` settings.

## Volto integration

To use this product in {term}`Volto`, you needs to include the following {term}`add-on` in your project: {term}`volto-turnstile`.

## Translations

This product support the following languages:

- English

- Spanish

## Compatibility

- Tested with `Python` 3.12 and {term}`Plone` 6.1.5.

## Install it

To install in your project, the {term}`collective.volto.turnstile` {term}`add-on` with `pip` command:

```shell
pip install collective.volto.turnstile
```

## Enable it

Visit http://localhost:8080/Plone in a browser, login, so go to `Site setup`, next to `Add-ons` control panel,
find the {term}`collective.volto.turnstile` {term}`add-on` and select the `Install` button for enabled it.

## Settings it

To use this {term}`add-on`, go to the `Site setup`, next to the ``Add-on Configuration`` icon, as shown below:

<img width="290" alt="Add-on Configuration" src="../images/addon-configuration-cloudflare-turnstile-icon.png">

This {term}`Cloudflare Turnstile Settings`, you can access the control panel, as shown below:

<img width="720" alt="Cloudflare Turnstile Settings" src="../images/cloudflare-turnstile-settings.png">

In this control panel, you can configure the following fields:

- {term}`Site Key`, **(public key)**.

- {term}`Secret Key`, **(private key)**.

## Use it

To use the {term}`Cloudflare Turnstile` integration you need add the {term}`volto-turnstile` {term}`add-on`, in
your {term}`Volto` project and use the amazing features into this {term}`add-on.

```{tip}
For example, to secure your forms, you need yo use the {term}`TurnstileWidget` component from the {term}`volto-turnstile`
{term}`add-on` in your source code forms.
```
