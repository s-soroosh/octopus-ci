__author__ = 'soroosh'

from distutils.core import setup
import os.path
import setuptools

def read_version(package):
    data = {}
    with open(os.path.join(package, '__init__.py'), 'r') as fd:
        exec(fd.read(), data)
    return data['__version__']

CONSOLE_SCRIPTS = ['octopus = ci.cli:main']
setup(
    name='octopus-ci',
    version=read_version('ci'),
    description='Bunch of commands to help continuous integration',
    author='Soroosh Sarabadani',
    author_email='soroosh.sarabadani@zalando.de',
    url='https://github.com/psycho-ir/octopus-ci',
    keywords=['ci tools, probe port'],
    packages=setuptools.find_packages(exclude=['tests', 'tests.*']),
    install_requires=['click'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    entry_points={'console_scripts': CONSOLE_SCRIPTS},
)