Title: Using CartoDB to visualize how far birds migrate in a single night
Slug: forward-trajectory-visualizations
Date: 2015-06-18 13:50
Author: Peter Desmet, Hans van Gasteren
Tags: birds, visualization, radar, ENRAM, CartoDB
Summary: We created three nocturnal bird migration forward trajectory visualizations for ENRAM.

Last week we participated in a very productive [workshop in Amsterdam](http://www.enram.eu/activities/visualisations-from-show-cases-to-production) organized by working group 3 of ENRAM. ENRAM is the European Network for the Radar Surveillance of Animal Movement funded by [COST](http://cost.eu/) and the workshop was a follow-up on the hackathon at which we created the [flow visualization]({filename}bird-migration-flow-visualization.md) last year.

One of our goals this year was to visualize forward trajectory model data for bird migration. We were inspired by the fabulous [Alcatraz escape simulation](http://rolfhut.nl/alcatrazenglish/) made by Dutch researchers in CartoDB to try this ourselves.

## Long-range surveillance radar

The source data for our visualizations were gathered and processed by a bird radar detection system called [ROBIN](http://www.robinradar.com). The ROBIN system received a radar signal from two long-range surveillance radars in Belgium and the Netherlands. Every half hour radar measurements were sampled from ten successive high-resolution images and processed to extract location, ground speed, and track direction of individual birds or flocks. For this project we used data from the first two hours after sunset on April 6 and 7, 2013. During this period birds take-off from the radar locations to continue their nocturnal spring migration.

## Forward trajectory model

For each individual bird track we extracted time, location, ground speed, and track direction and calculated the airspeed and heading using the wind at 925hPa. We used these parameters to simulate a forward trajectory based on a model described in [Shamoun-Baranes & van Gasteren 2011](http://doi.org/10.1016/j.anbehav.2011.01.003). By keeping the birds’ airspeed and heading constant, influences of wind will effect new positions each 5 minutes and result in the presented forward trajectory until sunrise. Strong following winds during the night or location can increase the ground speeds above 100 km per hour.

## Night 1

In [this visualization](https://inbo.cartodb.com/u/lifewatch/viz/caa466f4-0f7b-11e5-9d94-0e4fddd5de28/public_map) we show nocturnal bird migration on the night of April 6-7, 2013. Bird tracks were measured every half hour and are shown as different groups in the visualization. The wind is shown as small blue tracks in the background. Note that most birds reach the German-Polish border and a few are able to reach central Poland if they took off just after sunset and flew all night.

<iframe width="100%" height="500" frameborder="0" src="https://inbo.cartodb.com/u/lifewatch/viz/caa466f4-0f7b-11e5-9d94-0e4fddd5de28/embed_map" allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>

## Night 2

In [this visualization](https://inbo.cartodb.com/u/lifewatch/viz/eb60c596-1060-11e5-aa6e-0e853d047bba/public_map) we use the same method to show nocturnal bird migration on the night of April 7-8, 2013. Note that some birds even reach the Baltic states in a single night, assuming they continued their flights until sunrise.

<iframe width="100%" height="500" frameborder="0" src="https://inbo.cartodb.com/u/lifewatch/viz/eb60c596-1060-11e5-aa6e-0e853d047bba/embed_map" allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>

## Night 2: Songbirds and waterbirds based on airspeed

In [this visualization](https://inbo.cartodb.com/u/lifewatch/viz/88c30be4-1063-11e5-a9ae-0e853d047bba/public_map) we show the same night (April 7-8), but we define two classes of birds based on the birds’ airspeed:

* Songbirds, with an airspeed below 16m/s, shown in orange
* Waterbirds (geese, ducks, and waders) with an airspeed above 16m/s, shown in blue.

This visualisation shows that especially waterbirds (ducks and/or waders) dominated the bird migration (light blue colours) and due to their faster airspeeds could reach the Baltic states in a single night, a distance of 900km in 10 hours (i.e. 90km/h or 25m/s). This is much faster than what would be possible based on their powered flight alone, i.e. their airspeed, which was on average 21m/s on which they could potentially have flown 750km in a single night without wind. Birds mainly profited from the following winds in their last hours above Poland.

<iframe width="100%" height="500" frameborder="0" src="https://inbo.cartodb.com/u/lifewatch/viz/88c30be4-1063-11e5-a9ae-0e853d047bba/embed_map" allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>

The SQL and CartoCSS for these visualizations are available in [this gist](https://gist.github.com/peterdesmet/9934ed062ddaaba04963).
