rikeripsum
==========

Generates text - like lorem ipsum - but uses real English. Taken from random samplings of dialog spoken by Commander William Riker in Star Trek: The Next Generation.

This project was inspired by the many other "lorem ipsum" type generators out there that aim to use real English rather than jibberish. 

@jessicaspacekat (https://twitter.com/jessicaspacekat) came up with the brilliant idea of using Riker's dialog for generating text. She created a fancy javascript generator, but I wanted something I could use in my projects - for provisioning sample data to test with.

I found a site, http://antoa.com/tng/, which contains the scripts of every episode of Star Trek: The Next Generation. I scraped the site then parsed out all Riker's lines. After a little bit of cleaning up, I created a large object full of every line he's ever spoken in TNG. I saved that to a pickle for quick loading, and wrote rikeripsum.py to generate random sentences. 

#Future Improvements
* Ability to specify the number of words you'd like sentences to have. 
* General customizations.
* Ability to select which character you'd like to pull lines from (this is started). 

