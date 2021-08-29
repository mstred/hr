from setuptools import setup, find_packages

with open('README.md', encoding='UTF-8') as readme_file:
    readme = readme_file.read()

setup(
    name='hr',
    version='0.1.0',
    description='Command line user export utility',
    long_description=readme,
    author='Edson Samuel Jr',
    email='samuedson@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[],
    entry_points={
        'console_scripts': 'hr=hr.cli:main'
    }
)
