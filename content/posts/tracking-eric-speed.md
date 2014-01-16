Title: What is the average speed of seagull Eric?
Slug: tracking-eric-speed
Date: 2013-12-01 11:00
Author: Peter Desmet
Tags: bird tracking, visualization, CartoDB, tutorial
Summary: ...
Status: draft

In our [previous post]({filename}tracking-eric.md) we explored how we can visualize two months of tracking data with [CartoDB](http://cartodb.com/). This time, we have another look at the data to discover what distance and speed lesser black-backed gull Eric covered.

## Calculating the distance

Similar to how we calculated `duration_in_seconds`[^1], we will associate a `distance_in_meters` to each occurrence point[^2]. We do this by calculating the distance between `the_geom` of the current point and `the_geom` of the previous point, using the [lag()](http://www.postgresql.org/docs/9.3/static/functions-window.html) and [st_distance_sphere()](http://http://postgis.net/docs/ST_Distance_Sphere.html) functions.  Although we can do this in a view, we'll add `duration_in_meters` as a field in the table for further use:

	:::sql
	ALTER TABLE tracking_eric ADD COLUMN distance_in_meters double precision
	
Then:

	:::sql
	WITH calc_distance AS (
        SELECT
            cartodb_id,
            ST_Distance_Sphere(the_geom,lag(the_geom,1) OVER(ORDER BY date_time)) AS distance_in_meters
        FROM tracking_eric
        ORDER BY date_time
    )
    UPDATE tracking_eric
    SET distance_in_meters = c.distance_in_meters
    FROM calc_distance c
    WHERE c.cartodb_id = tracking_eric.cartodb_id

[^1]: See "Analyzing time spent per UTM 1km square" in the [previous post]({filename}tracking-eric.md).
[^2]: You can visualize both parameters as the time and distance it took to **arrive** at that point, which is why the first record has `null` for these parameters.
