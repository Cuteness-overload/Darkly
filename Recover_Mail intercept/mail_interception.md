# Mail Interception

When navigating the website, we come across another page, this time to recover your password in case you forgot it. 
When inspecting the source code, it seems that an email is sent to
```
webmaster@borntosec.com
```
when we submit the request. By modifying the value of that form , we should be able to intercept the email and potentially do nefarious things. 
THIS SHOULD BE SERVER SIDE LOGIC.
