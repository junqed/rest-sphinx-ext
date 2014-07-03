# coding: utf-8

from setuptools import setup, find_packages

setup(name='rest-sphinx-ext',
      version='0.1',
      description='Sphinx extention for collecting docs from view functions',
      classifiers=[
          "Programming Language :: Python"
      ],
      author='Eugene Fominykh',
      author_email='junqed@gmail.com',
      install_requires=[
        'Sphinx>=1.2.1',
      ],
      keywords='sphinx python',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
)
