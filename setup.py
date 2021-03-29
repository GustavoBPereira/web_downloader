from setuptools import find_packages
from setuptools import setup


setup(
    name='site_downloader',
    version='0.1',
    description='Crawler for sites and download it',
    long_description='Crawler for sites and download it',
    license='MIT',
    author='Gustavo Brito',
    author_email='britopereiragustavo@gmail.com',
    url='https://github.com/GustavoBPereira/web_downloader/',
    download_url='https://github.com/GustavoBPereira/web_downloader/',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['Scrapy==2.4.1', 'beautifulsoup4==4.9.3'],
    classifiers=[
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Framework :: Scrapy',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Systems Administration :: Authentication/Directory',
    ],
    keywords=['scrapy'],
)