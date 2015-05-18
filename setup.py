#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ast
import re
from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()


_version_re = re.compile(r'__version__\s+=\s+(.*)')


with open('photo_organizer/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


install_requirements = [
    # TODO: put package requirements here
]


entry_points = {
    # TODO: put entry points (e.g. 'console_scripts') here
}


setup(
    name='photo-organizer',
    version=version,
    description='Organize some photos by EXIF tags',
    long_description=readme,
    author='Andy Freeland',
    author_email='andy@andyfreeland.net',
    url='https://github.com/rouge8/photo-organizer',
    packages=find_packages(exclude=['tests']),
    install_requires=install_requirements,
    entry_points=entry_points,
    zip_safe=False,
    classifiers=[
        'Private :: Do Not Upload',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
