Title: Visualizing three gulls for the VLIZ Young Marine Scientists' Day
Slug: vliz-jcd-2014
Date: 2014-01-30 11:00
Author: Peter Desmet, Eric Stienen
Tags: bird tracking, visualization, CartoDB
Summary: ...
Status: draft

We will be presenting some preliminary results from our bird tracking network at the [VLIZ Young Marine Scientists' Day](http://www.vliz.be/jcd/en) on March 7 in Brugge. The study is conducted in close collaboration with the [Terrestrial Ecological Unit (TEREC)](http://www.ecology.ugent.be/terec/) of the University of Ghent, the [Flanders Marine Institute (VLIZ)](www.vliz.be/en) and [UvA-BiTS](http://www.uva-bits.nl/) at the University of Amsterdam.

Here we report on the specific movements of one breeding [Lesser Black-backed Gull](http://en.wikipedia.org/wiki/Lesser_Black-backed_Gull) and two [Herring Gulls](http://en.wikipedia.org/wiki/European_Herring_Gull) during and after breeding season, showing how the movements of the gulls vary during the course of the breeding season and fluctuate with the tidal movements. The movements are visualized with [CartoDB](http://cartodb.com), an open source tool to visualize and analyze geospatial data on the web (see also our [previous post]({filename}tracking-eric.md)).

## Eric

The GPS positions of the Lesser Black-backed Gull called Eric (which was also presented in our [previous post]({filename}tracking-eric.md)) show that he changes his foraging behaviour to fulfil the growing energetic needs during the breeding season. When still incubating eggs in Zeebrugge, Eric mainly foraged in the agricultural areas to the southeast of the colony (May). He also made regular trips to Moeskroen (June), about 65 km from the colony site, to feed on potato chips that were declared unfit for human consumption and dumped in containers. After hatching of the eggs and with the growth of the chicks in July, energy needs rapidly increased and Eric more and more foraged at sea probably to feed on energy rich discarded fish.

<iframe width="100%" height="550" frameborder="0" src="http://lifewatch-inbo.cartodb.com/viz/b43fa5a6-7dd0-11e3-ba2a-5f9e077d1162/embed_map?title=true&description=true&search=false&shareable=true&cartodb_logo=true&layer_selector=false&legends=true&scrollwheel=true&sublayer_options=1&sql=SELECT%20%0AST_MakeLine(the_geom_webmercator%20ORDER%20BY%20date_time%20ASC)%20AS%20the_geom_webmercator%2C%20%0Aextract(month%20FROM%20date_time)%20as%20month%0AFROM%20three_gulls%0AWHERE%20bird_name%20%3D%20'Eric'%20%0AAND%20date_time%20%3C%20'2013-08-01'%0AGROUP%20BY%20month%0AORDER%20BY%20month%20DESC&sw_lat=51.12959947058646&sw_lon=2.5148391723632812&ne_lat=51.54996450656601&ne_lon=3.8331985473632812"></iframe>

*viz*

## Jurgen

During incubation of the eggs in May, Jurgen, a Herring Gull that nested on a roof top in Ostend, most often foraged close to his nest (within 10km) mainly at the hard substrates probably to feed on crabs and shellfish. Sometimes he made longer trips to the open sea. During the chick-rearing season (**month**) Jurgen more often made trips to the sea, up to about 30 km form the colony. After his chicks had fledged (August and September) and energy demands decreased, his foraging range reduced and he almost exclusively foraged and rested at the hard substrates (jetties) in the vicinity of Ostend. In October Jurgen again changes his foraging strategy and he now regularly feeds inland in the agricultural areas to the southeast of Ostend and less often returns to the colony site.

*viz*

*viz*

## Anne

Finally we show the micro-scale movements of Anne, a Herring Gull that nested in Ostend. Even more than Jurgen, Anne was regularly found feeding and resting on the jetties and the beaches near Ostend. If we zoom in on her behaviour clear tidal patterns can be seen. At low tide, Anne used the mudflats and the lower parts of the jetties to feed on arthropods and shellfish. During high tide she rested on the higher parts of the jetties or at the beach.

<iframe width="100%" height="600" frameborder="0" src="http://lifewatch-inbo.cartodb.com/viz/b8d2720e-7d37-11e3-9408-7dfc5fbee961/embed_map?title=true&description=true&search=false&shareable=true&cartodb_logo=true&layer_selector=false&legends=true&scrollwheel=true&sublayer_options=1&sql=SELECT%20*%20FROM%20three_gulls%20WHERE%20bird_name%20%3D%20'Anne'%20AND%20tidal_height%20IS%20NOT%20NULL&sw_lat=51.210297904587534&sw_lon=2.859519124031067&ne_lat=51.21688423563423&ne_lon=2.880118489265442"></iframe>

These analyses use only a small part of the tracking data of the gulls that were received until now. We hope to answer many research questions at multiple scales with the data gathered over the next few years. These data will also be made available as open data to stimulate further use. A subset of the data for Eric can already be [visualized and downloaded]({filename}tracking-eric.md).
