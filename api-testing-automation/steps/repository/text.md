First, let's move to the working directory of the app.

`cd /root/filesystem/app`{{exec}}

Start with initializing a new Git repository in the current directory.

`git init`{{exec}}

This command can show you how the repository looks like:

`tree -a`{{exec}}

As we see, our working directory includes a folder named .git, it's the Git setting files for our project. Then we have our API inside the folder named src, and our test cases inside the folder named tests. There's also a file named .pytest.ini standing alone, it's the configuration file for pytest.
