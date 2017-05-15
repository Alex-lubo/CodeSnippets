--get remote branch to local:
git checkout --track origin/branch-name
the command will create a local branch named branch-name ,tracking the remote branch origin/branch-name.
--track is shortband for git checkout -b [branch] [remotename]/[branch]

If you are trying to "checkout" a new remote branch (that exists only on the remote, but not locally), here's what you'll need:

git fetch origin
git checkout --track origin/<remote_branch_name>