# py-gitremind

Time is the only resource that you cannot buy back. Oh you can trade money for future time, but wasted time is gone forever. Losing your work, is the same as losing your time. This application watches a folder and commits changes to the repository on configurable schedule and branch. 

I built this application because I find myself often forgetting to submit my work at the end of a workday or at an otherwise critical stage of development. I also find it particularly tedious to create a new branch and commit my work to that branch. Supposedly, one could argue that this only takes a few moments, but a few moments summed up over the course of a lifetime could be weeks drained away on something that is otherwise capable of being automated.

The script is extremely simple, intentionally. Fork it!


## Requirements

```
apt-get install python3 libnotify-bin 
```
## Usage 

```
git clone https://github.com/1beb/py-gitremind.git
# Adjust systemd/gitremind.timer
# Adjust defaults in gitremind/gitremind.py
sudo install.sh
```

## Removal

```
sudo uninstall.sh
```

# Appendix

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


