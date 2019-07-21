import git
import os
import re
import subprocess as s
import datetime


def gitremind_wrap(cmd="find ~ -name .git -type d -prune"):

    locations = os.popen(cmd).read().split('\n')
    locations = [re.sub('.git','', x) for x in locations]

    for location in locations:
        print(location)
    
    pass

def gitremind(
    location,
    new_file_action="add",
    new_file_size_limit=1, 
    push_action="always",
    default_commit_message="Automatic commit by py-gitremind",
    branch_action="new",
    master_branch="master",
    ):


    repo = git.Repo(location)

    if len(repo.index.diff(None)):
        if repo.active_branch.name == master_branch:
            branchname = 'pgr_' + re.sub('-','_',str(datetime.date.today()))
            print('Creating new branch - ' + branchname)
            repo.git.branch(branchname)
        else:
            if branch_action == 'new':
                # Add warning or notification about creating new branch from branch
                branchname = 'pgr_' + re.sub('-','_',str(datetime.date.today()))
                print('Creating new branch - ' + branchname)
                repo.git.branch(branchname)


    if len(repo.untracked_files) > 0:
        # if there are untracked files
        untracked = repo.untracked_files
        for f in untracked:
            size = os.stat(os.path.join(location, f)).st_size/1024/1024
            if size < (new_file_size_limit*1.05):
                repo.index.add([f])
                print('Adding file: ' + f)
            else:
                print('File too large, skipping: ' + f)

    if len(repo.index.diff(None)):
        repo.index.commit(default_commit_message)
        print('Commiting changes')



# s.call(['notify-send', 'Hello', 'There!'])
