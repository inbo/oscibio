Title: There and back again: gull migration data visualized
Slug: gull-migration-data
Date: 2015-05-12 16:00
Author: Peter Desmet
Tags: birds, bird tracking, open data, visualization, CartoDB
Summary: Using CartoDB to tell migration stories in our recently republished gull tracking data.

In July last year, we [released the gull tracking data from the 2013 breeding season]({filename}bird-tracking-data-published.md) as open data. We have now complemented the dataset with tracking data from the 2013/2014 migration/wintering season and the 2014 breeding season. The [dataset now contains over 1.1 million occurrence records](http://doi.org/10.15468/02omly) from 60 tracked gulls, including migration data, which wasn't included before.

The Herring Gulls don't migrate (a trip to the Nord of France at the most), but the Lesser Black-backed Gulls migrate to Spain, Morocco, or even further south.

## Will they come back?

We don't have tracking data from all gulls however: data collected by the [trackers](http://www.uva-bits.nl) can only be retrieved via an antenna network set up close to the breeding colony[^1]. If the bird does not return to the colony or if it is impossible to establish a connection (e.g. because the bird has removed the tracker antenna), then the data are unobtainable, even though the tracker might continue to collect those (until the solar powered battery runs out).

[^1]: Not via satellite, which would be very expensive and require even more power from the battery.

From the 22 Lesser Black-backed Gull that were tagged in 2013, we were able to retrieve migration data from nine individuals on their return to the colony in March-April 2014. Below is an animated map using CartoDB's recently added [heatmap feature](http://blog.cartodb.com/introducing-heatmaps/), aggregating all tracking data from the 22 Lesser Black-backed Gulls over 12 months (June 2013 - May 2014).

<iframe width="100%" height="800" frameborder="0" src="https://inbo.cartodb.com/u/lifewatch/viz/a9845fda-03a3-11e5-8d7f-0e4fddd5de28/embed_map" allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>

## Gull Harry

The trackers also allow us to look at individual stories. The migration story of Harry is one of the most interesting. After the breeding season, Harry stayed close to two months in the UK, after which he migrated to Seville, Spain. On the way back north in March, it looks like Harry hitchhiked on a boat in the Bay of Biscay. Unfortunately, this boat was going south, so he had to fly the distance twice[^2].

<iframe width="100%" height="800" frameborder="0" src="https://inbo.cartodb.com/u/lifewatch/viz/afe199fa-f5b2-11e4-8503-0e853d047bba/embed_map" allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>

[^2]: More stories can be discovered on the [LifeWatch Belgium website](http://lifewatch.be/en/historical-data-birds).

## Gull Eric

So, how is [everyone's favourite gull Eric]({filename}tracking-eric.md) doing? As you can see below, Eric had a succesful migration to Agadir, Morocco. On March 29, 2014 he flew back to the breeding colony, where he arrived 8 days later on 5 April 2015. Sadly, we lost of track of Eric in May. The last occurrence we were able to retrieve dates `2014-05-11T03:22:52Z`, on the roof of a building in Zeebrugge. His tracker antenna probably malfunctioned. We are grateful he got so many people interested in our bird tracking network and wish him a happy untracked future.

<iframe width="100%" height="800" frameborder="0" src="https://inbo.cartodb.com/u/lifewatch/viz/88a48488-ea59-11e4-849b-0e853d047bba/embed_map" allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>

## Presentation

The bird tracking network (and other tools to study bird migration) was presented by [Peter Desmet](https://twitter.com/peterdesmet) at the [Empowering Biodiversity Research conference](http://www.biodiversity.be/conference2015) on May 21, 2015 in Brussels, which was co-organized by LifeWatch Belgium. You can find the presentation below. If you have questions, don't hesitate to contact us (via [Twitter](https://twitter.com/LifeWatchINBO) or [email](mailto:opendata@inbo.be)).

<script async class="speakerdeck-embed" data-slide="1" data-id="937c31af2ba3456893376a402b3bf29e" data-ratio="1.33333333333333" src="//speakerdeck.com/assets/embed.js"></script>
