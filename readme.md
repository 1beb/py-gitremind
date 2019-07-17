# py-gitremind

You can trade time in the future for money, but you can't trade money for time that has already past. In the new business reality of speed over everything, losing your work because you forgot to commit is unthinkable. With this in mind, I have created a simply python script that watches a folder (default ~) and does the dirty work of committing, creating a new branch and pushing for you. 

Let's say a commit takes 2.5 seconds. If you commit at least daily, there are 261 days in a year. Setting up this script can save you about 11 minutes. 

The script is extremely simple, intentionally. Fork it!

## Design

### Variables

1. Set watch folder (default ~)
2. Set interval (default 30 mins)
3. Set process as systemd (undecided)
4. Set new file action (undecided)
5. Set push action (undecided)
6. Set default commit message
7. Set default branch action (commit to branch, commit to daily branch, commit to current branch non-master)

### Commit Logic

- search through watch folder
- find uncommitted changes
- if new files, read new file action variable, add or ignore appropriately, respect gitignore
- if on branch master, checkout new branch named after day
- if not on branch master, commit to current branch
- commit using generic message "Automatic commit by pygitremind"

### Devops

See: https://tecadmin.net/setup-autorun-python-script-using-systemd/

- Create install script
 -- copy to usr/bin/pygitremind.py
 -- install sysdemd service files
 -- start system process
- Create uninstall script
- Create systemd service files (service + timer)


