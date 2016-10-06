from setuptools import find_packages, setup
from channels_api import __version__

setup(
    name='channelsrestframework',
    version=__version__,
    url='https://github.com/madra/channels-rest-framework',
    author='Madra David',
    author_email='david@madradavid.com',
    download_url='https://github.com/madra/channels-rest-framework/tarball/0.1',
    description="Build a RESTful API on top of WebSockets using Django channels and Django Rest Framework.",
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=1.8',
        'channels>=0.14',
        'djangorestframework>=3.0'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
