# [Meta Github-Pages](http://github.com/AstromechZA/meta_github_pages)
A guide to using a GIT submodule for storing your Github pages content for a project repository.

### Steps

1. You are starting off with a repository that might already contain content and has no `gh-pages` branch yet.
2. Create the beginning of a new branch

    ```sh
    $ git symbolic-ref HEAD refs/heads/gh-pages
    ```

3. Remove entire index

    ```sh
    $ rm .git/index
    ```

4. Clean everything out

    ```sh
    $ git clean -dx --force
    ```

5. Add a blank index page (still in repository root folder)

    ```sh
    $ touch index.html
    ```

6. Commit and push!

    ```sh
    $ git add .
    $ git commit -m "Created blank index page"
    $ git push origin gh-pages
    ```

    Now we have a branch for our web content pushed to Github.

7. Switch back to master and link in the branch as a submodule

    ```sh
    $ git checkout master
    $ git submodule add -b gh-pages git@github.com:<username>/<repo name>.git <sub directory>
    $ git commit -m "Linked Github pages submodule"
    $ git push -u origin master
    ```

    **Note**: the `<sub directory>` must not exist yet.

Now the `gh-pages` branch is linked as a subdirectory in `master`. The workflow now
for updating your web content is as follows:

1. `$ cd <sub directory>` (now you're on the gh-pages branch)
2. Make your changes to the website
3. `$ git add .`
4. `$ git commit -m "Moar web content"`
5. `$ git push`
6. `$ cd <repository root>` (now you're back on master)

**Note**: Step 3, 4, and 5 are still in the &lt;sub directory&gt;.

**Note**: You can skip step 5 and use `git push --recurse-submodules` when pushing in master.

### What to do from here

This technique is great if you are generating your web content from your master branch via
build scripts or if you simply want a better way of working without having to switch branches
too often.

This website uses a Python `make.py` script to compile the `README.md` Markdown file into the html of this
document. Bootstrap and Github css is copied into the web folder to make it look a little prettier.

[Checkout the source code in the Github repository to see how this works!](http://github.com/AstromechZA/meta_github_pages)

```sh
$ pip install -r requirements.text
$ python make.py
```
