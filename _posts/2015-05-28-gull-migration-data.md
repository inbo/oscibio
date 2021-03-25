---
title: "There and back again: gull migration data visualized"
description: Using CartoDB to tell migration stories in our recently republished gull tracking data.
background: /assets/backgrounds/2015-05-28-gull-migration-data.jpg
date: 2015-05-28 13:00
author: Peter Desmet
categories: [LifeWatch, bird tracking, visualization, CartoDB, presentation]
---

{: .alert .alert-warning}
We no longer have a CartoDB/CARTO account and have replaced embedded maps with screenshots.

In July last year, we [released the gull tracking data from the 2013 breeding season]({% post_url 2014-07-22-bird-tracking-data-published %}) as open data. We have now complemented the dataset with tracking data from the 2013/2014 migration/wintering season and the 2014 breeding season. The [dataset now contains over 1.1 million occurrence records](https://doi.org/10.15468/02omly) from 60 tracked gulls, including migration data, which wasn't included before.

The Herring Gulls don't migrate (a trip to the Nord of France at the most), but the Lesser Black-backed Gulls migrate to Spain, Morocco, or even further south.

## Will they come back?

We don't have tracking data from all gulls however: data collected by the [trackers](http://www.uva-bits.nl) can only be retrieved via an antenna network set up close to the breeding colony[^1]. If the bird does not return to the colony or if it is impossible to establish a connection (e.g. because the bird has removed the tracker antenna), then the data are unobtainable, even though the tracker might continue to collect those (until the solar powered battery runs out).

[^1]: Not via satellite, which would be very expensive and require even more power from the battery.

From the 22 Lesser Black-backed Gull that were tagged in 2013, we were able to retrieve migration data from nine individuals on their return to the colony in March-April 2014. Below is an animated map using CartoDB's recently added [heatmap feature](http://blog.cartodb.com/introducing-heatmaps/), aggregating all tracking data from 6 Lesser Black-backed Gulls over 12 months (June 2013 - May 2014).

<!--<iframe width="100%" height="520" frameborder="0" src="https://inbo.carto.com/u/lifewatch/builder/81a2594d-f6e6-42e4-9a1e-add22753b8a1/embed" allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>-->
![map-1](/assets/images/2015-05-28-gull-migration-data-map-1.png)

## Hitchhiking Harry

The trackers also allow us to look at individual stories. The migration story of Harry is one of the most interesting. After the breeding season, Harry stayed close to two months in the UK, after which he migrated to Seville, Spain. On the way back north in March, it looks like Harry hitchhiked on a boat in the Bay of Biscay. Unfortunately, this boat was going south, so he had to fly the distance twice[^2].

<!--<iframe width="100%" height="520" frameborder="0" src="https://inbo.carto.com/u/lifewatch/builder/afe199fa-f5b2-11e4-8503-0e853d047bba/embed" allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>-->
![map-2](/assets/images/2015-05-28-gull-migration-data-map-2.png)

[^2]: More stories can be discovered on the [LifeWatch Belgium website](http://lifewatch.be/en/historical-data-birds).

## Where's Eric?

So, how is [everyone's favourite gull Eric]({% post_url 2013-10-01-tracking-eric %}) doing? As you can see below, Eric had a successful migration to Agadir, Morocco in 2013. On March 29, 2014 he flew back to the breeding colony in Zeebrugge, where he arrived eight days later. In May that year we lost track of Eric: the last occurrence we were able to retrieve dates `2014-05-11T03:22:52Z`, on the roof of a building in Zeebrugge. His tracker probably malfunctioned or he didn't stay around the antenna long enough to send more data.

<!--<iframe width="100%" height="520" frameborder="0" src="https://inbo.carto.com/u/lifewatch/builder/88a48488-ea59-11e4-849b-0e853d047bba/embed" allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>-->
![map-3](/assets/images/2015-05-28-gull-migration-data-map-3.png)

So, is he still alive? We don't know for sure, but we do know that he migrated successfully back to Agadir, Morocco in 2014. As do all our gulls, Eric is ringed with two leg rings: a standard metal ring with code `L907172`, which can be read and reported if he is captured or found dead, but also a blue ring with code `URAM`, which can be observed from a distance with binoculars. Thanks to the blue ring and a network of voluntary observers, we know that Eric made it to Agadir in 2014: he was observed there nine times, by three different observers, between January 12 and March 21, 2015. Eric is ringed since July 2008, and he has been observed in Agadir almost every year since then. We hope he's still doing fine today and we are grateful he got so many people interested in our bird tracking network.

## Presentation

The bird tracking network (and other tools to study bird migration) was presented by [Peter Desmet](https://twitter.com/peterdesmet) at the [Empowering Biodiversity Research conference](http://www.biodiversity.be/conference2015) on May 21, 2015 in Brussels, which was co-organized by LifeWatch Belgium. You can find the presentation below. If you have questions, don't hesitate to contact us (via [Twitter](https://twitter.com/LifeWatchINBO) or [email](mailto:opendata@inbo.be)).

<script async class="speakerdeck-embed" data-slide="1" data-id="937c31af2ba3456893376a402b3bf29e" data-ratio="1.33333333333333" src="//speakerdeck.com/assets/embed.js"></script>
