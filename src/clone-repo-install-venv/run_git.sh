#!/bin/bash

# Purpose:
#   - Clones a repo, checks out to the branch if given.
#   - Installs python venv and requirements.
# Usage: ./script.sh git_url branch_name
# Author: Himel Das

if [ $1 ]
then
	url=$1
	regex="^(https|git)(:\/\/|@)([^\/:]+)[\/:]([^\/:]+)\/(.+).git$"
else
	echo "Please pass the link to the git repo as the first argument."
	exit 1
fi

if [[ $url =~ $regex ]]
then
	git clone $url   
    repo=$(basename $url .git)
    cd $repo
else
	echo "Invalid git url passed."
	exit 1
fi

if [ $2 ]
then
	branch=$2
	git checkout $branch
fi

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
