#!/usr/bin/env python
"""
Plain Text Render extention for Python Markdown 

GitHub: https://github.com/Python-Markdown/markdown/

Started and maintaned by Kostiantyn Chumachenko (https://github.com/kostyachum)



License: BSD (see LICENSE.md for details).
"""


import os
from setuptools import setup


__version__, __version_info__ = '1.0.0', (1, 0, 0, 'final', 0)

# Get development Status for classifiers
dev_status_map = {
    'dev':   '2 - Pre-Alpha',
    'alpha': '3 - Alpha',
    'beta':  '4 - Beta',
    'rc':    '4 - Beta',
    'final': '5 - Production/Stable'
}
DEVSTATUS = dev_status_map[__version_info__[3]]

with open('README.md') as f:
    long_description = f.read()

setup(
    name='Plain Text Markdown Extention',
    version=__version__,
    url='https://github.com/kostyachum/python-markdown-plain-text/',
    project_urls={
        'Documentation': 'https://github.com/kostyachum/python-markdown-plain-text/',
        'GitHub Project': 'https://github.com/kostyachum/python-markdown-plain-text',
        'Issue Tracker': 'https://github.com/kostyachum/python-markdown-plain-text/issues'
    },
    description='Plain Text Render extention for Python Markdown .',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Kostiantyn Chumachenko ',
    author_email='kostyachum@gmail.com',
    maintainer='Kostiantyn Chumachenko',
    maintainer_email='kostaychum@gmail.com',
    license='MIT License',
    packages=['markdown_plain_text'],
    python_requires='>=3.6',
    install_requires=["markdown>=3.3.3;python_version<'3.10'"],    
    classifiers=[
        'Development Status :: %s' % DEVSTATUS,
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',        
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Communications :: Email :: Filters',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Software Development :: Documentation',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Filters',        
        'Topic :: Text Processing :: Markup :: Markdown'
    ]
)
