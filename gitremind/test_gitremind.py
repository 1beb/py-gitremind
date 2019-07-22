from unittest import TestCase
import os
import re
import shutil
import git
import datetime
from gitremind import gitremind, gitremind_wrap

class TestGitRemind(TestCase):

    def create_repo(self):
        try:
            os.mkdir('tmprepo')
        except OSError:
            print('Could not create directory')
        
        f = open('tmprepo/readme.md', 'w+')

        for i in range(10):
            f.write("This is line %d\r\n" % (i+1))

        f.close()

        git.Repo.init(os.path.join('tmprepo'))

    
    def delete_repo(self):
        shutil.rmtree('tmprepo')

    def create_file_of_size(self, size=1):
        f = open(os.path.join('tmprepo','newfile.txt'),"wb")
        f.seek(size * 1024 * 1024)
        f.write(b"\0")
        f.close()

    def test_branch_action_new(self):
        self.create_repo()
        self.create_file_of_size()
        gitremind('tmprepo',branch_action="new")
        repo = git.Repo('tmprepo')

        self.assertTrue(
            os.stat(os.path.join('tmprepo','newfile.txt')).st_size < 1.1*1024*1024
        )
        self.assertTrue(repo.active_branch.name != 'master')
        branchname = 'pgr_' + re.sub('-','_',str(datetime.date.today()))
        self.assertTrue(repo.active_branch.name == branchname)
        self.delete_repo()
    
    def test_branch_action_same_if_not_master(self):
        self.create_repo()
        self.create_file_of_size()
        repo = git.Repo('tmprepo')
        repo.git.checkout('-b','new_branch')
        self.assertTrue(repo.active_branch.name == 'new_branch')
        gitremind('tmprepo',branch_action="same-if-not-master")
        self.assertTrue(repo.active_branch.name == 'new_branch')
        self.delete_repo()


    def test_new_file_action_add(self):
        self.create_repo()
        self.create_file_of_size()
        gitremind('tmprepo',branch_action="new", new_file_action="add")
        repo = git.Repo('tmprepo')
        self.assertTrue(os.stat(os.path.join('tmprepo','newfile.txt')).st_size < 1.1*1024*1024)
        self.assertTrue(repo.active_branch.name != 'master')
        branchname = 'pgr_' + re.sub('-','_',str(datetime.date.today()))
        self.assertTrue(list(repo.index.entries.keys())[0][0] == 'newfile.txt')
        self.assertTrue(repo.active_branch.name == branchname)
        self.delete_repo()

    def test_new_file_action_limit(self):
        self.create_repo()
        self.create_file_of_size(2)
        gitremind('tmprepo',branch_action="new", new_file_action="add", new_file_size_limit=1)
        repo = git.Repo('tmprepo')
        self.assertTrue(os.stat(os.path.join('tmprepo','newfile.txt')).st_size > 1.1*1024*1024)
        self.assertTrue(repo.active_branch.name != 'master')
        branchname = 'pgr_' + re.sub('-','_',str(datetime.date.today()))
        self.assertTrue(list(repo.index.entries.keys())[0][0] != 'newfile.txt')
        self.assertTrue(repo.active_branch.name == branchname)
        self.delete_repo()

    def test_new_file_ignore(self):
        self.create_repo()
        self.create_file_of_size()
        gitremind('tmprepo',branch_action="new", new_file_action="ignore")
        repo = git.Repo('tmprepo')
        self.assertTrue(os.stat(os.path.join('tmprepo','newfile.txt')).st_size < 1.1*1024*1024)
        self.assertTrue(repo.active_branch.name == 'master')
        self.assertTrue(len(repo.untracked_files) == 2)
        self.assertTrue(repo.untracked_files == ['newfile.txt', 'readme.md'])
        self.delete_repo()


class TestGitRemindWrap(TestCase):

    def create_repo(self, folder='tmprepo'):
        try:
            os.mkdir(folder)
        except OSError:
            print('Could not create directory')
        
        f = open(os.path.join(folder,'readme.md'), 'w+')

        for i in range(10):
            f.write("This is line %d\r\n" % (i+1))

        f.close()

        git.Repo.init(folder)

    
    def delete_repo(self, folder='tmprepo'):
        shutil.rmtree(folder)

    def create_file_of_size(self, size=1, folder='tmprepo'):
        f = open(os.path.join(folder,'newfile.txt'),"wb")
        f.seek(size * 1024 * 1024)
        f.write(b"\0")
        f.close()

    def test_gitremind_wrap(self):
        self.create_repo(folder='tmprepo1')
        self.create_repo(folder='tmprepo2')
        self.create_file_of_size(folder='tmprepo1')
        self.create_file_of_size(folder='tmprepo2')
        gitremind_wrap(cmd='find . -name .git -type d -prune')

        repo = git.Repo('tmprepo1')
        self.assertTrue(os.stat(os.path.join('tmprepo1','newfile.txt')).st_size > 1.1*1024*1024)
        self.assertTrue(repo.active_branch.name != 'master')
        branchname = 'pgr_' + re.sub('-','_',str(datetime.date.today()))
        self.assertTrue(list(repo.index.entries.keys())[0][0] != 'newfile.txt')
        self.assertTrue(repo.active_branch.name == branchname)
        self.delete_repo(folder='tmprepo1')

        repo = git.Repo('tmprepo2')
        self.assertTrue(os.stat(os.path.join('tmprepo2','newfile.txt')).st_size > 1.1*1024*1024)
        self.assertTrue(repo.active_branch.name != 'master')
        branchname = 'pgr_' + re.sub('-','_',str(datetime.date.today()))
        self.assertTrue(list(repo.index.entries.keys())[0][0] != 'newfile.txt')
        self.assertTrue(repo.active_branch.name == branchname)
        self.delete_repo(folder='tmprepo2')


        
