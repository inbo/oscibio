---
title: frictionless 1.3.0
description: We released a new version of our R package frictionless.
background: https://images.unsplash.com/photo-1722797337046-9102a0ded0bd?q=80&w=1282&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
author: Peter Desmet
tags: [LifeWatch, software, R]
toc: true
---

We just released a new version (1.3.0) of our R package **frictionless**.

With frictionless you can read and write Frictionless Data
Packages. A [Data Package](https://specs.frictionlessdata.io/data-package/) is a simple container format and standard to describe and package a collection of (tabular) data. It is typically used to publish
[FAIR](https://www.go-fair.org/fair-principles/) and open datasets. We use it extensively for publishing datasets.

## What has changed?

frictionless 1.3.0 will be the last release that adopts [version 1 of the Data Package standard](https://specs.frictionlessdata.io/). The next release (frictionless 2.0.0) will adopt [Data Package version 2](https://datapackage.org/). So we wanted to incorporate the necessary changes for users who want to stick with version 1, such as indicating what version of the standard is read, warning them if a version is unsupported, etc. The release also includes a number of improvements, deprecations and functions that are useful for developers.

{:.alert .alert-info}
This work was funded by the NLnet foundation as part of the [Frictionless Libraries](https://nlnet.nl/project/Frictionless-Libs/) project.

## Changes for users

* New `version()` determines what version of the Data Package standard is used by a Data Package (e.g. `"1.0"`, `"2.0"`, `">=2.0"`), based on the presence and value of the `$schema` property. This information is also returned by `print()`.
* `read_package()` now warns when reading a `datapackage.json` that uses a version of the Data Package standard not supported by frictionless (i.e. anything other than version `"1.0"`).
* `read_resource()` no longer guesses the type for fields without a `type`, but sets it to character (the default for a CSV). This aligns with a clarification in the [specification](https://datapackage.org/overview/changelog/#any-field-type-updated).
* `read_resource()` now supports reading from remote zip files, thanks to support in `{vroom}` (1.3.0).
* `add_resource()` with `replace = TRUE` adds the resource if there is none to replace, rather than throwing an error.
* `add_resource()` now retains the URL to a provided schema, rather than including it verbosely.
* `write_package()`'s overwrite behavior is now as intended and documented in the function.

For an overview of all the changes, including those for developers, see the [CHANGELOG](https://docs.ropensci.org/frictionless/news/index.html#frictionless-130).

## How to install frictionless?

The package is available on CRAN and can be installed with:

```R
install.packages("frictionless")
```

For more information, see the [package documentation](https://docs.ropensci.org/frictionless/). Found a bug? Please [report an issue](https://github.com/frictionlessdata/frictionless-r/issues).
