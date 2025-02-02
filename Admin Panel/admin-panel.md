# Admin Panel
Browsing the site and testing various basic urls, we eventually come across "/admin". This gives us access to the admin panel, but we need a user and a password. The classic passwords “admin:admin, admin:password, administrator:administrator, root:toor” are useless.

A little later, digging into robots.txt (a page used by websites to tell crawlers what they can show in search engines and use for SEO), we see that "/whatever" exists. Navigating to it gives us access to a file named `htpasswd`.

## The Vuln
htpasswd is a file used for stocking credentials allowing access to certain webpages (such as admin panels). We remember the admin panel we found earlier. Maybe the credentials in htpasswd could work there?

Thankfully the MD5 hash of the password is easily cracked by imply searching the hash online as it was a very common password. Now armed with the credentials `root:qwerty123@`, let's access the admin panel!

## Flag
Woohoo, Congratulations, here's the flag!
```
d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff
```