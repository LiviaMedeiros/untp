#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = 'untp',
    version = '2.0.0',
    description = 'A command line tool to split TexturePacker published files.',
    url = 'https://github.com/neobenedict/untp',
    author = 'justbilt, neobenedict',
    author_email = '',
    license = 'MIT License',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],    
    keywords = 'untp texturepacker cocos',
    install_requires = [
        'Pillow',
        'parse'
    ],
    packages = find_packages("src"),
    package_dir = {'':'src'},
    entry_points = {
        'console_scripts': [
            'untp = untp.untp:main',
        ],
    }
)