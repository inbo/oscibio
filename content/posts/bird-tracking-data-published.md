Title: Gull tracking data from the 2013 breeding season published as open data
Slug: bird-tracking-data-published
Date: 2014-07-22 15:20
Author: Peter Desmet
Tags: birds, bird tracking, open data, GBIF
Summary: Our first set of tracking data are now available for everyone to use.

We have written about our bird tracking network [before](http://lifewatch.inbo.be/blog/tag/bird-tracking.html) - the network we set up with the Flanders Marine Institute (VLIZ) to track large birds with [advanced GPS trackers](http://www.uva-bits.nl) - showing how the data can be [visualized with CartoDB]({filename}jcd-2014.md) and releasing a small sample dataset of the famous [Lesser Black-backed Gull Eric]({filename}tracking-eric.md).

This tracking network is collecting rich, fascinating, and beautiful data: data which potential we do not want to limit to our research questions and needs. This is why we are happy to announce that we have just published **all gull tracking data from the 2013 breeding season** as open data, available to anyone!

<iframe width="100%" height="600" frameborder="0" src="//lifewatch-inbo.cartodb.com/viz/a12cbfc4-0e4b-11e4-8aa1-0e230854a1cb/embed_map?title=false&description=false&search=false&shareable=true&cartodb_logo=false&layer_selector=false&legends=true&scrollwheel=true&fullscreen=true&sublayer_options=1&sql=SELECT%0A%09t.cartodb_id%2C%0A%09t.the_geom%2C%0A%09t.the_geom_webmercator%2C%0A%09CASE%0A%09%09WHEN%20d.scientific_name%20%3D%20'Larus%20fuscus'%20THEN%201%0A%09%09WHEN%20d.scientific_name%20%3D%20'Larus%20argentatus'%20THEN%202%0A%09END%20AS%20species_number%0AFROM%0A%09bird_tracking%20AS%20t%0A%09LEFT%20JOIN%20bird_tracking_devices%20AS%20d%0A%09ON%20t.device_info_serial%20%3D%20d.device_info_serial%0AWHERE%0A%09t.userflag%20%3D%20false%0A%09AND%20d.project_shortname%20%3D%20'gull'&sw_lat=51.102834783597565&sw_lon=2.485407292842865&ne_lat=51.4494738511512&ne_lon=3.6932167410850525" allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>

The [dataset](http://www.gbif.org/dataset/83e20573-f7dd-4852-9159-21566e1e691e) contains over 440,000 occurrences (visualized above), recorded by 27 GPS trackers mounted on 22 [Lesser Black-backed Gulls](http://en.wikipedia.org/wiki/Lesser_Black-backed_Gull) and 5 [Herring Gulls](http://en.wikipedia.org/wiki/European_Herring_Gull) breeding at the Belgian coast. The metadata provides extensive information regarding the sampling protocol, taxonomic, geographic, and temporal scope, and involved parties.

As with all our species occurrence data, we make use of GBIF tools (see [this blog post]({filename}vis-data-published.md)) to document, standardize, and publish the data. In addition, we created a GitHub repository where you can [report issues](https://github.com/LifeWatchINBO/bird-tracking-gull-occurrences/issues) or get the [metadata in Markdown format](https://github.com/LifeWatchINBO/bird-tracking-gull-occurrences/blob/master/paper.md). We also opened up access to the tracking data via our [CartoDB API](https://github.com/LifeWatchINBO/bird-tracking/blob/master/cartodb/README.md).

We have dedicated the data to the public domain under a [Creative Commons Zero waiver](http://creativecommons.org/publicdomain/zero/1.0/), allowing anyone to use these without restrictions. We do appreciate it however if you provide a link to the [original dataset](http://dataset.inbo.be/bird-tracking-gull-occurrences) when possible and we are always interested to see what you did with the data. Leave a comment, reach us at [LifeWatchINBO](https://twitter.com/LifeWatchINBO) or see our contact information in the metadata.

We hope by working openly we can build a vibrant community around these data and data we plan to publish in the future. Go exploring at [Bird tracking - GPS tracking of Lesser Black-backed Gull and Herring Gull breeding at the Belgian coast](http://www.gbif.org/dataset/83e20573-f7dd-4852-9159-21566e1e691e).

