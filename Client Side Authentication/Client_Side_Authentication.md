# User Authentication

We can notice that the website stores a cookie called `i_am_admin`

Checking it's value: `68934a3e9455fa72420237eb05902327` , we can see it is the MD5 hash of the word "false"

Modifiying it to `b326b5062b2f0e69046810717534cb09`, the MD5 hash of "true" gives us a popup with a flag when reloading a page.
