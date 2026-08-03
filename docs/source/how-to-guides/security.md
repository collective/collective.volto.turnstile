---
myst:
  html_meta:
    "description": "Cloudflare Turnstile integration with Plone how-to guides"
    "property=og:description": "Cloudflare Turnstile Plone how-to guides"
    "property=og:title": "Cloudflare Turnstile integration with Plone how-to guides"
    "keywords": "Cloudflare, Turnstile, service, Plone, integration, documentation, how-to, guides"
---

# Security access

The {term}`collective.volto.turnstile` {term}`add-on` includes the following roles and permissions:

## Roles

- ``Cloudflare Turnstile`` role.

  ```{note}
  New feature inclueded in this {term}`add-on`.
  ```

## Permissions

- ``volto.turnstile: Manage Cloudflare Turnstile Settings``

  ```{note}
  New feature inclueded in this {term}`add-on`.
  ```

  This permission grants access to the following roles:

  - ``Cloudflare Turnstile`` role.

    ```{tip}
    If to grant this role to a user, this inherited the permissions that included, and there are details bellow:
    ```

- The ``Plone Site Setup: Overview`` permission grants access to the `Site Setup: Overview ` view to the following roles:

  - The ``Manager`` role.

  - The ``Site Administrator`` role.

  - The ``Cloudflare Turnstile`` role.
