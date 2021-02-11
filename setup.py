#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as requirements_file:
    readme = requirements_file.read()

requirements = []

setup_requirements = []

tests_require = []

setup(
    author="Daniel Wendelken",
    author_email='wendeldr@ucmail.uc.edu',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Useful Python helpers.",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords='swan',
    name='swan',
    packages=find_packages(include=['swan', 'swan.*']),
    setup_requires=setup_requirements,
    url='https://github.com/wendeldr/swan',
    version='0.1.0',
    zip_safe=False,
)