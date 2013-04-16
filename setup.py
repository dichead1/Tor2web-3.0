#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import hashlib
import urllib2
from distutils import log
from setuptools import setup

def walk_dir_and_callback(dirname, cb):
    """
    Args:
        dirname: directory to walk

        cb: callback function to call on every path. Will take as argument a
            path.
    """
    for path, _, filenames in os.walk(os.path.join('tor2web', dirname)):
        for filename in filenames:
            cb(os.path.join(path, filename))

install_directory = os.path.join('/', 'etc', 'tor2web')

# These are static files that are part of the tor2web package
tor2web_package_data = []

# These are data files that are to be customized by the user
data_dirs = ['lists', 'templates', 'static']
data_files = [(install_directory, ['tor2web.conf.example'])]

for d in data_dirs:
    data_paths = []
    def cb(path):
        data_paths.append(path)
    walk_dir_and_callback(d, cb)
    data_files.append((os.path.join(install_directory, d), data_paths))

setup(
    name="tor2web",
    version="0.2",
    author="Random GlobaLeaks developers",
    author_email = "info@globaleaks.org",
    url="https://tor2web.org/",
    install_requires=open('requirements.txt').readlines(),
    packages=["tor2web", "tor2web.utils", "twisted.plugins"],
    package_data={"twisted": ["plugins/tor2web_plugin.py"],
                  "tor2web": tor2web_package_data},

    data_files=data_files,
    scripts=["scripts/tor2web"]
)
try:
    from twisted.plugin import IPlugin, getPlugins
    list(getPlugins(IPlugin))
except Exception, e:
    log.warn("Failed to update Twisted plugin cache.")
    log.warn(str(e))
