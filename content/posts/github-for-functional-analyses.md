# Why we document our functional requirements on a Github repository

We had some issues with the traditional way of documenting functional requirements in a Word file:

- It's hard to make sure everybody on the team is working with the latest version,
- it's a pain to keep it up to date: when an illustration of say a UI sketch changes, you have to open your drawing tool, export an image, import it in the Word file, layout the document again, change the version number (or not, which is not correct) and redistribute the new version,
- you can't expect the business to read this document several times. They might read the first version, but after three versions, nothing is being verified anymore.
- The analist is spending way to much time layouting the document over and over and over again.

We distilled a couple of practices out of our experience that should enhance our situation:

## 1. Keep your content separated from your layout,

We write all our documentation in Markdown. Basically, those are txt files in a standardized format that allow you to write headers, bulletted lists, numbered lists, code blocks, etc. You can think of Markdown as a readable html file and indeed, with a Markdown editor you can easily generate html from your Markdown. Add a css file to your html, and you get a nicely formatted page. The benefit of using Markdown is that you can focus on content without worrying about layout. Also, you can insert links in your Markdown files to other files or images (similarly as you would do with html) meaning that when you change an image, you don't have to change the Markdown file as it renders the image when your viewing the file with an editor. Using Markdown removed a lot of layouting overhead.

We even document our domain model as xsd file and our UI sketches as html. Everything is txt now, no layout issues anymore.

## 2. Organize your content well

All our Markdown files are organized in logical folders and subfolders. This is not only for finding relevant information quickly, but also makes it possible to automatically generate output. More on that later.

## 3. Avoid redundancy in your documentation

Ok, this one might be impossible. But at least be aware of the advantage of having non redundant information and try to avoid redundancy whenever possible. If you need an explanation for a concept, add a link to the concepts file in your Markdown file in stead of repeating yourself. This is very similar to the DRY principle in coding: don't repeat yourself. By not repeating yourself, if something changes, you only have to change it at one place. This makes your documentation light and makes it much easier to keep your documentation up to date with the ongoing development.

# And then we added git/Github

At this point, we had all our documentation as txt files (Markdown for documentation, html for UI sketches, xsd for domain model, tsv for controlled vocabulary and even a json file to describe the expected fields in an input Excel file). Besides the fact that we have separated all content from the layout, this brings another advantage: you can use a revision system to keep track of all changes made to the documentation similar to what you would do with source code. We use git and Github to do this and I'll explain how we do it in the next paragraphs.

## Git keeps track of the changes made to the documentation

When somebody changes something to the documentation, he has to commit that change and include a commit message stating why he or she changed it. Git stores all commits and you can easily go back to earlier versions. You can view the history of each file (say for example the xsd file containing the domain model) to see how it evolved, which changes were made by who and why.

## Git distinguishes the master copy of the documentation from working copies

Git can work with several current versions of your documentation. It calls those 'branches'. The most important branch is the master branch. For developers, the master branch contains the stable production code. Changes to the master branch are only allowed when they have been tested and made sure they don't break anything. The master branch is treated with extreme care.

We treat the master branch of our documentation exactly that way. Nobody makes changes to the master branch on its own. All changes pass revision by other team members. If you want to add stuff to the master branch, you first create a new branch, make your changes on that branch, and than send a pull request, which is a request to merge the changes of your branch into the master branch. We have the convention that you do not accept your own pull requests, so somebody else from the team has to review your changes, approve them (or point you to mistakes) and accept the changes when everything seems ok.

This system has several advantages:

- The latest stable version is always the master branch. No discussion about that.
- Everybody can work on a local branch simultanously. You don't have to wait for someone to finish his work and redistribute a new version which you can start editing. What happens when two people edit the same thing? This is what git was designed for. When two team members edited the same line in the same file, git detects the conflict. You have to resolve the conflict manually by indicating which edit can override the other.
- Changes always pass a revision before getting into the master branch.

## So what does Github do?

All the above can be accomplished using git only. Github is a central place where you can host you repository.  Everybody from the team checks out the documentation from the repository in order to stay up to date. Using Github allows you to:

- Don't have to set up a server for your central repository yourself,
- Take advantage of the brilliant UI Github offers to browse through files, history, pull requests, etc. This is more fun because Github understands Markdown and renders those files with a simple layout which makes it easier to read,
- Discuss pull requests containing edits that need to be merged into the master branch before accepting them,
- Report issues using the included issue tracker and discuss and assign issues,
- Host associated html pages (in our case, our mockup) with github-pages,
- Use the included wiki,
- Much, much more.

## How do we involve the business? 

The business has no access to our repository. It's too technical, they would get lost. In stead of bombing them with several versions of our requirements document, which they don't read more than once, we communicate with them only about certain topics. If something needs to be added or edited to our documentation, we perform the edits and send a pull request. We don't send this back to the business for approval, this should be done before making the edits to the documentation.

Nevertheless, a formal document containing the entire requirements documentation is still needed. We consider this an output of our repository. Now here comes the really cool stuff. With everything in text files, and organized well, this document can be generated. After all, this document is nothing more than a concatenation of all the text files, in a logical order. If you started every text file with a header, that's really all you need to do.

However, we're still having trouble with images though. As we don't include images in our repository, they can't be added to the final document. So you still need some manual intervention there. Also stuff like autonumbering, and a generated table of contents is not been taken care of at this point (although that is technically possible).

## Disadvantages

No method is perfect. Here are some disadvantages:

- Using git is pretty technical. All our team members have a little hacking background so we use the command line for that. However, that might not be feasible with every team and you might need to look for a GUI (of which we cannot suggest one). Nevertheless, some basic to average knowledge of git is required.
- You need to find solutions to work with images. Images can be included in repositories (and in fact, Github has a neat interface to review edits on images) but we prefer not to do so. Every "export..." and "save as..." that you can exclude from your process makes your documentations easier to maintain. If you want to follow this philosophy, you need to look for other ways to document the content of you images. We, for example, used an `xsd` to document our domain model, but we can't immediately come up with a solution for activity diagrams or use case diagrams.
- You need to streamline the process of creating a final (as in static) document. A little time will need to be invested in creating a generate script (which can be re-used in other projects though) and even that might not completely liberate you from some layouting work.

# Conclusions

Documenting our requirements as txt files and keeping track of their changes using git/Github allowed us to:

- Reduce the layouting work and focus more on the content,
- Keep the documentation manageble so we can keep it up to date with ongoing development,
- Easily collaborate,
- Keep track of edits, comments on edits, discussions, issues, ...

Definitely worth a try!

