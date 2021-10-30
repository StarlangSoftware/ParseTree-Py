from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='NlpToolkit-ParseTree',
    version='1.0.8',
    packages=['ParseTree', 'ParseTree.NodeCondition'],
    url='https://github.com/StarlangSoftware/ParseTree-Py',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='Constituency Parse Tree Library',
    install_requires = ['NlpToolkit-Dictionary'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
