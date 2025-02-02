# Password Bruteforcing

A classic vulnerability is weak passwords or common passwords. Attacker can try to bruteforce users' passwords using a variety of techniques, such as small bash scripts up to more advanced tools like Burpsuite.

I decided to try this approach on the signin page, hoping to get lucky. I knew that if succesful, the page would most probably contain the word "flag" in it, resulting in me doing a `grep 'flag'` in my little script.

I also utilised a commonly used file named "rockyou.txt" which contains a list of the most common passwords.

Please see the script for more details. The password has been moved up in the list so as to make the demonstration quicker. it was initially position 73.

## Flag

```
b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2
```