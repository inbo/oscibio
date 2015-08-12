Title: A tutorial on visualizing bird tracking data with CartoDB
Slug: cartodb-tracking-data-tutorial.md
Date: 2015-08-10 12:00
Author: Peter Desmet
Tags: bird-tracking, visualization, CartoDB
Summary: ...

We have been using [CartoDB for bird tracking data](http://lifewatch.inbo.be/blog/tag/cartodb.html) for a while now and are very happy to that see that we have inspired others to do the [same](http://birdmapsuk.blogspot.com/2015/06/gulls-part-two.html), including for [other species](http://blog.cartodb.com/fisher/). To introduce even more people to this great tool for animal tracking data, I was invited to give a hands-on course at two workshops[^1]. Rather than keeping the course material private, I've decided to publish it here on this blog, so anyone can use it.

[^1]: The [Animal Movement Analysis Summer Course](http://horizon.science.uva.nl/scge2015-wiki/doku.php) organized by the [Institute for Biodiversity and Ecosystem Dynamics](http://ibed.uva.nl/) on July 10 and the [LifeWatch GIS and WebGis workshop](http://biodiversity.be/conference2015/workshops/) organized by the Université catholique de Louvain and INBO on September 16.

Note: If you want to follow along with this tutorial, you'll at least need to do the actions in **bold**, all the rest in optional.

## Introduction

[CartoDB](http://cartodb.com) is a tool to explore, analyze and visualize geospatial data online. In my opinion, it's like Gmail or GitHub: one of the best software tools ever. CartoDB is used in a [wide area of domains](https://cartodb.com/gallery) and has [great documentation](http://docs.cartodb.com/), but in this tutorial I'll focus on how it can be used for exploring and visualizing animal tracking data. Since [we are tracking birds](http://lifewatch.inbo.be/blog/tag/bird-tracking.html), I'll use our open data of Lesser Black-backed Gulls in the examples, but the methods can be applied to other animal tracking data as well. This tutorial is by no means meant to be exhaustive: it's a step by step guide to get you started and hopefully inspire you to do cool things with your own data.

## Create an account

**Go to <https://cartodb.com/signup> to create an account.** Free accounts allow you to upload 50MB of data, but all your data and maps will be public[^2].

[^2]: They are public in the sense that they can be discovered on your public profile, for which you need to know your user name.

## Login

1. On login, you see your private dashboard. This is where you can upload data, create maps and manage your account.
2. CartoDB will display contextual help messages to get you to know the tool. For an overview, see [the documentation on the CartoDB editor](http://docs.cartodb.com/).
3. At the top, you can toggle between your `Maps` and `Datasets` dashboard.
4. You also have a public profile (`https://user.cartodb.com/maps`). All datasets you upload and maps you create will be visible there.

## Upload data

For this tutorial, well use [our open bird tracking data]({filename}bird-tracking-data-published.md). To make it easier for you to follow along with a free CartoDB account, you can [download a subset of the data here]({filename}/files/bird_tracking.csv), containing migration data for three gulls. If you want to know how that subset was created, here's the SQL query I used:

    :::SQL
    SELECT
        t.the_geom_webmercator,
        t.altitude,
        t.date_time,
        t.device_info_serial,
        t.direction,
        t.latitude,
        t.longitude,
        |/(t.x_speed^2 + t.y_speed^2) AS speed_2d,
        d.bird_name
    FROM bird_tracking t
        LEFT JOIN bird_tracking_devices d
        ON t.device_info_serial = d.device_info_serial
    WHERE
        t.userflag IS FALSE AND
        t.date_time >= '2013-08-15' AND
        t.date_time < '2014-05-01' AND
        d.bird_name IN (
            'Eric',
            'Nico',
            'Sanne'
        )
    ORDER BY
        d.bird_name,
        t.date_time

1. **Download [this zipped bird tracking csv file]({filename}/files/bird_tracking.zip).**
2. **Go to your datasets dashboard.**
3. **Upload the file** by dragging it to your browser window. CartoDB recognizes [multiple files formats](http://docs.cartodb.com/cartodb-editor.html#supported-file-formats).

## Data view

1. CartoDB is powered by PostgreSQL & PostGIS and has created a database table from your file and done some automatic interpretation of the data types. Some additional columns have been created as well, such as `cartodb_id`.
2. Geospatial data are interpreted automatically in `the_geom`. This interpretation assumes the geodetic datum to be `WGS84`. `the_geom` supports points, lines and polygons, but only one type per dataset.
3. Click the arrow next to field name to manipulate columns, such as sorting, renaming, deleting or changing data types.
4. Most of the functionality is in the collapsed toolbar on the right, such as merging datasets, adding rows or columns, and filters.
5. Filters are great for exploring the data. **Try out the filter for altitude.**

    ![Filters]({filename}/images/cartodb-filters.png)

6. Filters are actually just SQL, a much more powerful language to select, aggregate or update your data. CartoDB supports all PostgreSQL and PostGIS SQL functions.
7. Click `SQL` in the toolbar and **try this SQL** to get some statistics about the scope of the dataset:

        :::SQL
        SELECT
            count(*) AS occurrences,
            min(date_time) AS min_date_time,
            max(date_time) AS max_date_time,
            count(distinct device_info_serial) AS individuals
        FROM bird_tracking

8. **Click** `Clear view` to remove any applied SQL.
 
## Create your first map

1. **Click** `Visualize` in the top right to create your first map.
2. Once created, click the title `bird_tracking1` and rename it to `My first map`[^3].
3. **Click** `Map view`.
4. You can change the background map by clicking `Change basemap` in the bottom right[^4]. `Positron` is a good default basemap, but there are many other options available and even more via `Yours` (including maps from NASA). Note that for the `Positron` and `Dark matter` basemaps, city labels will be [positioned on top of your data](http://blog.cartodb.com/let-your-labels-shine/), making them more readable. Choose `Positron (labels below)` to turn this off or `Positron (lite)` to have no labels at all.
5. Click `Options` in the bottom right to select the map interaction options you want to provide to the visitors of your map, such as `Zoom controls` or a `Fullscreen` button.
6. The map view also provides a toolbar on the right, where you'll recognize the same `SQL` and `Filters` features from the data view.
7. **Click** `Wizards` in the toolbar to see a plethora of visualization options. These are all explained in the [CartoDB documentation](http://docs.cartodb.com/cartodb-editor.html#map-wizards).
8. **Try** `Intensity` with the following options to get a sense of the distribution of occurrences:

    ![Intensity map]({filename}/images/cartodb-intensity.png)

9. **Try** `Choropleth` with the following options to see the relative altitude distribution (see the [documentation](http://docs.cartodb.com/cartodb-editor.html#choropleth) for different quantification methods):

    ![Choropleth map]({filename}/images/cartodb-choropleth.png)

10. Just like the filters are powered by SQL, the wizards are powered by CartoCSS, which you can use to fine-tune your map. **Click** `CSS` in the toolbar to discover how the quantification buckets (in this case `Quantile`) are defined:

        :::CSS
        /** choropleth visualization */

        #bird_tracking{
          marker-fill-opacity: 0.8;
          marker-line-color: #FFF;
          marker-line-width: 0.5;
          marker-line-opacity: 1;
          marker-width: 7;
          marker-fill: #F2D2D3;
          marker-allow-overlap: true;
        }
        #bird_tracking [ altitude <= 6965] {
           marker-fill: #C1373C;
        }
        #bird_tracking [ altitude <= 634] {
           marker-fill: #CC4E52;
        }
        #bird_tracking [ altitude <= 338.5] {
           marker-fill: #D4686C;
        }
        #bird_tracking [ altitude <= 66.5] {
           marker-fill: #EBB7B9;
        }
        #bird_tracking [ altitude <= -205.5] {
           marker-fill: #F2D2D3;
        }

[^3]: Maps can have spaces and punctation in their name, dataset names use lowercase and underscores.
[^4]: You'll have dismiss to [cool](http://blog.cartodb.com/one-click-mapping/), but somewhat obstrusive `Analyzing dataset` pop-up.

## Create a map of migration speed

1. We want to save our previous work and create another map. **Click** `Edit > Duplicate map` and **name it** `Where does gull 311 rest?`.
2. **Add a `WHERE` clause to the SQL** to only select gull 311 between specific dates:

    ```SQL
    SELECT *
    FROM scge_lbbg_migration
    WHERE
        device_info_serial = 311
        AND date_time >= '2010-08-01'
        AND date_time <= '2011-03-30'
    ```

3. We want to visualize the travel speed of gull 311. The best way to start is to **create a `Choropleth` map**, with the following options:

    ![Start from a choropleth map](migration-speed-1.png)

4. Most of the dots are red and the story does not come across yet. Let's dive into the CSS to **fine-tine the map**. We basically set all dots to green, except where the speed is below 2m/s, which we show larger and in red:

    ```CSS
    /** choropleth visualization */

    #scge_lbbg_migration{
      marker-fill-opacity: 0.8;
      marker-line-color: #FFF;
      marker-line-width: 0.5;
      marker-line-opacity: 1;
      marker-width: 6;
      marker-fill: #1a9850;
      marker-allow-overlap: true;
    }
    #scge_lbbg_migration [ speed_2d < 2] {
      marker-fill: #d73027;
      marker-width: 10;
      marker-line-width: 1;
    }
    ```

5. **Click** `Legends` in the toolbar to manually set what to be shown in the legend:

    ![Update the legend](migration-speed-2.png)

6. Click a point and chose `Select field` to **create an info window**.

    ![Define info windows](migration-speed-3.png)

7. **Describe your map** by clicking `Edit metadata...` in the top left.
8. **Share your map** by clicking `Publish` in the top right. The sharing dialog box provides you with a link to the map or the code to embed it in a web page. The `CartoDB.js` is for advanced use in apps.
9. **Copy the link and paste it in a new browser tab** to verify the info windows and the bounding box (i.e. is the interesting part of the data visible?). Anything you update in your map (including zoom level and bounding box) will affect the public map (reload the page to see the changes).

[See the final map](https://inbo.cartodb.com/u/lifewatch/viz/7ad8e926-2644-11e5-9890-0e4fddd5de28/public_map)

## Create a map of tracks per month

1. **Duplicate** your map and **name it** `Tracks per month`.
2. This time we want to string the occurrences together as lines: one line per individual (sorted on date), per month. **This can be done in the SQL**. See the [PostgreSQL documentation](http://www.postgresql.org/docs/9.4/static/functions-datetime.html) for date functions. `the_geom_webmercator` is a geospatial field that is calculated by CartoDB in the background based on `the_geom` and is used for the actual display on the map. Since we're defining a new geospatial field (i.e. a line), we have to explicitely include it.

    ```SQL
    SELECT
        ST_MakeLine(the_geom_webmercator ORDER BY date_time ASC) AS the_geom_webmercator,
        extract(month from date_time) AS month,
        device_info_serial
    FROM scge_lbbg_migration
    WHERE
        date_time >= '2010-08-01'
        AND date_time <= '2010-12-31'
    GROUP BY
        device_info_serial,
        month
    ```

3. We want to display each month in a different colour, so **start with a `Choropleth` map**, with the following options:

    ![Start from a choropleth map](month-tracks-1.png)

4. We will also include labels (start doing this in the `Choropleth` options), so you can still see which track belongs to which individual. **Fine-tune the map in the CSS**:

    ```CSS
    /** choropleth visualization */

    #scge_lbbg_migration{
      polygon-opacity: 0;
      line-color: #FFFFCC;
      line-width: 1.5;
      line-opacity: 0.8;
    }

    #scge_lbbg_migration::labels {
      text-name: [device_info_serial];
      text-face-name: 'Lato Bold';
      text-size: 12;
      text-label-position-tolerance: 10;
      text-fill: #000;
      text-halo-fill: #FFF;
      text-halo-radius: 2;
      text-dy: -10;
      text-allow-overlap: false;
      text-placement: interior;
      text-placement-type: simple;
    }

    #scge_lbbg_migration [ month <= 12] {
       line-color: #253494;
    }
    #scge_lbbg_migration [ month <= 11] {
       line-color: #2C7FB8;
    }
    #scge_lbbg_migration [ month <= 10] {
       line-color: #41B6C4;
    }
    #scge_lbbg_migration [ month <= 9] {
       line-color: #A1DAB4;
    }
    #scge_lbbg_migration [ month <= 8] {
       line-color: #FFFFCC;
    }
    ```

5. **Update the legend**:

    ![Update the legend](month-tracks-2.png)

6. To provide some more context, let's annotate the map. In the top right, **click** `Add Element > Add annotation item` and **indicate summer and winter locations**:

    ![Add annotatinos](month-tracks-3.png)

7. Finally, **update the description** in `Edit metadata...` and **publish your map**.

[See the final map](https://inbo.cartodb.com/u/lifewatch/viz/3f607d1c-264b-11e5-9d8b-0e018d66dc29/public_map)

## Create an animated map

1. **Duplicate** your map and **name it** `Migration in time`.
2. This time, we'll add a map on top of the previous one. **Click** `+` on the right hand side to add a new layer and **choose the same table** `scge_lbbg_migration`.

    ![Add a layer](torque-1.png)

3. **Apply the same time contraints** in the SQL:

    ```SQL
    SELECT * 
    FROM scge_lbbg_migration
    WHERE
        date_time >= '2010-08-01'
        AND date_time <= '2010-12-31'
    ```

4. From the `Wizards`, **choose** `Torque cat`, with the following options. The `Time Column` should always be your date.

    ![Torque cat](torque-2.png)

    ![Torque cat](torque-3.png)

5. The final CSS looks like this:

    ```CSS
    /** torque_cat visualization */

    Map {
    -torque-frame-count:256;
    -torque-animation-duration:30;
    -torque-time-attribute:"date_time";
    -torque-aggregation-function:"CDB_Math_Mode(torque_category)";
    -torque-resolution:1;
    -torque-data-aggregation:linear;
    }

    #scge_lbbg_migration{
      comp-op: source-over;
      marker-fill-opacity: 0.9;
      marker-line-color: #FFF;
      marker-line-width: 0;
      marker-line-opacity: 1;
      marker-type: ellipse;
      marker-width: 3;
      marker-fill: #FF9900;
    }
    #scge_lbbg_migration[frame-offset=1] {
     marker-width:5;
     marker-fill-opacity:0.45; 
    }
    #scge_lbbg_migration[frame-offset=2] {
     marker-width:7;
     marker-fill-opacity:0.225; 
    }
    #scge_lbbg_migration[value=1] {
       marker-fill: #D6301D;
    }
    #scge_lbbg_migration[value=2] {
       marker-fill: #A53ED5;
    }
    #scge_lbbg_migration[value=3] {
       marker-fill: #FFCC00;
    }
    ```

6. **Update the legend**, **remove the `device_info_serial` labels** from the other layer (they are no longer required) and **publish your map**.

[See the final map](https://inbo.cartodb.com/u/lifewatch/viz/a36b9c78-2679-11e5-a586-0e853d047bba/public_map)

## Further reading

This is just the beginning: upload your own tracking data, play with the settings, and start creating beautiful maps. For inspiration and tutorials, see:

* [LifeWatch INBO maps](https://inbo.cartodb.com/u/lifewatch/maps): lots of tracking data maps
* [LifeWatch INBO blog posts on CartoDB](http://lifewatch.inbo.be/blog/tag/cartodb.html): tutorials and things we`ve build with CartoDB
* [CartoDB map gallery](https://cartodb.com/gallery/): the cream of the crop of CartoDB maps
* [CartoDB academy](http://academy.cartodb.com/): step by step tutorials on how to create maps in CartoDB
* [CartoDB documentation](http://docs.cartodb.com/): if you want to know more about all the features
