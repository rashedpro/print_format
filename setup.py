from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in print_format/__init__.py
from print_format import __version__ as version

setup(
	name="print_format",
	version=version,
	description="this app for print foramt",
	author="rashedpro2025@gmail.com",
	author_email="rashedpro2025@gmail.com[C",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
