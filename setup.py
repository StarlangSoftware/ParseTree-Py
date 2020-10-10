from setuptools import setup

setup(
    name='NlpToolkit-ParseTree',
    version='1.0.5',
    packages=['ParseTree', 'ParseTree.NodeCondition'],
    url='https://github.com/olcaytaner/ParseTree-Py',
    license='',
    author='olcaytaner',
    author_email='olcaytaner@isikun.edu.tr',
    description='Constituency Parse Tree Library',
    install_requires = ['NlpToolkit-Dictionary']
)
