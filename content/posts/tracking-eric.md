Title: Using CartoDB to visualize two months in the life of seagull Eric
Slug: tracking-eric
Date: 2013-10-01 11:15
Author: Peter Desmet
Tags: CartoDB, tracking data, birds, tutorial, LW-2012-006
Summary: Exploring different ways to visualize and analyze tracking data with CartoDB.

As part of our terrestrial observatory, we are tracking large birds with lightweight, solar powered GPS tags. The project[^1] is lead by INBO researchers Eric Stienen (for gulls) and Anny Anselin (for the western marsh harrier) in collaboration with the [VLIZ](http://www.vliz.be/EN/INTRO) and [UvA-BiTS](http://www.uva-bits.nl/).

30 birds have been tagged over the course of this spring and summer. The preliminary results were presented in the media and you can [follow the birds live](http://www.lifewatch.be/birds). Most birds have started their annual migration south however, where the antennas we use to download the data cannot pick them up. A good time to visualize some of the data we got.

## Meet Eric and CartoDB

As an example, I will visualize two months of tracking data (June-July) from Eric in CartoDB. Eric is male [Lesser Black-backed Gull](http://en.wikipedia.org/wiki/Lesser_Black-backed_Gull), breeding in the colony of Zeebrugge. [CartoDB](http://cartodb.com/) is an open source tool to visualize and analyze geospatial data on the web, developed by [Vizzuality](http://vizzuality.com/).

## Intensity map of occurrences

After uploading the tracking data (which are stored as [occurrence data](https://lifewatch-inbo.cartodb.com/tables/tracking_eric/): place, time, and some parameters) to CartoDB, one of the easiest maps to make is an intensity map. Overlapping points generate a higher colour intensity, highlighting clusters on the map.

<iframe width="100%" height="500" frameborder="0" src="http://lifewatch-inbo.cartodb.com/viz/71db3552-211b-11e3-bfc7-3f86888f001b/embed_map?title=false&description=false&search=false&shareable=false&cartodb_logo=true&layer_selector=false&legends=true&scrollwheel=true&sublayer_options=1&sql=&sw_lat=51.32637473423621&sw_lon=3.1468963623046875&ne_lat=51.351575865010346&ne_lon=3.2292938232421875"></iframe>

The dark red spot on the pier marks the nest of Eric. You can zoom and pan the map, or click on individual points to get the date and time of recording.

## Map of trips per day

To get a better sense of the trips Eric made during those two months, we can string the points together in a path. All of this can be done in SQL, since CartoDB is built on [PostgreSQL](http://www.postgresql.org/) and [PostGIS](http://postgis.net/). In order to get a path per day, we first need to create a `day_of_year` column:

	:::sql
	ALTER TABLE tracking_eric ADD COLUMN day_of_year integer
	UPDATE tracking_eric SET day_of_year = extract(DOY FROM date_time)

Next, we order the points per `date_time`, group them by `day_of_year` and make a line[^2]:

	:::sql
	SELECT ST_MakeLine(the_geom_webmercator ORDER BY date_time ASC) AS 	the_geom_webmercator, day_of_year
	FROM tracking_eric
	GROUP BY day_of_year

If we visualize this as a choropleth map, we get this:

<iframe width="100%" height="500" frameborder="0" src="http://lifewatch-inbo.cartodb.com/viz/44cf305c-21f9-11e3-9f83-4f522829d789/embed_map?title=false&description=false&search=false&shareable=false&cartodb_logo=true&layer_selector=false&legends=true&scrollwheel=true&sublayer_options=1&sql=SELECT%20ST_MakeLine(the_geom_webmercator%20ORDER%20BY%20date_time%20ASC)%20AS%20the_geom_webmercator%2C%20day_of_year%0AFROM%20tracking_eric%0AGROUP%20BY%20day_of_year&sw_lat=50.963616518684226&sw_lon=1.8189239501953125&ne_lat=51.76953957596102&ne_lon=4.4556427001953125"></iframe>

You may discover as I did, that Eric flew multiple times to Mouscron in June, while he stayed closer to his nest in July.

## Visualizing in time

To truly visualize Eric in time, I used the library [Torque](https://github.com/CartoDB/torque) (also developed by Vizzuality):

<iframe width="100%" height="500" frameborder="0" src="http://lifewatch-inbo.cartodb.com/viz/4f97b83c-4af9-11e3-86e2-cff6e432732d/embed_map?title=false&description=false&search=false&shareable=false&cartodb_logo=true&layer_selector=false&legends=false&scrollwheel=true&sublayer_options=1&sql=&sw_lat=50.611237544825876&sw_lon=1.8216383457183838&ne_lat=51.45753372278527&ne_lon=4.458357095718384"></iframe>

The visualization compresses two months of data in 120 seconds. As with the previous maps, you can zoom and pan the map.

*Note: since publishing this post, [Torque has been integrated in CartoDB](http://blog.cartodb.com/post/66687861735/torque-is-live-try-it-on-your-cartodb-maps-today). The map above now uses the integrated version.*

## Analyzing time spent per UTM 1km square

So far, I only created visualizations of the data, but CartoDB also allows me to analyze the data. I would like to know how much time Eric spent per square kilometer. This was quite a challenge for my novice SQL skills, but [good documentation](http://www.postgresql.org/docs/9.3/interactive/index.html) goes a long way.

First, we need to calculate the duration for each occurrence point. We can do this by calculating the difference between the `date_time` of the current point and the `date_time` of the previous point (the `lag()` function), and then translating this to seconds (the `extract()` function):

    :::sql
    ALTER TABLE tracking_eric ADD COLUMN duration_in_seconds integer

Then:

    :::sql
    WITH calc_duration AS (
        SELECT
        cartodb_id,
        extract(epoch FROM (date_time - lag(date_time,1) OVER(ORDER BY date_time))) AS duration_in_seconds
        FROM tracking_eric
        ORDER BY date_time
    )
    UPDATE tracking_eric
    SET duration_in_seconds = calc_duration.duration_in_seconds
    FROM calc_duration
    WHERE calc_duration.cartodb_id = tracking_eric.cartodb_id

Next, we upload a reference grid to CartoDB. I uploaded a [shapefile of all UTM 1km squares of Belgium](http://www.eea.europa.eu/data-and-maps/data/eea-reference-grids). Then we [join the two tables](http://developers.cartodb.com/tutorials/joining_data.html) by geospatial intersection[^3]:

    :::sql
    SELECT 
    row_number() OVER (ORDER BY utm.the_geom_webmercator) AS cartodb_id,
    utm.the_geom_webmercator,
    sum(duration_in_seconds) as duration_in_seconds
    FROM utm_1km AS utm, tracking_eric AS eric
    WHERE ST_Intersects(utm.the_geom_webmercator, eric.the_geom_webmercator) 
    GROUP BY utm.the_geom_webmercator

The resulting map, with a logaritmic choropleth scale, looks like this[^4]:

<iframe width="100%" height="500" frameborder="0" src="http://lifewatch-inbo.cartodb.com/viz/054aa85c-25e2-11e3-8e2c-b3655fb9f73d/embed_map?title=false&description=false&search=false&shareable=false&cartodb_logo=true&layer_selector=false&legends=true&scrollwheel=true&sublayer_options=1&sql=SELECT%20%20%0Autm.the_geom_webmercator%2C%20sum(duration_in_seconds)%20as%20duration_in_seconds%0A%20%20%20%20FROM%20utm_1km%20AS%20utm%2C%20tracking_eric%20AS%20eric%0A%20%20%20%20WHERE%20ST_Intersects(utm.the_geom_webmercator%2C%20eric.the_geom_webmercator)%20%0A%20%20%20%20GROUP%20BY%20utm.the_geom_webmercator&sw_lat=51.00684227163969&sw_lon=2.62847900390625&ne_lat=51.411199044550045&ne_lon=3.94683837890625"></iframe>

You can click on each square to get the time Eric spent there in seconds over two months time. We can now also easily figure out where Eric stayed more than an hour, by changing the above query to:

    :::sql
    WITH utm_squares AS (
        SELECT
        row_number() OVER (ORDER BY utm.the_geom_webmercator) AS cartodb_id,
        utm.the_geom_webmercator,
        sum(duration_in_seconds) as duration_in_seconds
        FROM utm_1km AS utm, tracking_eric AS eric
        WHERE ST_Intersects(utm.the_geom_webmercator, eric.the_geom_webmercator)
        GROUP BY utm.the_geom_webmercator
    )
    SELECT * FROM utm_squares WHERE duration_in_seconds > 3600

<iframe width="100%" height="500" frameborder="0" src="http://lifewatch-inbo.cartodb.com/viz/f1bb680c-25ec-11e3-aaeb-6796bd794fbd/embed_map?title=false&description=false&search=false&shareable=false&cartodb_logo=true&layer_selector=false&legends=true&scrollwheel=true&sublayer_options=1&sql=SELECT%0Arow_number()%20OVER%20(ORDER%20BY%20utm.the_geom_webmercator)%20AS%20cartodb_id%2C%0Autm.the_geom_webmercator%2C%20sum(duration_in_seconds)%20as%20duration_in_seconds%0AFROM%20utm_1km%20AS%20utm%2C%20tracking_eric%20AS%20eric%0AWHERE%20ST_Intersects(utm.the_geom_webmercator%2C%20eric.the_geom_webmercator)%20and%20duration_in_seconds%20%3E%20300%0AGROUP%20BY%20utm.the_geom_webmercator&sw_lat=51.00684227163969&sw_lon=2.62847900390625&ne_lat=51.411199044550045&ne_lon=3.94683837890625"></iframe>

## Conclusion

In my opinion [CartoDB](http://cartodb.com) is an intuitive, yet very powerful tool to visualize and analyse data, which is why I've been a fan from day one. I hope we can [install](https://github.com/CartoDB/cartodb20) and use it for all our tracking data, in collaboration with the VLIZ and UvA-BiTS. If you're eager to explore yourself, CartoDB is offered as a [freemium service](http://cartodb.com/pricing/‎). The data used in this post are dedicated to the public domain under a [Creative Commons Zero](http://creativecommons.org/publicdomain/zero/1.0/) waiver at:

* CartoDB: <https://lifewatch-inbo.cartodb.com/tables/tracking_eric/>
* API: <https://lifewatch-inbo.cartodb.com/api/v2/sql?q=SELECT * FROM tracking_eric>

[^1]: The highly imaginative project name is LW-2012-006, and you can read more on it on the [LifeWatch Belgium website](http://www.lifewatch.be/birds).
[^2]: A [more in-depth tutorial](http://developers.cartodb.com/tutorials/gps_track.html) is available on the CartoDB website. The main difference is that I stored the result as a view rather than a table, which is why I used `the_geom_webmercator` and not `the_geom`.
[^3]: CartoDB requires an `cartodb_id` to allow click interaction. I am cheating here by generating a new one based on `row_number()`.
[^4]: Obviously, for a real analysis, I would have to use a reference grid that extends beyond the borders of Belgium.
