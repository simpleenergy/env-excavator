.PHONY: clean-pyc clean-build

help:
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "testall - run tests on every Python version with tox"
	@echo "release - package and upload a release"
	@echo "sdist - package"

clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

lint:
	tox -e flake8

test:
	py.tests tests

test-all:
	tox

release: clean
	python setup.py sdist bdist_wheel upload

sdist: clean
	python setup.py sdist bdist_wheel
	ls -l dist

docs:
	rm -f docs/hexes.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ hexes
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	open docs/_build/html/index.html
