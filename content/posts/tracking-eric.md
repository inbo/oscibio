Title: Visualizing two months in the life of seagull Eric with CartoDB
Slug: tracking-eric
Date: 2013-09-30 16:00
Author: Peter Desmet
Tags: CartoDB, tracking data, birds, tutorial, LW-2012-006
Summary: ...
Status: draft

As part of our terrestrial observatory, we are tracking large birds with lightweight, solar powered GPS tags. The project[^1] is lead by INBO researchers Eric Stienen (for gulls) and Anny Anselin (for the western marsh harrier) in collaboration with the [VLIZ](http://www.vliz.be/EN/INTRO) and [UvA-BiTS](http://www.uva-bits.nl/).

30 birds have been tagged over the course of this spring and summer. The preliminary results were presented in the media and you can [follow the birds live](http://www.lifewatch.be/vogels). Most birds have started their annual migration south however, where the antennas we use to download the data cannot pick them up. A good time to visualize some of the tracking data we got.

## Meet Eric and CartoDB

As an example, I will visualize two months of tracking data (June-July) from Eric in CartoDB. Eric is male [Lesser Black-backed Gull](http://en.wikipedia.org/wiki/Lesser_Black-backed_Gull), breeding in the colony of Zeebrugge. [CartoDB](http://cartodb.com/) is a tool to visualize and analyze geospatial data on the web, developed by [Vizzuality](http://vizzuality.com/).

## Intensity map of occurrences

After uploading the tracking data (which are stored as occurrence data: place, time, and some parameters) to CartoDB, one of the easiest maps to make is an intensity map. Overlapping points generate a higher colour intensity, highlighting clusters on the map.

<iframe width="100%" height="500" frameborder="0" src="http://lifewatch-inbo.cartodb.com/viz/71db3552-211b-11e3-bfc7-3f86888f001b/embed_map?title=false&description=false&search=false&shareable=false&cartodb_logo=true&layer_selector=false&legends=true&scrollwheel=true&sublayer_options=1&sql=&sw_lat=51.32637473423621&sw_lon=3.1468963623046875&ne_lat=51.351575865010346&ne_lon=3.2292938232421875"></iframe>

The dark red spot on the pier marks the nest of Eric. You can zoom and pan the map, or click on individual points to get the date and time of recording.

## Map of paths per day

To get a better sense of the trips Eric made during those two months, we can string the points together on a path. All of this can be done in SQL (CartoDB is built on [Postgresql](http://www.postgresql.org/)). In order to get a path per day, we first need to create a `day_of_year` column:

	:::sql
	ALTER TABLE tracking_eric ADD COLUMN day_of_year integer
	UPDATE tracking_eric SET day_of_year = extract(DOY FROM date_time)

Next, we order the points per `date_time`, group them by `day_of_year` and make a line:

	:::sql
	SELECT ST_MakeLine(the_geom_webmercator ORDER BY date_time ASC) AS 	the_geom_webmercator, day_of_year
	FROM tracking_eric
	GROUP BY day_of_year

A [more in-depth tutorial](http://developers.cartodb.com/tutorials/gps_track.html) is available on the CartoDB website. The main difference is that I stored the result as a view rather than a table, which is why I used `the_geom_webmercator` and not `the_geom`.

If we visualize this as a choropleth map, we get this:

<iframe width="100%" height="500" frameborder="0" src="http://lifewatch-inbo.cartodb.com/viz/44cf305c-21f9-11e3-9f83-4f522829d789/embed_map?title=false&description=false&search=false&shareable=false&cartodb_logo=true&layer_selector=false&legends=true&scrollwheel=true&sublayer_options=1&sql=SELECT%20ST_MakeLine(the_geom_webmercator%20ORDER%20BY%20date_time%20ASC)%20AS%20the_geom_webmercator%2C%20day_of_year%0AFROM%20tracking_eric%0AGROUP%20BY%20day_of_year&sw_lat=50.963616518684226&sw_lon=1.8189239501953125&ne_lat=51.76953957596102&ne_lon=4.4556427001953125"></iframe>

You may discover as I did, that Eric flew multiple times to Mouscron in June, while he stayed closer to his nest in July.

## Visualizing in time

To truly visualize Eric in time, I used the library [Torque](https://github.com/CartoDB/torque) (also developed by Vizzuality):

<iframe width="100%" height="500" frameborder="0" src="http://lifewatchinbo.github.io/torque/examples/tracking_eric.html"></iframe>

The visualization compresses two months of data in 150 seconds. As with the previous maps, you can zoom and pan the map.

[^1]: The highly imaginative project name is LW-2012-006, and you can read more on it [here](http://www.lifewatch.be/vogels) and [here](http://www.lifewatch.be/project/2-uncategorised/4-observatories).