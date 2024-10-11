Finally let's try to commit again

...

Add all changes in the current directory to the staging area, the stage before commit.

`git add .`{{exec}}

Make a commit with comment indicating that we have fixed the error of division by zero.

`git commit -m "Fix ZeroDivisionError in "`{{exec}}

<!-- TODO: GIT HOOK PRE-COMMIT GONNA RUN ALL OUR TESTS REGRESSIVELY? -->

All tests pass and commit added

`git log`
