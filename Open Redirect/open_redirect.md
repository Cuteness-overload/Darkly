# Open Redirect

The footer of the website contains links that redirect you to facebook, twitter and instagram. However these redirects aren't properly done as we can make it seem as though this is an official link, while changing the site to one of our own, leading to potential phishing scams.
```
http://127.0.0.1:4443/index.php?page=redirect&site=facebook
vs
http://127.0.0.1:4443/index.php?page=redirect&site=malicious
```
