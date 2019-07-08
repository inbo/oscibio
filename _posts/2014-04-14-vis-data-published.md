---
title: VIS, a database on fishes in Flanders, is published as open data
description: How we used GBIF tools and CC0 to publish over 400,000 fish occurrences.
date: 2014-04-14 11:40
author: Peter Desmet
tags: [Fish, GBIF, Open data]
---

## Introduction

In addition to the new infrastructure we are setting up for our terrestrial and freshwater observatory[^1], we are also integrating existing systems of the INBO into the LifeWatch infrastructure. As the majority of our systems contain species occurrence data, we are making use of [GBIF tools](http://www.gbif.org/publishingdata/summary) to standardize, document, and publish our data. One of the systems[^2] that we have just made available in such a way is the **Fish Information System (VIS)**, releasing more than 400,000[^3] fish occurrences as [two datasets](http://www.gbif.org/dataset/search?q=vis+-+Fishes) into the public domain, where they can be used by anyone.

[^1]: Such as the [bird tracking network](http://lifewatch.inbo.be/blog/tag/bird-tracking.html).

[^2]: [Florabank1](http://doi.org/10.3897/phytokeys.12.2849), one of our other systems, has been available since August 2011. It currently holds over [3.5 million plant occurrence records](http://www.gbif.org/dataset/271c444f-f8d8-4986-b748-e7367755c0c1).

[^3]: This was incorrectly reported as 440.000 records before. The inflated number of occurrence records was caused by a import issue in the estuarine dataset.

## Background

The [Fish Information System](http://vis.milieuinfo.be) is a database set up by the INBO to monitor the status of fishes and their habitats in Flanders, Belgium. It contains data regarding occurrences, stocks, pollutants, indexes, and reintroductions. The consolidated database was set up in 2001, but sampling has been going on since 1992. The data are used to calculate the EQR (Ecological Quality Ratio) in the framework of the EU water directive and Natura2000, as well as to provide updated information for the Flemish red list of freshwater fishes.

Although summarized data are publicly accessible to users via <http://vis.milieuinfo.be>, these cannot be accessed via a webservice and do not meet the [criteria for open data](http://opendefinition.org) we strive for.

![Map of VIS sampling locations]({filename}/images/vis-sampling-locations.png)

*Map of the all the sampling locations in VIS (orange = inland waters, green = estuarine waters).*

## Publishing data using GBIF tools

In collaboration with Dimitri Brosens from the [Belgian Biodiversity Platform](http://www.biodiversity.be) and the involved researchers, we published the data as two datasets: [one for inland waters](http://www.gbif.org/dataset/823dc56e-f987-495c-98bf-43318719e30f) and [one for estuarine waters](http://www.gbif.org/dataset/274a36be-0626-41c1-a757-3064e05811a4).

For each dataset we created an SQL view in the VIS database, expressing all species occurrence information as [Darwin Core terms](http://rs.tdwg.org/dwc/terms/index.htm). Darwin Core is the [international standard for expressing biodiversity data](http://doi.org/10.1371/journal.pone.0029715). This view is then used by our [GBIF Integrated Publishing Toolkit (IPT)](http://data.inbo.be/ipt) to serve the data as a tab-delimited text file.

In addition, we described the datasets in detail. These metadata are recorded in our IPT in the [Ecological Metadata Language (EML)](http://en.wikipedia.org/wiki/Ecological_Metadata_Language), the international standard for expressing such information. The metadata include information regarding the project, involved parties, sampling methods, and taxonomic, geographic, and temporal scope.

Both data and metadata are then published as a **Darwin Core Archive**, a zipped folder containing the standardized files[^4]. Darwin Core Archives are the recommended method for disclosing biodiversity data in bulk, allowing users and machines to download, read, and use the data and metadata. Updates to the data are published regularly to our IPT, as new versions of the same Darwin Core Archive.

[^4]: You download these files directly from our IPT: [Fishes in inland waters](http://data.inbo.be/ipt/archive.do?r=vis-inland-occurrences) (6MB) & [Fishes in estuarine waters](http://data.inbo.be/ipt/archive.do?r=vis-estuarine-occurrences) (1.2MB)

To increase discoverability[^5], we registered the datasets with the **Global Biodiversity Information Facility (GBIF)**. This not only allows users to [discover the data](http://www.gbif.org/dataset/search?q=vis), but also allows machines to [interface with the data](http://www.gbif.org/developer/occurrence) and [metadata](http://www.gbif.org/developer/registry) via the robust webservices developed by GBIF.

[^5]: Since the registration of the [first dataset](http://www.gbif.org/dataset/823dc56e-f987-495c-98bf-43318719e30f/activity), the dataset has already generated 120 downloads in the last 3.5 months, covering 25.861.296 records (71 times the size of the dataset).

## Open data

The researchers have dedicated the datasets to the public domain under a [Creative Commons Zero waiver](http://creativecommons.org/publicdomain/zero/1.0/), allowing anyone to use the data without restrictions. By providing the data under such a waiver and in bulk (i.e. the Darwin Core Archive), these now meet [all the criteria for open data](http://opendefinition.org/od/). Visit the dataset pages to discover and download the data yourself:

* [VIS - Fishes in inland waters in Flanders, Belgium](http://www.gbif.org/dataset/823dc56e-f987-495c-98bf-43318719e30f) (359,262 records)
* [VIS - Fishes in estuarine waters in Flanders, Belgium](http://www.gbif.org/dataset/274a36be-0626-41c1-a757-3064e05811a4) (44,694 records)
