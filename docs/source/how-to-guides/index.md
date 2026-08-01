---
myst:
  html_meta:
    "description": "Cloudflare Turnstile integration with Plone how-to guides"
    "property=og:description": "Cloudflare Turnstile integration with Plone how-to guides"
    "property=og:title": "Cloudflare Turnstile integration with Plone how-to guides"
    "keywords": "Cloudflare, Turnstile, service, Plone, integration, documentation, how-to, guides"
---

# General information

This part of the documentation contains how-to guides, including installation and usage.

## Features

- Control panel in {term}`Plone` registry to manage {term}`Cloudflare Turnstile Settings`.

- A Restricted RESTful API endpoint that exposes the {term}`Cloudflare Turnstile Settings` for {term}`Volto` _integration_.

- A Public RESTful API endpoint to get the {term}`Site key` from the {term}`Cloudflare Turnstile Settings` settings.

## Volto integration

To use this product in {term}`Volto`, you needs to include the following {term}`add-on` in your project: {term}`volto-turnstile`.

## Translations

This product has been translated into

- English

- Spanish

## Compatibility

- Tested with Python 3.12 and {term}`Plone` 6.1.5.

## Install it

Install {term}`collective.volto.turnstile` with `pip`:

```shell
pip install collective.volto.turnstile
```

## Enable it

Go to the `Site setup`, next to the `Add-ons` control panel, find the `collective.volto.turnstile` {term}`add-on` and click on the `Install` button. 

Visit http://localhost:8080/ in a browser, login, create a {term}`Plone` site, enabled the {term}`add-on` and check the awesome new features.

## Settings it

To use this {term}`add-on`, go to the `Site setup`, next to the ``Add-on Configuration`` icon, as shown below:

<img width="290" alt="Add-on Configuration" src="../images/addon-configuration-cloudflare-turnstile-icon.png">

This {term}`Cloudflare Turnstile Settings`, you can access the control panel, as shown below:

<img width="720" alt="Cloudflare Turnstile Settings" src="../images/cloudflare-turnstile-settings.png">

In this control panel, you can configure the following fields:

- {term}`Site Key`, **(public key)**.

- {term}`Secret Key`, **(private key)**.

## Use it

To use the {term}`Cloudflare Turnstile` integration you need add the {term}`volto-turnstile` {term}`add-on`, in your {term}`Volto` project and
use the amazain features incluided.
