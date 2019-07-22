import git
import os
import re
import datetime


def gitremind_wrap(
    new_file_action="add",
    new_file_size_limit=1, 
    push_action="always",
    default_commit_message="Automatic commit by py-gitremind",
    branch_action="new",
    master_branch="master",
    cmd="find ~ -name .git -type d -prune"):

    locations = os.popen(cmd).read().split('\n')[:-1]
    locations = [re.sub('.git','', x) for x in locations]

    for location in locations:
        gitremind(location,    
            new_file_action,
            new_file_size_limit, 
            push_action,
            default_commit_message,
            branch_action,
            master_branch)
    

def gitremind(
    location,
    new_file_action="add",
    new_file_size_limit=1, 
    push_action="always",
    default_commit_message="Automatic commit by py-gitremind",
    branch_action="new",
    master_branch="master"):


    repo = git.Repo(location)

    if (len(repo.untracked_files) > 0) & (new_file_action != 'ignore'):
        # if there are untracked files
        untracked = repo.untracked_files
        for f in untracked:
            size = os.stat(os.path.join(location, f)).st_size/1024/1024
            if size < (new_file_size_limit*1.05):
                repo.index.add([f])
                print('Adding file: ' + f)
            else:
                print('File too large, skipping: ' + f)

    if (len(repo.index.diff(None)) > 0) | (len(repo.index.entries) > 0):
        if (repo.active_branch.name == master_branch) | (branch_action =='new'):
            branchname = 'pgr_' + re.sub('-','_',str(datetime.date.today()))
            print('Creating new branch - ' + branchname)
            repo.git.checkout('-b',branchname)

        print('Commiting changes')
        repo.index.commit(default_commit_message)

    if push_action == "always":
        try:
            repo.git.push()
        except git.exc.GitCommandError:
            print("No remote setup for - " + location)

# s.call(['notify-send', 'Hello', 'There!'])
