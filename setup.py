# setup.py
from setuptools import setup, find_packages

setup(
    name='cypherseed',
    version='0.1',
    description="Simple high-entropy passphrase generation tool.",
    url="https://github.com/fidacura/cypherseed",
    author="fidacura",
    author_email="hello@fidacura.xyz",
    license='MIT',
    packages=find_packages(),
    install_requires=[
        # cypherseed-deps
    ],
    entry_points={
        'console_scripts': [
            'cypherseed=cypherseed:main',
        ],
    },
)