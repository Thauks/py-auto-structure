from setuptools import setup, find_packages

with open('README.md', 'r') as readme_file:
    long_description = readme_file.read()

setup(
    name='py-auto-structure',
    version='0.1.3',
    author='Thauks',
    description='A tool to create a directory structure based on a YAML file',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/thauks/py-auto-structure',
    packages=find_packages(),
    install_requires=[
        'pyyaml',
        'wheel',
        'setuptools',
        'twine',
    ],
    entry_points={
        'console_scripts': [
            'py-auto-structure=project_builder.project_builder:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    license='MIT',
    python_requires='>=3.6',
    keywords=['directory', 'structure', 'YAML', 'tool'],
    package_data={'': ['*.yaml'],}
)
