# LifeWatch INBO blog

This repository contains the content and settings for the [LifeWatch INBO blog](http://lifewatch.inbo.be/blog). It is generated into a static website with [Pelican](http://docs.getpelican.com/en/3.1.1/).

## Installation instructions

1. On your local computer, make sure you have cloned the [lifewatch-blog](https://github.com/LifeWatchINBO/lifewatch-blog) and [eurasian-spoonbill](https://github.com/LifeWatchINBO/eurasian-spoonbill) repository to the same directory. The latter one is the theme of the blog and required to generate the correct output.
2. Create a virtual Python environment (if not yet installed, install `virtualenv` first: `sudo pip install virtualenv`):

  ```shell
  cd lifewatch-blog
  virtualenv py-env --python=python2.7
  source py-env/bin/activate
  pip install pelican
  pip install markdown
  ```
3. Create `test-output` directory

  ```shell
  mkdir test-output
  ```

## Writing setup instructions

1. Start a simple server from `test-output`. Note: the port `8080` is hardcoded in the `dev-settings.py`.

  ```shell
  cd test-output
  python -m SimpleHTTPServer 8080
  ```

2. Go to <http://localhost:8080> to see the test website.
3. To generate new content, you'll need Pelican, which will run in the virtual environment you have set up. Activate the virtual environment:

  ```shell
  cd ..
  source py-env/bin/activate
  ```

## Writing instructions

1. Write content locally on the `dev` branch.
2. Go to `content/posts` and create a new one by copy/pasting another one and updating the filename, text and metadata.
3. The syntax of the post is:

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

5. Generate your content locally with `pelican -s dev-settings.py` (which will generate the files in `test-output`). You can also use `pelican -s dev-settings.py --autoreload` for automatic generation.
6. See your content locally at <http://localhost:8080>.
7. Push your commits to GitHub (content in `test-output` will be ignored).
8. Ask for feedback via a pull request (`dev` -> `master`).
9. Incorporate feedback.
7. Update the post date.

## Publishing instructions

### Generate output

1. Generate output locally with `pelican -s settings.py`. Files will be updated in the `output` folder.
2. Verify the output in your browser.
3. Push your commits to GitHub (these will be included in the open pull request).
4. Accept the pull request to `master`.

### Update content on server

1. Login to the production server.
2. Go to the `lifewatch-blog` directory.
3. Use `git pull https://github.com/inbo/lifewatch-blog master`.
4. Verify on <http://lifewatch.inbo.be/blog>.
