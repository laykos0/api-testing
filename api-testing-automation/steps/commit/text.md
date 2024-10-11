## Stage and Commit Changes

Now, switch back to the main app directory.

`cd /root/filesystem/app`{{exec}}

Let's try Commit some changes to the API including the faulty endpoint

`git add .`{{exec}}

`git commit -m "message"`{{exec}}

<p align="center">
  <img src="./hooks.png" width="350px">
</p>

As shown in the flowchart, the line of command `git add .` stage changes in the git directory, and `git commit -m "message"` attempts to commit the changes. However, since the pre-commit hook is set, the tests must be passed to successfully commit the changes.

## Verification with Git

We see that our tests failed, therefore the commit also fails. Let' verify it with Git:

`git log`{{exec}}

 It should print 
 
`fatal: your current branch 'master' does not have any commits yet`