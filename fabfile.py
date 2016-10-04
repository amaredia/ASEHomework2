from fabric.api import *

def build():
	local('python run.py', capture=False)

def unitTestAll():
	local('python -m unittest discover', capture=False)
