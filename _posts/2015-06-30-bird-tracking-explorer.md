---
title: Bird tracking explorer released
description: We've developed an open source tool to let you explore our bird tracking data.
date: 2015-06-30 15:00
author: [Bart Aelterman, Peter Desmet]
categories: [Birds, Bird tracking, Visualization, Software, CartoDB]
---

As we have written before, our [bird tracking data are open]({% post_url 2014-07-22-bird-tracking-data-published %}): you can download these in [bulk](https://doi.org/10.15468/02omly), via the [CartoDB API](https://github.com/inbo/bird-tracking/blob/f80497eb105eb02d7238b9ae59f2feabe205b4f5/cartodb/README.md) or the [GBIF API](http://api.gbif.org/v1/occurrence/search?datasetkey=83e20573-f7dd-4852-9159-21566e1e691e). These methods don't allow you however to quickly explore a single individual, for a certain time period[^1]. This is why we're happy to announce our [bird tracking explorer](http://inbo.github.io/bird-tracking/explorer/index.html), an experimental, open source tool that allows you to do just that.

[^1]: The [birdmap developed by VLIZ](http://www.lifewatch.be/birdmap?group=Kleine%20mantelmeeuw) does allow you to do this for the real-time data.

[![Bird tracking explorer](/assets/img/post-bird-tracking-explorer.png)](http://inbo.github.io/bird-tracking/explorer/index.html)

## Features

* **Select a bird**: The explorer is designed to explore the activity of a single individual, which you can select from the dropdown menu. Basic metadata about the selected bird (sex, species, ring code, caught date) are indicated on the right.
* **Map**: All public occurrences of the selected individual are shown on the map, which you can zoom and pan.
* **Year chart**: The year chart gives you an overview of the activity of the bird over time. Each day (clustered in months) is represented by a square, which colour indicates the number of kilometers the bird travelled that day. Hover over a square to get the exact kilometers.

The map and year chart already give you a general overview of the area and time in which the bird was active, you can explore the data even further by clicking a day (square) or month (label) on the year chart. This will cause the map to refresh and only show occurrences from that day or month and two additional charts to be drawn below the year chart:

* **Month chart**: This chart on the left is similar to the year chart, but shows a metric (see further) per hour, clustered by day of the month. This is helpful to compare daily patterns.
* **Day chart**: If a single day is selected, this chart on the right shows the same daily metric as a line chart.
* **Select a metric**: Buttons above the charts allow you to toggle between the two metrics to be shown by the charts:
    * **Distance travelled**/hour: an indication of activity.
    * **Furthest distance from catch location**/hour: an indication of migration/trips, as the catch location is generally in the vicinity of the birds’ nest.

![Metric charts](/assets/img/post-bird-tracking-explorer-metric-charts.png)

These charts can highlight interesting patterns in the birds’ behaviour, e.g. the image above shows how gull [Eric]({% post_url 2013-10-01-tracking-eric %}) is travelling to a location at about 70 kilometers from his colony in the afternoon for five consecutive days in June 2013. That location happened to be a [potato chips factory](http://www.standaard.be/cnt/dmf20130618_00627212), where he fed on discarded chips declared unfit for human consumption.

## Technology

We developed the bird tracking explorer to learn and experiment with some open source technologies:

* **CartoDB API**: We have [blogged]({{ site.archive_permalink | relative_url }}?category=CartoDB) about the mapping tool CartoDB before. Perhaps a lesser-known feature of CartoDB is its [SQL API](https://github.com/inbo/bird-tracking/blob/f80497eb105eb02d7238b9ae59f2feabe205b4f5/cartodb/README.md), which allows you to query datasets in plain SQL giving you enormous flexibility. All data shown by the explorer are queried via the CartoDB API. 
* **CartoDB.js**: A [JavaScript library](http://docs.cartodb.com/cartodb-platform/cartodb-js.html) to create CartoDB maps on the fly in the browser. We use it to build the map and update it when a user selects a new bird or date.
* **jQuery**: A [Javascript library](https://jquery.com/) to interact with the SQL API and add interactivity to the page.
* **Cal-Heatmap**: A [Javascript library](https://cal-heatmap.com/) to create interactive calendar heat maps, used for the year and month charts. Requires [D3](http://d3js.org).
* **C3.js**: A [JavaScript library](http://c3js.org/) to create interactive charts, used for the day chart. Requires [D3](http://d3js.org).
* **Bootstrap**: A [HTML, CSS and JavaScript framework](http://getbootstrap.com/) to quickly create a nice, responsive design.

## Go explore

The bird tracking explorer currently contains data from 63 individuals (44 Lesser Black-backed Gulls, 16 Herring Gulls and 3 Western Marsh Harriers). Depending on the individual, tracks are available from May 2013 until August 2014. That includes the winter period during which certain birds migrate to Spain and Africa. So go ahead, and [explore the bird tracking data yourself](http://inbo.github.io/bird-tracking/explorer/index.html). Developers might want to explore the [open source code on GitHub](https://github.com/inbo/bird-tracking).

If you have a comment, remark or suggestion, leave a comment below or [create an issue](https://github.com/inbo/bird-tracking/issues).
