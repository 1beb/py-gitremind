import git
import os
import re
import subprocess as s


watch = "~"
interval = 30
new_file_action = "add" # add | limit | ignore | warn
new_file_size_limit = 1 # 1 megabyte
push_action = "always" # always | ignore | warn
default_commit_message = "Automatic commit by py-gitremind"
branch_action = "new" # new | new-if-master | same-if-not-master
cmd = 'find ~ -name .git -type d -prune'
locations = os.popen(cmd).read().split('\n')
locations = [re.sub('.git','', x) for x in locations]

for location in locations:
    pass
    # Do this

location = locations[0]
repo = git.Repo(location)
if len(repo.index.diff(None)):
    if repo.active_branch.name == 'master':
        # checkout new branch
    else:
        # 
else:
    pass


if len(repo.untracked_files) > 0:
    # if there are untracked files
    pass    


# s.call(['notify-send', 'Hello', 'There!'])
