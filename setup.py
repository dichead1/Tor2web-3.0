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

# These are data files that are to be customized by the user
data_dirs = ['lists', 'templates', 'static']
data_files = []

for d in data_dirs:
    data_paths = []
    def cb(path):
        data_paths.append(path)
    walk_dir_and_callback(d, cb)
    data_files.append((os.path.join(install_directory, d), data_paths))

requires = [
"twisted (==12.3.0)",
"zope.interface (>=4.0.0)",
"pyOpenSSL"
]

setup(
    name="tor2web",
    version="0.3",
    author="Random GlobaLeaks developers",
    author_email = "info@globaleaks.org",
    url="https://tor2web.org/",
    packages=["tor2web", "tor2web.utils"],
    data_files=data_files,
    scripts=["scripts/tor2web"],
    requires=requires
)

try:
    from twisted.plugin import IPlugin, getPlugins
    list(getPlugins(IPlugin))
except Exception, e:
    log.warn("Failed to update Twisted plugin cache.")
    log.warn(str(e))
