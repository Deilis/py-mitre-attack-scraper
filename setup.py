from setuptools import setup, find_packages

#Setup 
setup(
    name='mitre-attack-scrapper',
    version='0.0.1',
    description='A tool for scrapping MITRE ATT&CK framework data',
    author='Deividas Lis',
    author_email='lis.deividas@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        #Dependencies to add here! <-- DONT FORGET THAT'S NOTE FOR MYSELF
        'requests',
        'beutifulsoup4',
    ]
)