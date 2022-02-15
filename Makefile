test: test_deps
	python -m pytest

test_deps:
	python -m pip install pytest

package_deps:
	python -m pip install wheel

setup_packages: package_deps gym/setup.py
	python gym/setup.py sdist
	python gym/setup.py bdist_wheel

dev_packages: gym/setup.py
	cd gym && python setup.py develop

.PHONY: test package_deps