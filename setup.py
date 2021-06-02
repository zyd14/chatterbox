import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='ApiToolbox',
    version='0.0.1',
    author='zromer@fredhutch.org',
    description='Provides basic tools for quickly implementing RESTful APIs in Flask',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sciscogenetics/ApiToolbox',
    packages=setuptools.find_packages(),
    install_requires=["aiodns==2.0.0",
                        "aiohttp==3.6.0",
                        "aniso8601==8.0.0",
                        "async-timeout==3.0.1",
                        "atomicwrites==1.3.0",
                        "attrs==19.1.0",
                        "botocore==1.12.230",
                        "cffi==1.12.3",
                        "chardet==3.0.4",
                        "Click==7.0",
                        "docutils==0.15.2",
                        "Flask==1.0.2",
                        "Flask-RESTful==0.3.6",
                        "flask-restplus==0.13.0",
                        "future==0.16.0",
                        "idna==2.8",
                        "idna-ssl==1.1.0",
                        "importlib-metadata==0.23",
                        "itsdangerous==1.1.0",
                        "Jinja2==2.10.1",
                        "jmespath==0.9.4",
                        "jsonpickle==1.2",
                        "MarkupSafe==1.1.1",
                        "marshmallow==2.19.2",
                        "more-itertools==7.2.0",
                        "multidict==4.5.2",
                        "pluggy==0.13.0",
                        "py==1.8.0",
                        "pycares==3.0.0",
                        "pycparser==2.19",
                        "pytest==3.8.2",
                        "python-dateutil==2.8.0",
                        "python-slugify==1.2.4",
                        "pytz==2019.2",
                        "six==1.12.0",
                        "slackclient==2.0.0",
                        "typing==3.7.4.1",
                        "typing-extensions==3.7.4",
                        "Unidecode==1.1.1",
                        "urllib3==1.26.5",
                        "Werkzeug==0.15.6",
                        "wrapt==1.11.2",
                        "yarl==1.3.0",
                        "zipp==0.6.0"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)