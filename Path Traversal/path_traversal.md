# Path Traversal
A common vulnerability, though less nowadays is Path Traversal. This happens when permissions aren't properly set server-side on where the user is allowed to go. A common way to test this is by doing the following:
```
website.com/../../../../../../../../../../../etc/passwd
```

While this did not give any results on our website, we can notice that the page to show is decided by a php script with a query to a page name. Let's try editing the page name to be like above:
```
http://127.0.0.1:4443/?page=../../../../../../../../../../../etc/passwd
```
