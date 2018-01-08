from setuptools import setup, find_packages

VERSION = '0.0.1'

setup(
    name='sparkviz',
    version=VERSION,
    author='Holden Karau',
    author_email='holden@pigscanfly.ca',
    packages=find_packages(),
    url='https://github.com/nteract/improved-spark-viz',
    license='LICENSE',
    description='Improve visualizations for PySpark',
    long_description=open('README.md').read(),
    install_requires=[
        'pyspark>=2.2.0',
        'pandas',
    ],
    test_requires=[
        'nose==1.3.7',
        'coverage>3.7.0',
        'unittest2>=1.0.0',
        'spark-testing-base',
    ],
)
