## MEMEMASTER V2

Site for watching memes scrapped from other sites.

No ads, no buttons, no additional links, no stupid headers taking
1/3 of screen, no logging, no comments, no 'disable adblock' requests - only pure fun.

To see site in full glory, please visit:

[MEMEMASTER_V2](https://lukaszszymankiewicz.github.io/mememasterv2/)

## Disclaimer

This code is for personal and educational use only (and made purely for fun!),
I do not recommend to use it in ANY other way!

Please remember that most of these memes are owned by scrapped sites, and propably 
some legal consequences will occur if these memes are used in any other way than above.

## How it works?

 - Github action is running Python scrapper and store is in `json` file,
 - Then, another Github action commits the resulted `json` file to the main branch of the repo,
 - Repo is set to serve as Github Pages,
 - JS script is interpreting the `json` file and fills the html page.
