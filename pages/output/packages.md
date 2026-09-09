---
title: Packages
description: Our open source R and Python software packages
background: https://images.unsplash.com/photo-1546864831-f1ca1eaf4e2a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1500&q=80
permalink: /packages/
toc: true
---

[biorad]: http://adokter.github.io/bioRad
[biorad_github]: https://github.com/adokter/bioRad
[biorad_logo]: https://raw.githubusercontent.com/adokter/bioRad/master/man/figures/logo.png

[camtrapdp]: https://inbo.github.io/camtrapdp/
[camtrapdp_github]: https://github.com/inbo/camtrapdp

[camtraptor]: https://inbo.github.io/camtraptor/
[camtraptor_github]: https://github.com/inbo/camtraptor
[camtraptor_logo]: https://raw.githubusercontent.com/inbo/camtraptor/master/man/figures/logo.png

[etn]: https://inbo.github.io/etn/
[etn_github]: https://github.com/inbo/etn
[etn_logo]: https://raw.githubusercontent.com/inbo/etn/main/man/figures/logo.png

[frictionless]: https://docs.ropensci.org/frictionless/
[frictionless_github]: https://github.com/frictionlessdata/frictionless-r

[getrad]: https://aloftdata.github.io/getRad/
[getrad_github]: https://github.com/aloftdata/getRad

[movepub]: https://inbo.github.io/movepub/
[movepub_github]: https://github.com/inbo/movepub/

[pywhip]: https://inbo.github.io/pywhip/
[pywhip_github]: https://github.com/inbo/pywhip

[rgbif]: https://docs.ropensci.org/rgbif/
[rgbif_github]: https://github.com/ropensci/rgbif 
[rgbif_logo]: https://raw.githubusercontent.com/ropensci/rgbif/master/man/figures/logo.png

[trias]: https://trias-project.github.io/trias
[trias_github]: https://github.com/trias-project/trias
[trias_logo]: https://raw.githubusercontent.com/trias-project/trias/main/man/figures/logo.png

[waterinfo]: https://docs.ropensci.org/wateRinfo/
[waterinfo_github]: https://github.com/ropensci/wateRinfo
[waterinfo_logo]: https://raw.githubusercontent.com/ropensci/wateRinfo/main/man/figures/logo.png

<!--
### title [![logo][pkg_logo]{:width="120" .float-right}][pkg]

**R**{:.badge .bg-dark} **pkg title**: pkg description

{:.btn-group}
[Documentation][pkg]{:.btn .btn-sm .btn-primary}
[Source code][pkg_github]{:.btn .btn-sm .btn-light}
-->

## bioRad [![logo][biorad_logo]{:width="120" .float-right}][biorad]

