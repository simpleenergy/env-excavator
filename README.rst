=============================
env-excavator
=============================

.. image:: https://badge.fury.io/py/env-excavator.png
    :target: https://badge.fury.io/py/env-excavator

.. image:: https://travis-ci.org/simpleenergy/env-excavator.png?branch=master
    :target: https://travis-ci.org/simpleenergy/env-excavator

Tools for exconverting environment variables to native python objects

Quickstart
----------

Install env-excavator::

    pip install env-excavator

Example use it in a project::

    >>> import os
    >>> import excavator
    >>> os.environ['FROM_EMAIL'] = 'admin@example.com'
    >>> excavator.env_string('FROM_EMAIL')
    ... 'admin@example.com'
    >>> os.environ['DEBUG'] = 'True'
    >>> DEBUG = excavator.env_bool('DEBUG')
    ... True
    >>> os.environ['ALLOWED_HOSTS'] = '.example.com,.example.net'
    >>> excavator.env_list('ALLOWED_HOSTS')
    ['.example.com', '.example.net']
