#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from mockpy import version

with open('Readme.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    "cherrypy",
    "colorama",
    "watchdog",
    "pyyaml"
]

test_requirements = [
    "mock",
    "pytest"
]

setup(
    app=['mockpy.py'],
    name='mockpy',
    version=version.VERSION,
    description="Mockpy is a python open source line utility to create development mock servers..",
    long_description=readme + '\n\n' + history,
    author="Omar Abdelhafith",
    author_email='o.arrabi@me.com',
    url='https://github.com/Ezhvsalate/mockpy',
    packages=[
        'mockpy',
        "mockpy.core",
        "mockpy.models",
        "mockpy.utils",
        "mockpy.status",
    ],
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='mockpy',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.6'
    ],
    test_suite='tests',
    tests_require=test_requirements,
    entry_points={
        'console_scripts': [
            'mockpy=mockpy.mockpy:start',
        ],
    },
)
