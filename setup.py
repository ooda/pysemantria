from os.path import join, dirname

from setuptools import setup, find_packages

setup(
    name='semantria',
    version='0.0.1',
    description="Semantria's Python API",
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    author='Hugues Demers',
    author_email='hugues.demers@ooda.ca',
    url='https://github.com/ooda/semantria-python',
    license="MIT",
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[]
)

