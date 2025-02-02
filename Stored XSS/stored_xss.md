# Stored XSS

On the feedback page, we can see that we can permanently modify the webpage by signing the guestbook.

This is a classic situation inwhich a vulnerability such as "stored xss" can occur. This is especially dangerous as the payload is sotred on theserver and is accessible to all users.

A key way toavoid this is by properly sanitizing the input, for instance by removing certain html tags like `<script>`.

## The Vuln
After some trial and error (and a lot of max size modification of the name field), i figure out that the `<img>` tag is not escaped / removed server side.

I then attempt a classic XSS payload in the name field as follows:
```
<img src=x onerror=alert("XSS")>
```
This indeed gives us a popup saying XSS once submitted (and on every page refresh). XSS ACHIEVED :D

But still no flag D: Well it turns out the site is very wierdly coded.

All you needed to do to get the flag was write "script" into the name or message field. WTF.
