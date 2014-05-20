# LifeWatch INBO blog

This repository contains the content and settings for the [LifeWatch INBO blog](http://lifewatch.inbo.be/blog). It is generated into a static website with [Pelican](http://docs.getpelican.com/en/3.1.1/).

## Instructions

Make sure you have cloned the `lifewatch-blog` and `eurasian-spoonbill` repository to the same local directory. The latter one is the theme repository and is only necessary if you want to generate output.

### Write and ask feedback

1. Write content on your local `dev` branch.
2. Optional: test locally with `pelican -s dev-settings.py -o /path/to/output`.
3. Push your commits to GitHub.
4. Ask for feedback via a pull request (`dev` -> `master`).
5. Incorporate feedback.
6. Update the post date.

### Generate output

1. Generate output locally with `pelican -s settings.py`. Files will be updated in the `output` folder.
2. Verify the output in your browser.
3. Push your commits to GitHub (these will be included in the open pull request).
4. Accept the pull request to `master`.

### Update content on server

1. Login to the production server.
2. Go to the `lifewatch-blog` directory.
3. Use `git pull`.
4. Verify on <http://lifewatch.inbo.be/blog>.