**R**{:.badge .bg-dark} **Biological analysis and visualization of weather radar data**: Extract, visualize and summarize aerial movements of birds and insects from weather radar data. See [Dokter et al. 2019](https://doi.org/10.1111/ecog.04028) for a software paper describing the package and methodologies.

{:.btn-group}
[Documentation][biorad]{:.btn .btn-sm .btn-primary}
[Source code][biorad_github]{:.btn .btn-sm .btn-light}

## camtrapdp

**R**{:.badge .bg-dark} **Read and manipulate Camera Trap Data Packages (Camtrap DP)**: [Camtrap DP](https://camtrap-dp.tdwg.org) is a data exchange format for camera trap data. With camtrapdp you can read, filter and transform data (including to [Darwin Core](https://dwc.tdwg.org)) before further analysis in e.g. [camtraptor](https://inbo.github.io/camtraptor/) or [camtrapR](https://cran.r-project.org/package=camtrapR).

{:.btn-group}
[Documentation][camtrapdp]{:.btn .btn-sm .btn-primary}
[Source code][camtrapdp_github]{:.btn .btn-sm .btn-light}

## camtraptor [![logo][camtraptor_logo]{:width="120" .float-right}][camtraptor]

**R**{:.badge .bg-dark} **Explore and Visualize Camera Trap Data Packages**: It offers a step-by-step workflow to read Camtrap DP files, filter data of interest, summarize information (e.g. number of observed species) and visualize this per deployment on an interactive map. You can also use it to transform data for analysis in [camtrapR](https://cran.r-project.org/package=camtrapR).

{:.btn-group}
[Documentation][camtraptor]{:.btn .btn-sm .btn-primary}
[Source code][camtraptor_github]{:.btn .btn-sm .btn-light}

## etn [![logo][etn_logo]{:width="120" .float-right}][etn]

**R**{:.badge .bg-dark} **Access data from the European Tracking Network (ETN)**: With etn you can query metadata (animals, tags, deployments, receivers, projects) and data (acoustic detections, sensor data) from the [ETN](https://www.lifewatch.be/etn/) database and use these in your analyses. Data access requires user credentials and is subject to a data policy.

{:.btn-group}
[Documentation][etn]{:.btn .btn-sm .btn-primary}
[Source code][etn_github]{:.btn .btn-sm .btn-light}

## frictionless

**R**{:.badge .bg-dark} **Read and write Frictionless Data Packages**: A [Data Package](https://specs.frictionlessdata.io/data-package/) is a simple container format and standard to describe and package a collection of (tabular) data. It is typically used to publish [FAIR](https://www.go-fair.org/fair-principles/) and open datasets.

{:.btn-group}
[Documentation][frictionless]{:.btn .btn-sm .btn-primary}
[Source code][frictionless_github]{:.btn .btn-sm .btn-light}

## getRad

**R**{:.badge .bg-dark} **Download radar data for biological research**: It gives access to both polar volume radar data and [vertical profile data](https://aloftdata.eu/vpts-csv/) from [different sources](https://aloftdata.github.io/getRad/articles/supported_sources.html) and loads it directly into R. getRad also facilitates further exploration of the data by other tools such as [bioRad](#bioRsad) by standardizing the data.

{:.btn-group}
[Documentation][getrad]{:.btn .btn-sm .btn-primary}
[Source code][getrad_github]{:.btn .btn-sm .btn-light}

## movepub

**R**{:.badge .bg-dark} **Prepare Movebank data for publication**: With movepub you can document data with metadata following the [Data Package](https://datapackage.org) standard and transform these to [Darwin Core](https://dwc.tdwg.org) and Ecological Metadata Language ([EML](https://eml.ecoinformatics.org/)) for publication to the Global Biodiversity Information Facility ([GBIF](https://www.gbif.org)) and the Ocean Biodiversity Information System ([OBIS](https://obis.org)).

{:.btn-group}
[Documentation][movepub]{:.btn .btn-sm .btn-primary}
[Source code][movepub_github]{:.btn .btn-sm .btn-light}

## pywhip

**Python**{:.badge .bg-dark} **Validate data against whip specifications**: pywhip is a Python package to validate data against [whip specifications](https://github.com/inbo/whip), a human and machine-readable syntax to express specifications for data.

{:.btn-group}
[Documentation][pywhip]{:.btn .btn-sm .btn-primary}
[Source code][pywhip_github]{:.btn .btn-sm .btn-light}

## rgbif [![logo][rgbif_logo]{:width="120" .float-right}][rgbif]

**R**{:.badge .bg-dark} **Interface to the Global Biodiversity Information Facility API**: rgbif gives you access to [GBIF](https://www.gbif.org/) mediated data via its [REST API](https://www.gbif.org/developer/summary). GBIF (the Global Biodiversity Information Facility) is an international network and data infrastructure funded by the world's governments and aimed at providing anyone, anywhere, open access to data about all types of life on Earth.

{:.btn-group}
[Documentation][rgbif]{:.btn .btn-sm .btn-primary}
[Source code][rgbif_github]{:.btn .btn-sm .btn-light}

## trias [![logo][trias_logo]{:width="120" .float-right}][trias]

**R**{:.badge .bg-dark} **Process data for the project Tracking Invasive Alien Species (TrIAS)**: trias was originally conceived to provide functionalities for the [Tracking Invasive Alien Species (TrIAS)](https://trias-project.be) project. However, it has been further developed to support other similar projects, such as the [LIFE RIPARIAS](https://www.riparias.be) and [B-Cubed](https://docs.b-cubed.eu/) projects.

{:.btn-group}
[Documentation][trias]{:.btn .btn-sm .btn-primary}
[Source code][trias_github]{:.btn .btn-sm .btn-light}

## wateRinfo [![logo][waterinfo_logo]{:width="120" .float-right}][waterinfo]

**R**{:.badge .bg-dark} **Download time series data from Waterinfo.be**: wateRinfo facilitates access to [waterinfo.be](https://www.waterinfo.be/), a website managed by the [Flanders Environment Agency (VMM)](https://en.vmm.be/) and [Flanders Hydraulics Research](https://www.waterbouwkundiglaboratorium.be/). The website provides access to real-time water and weather related environmental variables for Flanders (Belgium), such as rainfall, air pressure, discharge, and water level. The package provides functions to search for stations and variables, and download time series.

{:.btn-group}
[Documentation][waterinfo]{:.btn .btn-sm .btn-primary}
[Source code][waterinfo_github]{:.btn .btn-sm .btn-light}
