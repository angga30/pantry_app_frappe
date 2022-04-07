from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in management_pantry/__init__.py
from management_pantry import __version__ as version

setup(
	name="management_pantry",
	version=version,
	description="Management for supplies pantyr",
	author="Prabunesia Teknologi",
	author_email="angga@prabunesia.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
