This repository contains the content and settings for the [LifeWatch INBO blog](http://lifewatch.inbo.be/blog). It is generated into a static website with [Pelican](http://docs.getpelican.com/en/3.1.1/).

## Installation instructions

On your local computer, make sure you have cloned the `lifewatch-blog` and `eurasian-spoonbill` repository to the same directory. The latter one is the theme of the blog and required to generate the correct output.

### Create virtual Python environment

If not yet installed, install `virtualenv` first: `sudo pip install virtualenv`.

```shell
cd lifewatch-blog
virtualenv py-env --python=python2.7
source py-env/bin/activate
pip install pelican
pip install markdown
```

### Create test-output directory

```shell
mkdir test-output
```

### Start simple server

```shell
cd test-output
python -m SimpleHTTPServer 8080
```

Go to <http://localhost:8080> for the test website. Use the publishing instructions to generate the website.

### Activate virtual Python environment

Could be done in a new terminal window.

```shell
.. cd
source py-env/bin/activate
```

## Publishing instructions

### Write and ask feedback

1. Go to `content`
2. Write content on your local `dev` branch.
3. Optional: test locally with `pelican -s dev-settings.py` which will generate the website in `test-output` at <http://localhost:8080>.
4. Push your commits to GitHub.
5. Ask for feedback via a pull request (`dev` -> `master`).
6. Incorporate feedback.
7. Update the post date.

### Generate output

1. Generate output locally with `pelican -s settings.py`. Files will be updated in the `output` folder.
2. Verify the output in your browser.
3. Push your commits to GitHub (these will be included in the open pull request).
4. Accept the pull request to `master`.

### Update content on server

1. Login to the production server.
2. Go to the `lifewatch-blog` directory.
3. Use `git pull https://github.com/LifeWatchINBO/lifewatch-blog master`.
4. Verify on <http://lifewatch.inbo.be/blog>.
