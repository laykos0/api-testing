## Finalize and Commit Changes

After fixing the error in the API, let's try to commit again.

Add all changes in the current directory to the staging area before the commit.

`git add .`{{exec}}

Make a commit with a message indicating that we have fixed the division by zero error:

`git commit -m "Fix ZeroDivisionError in GET /divide"`{{exec}}

<!-- TODO: GIT HOOK PRE-COMMIT GONNA RUN ALL OUR TESTS REGRESSIVELY? -->

## Verification with Git

Now all tests should pass and commit should be added.

Let's verify it with Git.

`git log`{{exec}}

It should now print your commit.
