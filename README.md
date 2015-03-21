# Meta Github-Pages
Guide to using a GIT submodule for storing your github pages content for a project repository.

### Steps

1. You are starting off with a repository that already contains content and has no `gh-pages` branch yet.
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
    $ git clean -fdx
    ```
