from setuptools import setup

__author__ = "Hanyu Jin"
__version__ = '1.0.0'
__email__ = "henrychin2006@gmail.com"
__license__ = "MIT"
__copyright__ = "Copyright Hanyu Jin"

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = "pymannkendall",
    version = __version__,
    author = __author__,
    author_email = __email__,
    description = ("A python package for liang-klleeman infomation flow causality test."),
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Koni2020/pyLiang",
    packages = ["pyLiang"],
    license = __license__,
    install_requires = ["numpy"],
    classifiers = [
		"Programming Language :: Python :: 2.7",
		"Programming Language :: Python :: 3.4",
		"Programming Language :: Python :: 3.5",
		"Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
		"Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
		"Intended Audience :: Science/Research",
		"Operating System :: OS Independent",
		"Topic :: Scientific/Engineering",
		"Development Status :: 1 - Production/Stable"
    ]
)

