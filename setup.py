#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='Protego',
      version='0.2.1',
      description='Pure-Python robots.txt parser with support for modern conventions',
      long_description=open("README.rst").read(),
      long_description_content_type='text/x-rst',
      url='https://github.com/scrapy/protego',
      author='Anubhav Patel',
      author_email='anubhavp28@gmail.com',
      license='BSD',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      py_modules=['protego'],
      python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
      install_requires=['six'],
      tests_require=['pytest'],
      include_package_data=True,
      keywords=['robots.txt', 'parser', 'robots', 'rep'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
      ],
      )
