#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import io
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup

def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()


setup(
    name='{{ cookiecutter.distribution_name }}',
    version='{{ cookiecutter.version }}',
{%- if cookiecutter.license != "no" %}
    license='{{ {
        "BSD 2-Clause License": "BSD-2-Clause",
        "BSD 3-Clause License": "BSD-3-Clause",
        "MIT license": "MIT",
        "ISC license": "ISC",
        "Apache Software License 2.0": "Apache-2.0",
        "GNU Lesser General Public License v3 or later (LGPLv3+)": "LGPL-3.0-or-later",
        "GNU Lesser General Public License v3 (LGPLv3)": "LGPL-3.0-only",
        "GNU Lesser General Public License v2.1 or later (LGPLv2+)": "LGPL-2.1-or-later",
        "GNU Lesser General Public License v2.1 (LGPLv2)": "LGPL-2.1-only",
      }[cookiecutter.license]
    }}',
{%- endif %}
    description="",
    long_description="",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
{%- if cookiecutter.license == "no" %}
{%- elif cookiecutter.license in ["BSD 2-Clause License", "BSD 3-Clause License"] %}
        'License :: OSI Approved :: BSD License',
{%- elif cookiecutter.license == "MIT license" %}
        'License :: OSI Approved :: MIT License',
{%- elif cookiecutter.license == "ISC license" %}
        'License :: OSI Approved :: ISC License (ISCL)',
{%- elif cookiecutter.license == "Apache Software License 2.0" %}
        'License :: OSI Approved :: Apache Software License',
{%- elif 'LGPLv3+' in cookiecutter.license %}
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)'
{%- elif 'LGPLv3' in cookiecutter.license %}
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)'
{%- elif 'LGPLv2' in cookiecutter.license %}
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)'
{%- elif 'LGPLv2' in cookiecutter.license %}
        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)'
{%- endif %}
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Utilities',
        'Private :: Do Not Upload',
    ],
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    python_requires='>=3.6',
    install_requires=[
{%- if cookiecutter.command_line_interface == 'typer' %}
        'typer',
{%- elif cookiecutter.command_line_interface == 'click' %}
        'click',
{%- endif %}
        # eg: 'aspectlib==1.1.1', 'six>=1.7',
    ],
    extras_require={
        'dev': ['pytest']
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    },
{%- if cookiecutter.command_line_interface != 'no' %}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.command_line_interface_bin_name }} = {{ cookiecutter.package_name }}.cli:main',
        ]
    },
{%- endif %}
)
