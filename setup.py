from distutils.core import setup

setup(
    name='RikerIpsum',
    version='1.1',
    packages=['rikeripsum',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description='''Generates text - like lorem ipsum - but uses real English. Taken from random samplings of dialog spoken by Commander William Riker in Star Trek: The Next Generation.
    
    This project was inspired by the many other "lorem ipsum" type generators out there that aim to use real English rather than jibberish.
    
    @jessicaspacekat (https://twitter.com/jessicaspacekat) came up with the brilliant idea of using Riker's dialog for generating text. She created a fancy javascript generator, but I wanted something I could use in my projects - for provisioning sample data to test with. I also wanted to use all of Riker's dialog, rather than a limited subset.
    
    I found a site, http://antoa.com/tng/, which contains the scripts of every episode of Star Trek: The Next Generation. I scraped the site then parsed out all Riker's lines. After a little bit of cleaning up, I created a large object full of every line he's ever spoken in TNG. I saved that to a pickle for quick loading, and wrote rikeripsum.py to generate random sentences.
    ''',  
    data_files=[('data', ['rikeripsum/data/riker.pickle']),], 
    package_data = {
        '': ['*.pickle', 'data/riker.pickle' ],
    }, 
    include_package_data = True, 
)
