-- install git 
  sudo add-apt-repository ppa:git-core/ppa
  sudo apt-get update
  sudo apt-get install git
  
-- config git
1. generate ssh
 ssh-keygen -t rsa -C "name@company.com"
 
2. add sshkey

3. config name and mail
  git config --global user.name "name"
  git config --global user.email "name@company.com"




--get remote branch to local:
git checkout --track origin/branch-name
the command will create a local branch named branch-name ,tracking the remote branch origin/branch-name.
--track is shortband for git checkout -b [branch] [remotename]/[branch]

If you are trying to "checkout" a new remote branch (that exists only on the remote, but not locally), here's what you'll need:

git fetch origin
git checkout --track origin/<remote_branch_name>
