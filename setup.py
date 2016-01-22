
from setuptools import setup, find_packages
import sys, os

setup(name='zeus',
    version='0.1.0',
    description="A command line interface",
    long_description="A command line interface",
    classifiers=[],
    keywords='',
    author='Cristobal Villarroel',
    author_email='cristobal23@gmail.com',
    url='https://www.github.com/cristobal23/zeus',
    license='BSD-3-Clause',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    install_requires=[
        ### Required to build documentation
        # "Sphinx >= 1.0",
        ### Required for testing
        # "nose",
        # "coverage",
        ### Required to function
        'cement',
        ],
    setup_requires=[],
    entry_points="""
        [console_scripts]
        zeus = zeus.cli.main:main
    """,
    namespace_packages=[],
    )
