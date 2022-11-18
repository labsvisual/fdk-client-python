"""Library Metadata Information."""

from setuptools import find_packages
from setuptools import setup

description = ('Configurable wrapper around Fynd APIs which helps '
               'to call Fynd APIs using function and classes.')

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='fdk_client',
    version='0.1.28',
    author='Manish Magnani',
    author_email='manishmagnani@gofynd.com',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/gofynd/fdk-client-python',
    packages=find_packages(
        exclude=('tests*', 'documentation', '_macros')),
    license='',
    install_requires=[
        "aiohttp==3.8.3",
        "async-timeout==4.0.2",
        "attrs==21.2.0",
        "backcall==0.2.0",
        "chardet>=3.0.4",
        "decorator==5.1.0",
        "idna>=2.10",
        "ipython==7.31.1",
        "jedi==0.18.0",
        "marshmallow==3.12.2",
        "matplotlib-inline==0.1.3",
        "multidict>=4.7.6",
        "parso==0.8.2",
        "pexpect==4.8.0",
        "pickleshare==0.7.5",
        "prompt-toolkit==3.0.21",
        "ptyprocess==0.7.0",
        "Pygments==2.10.0",
        "pytz>=2021.3",
        "traitlets==5.1.1",
        "typing-extensions==3.10.0.2",
        "ujson==5.4.0",
        "wcwidth==0.2.5",
        "yarl==1.6.3"
    ],
    classifiers=[
        'Programming Language :: Python :: 3.8.2'
    ],
)
