# py-gitremind

A python script/process that automatically commits your work on a previously determined interval.

## Design

### Variables

1. Set watch folder (default ~)
2. Set interval (default 30 mins)
3. Set process as systemd (undecided)
4. Set new file action (undecided)
5. Set push action (undecided)
6. Set default commit message

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
 -- 
- Create uninstall script
- Create systemd service files (service + timer)
- 

