#!/usr/bin/env python

from distutils.core import setup


setup(name='ssh-selector',
      version='1.0',
      description='Simple selector script for ssh',
      author='Martin Kuzma',
      scripts= ['src/ssh-selector.py', 'sshs'],
      data_files=[
            ('/etc/ssh-selector/', ['config/config.json'])
      ]
      )