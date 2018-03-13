# Contributing guidelines

## Writing a post

You can either write a post via the GitHub user interface or locally. The procedure is the same:

1. Create a new branch
2. Start a new post by copy/pasting one from `content/posts` and update the filename and metadata
3. Write your post using the following syntax:

    ```Markdown
    ---
    title: Jurassic Park
    slug: jurassic-park
    date: 2012-12-17 17:00
    authors: Alan Grant, Ian Malcolm // Or Author: Alan Grant
    tags: dinosaurs, endorsement, quote
    summary: After much consideration...
    status: draft // To hide the post from the index list for now
    ---

    Blog content is written in Markdown
      
    ## Headings start at H2 (since post title is H1)

    Links to other posts: [bird tracking data are open]({filename}bird-tracking-data-published.md)

    Images: ![Bird tracking explorer]({filename}/images/bird-tracking-explorer.png)

    Code (without the \):

    \```SQL
    SELECT * FROM bird_tracking
    \```
    ```

4. Commit and push your changes
5. Create a pull request and ask for feedback
6. Incorporate the feedback and finish your post

## Generate website

Content is generated as a static website with [Pelican](http://docs.getpelican.com). This needs to be done locally. Ask [@peterdesmet](https://github.com/peterdesmet) to do this or follow the deployment instructions in the [README](README.md).
