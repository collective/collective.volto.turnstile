---
myst:
  html_meta:
    "description": "Cloudflare Turnstile integration with Plone how-to guides"
    "property=og:description": "Cloudflare Turnstile integration with Plone how-to guides"
    "property=og:title": "Cloudflare Turnstile integration with Plone how-to guides"
    "keywords": "Plone, Cloudflare Turnstile integration with Plone, how-to, guides"
---

# How-to guides

This part of the documentation contains how-to guides, including installation and usage.

## Features

- Control panel in Plone registry to manage ``Cloudflare Turnstile`` settings.
- RestApi endpoint that exposes these settings for Volto.

## Volto integration

To use this product in Volto, your Volto project needs to include a new add-on: https://github.com/collective/volto-acumbamail

## Translations

This product has been translated into

- English
- Spanish

## Compatibility

- Tested with Python 3.12 and Plone 6.1.5.

## Install it

Install `collective.volto.turnstile` with `pip`:

```shell
pip install collective.volto.turnstile
```

## Enable it

Go to the `Site setup`, next to the `Add-ons` control panel, find the `collective.volto.turnstile` add-on and click on the `Install` button. 

## Use it

To use this add-on, go to the `Site setup`, next to the ``Add-on Configuration`` icon, as shown below:

<img width="290" alt="image" src="../../images/addon-configuration-cloudflare-turnstile-icon.png" alt="Add-on Configuration">

This `Cloudflare Turnstile Settings`, you can access the control panel, as shown below:

<img width="720" alt="image" src="../../images/cloudflare-turnstile-settings.png" alt="Cloudflare Turnstile Settings">

In this control panel, you can configure the following fields:

- ``Site Key`` **(public key)**.

- ``Site Secret`` **(private key)**.

## Security access

The  `collective.volto.turnstile` add-on includes the following roles and permissions:

### Roles

- ``Cloudflare Turnstile`` role (**NEW!!!**).

### Permissions

- ``volto.turnstile: Manage Cloudflare Turnstile Settings`` permission (**NEW!!!**) grants access to the following roles:

  - ``Cloudflare Turnstile`` role.

- The ``Plone Site Setup: Overview`` permission grants access to the `Site Setup: Overview ` view to the following roles:

  - The ``Manager`` role.

  - The ``Site Administrator`` role.

  - The ``Cloudflare Turnstile`` role.
