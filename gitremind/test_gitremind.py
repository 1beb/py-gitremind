from unittest import TestCase
import os
import re
import shutil
import git
import datetime
from gitremind import gitremind

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
        self.assertTrue(
            repo.active_branch.name == 'master'
        )
        branchname = 'pgr_' + re.sub('-','_',str(datetime.date.today()))
        self.assertTrue(
            repo.active_branch.name == branchname
        )

        self.delete_repo()

    def test_branch_action_new_if_master(self):
        pass
    
    def test_branch_action_same_if_not_master(self):
        pass

    def test_new_file_action_add(self):
        pass

    def test_new_file_action_limit(self):
        pass

    def test_new_file_ignore(self):
        pass

    def test_new_file_action_warn(self):
        pass

    def test_new_file_size_limit(self):
        pass
