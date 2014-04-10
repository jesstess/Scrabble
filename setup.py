from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='Scrabble',
    version='1.0',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    author='Jessica McKellar',
    author_email='jesstess@mit.edu',
    scripts=['bin/scrabble_cheater'],
    package_data = {'': ['*.txt']}
)
