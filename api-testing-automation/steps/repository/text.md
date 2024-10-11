## Initialize Git Repository
First, let's move to the **working directory** of the app.

`cd /root/filesystem/app`{{exec}}

Start with **initializing** a new **Git repository** in the current directory.

`git init`{{exec}}

To see what the **newly initialized repository** looks like, run:

`tree -a`{{exec}}

As we see, our working directory now includes:

- **`/src`**: Contains source code of the API. 
- **`/tests`**: Holds all of our test cases.
- **`/.git`**: Contains Git configuration files for our project.
- **`.pytest.ini`** - Configuration file for Pytest.

**Note**: Directory `./git` and file `.pytest.ini` are both **hidden**, hence flag `-a` is required.


