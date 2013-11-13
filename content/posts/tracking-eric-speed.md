Title: What is the average speed of seagull Eric?
Slug: tracking-eric-speed
Date: 2013-12-01 11:00
Author: Peter Desmet
Tags: CartoDB, tracking data, birds, tutorial, LW-2012-006
Summary: ...
Status: draft

In our [last post](|filename|tracking-eric.md) we discussed how we can visualize two months of tracking data with [CartoDB](http://cartodb.com/). This time, we have another look at the data to discover what distance and speed lesser black-backed gull Eric covered.

	:::sql
	WITH calc_distance AS (
        SELECT
            cartodb_id,
            st_distance_sphere(the_geom,lag(the_geom,1) OVER(ORDER BY date_time)) AS distance_in_meters
        FROM tracking_eric
        ORDER BY date_time
    )
    SELECT tr.cartodb_id, tr.the_geom_webmercator, tr.duration_in_seconds, distance_in_meters
    FROM tracking_eric tr, calc_distance cd
    WHERE tr.cartodb_id = cd.cartodb_id

