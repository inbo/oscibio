---
title: frictionless 1.1.0
description: We released a new version of our R package frictionless.
background: https://images.unsplash.com/photo-1696778083008-cf105a901e30?q=80&w=2370&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
author: Peter Desmet
tags: [LifeWatch, software, R]
toc: true
---

Our R package **frictionless** allows you to read and write Frictionless [Data Packages](https://specs.frictionlessdata.io/data-package/). A Data Package is a simple container format and standard to describe and package a collection of (tabular) data. It is typically used to publish [FAIR](https://www.go-fair.org/fair-principles/) and open datasets. We use it in the [LifeWatch](/projects/#lifewatch) project to publish our [bird tracking](https://github.com/inbo/bird-tracking?tab=readme-ov-file#datasets), [fish tracking](https://github.com/inbo/etn-occurrences?tab=readme-ov-file#datasets) and [camera trap data](https://camtrap-dp.tdwg.org/).

We developed the R package [frictionless](https://docs.ropensci.org/frictionless/) to facilitate our work, but it has since been picked up by other users and developers. Much of the feedback we gathered is now incorportated in a new release of the package: version 1.1.0.

## How to install frictionnless?

The package is available on CRAN and can be installed with:

```R
install.packages("frictionless")
```

For more information, see the [package documentation](https://docs.ropensci.org/frictionless/).

## What has changed?

Quite a lot. See the [CHANGELOG](https://docs.ropensci.org/frictionless/news/index.html#frictionless-110).

## What is next?

The Data Package standard is currently [undergoing changes](https://frictionlessdata.io/blog/2023/11/15/frictionless-specs-update/) to be released as a finalized product (Data Package v2), a process we are involved in. We plan to support these changes (and new features!) in an upcoming version of frictionless, so there's more to come!
