Title: Noctural bird migration forward trajectory visualizations
Slug: forward-trajectory-visualizations
Date: 2015-06-18 16:00
Author: Peter Desmet, Hans van Gasteren
Tags: birds, visualization, radar, ENRAM, CartoDB
Summary: ...

One of the goals we set for a short term scientific mission funded by the COST programme for the ENRAM action, was to visualize forward trajectory model data for bird migrations. We were inspired by the fabulous Alcatraz visualization made with CartoDB to try this ourselves too. The SQL and CartoCSS we created are documented in [this gist](https://gist.github.com/peterdesmet/9934ed062ddaaba04963).

## Forward trajectory model

A forward trajectory model based on [Shamoun-Baranes & van Gasteren 2011](http://doi.org/10.1016/j.anbehav.2011.01.003) is applied on bird tracks measured by two air defense radars during the first two hours after sunset on the evenings of April 6-7 and 7-8, 2013. The airspeed and heading of each track was extracted using the wind at 925hPa and kept constant throughout the simulated trajectory until sunrise. Strong following winds during the nights will increase the groundspeeds up to ~100 km per hour.

## Night 1

In [this visualization](https://inbo.cartodb.com/u/lifewatch/viz/caa466f4-0f7b-11e5-9d94-0e4fddd5de28/public_map) we show noctural bird migration on the night of April 6-7, 2013. Bird tracks were measured every half hour and are shown as different groups in the visualization.

<iframe width="100%" height="500" frameborder="0" src="https://inbo.cartodb.com/u/lifewatch/viz/caa466f4-0f7b-11e5-9d94-0e4fddd5de28/embed_map" allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>

## Night 2

In [this visualization](https://inbo.cartodb.com/u/lifewatch/viz/eb60c596-1060-11e5-aa6e-0e853d047bba/public_map) we show noctural bird migration on the night of April 7-8, 2013. Bird tracks were measured every half hour and are shown as different groups in the visualization.

<iframe width="100%" height="500" frameborder="0" src="https://inbo.cartodb.com/u/lifewatch/viz/eb60c596-1060-11e5-aa6e-0e853d047bba/embed_map" allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>

## Night 2: Songbirds and waterbirds based on airspeed

In [this visualization](https://inbo.cartodb.com/u/lifewatch/viz/88c30be4-1063-11e5-a9ae-0e853d047bba/public_map) we show the same night (April 7-8), but we define two classes of birds based on the birds' airspeed:

* songbirds, with an airspeed below 16m/s, shown in orange
* waterbirds (geese, ducks, and waders) with an airspeed above 16m/s, shown in blue.

<iframe width="100%" height="500" frameborder="0" src="https://inbo.cartodb.com/u/lifewatch/viz/88c30be4-1063-11e5-a9ae-0e853d047bba/embed_map" allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>

