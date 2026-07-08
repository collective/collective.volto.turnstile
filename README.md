# collective.volto.turnstile

[![Latest Version](https://img.shields.io/pypi/v/collective.volto.turnstile.svg)](https://pypi.org/project/collective.volto.turnstile/)

[![Supported - Python Versions](https://img.shields.io/pypi/pyversions/collective.volto.turnstile.svg?style=plastic)](https://pypi.org/project/collective.volto.turnstile/)

[![Number of PyPI downloads](https://img.shields.io/pypi/dm/collective.volto.turnstile.svg)](https://pypi.org/project/collective.volto.turnstile/)

[![License](https://img.shields.io/pypi/l/collective.volto.turnstile.svg)](https://pypi.org/project/collective.volto.turnstile/)

[![Cloudflare Turnstile](https://raw.githubusercontent.com/collective/collective.volto.turnstile/refs/heads/main/docs/source/_static/logo.svg)](https://www.cloudflare.com/products/turnstile/)

An integration for the [Cloudflare Turnstile](https://www.cloudflare.com/products/turnstile/) service with Plone

## Features

- Control panel in Plone registry to manage ``Cloudflare Turnstile`` settings.
- RestApi endpoint that exposes these settings for Volto.


## Screenshot

**Add-on Configuration Access**

<img width="290" alt="Add-on Configuration" src="https://raw.githubusercontent.com/collective/collective.volto.turnstile/refs/heads/main/docs/images/addon-configuration-cloudflare-turnstile-icon.png">

---

**Cloudflare Turnstile Settings control panel**

<img width="720" alt="Cloudflare Turnstile Settings" src="https://raw.githubusercontent.com/collective/collective.volto.turnstile/refs/heads/main/docs/images/cloudflare-turnstile-settings.png">

## Volto integration

To use this product in Volto, your Volto project needs to include a new add-on: https://github.com/collective/volto-turnstile

## Translations

This product has been translated into

- English
- Spanish

## Compatibility

- Tested with Python 3.12 and Plone 6.1.5.

## Installation

Install `collective.volto.turnstile` with `pip`:

```shell
pip install collective.volto.turnstile
```

And to create the Plone site:

```shell
make create-site
```

## Contribute

- [Issue tracker](https://github.com/collective/collective.volto.turnstile/issues)
- [Source code](https://github.com/collective/collective.volto.turnstile/)
- [Documentation](https://collectivevoltoturnstile.readthedocs.io/)

### Prerequisites ✅

-   An [operating system](https://6.docs.plone.org/install/create-project-cookieplone.html#prerequisites-for-installation) that runs all the requirements mentioned.
-   [uv](https://6.docs.plone.org/install/create-project-cookieplone.html#uv)
-   [Make](https://6.docs.plone.org/install/create-project-cookieplone.html#make)
-   [Git](https://6.docs.plone.org/install/create-project-cookieplone.html#git)
-   [Docker](https://docs.docker.com/get-started/get-docker/) (optional)

### Installation 🔧

1.  Clone this repository, then change your working directory.

    ```shell
    git clone git@github.com:collective/collective.volto.turnstile.git
    cd collective.volto.turnstile
    ```

2.  Install this code base.

    ```shell
    make install
    ```


### Add features using `plonecli` or `bobtemplates.plone`

This package provides markers as strings (`<!-- extra stuff goes here -->`) that are compatible with [`plonecli`](https://github.com/plone/plonecli) and [`bobtemplates.plone`](https://github.com/plone/bobtemplates.plone).
These markers act as hooks to add all kinds of subtemplates, including behaviors, control panels, upgrade steps, or other subtemplates from `plonecli`.

To run `plonecli` with configuration to target this package, run the following command.

```shell
make add <template_name>
```

For example, you can add a content type to your package with the following command.

```shell
make add content_type
```

You can add a behavior with the following command.

```shell
make add behavior
```

#### See also:

You can check the list of available subtemplates in the [`bobtemplates.plone` `README.md` file](https://github.com/plone/bobtemplates.plone/?tab=readme-ov-file#provided-subtemplates).
See also the documentation of [Mockup and Patternslib](https://6.docs.plone.org/classic-ui/mockup.html) for how to build the UI toolkit for Classic UI.

## Credits

Developed with the support of:

- [Instituto Municipal de Deportes - IMD, Seville City Council, Spain](https://imd.sevilla.org/).

  <img width="200" alt="IMD Logo" src="https://raw.githubusercontent.com/collective/collective.volto.turnstile/refs/heads/main/docs/images/imd-ayto-logo.svg">

### Acknowledgements 🙏

Generated using [Cookieplone (0.9.10)](https://github.com/plone/cookieplone) and [cookieplone-templates (eb40854)](https://github.com/plone/cookieplone-templates/commit/eb4085428af6261227bcb086ece110bbe5475d89) on 2025-11-06 19:48:38.313942. A special thanks to all contributors and supporters!

## Authors

This product was developed by [Leonardo J. Caballero G.](https://github.com/macagua).

<img width="100" alt="Leonardo J. Caballero G." src="https://avatars.githubusercontent.com/u/185395?v=4&size=100">

### Contributors

You can see a list of contributors in the [CONTRIBUTORS.md](https://raw.githubusercontent.com/collective/collective.volto.turnstile/refs/heads/main/CONTRIBUTORS.md) file.

## License

The project is licensed under GPLv2.
