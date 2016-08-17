# LifeWatch INBO blog

This repository contains the content and settings for the [LifeWatch INBO blog](http://lifewatch.inbo.be/blog). It is generated as a static website with [Pelican](http://docs.getpelican.com).

## 1. Write a post

1. Writing happens on the `draft` branch. If you write locally, do `git checkout draft`.
2. Start a new post by copy/pasting one from `_source/posts` and update the filename and metadata.
3. Write your post using the following syntax:

    ```Markdown
    Title: Jurassic Park
    Slug: jurassic-park
    Date: 2012-12-17 17:00
    Authors: Alan Grant, Ian Malcolm // Or Author: Alan Grant
    Tags: dinosaurs, endorsement, quote
    Summary: After much consideration...
    Status: draft // To hide the post from the index list for now

    Content as Markdown
      
    ## Headings start at H2 (since post title is H1)

    Links to other posts:
      
    [bird tracking data are open]({filename}bird-tracking-data-published.md)

    Images:
      
    ![Bird tracking explorer]({filename}/images/bird-tracking-explorer.png)

    Code (without the \):

    \```SQL
    SELECT * FROM bird_tracking
    \```
    ```

4. Commit and push your changes.
5. Ask for feedback via a [pull request](https://github.com/inbo/lifewatch-blog/compare/gh-pages...draft) (`draft` → `gh-pages`).
6. Incorporate the feedback and finish your post.

Your post is now 2 steps away from being published on the website. :sweat_smile:

## 2. Generate the website

You need Pelican to convert your post into static HTML and update the RSS, homepage, and necessary author/category pages. Ask [@peterdesmet](https://github.com/peterdesmet) to do it for you or do it yourself:

### Get the blog and theme repo

    git clone https://github.com/inbo/lifewatch-blog // If you didn't write locally already
    git clone https://github.com/inbo/eurasian-spoonbill

The latter one is the theme of the website and is required to make it look pretty. :dress:

### Create and activate an environment

Here we create an environment with [conda](http://conda.pydata.org/docs/get-started.html):

    conda create -n pelican python=3.5 pelican markdown --channel conda-forge

To activate:

    source activate pelican

To deactivate:

    source deactivate

### Generate the website

    cd lifewatch-blog/_source
    pelican -s dev-settings.py

Use the `--autoreload` option to generate the site for every change.

### Preview the website

In a new terminal tab:

    python http.server 8000

Which will serve the website at <http://localhost:8000/dev-output>

## 3. Publish the website

1. Update the post date and time.
2. Generate the website one last time, this time with the production settings: `pelican -s settings.py`.
3. Commit and push the generated files.
4. Get your pull request (see above) accepted or do it yourself.

Your changes are now included in the `gh-pages` branch, which serves the website at http://inbo.github.io/lifewatch-blog. That's the same as http://lifewatch.inbo.be/blog. Have a :beer:!
