Title: Releasing Nemo: 440.000+ fish occurrences are now available as open data
Slug: vis-data-published
Date: 2014-04-04 19:00
Author: Peter Desmet
Tags: data publication, GBIF
Summary: All species occurrence data from our Fish Information System can now be used by anyone.
Status: draft

## Introduction

In addition to the new infrastructure we are setting up for our terrestrial and freshwater observatory[^1], we are also integrating existing systems of the INBO into the LifeWatch infrastructure. As the majority of our systems contain species occurrence data, we are making use of [GBIF tools](http://www.gbif.org/publishingdata) to standardize, document, and publish our data. One of the systems[^2] that we have just made available in such a way is the **Fish Information System (VIS)**, releasing more than 440.000 fish occurrences as two datasets into the public domain, where they can be used by anyone.

If you want to explore the data right away, here are the two dataset pages on GBIF:

* [VIS - Fishes in inland waters in Flanders, Belgium](http://www.gbif.org/dataset/823dc56e-f987-495c-98bf-43318719e30f) (362.000 records)
* [VIS - Fishes in estuarine habitats in Flanders, Belgium](http://www.gbif.org/dataset/274a36be-0626-41c1-a757-3064e05811a4) (80.719 records)

[^1]: Such as the [bird tracking network](http://lifewatch.inbo.be/blog/tag/bird-tracking.html).

[^2]: [Florabank1](http://doi.org/10.3897/phytokeys.12.2849), one of our other systems, has been available since August 2011. It currently holds over [3.5 million plant occurrence records](http://www.gbif.org/dataset/271c444f-f8d8-4986-b748-e7367755c0c1).

## Background

The [Fish Information System](http://vis.milieuinfo.be) is a database set up by the INBO to monitor the status of fishes and their habitats in Flanders, Belgium. It contains data regarding occurrences, stocks, pollutants, indexes, and reintroductions. The consolidated database was set up in 2001, but sampling has been going on since 1992. The data are used to calculate the EQR (Ecological Quality Ratio) in the framework of the EU water directive and Natura2000, as well as to provide updated information for the Flemish red list of freshwater fishes.

Although summarized data are publicly accessible to users via <http://vis.milieuinfo.be>, these cannot be accessed via a webservice and do not meet the [criteria for open data](http://opendefinition.org) we strive for.

![Map of VIS sampling locations]({filename}/images/vis-sampling-locations.png)

*Map of the all the sampling locations in VIS (orange = inland waters, green = estuaries).*

## Data publication workflow using GBIF tools

In collaboration with Dimitri Brosens from the [Belgian Biodiversity Platform](http://www.biodiversity.be) and the involved researchers, we published the data as two datasets: one for inland waters and one for estuarine habitats.

For each dataset we created an SQL view in the VIS database, expressing all species occurrence information as [Darwin Core terms](http://rs.tdwg.org/dwc/terms/index.htm). [Darwin Core](http://doi.org/10.1371/journal.pone.0029715) is the international standard for expressing biodiversity data. This view is then used by our [GBIF Integrated Publishing Toolkit (IPT)](http://data.inbo.be/ipt) to serve the data as a tab-delimited text file.

In addition, we describe the dataset in detail. These metadata are recorded in our IPT in the [Ecological Metadata Language (EML)](http://en.wikipedia.org/wiki/Ecological_Metadata_Language), the international standard for expressing such information. The metadata include information regarding the project, involved parties, sampling methods, and taxonomic, geographic, and temporal scope.

Both data and metadata are then published as a **Darwin Core Archive**, a zipped folder containing the standardized files[^3]. Darwin Core Archives are the recommended method for disclosing biodiversity data, allowing users and machines to download, read, and use the data and metadata. Updates to the data are published regularly to our IPT, as new versions of the same Darwin Core Archive.

[^3]: You download these files directly from our IPT: [Fishes in inland waters](http://data.inbo.be/ipt/archive.do?r=vis-inland-occurrences) (6MB) & [Fishes in estuarine habitats](http://data.inbo.be/ipt/archive.do?r=vis-estuary-occurrences) (1.2MB)

To increase discoverability, we registered the datasets with the **Global Biodiversity Information Facility (GBIF)**. This not only allows users to [discover the data](http://www.gbif.org/dataset/search?q=vis), but allows machines to [interface with the data](http://www.gbif.org/developer/occurrence) and [metadata](http://www.gbif.org/developer/registry) as well, via the robust webservices developed by GBIF.

## Collaborating around open data

The datasets have been dedicated to the public domain under a [Creative Commons Zero waiver](http://creativecommons.org/publicdomain/zero/1.0/), allowing anyone to use the data without restrictions. By providing the data under such a waiver and in bulk (i.e. the Darwin Core Archive), these now meet [all the criteria for open data](http://opendefinition.org/od/).

Norms

We have also started to publicly document and solve issues with the data and metadata in a GitHub repository (https://github.com/LifeWatchINBO/vis-inland-occurrences/issues) as well as providing the metadata as an easy to read text file (https://github.com/LifeWatchINBO/vis-inland-occurrences/blob/master/paper.md). This not only allows users to be informed of ongoing activities, but also allows them to records issues and contribute suggestions themselves. We hope this creates an open community of data users.

Since its registration with GBIF on 24 December 2013, the dataset has already generated 94 downloads in the last 3 months, covering 21.175.785 records (58 times the size of the datasets).



FLORABANK
