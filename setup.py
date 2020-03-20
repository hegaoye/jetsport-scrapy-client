# coding=utf-8
from setuptools import setup, find_packages

setup(
    name='scrapy client',  # package name
    version='1.0-beta',  # package version
    author='jet sport',
    author_email='',
    description='',
    keywords=['src'],
    package=find_packages(include=['src']),
    include_package_data=True,
    platforms="scrapy client",
    entry_points={
        'console_scripts': [
            'run=run:main'
        ]
    },
    zip_safe=False
)
