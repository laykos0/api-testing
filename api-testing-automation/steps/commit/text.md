## Stage and Commit Changes

Now that the **pre-commit hook** has been set, switch back to the main app directory.

`cd /root/filesystem/app`{{exec}}

Let's try to commit changes to the project, including the faulty division endpoint.

`git add .`{{exec}}

`git commit -m "initial commit"`{{exec}}

## Explanation
Note that the since the **pre-commit hook is set**, the **commit fails**, as all of the **tests must pass** to **successfully commit** the changes. The diagram below illustrates the process.

<p align="center">
  <img src="./hooks.png" width="350px">
</p>

## Verification with Git

We see verify that the commit has been aborted by running:

`git log`{{exec}}

The expected output of the command is:

`fatal: your current branch 'master' does not have any commits yet`
