from setuptools import setup, find_packages

setup(
    name='app',
    version='1.0.0',
    description='Hivery Paranura RESTful API Challenge solution based on Flask-RESTPlus',
    url='https://github.com/gethujp/hivery-api-final',
    author='Jayaprakash',
    keywords='rest restful api flask swagger openapi flask-restplus',
    packages=find_packages(),
    install_requires=['flask-restplus==0.9.2'],
)
