Title: Visualizing 2 months in the life of seagull Eric with CartoDB
Slug: tracking-eric
Date: 2013-09-25 16:00
Author: Peter Desmet
Tags: CartoDB, tracking data, birds, LW-2012-006
Summary: ...
Status: draft

As part of our terrestrial observatory, we are tracking large birds with lightweight, solar-powered GPS tags. The project[^1] is lead by INBO researchers Eric Stienen (for gulls) and Anny Anselin (for the western marsh harrier) in collaboration with the [VLIZ](http://www.vliz.be/EN/INTRO) and [UvA-BiTS](http://www.uva-bits.nl/).

30 birds have been tagged over the course of this spring and summer. The preliminary results have been discussed in the media and some of the birds you can still [follow live](http://www.lifewatch.be/vogels). Most have started their migration south however (where our antennas used to download the data cannot pick them up), so we thought it would be a good time to visualize some of the generated data.

## Meet Eric and CartoDB

As an example, we will visualize two months of tracking data (June-July) from Eric in CartoDB. Eric is male [Lesser Black-backed Gull](http://en.wikipedia.org/wiki/Lesser_Black-backed_Gull), breeding in the colony of Zeebrugge. [CartoDB](http://cartodb.com/) is a tool to visualize and analyze geospatial data on the web.

<iframe width="100%" height="500" frameborder="0" src="http://lifewatch-inbo.cartodb.com/viz/71db3552-211b-11e3-bfc7-3f86888f001b/embed_map?title=false&description=false&search=false&shareable=false&cartodb_logo=true&layer_selector=false&legends=true&scrollwheel=true&sublayer_options=1&sql=&sw_lat=51.32637473423621&sw_lon=3.1468963623046875&ne_lat=51.351575865010346&ne_lon=3.2292938232421875"></iframe>

<iframe width="100%" height="500" frameborder="0" src="http://lifewatch-inbo.cartodb.com/viz/44cf305c-21f9-11e3-9f83-4f522829d789/embed_map?title=false&description=false&search=false&shareable=false&cartodb_logo=true&layer_selector=false&legends=true&scrollwheel=true&sublayer_options=1&sql=SELECT%20ST_MakeLine(the_geom_webmercator%20ORDER%20BY%20date_time%20ASC)%20AS%20the_geom_webmercator%2C%20day_of_year%0AFROM%20tracking_eric%0AGROUP%20BY%20day_of_year&sw_lat=50.963616518684226&sw_lon=1.8189239501953125&ne_lat=51.76953957596102&ne_lon=4.4556427001953125"></iframe>

<iframe width="100%" height="500" frameborder="0" src="http://lifewatchinbo.github.io/torque/examples/tracking_eric.html"></iframe>

[^1]: ...