#!/usr/bin/env python
# -*- coding: utf-8 -*-
import excavator

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = excavator.__version__

readme = open('README.rst').read()

setup(
    name='env-excavator',
    version=version,
    description="""Tools for exconverting environment variables to native python objects""",
    long_description=readme,
    author='Piper Merriam',
    author_email='piper@simpleenergy.com',
    url='https://github.com/simpleenergy/env-excavator',
    packages=[
        'excavator',
    ],
    include_package_data=True,
    license="MIT",
    zip_safe=False,
    keywords='env-excavator',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
