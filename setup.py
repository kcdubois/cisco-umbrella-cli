from setuptools import setup, find_packages

setup(
    name='cisco-umbrella-cli',
    description="Command-line interface for Cisco Umbrella API",
    author="Kevin C-Dubois",
    version='0.1.5',
    packages=find_packages(),
    install_requires=[
        'click',
        'requests',
        'marshmallow',
        'colorama'
    ],
    entry_points='''
        [console_scripts]
        umbrella-cli=umbrella_cli.cli:main
    ''',
)