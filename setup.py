try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import py2exe

config = {
"description": "Tests the probability of the user developing type-2 diabetes.",
"author": "Kyaw Oo",
"url": "N/A",
"download_url": "N/A",
"author_email": "ko3473@highamsparkschool.co.uk",
"version": "0.1",
"install_requires": ["nose"],
"packages": ["Type_2"],
"scripts": [],
"name": "Type-2"
}

setup(**config)
