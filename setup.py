from setuptools import setup, find_packages

with open('README.md', 'r') as readme_file:
    long_description = readme_file.read()

setup(
    name='py-auto-structure',
    version='0.1.0',
    author='Thauks',
    description='A tool to create a directory structure based on a YAML file',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/thauks/py-auto-structure',
    packages=find_packages(),
    install_requires=[
        'pyyaml',
    ],
    entry_points={
        'console_scripts': [
            'py-structure=project_builder:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
