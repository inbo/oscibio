# LifeWatch INBO blog

This repository contains the content and settings for the [LifeWatch INBO blog](http://lifewatch.inbo.be/blog). It is generated as a static website with [Pelican](http://docs.getpelican.com).

## Getting started

[See the contributing guide](CONTRIBUTING.md)

## Repo structure

Files and directories indicated with `GENERATED` should not be edited manually.

```
├── README.md         : Description of this repository
├── LICENSE           : Repository license
├── .gitignore        : Files and directories to be ignored by git
│
├── settings-local.py : Local settings for Pelican, generates website in "docs-local"
├── settings.py       : Production settings for Pelican, generates website in "docs" (used by GitHub pages)
│
├── content
│   ├── extra         : Static files that need to go in website root
│   ├── files         : Static files (e.g. pdfs)
│   ├── images        : Static images (e.g. screenshots)
│   ├── pages         : Website pages (in Markdown)
│   └── posts         : Website posts (in Markdown)
│
└── docs              : Website GENERATED
```

## Deployment

### Installation

1. Verify Python 3.3+ is installed: `python -V`
2. Install [Pelican](http://docs.getpelican.com/en/stable/install.html) (the static site generator): `pip install pelican`
3. Install the [Python implementation of Markdown](https://pypi.python.org/pypi/Markdown): `pip install markdown`
5. Clone the theme repo: `git clone https://github.com/inbo/eurasian-spoonbill`
6. Clone the website repo: `git clone https://github.com/inbo/lifewatch-blog`

### Build site

1. Navigate to the website directory: `cd lifewatch-blog`
2. Build the site:
    * Locally: `pelican -s settings-local.py` → website is generated in `docs-local/`
    * For the actual website: `pelican -s settings.py` → website is generated in `docs/`

## Contributors

[List of contributors](https://github.com/inbo/lifewatch-blog/contributors)

## License

This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
