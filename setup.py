from setuptools import setup, find_packages

# Setup
setup(
    name='mitre-attack-scraper',  
    version='0.0.1',
    description='A tool for scraping MITRE ATT&CK framework data',
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown',  
    author='Deividas Lis',
    author_email='lis.deividas@gmail.com',
    url='https://github.com/Deilis/mitre-attack-scraper',  
    license='MIT',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
        'beautifulsoup4', 
    ],
    classifiers=[
        'Development Status :: 3 - Alpha', 
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
    ],
    python_requires='>=3.12.4',  
)
