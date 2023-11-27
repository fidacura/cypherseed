# setup.py
from setuptools import setup, find_packages

setup(
    name='cypherseed',
    version='0.1',
    author="fidacura",
    author_email="hello@fidacura.xyz",
    description="",
    license="",
    url="https://github.com/fidacura/cypherseed",
    packages=find_packages(),
    install_requires=[
        # Add project dependencies here
    ],
    entry_points={
        'console_scripts': [
            'cypherseed=cypherseed.generator:main',
        ],
    },
)