# Scraping 
It can happen that poorly configured servers have dirlisting enabled, allowing us easy vision on the files and directories available. When perusing the robots.txt, we see that a .hidden page exists.

Navigating to it shows us one such dirlisting. As there seems to be <b>A LOT</b> of possibilities, let's write a quick scraper to get what we want, ie. the file containing the flag.
--> See scraper.py

And boom, flag obtained after some cleaning up and bug fixing *(lmao the infinite loop due to also scraping ./)*