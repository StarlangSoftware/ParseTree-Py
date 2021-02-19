from setuptools import setup

setup(
    name='NlpToolkit-ParseTree',
    version='1.0.6',
    packages=['ParseTree', 'ParseTree.NodeCondition'],
    url='https://github.com/StarlangSoftware/ParseTree-Py',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='Constituency Parse Tree Library',
    install_requires = ['NlpToolkit-Dictionary']
)
