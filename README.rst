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
    >>> import excavator as env
    >>> os.environ['FROM_EMAIL'] = 'admin@example.com'
    >>> env.get('FROM_EMAIL')
    'admin@example.com'
    >>> os.environ['DEBUG'] = 'True'
    >>> env.get('DEBUG', type=bool)
    True
    >>> os.environ['ALLOWED_HOSTS'] = '.example.com,.example.net'
    >>> env.get('ALLOWED_HOSTS', type=list)
    ['.example.com', '.example.net']
