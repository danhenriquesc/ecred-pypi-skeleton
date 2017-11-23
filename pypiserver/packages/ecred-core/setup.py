import os

import setuptools

module_path = os.path.join(os.path.dirname(__file__), 'ecred_core.py')
version_line = [line for line in open(module_path)
                if line.startswith('__version__')][0]

__version__ = version_line.split('__version__ = ')[-1][1:][:-2]

setuptools.setup(
    name="ecred-core",
    version=__version__,
    url="https://pypi.ecredpypiserver.com/ecred-core/",

    author="Serasa Experian",
    author_email="serasa@experian.com",

    description="Core of ecred.",
    long_description=open('README.rst').read(),

    py_modules=['ecred_core'],
    zip_safe=False,
    platforms='any',

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
