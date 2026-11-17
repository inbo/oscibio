---
title: frictionless 2.0.0
description: We released a new version of our R package frictionless.
background:
  img: https://images.unsplash.com/photo-1621848296279-7751546e9acc?q=80&w=1790&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D
  by: Tienko Dima
  href: https://unsplash.com/photos/green-trees-beside-body-of-water-during-daytime-uYoVf9I6ANI
author: Peter Desmet
tags: [LifeWatch, NLnet, software, R]
toc: true
---

{:.alert .alert-info}
This work was funded by the NLnet foundation as part of the [Frictionless Libraries](https://nlnet.nl/project/Frictionless-Libs/) project. See the [announcement](https://blog.okfn.org/2026/11/05/announcing-data-package-v2-support-in-frictionless-r-and-python-libraries/) on the Open Knowledge Foundation blog.

We just released a new major version (2.0.0) of our R package **frictionless**.

With frictionless you can read and write Frictionless Data Packages. A [Data Package](https://datapackage.org/) is a simple container format and standard to describe and package a collection of (tabular) data. It is typically used to publish [FAIR](https://www.gofair.foundation/fair-principles) and open datasets. We use it extensively for publishing datasets.

## What has changed?

frictionless now supports Data Packages using the [v2](https://datapackage.org/) specification, while maintaining support for those using [v1](https://specs.frictionlessdata.io/). When creating a package, resource or schema, it uses the v2 specification.

* frictionless no longer relies on v1 properties deprecated in v2, meaning all functions support both versions. They always return a package, resource and schema in the same version as provided.
* `create_package()`, `add_resource()` and `create_schema()` create a v2 package, resource and schema respectively. **This can be a breaking change for some workflows!** Also note that this can lead to mixed versions (e.g. a v1 package with a v2 resource).
* `upgrade_package()` can be used to upgrade a package, its resources and verbose schemas from v1 to v2 (harmonizing mixed versions).

For an overview of all the changes, see the [CHANGELOG](https://docs.ropensci.org/frictionless/news/index.html#frictionless-200). Does your workflow rely on the v1 specification? Use [frictionless 1.3.0]({% post_url 2026-07-31-frictionless-1.3.0 %}).

## How to install frictionless?

The package is available on CRAN and can be installed with:

```R
install.packages("frictionless")
```

For more information, see the [package documentation](https://docs.ropensci.org/frictionless/). Found a bug? Please [report an issue](https://github.com/frictionlessdata/frictionless-r/issues).
