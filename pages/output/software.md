---
title: Software
description: We develop open source software tools
background: https://images.unsplash.com/photo-1547954575-855750c57bd3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1500&q=80
permalink: /software/
toc: true
---

## Bird migration flow visualization

**JS**{:.badge .bg-dark} An interactive flow visualization of bird migration as detected by weather radars. Inspired by [air](http://air.nullschool.net) and developed for the [European Network for the Radar Surveillance of Animal Movement (ENRAM)](http://enram.eu). See [Shamoun-Baranes et al. 2016](https://doi.org/10.1371/journal.pone.0160106) for a paper describing the visualization. It was also used to visualize bird migration over Europe for [Nilsson et al. 2019](https://doi.org/10.1111/ecog.04003) ([download movie](https://zenodo.org/record/1172801/files/cartoviz.mov?download=1)).

{:.btn-group}
[Website](http://aloftdata.github.io/bird-migration-flow-visualization/viz/){:.btn .btn-sm .btn-primary}
[Source code](https://github.com/aloftdata/bird-migration-flow-visualization){:.btn .btn-sm .btn-light}

## CartoDB visualizations

**CartoDB**{:.badge .bg-dark} See our [blog posts](/blog?tag=CartoDB) on how we have visualized bird migration and tracking data with CartoDB.

## CROW

**JS**{:.badge .bg-dark} CROW is an online tool to visualize birds detected by weather radars. It pulls real-time open data of the Royal Meteorological Institute of Belgium (RMI) and visualizes it in the browser.

{:.btn-group}
[Website](https://www.meteo.be/birddetection){:.btn .btn-sm .btn-primary}
[Blog post](/blog/crow){:.btn .btn-sm .btn-light}
[Source code](https://github.com/inbo/crow){:.btn .btn-sm .btn-light}

## LIFE MICA dashboard

The MICA dashboard gives a comprehensive overview of all muskrat and coypu observations (both catches and field observations) in Flanders, the Netherlands and certain areas in Germany. The available data is automatically refreshed daily from [GBIF](https://www.gbif.org).

{:.btn-group}
[Website](http://mica.inbo.be/){:.btn .btn-sm .btn-primary}
[Source code](https://github.com/inbo/mica-dashboard){:.btn .btn-sm .btn-light}

## LIFE RIPARIAS early alert

The LIFE RIPARIAS early alert website allows field managers to be immediately aware when new observations of invasive species occur in Belgium by providing a flexible e-mail notification mechanism. The available data is automatically refreshed daily from [GBIF](https://www.gbif.org).

{:.btn-group}
[Website](https://alert.riparias.be){:.btn .btn-sm .btn-primary}
[Source code](https://github.com/riparias/early-warning-webapp){:.btn .btn-sm .btn-light}

## Vespa-Watch

**Python**{:.badge .bg-dark} Vespa-Watch is a website where citizen scientists can submit observations of [_Vespa velutina_](https://www.inaturalist.org/taxa/119019-Vespa-velutina), an invasive species in Belgium. The data are automatically synchronized with [iNaturalist](https://www.inaturalist.org/) for verification and used to manage the spread of the species.

{:.btn-group}
[Website](https://vespawatch.be){:.btn .btn-sm .btn-primary}
[Source code](https://github.com/inbo/vespa-watch){:.btn .btn-sm .btn-light}

## vptstools

**Python**{:.badge .bg-dark} vptstools is used in an operational pipeline to process incoming biological data derived from European weather radars. It reformats and deposits the data on the Aloft bucket, where it can be used by the radar aeroecology community.

{:.btn-group}
[Website](https://aloftdata.eu/browse/){:.btn .btn-sm .btn-primary}
[Source code](https://github.com/aloftdata/vptstools){:.btn .btn-sm .btn-light}

## Whip

**YAML**{:.badge .bg-dark} Whip is a human and machine-readable syntax to express specifications for data. We use it with the [pywhip](https://inbo.github.io/pywhip/) package to document and test if data provided by our partners meet the necessary requirements for publication. See [Van Hoey & Desmet 2018](https://speakerdeck.com/peterdesmet/whip-communicate-and-test-what-to-expect-from-data) for a presentation.

{:.btn-group}
[Documentation](https://github.com/inbo/whip/blob/master/docs/syntax.md){:.btn .btn-sm .btn-primary}
[Source code](https://github.com/inbo/whip){:.btn .btn-sm .btn-light}
