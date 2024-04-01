from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1.0'
DESCRIPTION = 'A utility tool for building and publishing Python packages to PyPI'
LONG_DESCRIPTION = 'WheelSmith is a command-line tool that simplifies the process of building and publishing Python packages to the Python Package Index (PyPI). It combines the steps of building wheels and uploading them to PyPI into a single command, making it easier for developers to distribute their packages.'

# Setting up
setup(
    name="wheelsmith",
    version=VERSION,
    author="Your Name",
    author_email="your.email@example.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['wheel', 'twine', 'rich'],
    keywords=['python', 'packaging', 'pypi', 'wheels', 'publishing'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    entry_points={
        'console_scripts': [
            'wheelsmith=wheelsmith.main:build_and_publish',
        ],
    },
)