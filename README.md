# LifeWatch INBO blog

This repository contains the content and settings for the [LifeWatch INBO blog](http://lifewatch.inbo.be/blog). It is generated as a static website with [Pelican](http://docs.getpelican.com).

## 1. Write a post

1. Start a new post by copy/pasting one from `_source/posts` and update the filename and metadata. You can do this either locally or on GitHub.
2. The syntax to use for your post is:

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

3. Commit and push your changes.
3. Ask for feedback via a pull request (`master` → `gh-pages`)
4. Incorporate the feedback

Your posts is now 2 steps away from being published on the website.

## 2. Generate the website

You need Pelican to convert your post into static HTML and update the RSS, homepage, and necessary author/category pages. Ask one of the contributors to do it for you or install all the necessary components yourself:

### Get the blog and theme repo

    git clone https://github.com/inbo/lifewatch-blog
    git clone https://github.com/inbo/eurasian-spoonbill

The latter one is the theme of the website and required to generate the correct output.

### Create and activate an environment

Here we create an environment with [conda](http://conda.pydata.org/docs/get-started.html):

    conda create -n pelican python=3.5 pelican markdown --channel conda-forge

To activate:

    source activate pelican

To deactivate:

### Generate output

    source deactivate

### Generate the website

    cd lifewatch-blog/_source
    pelican -s dev-settings.py

Use the `--autoreload` option to generate the site on every change.

### Preview the website

In a new terminal tab:

    python http.server 8000

Which will serve the website at <http://localhost:8000/dev-output>

## Publish the website

1. Update the post date and time.
2. Generate the website one last time, this time with the production settings: `pelican -s settings.py`.
3. Commit and push the generated files.
4. Accept the pull request.

Your changes are now included in the `gh-pages` branch, which serves the website at http://inbo.github.io/lifewatch-blog = http://lifewatch.inbo.be/blog.
