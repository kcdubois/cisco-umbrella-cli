from setuptools import setup, find_packages

setup(
    name='umbrella-cli',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'click',
        'requests',
        'marshmallow'
    ],
    entry_points='''
        [console_scripts]
        umbrella-cli=umbrella_cli.cli:cli
    ''',
)