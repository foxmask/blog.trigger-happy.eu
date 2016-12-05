title: Trigger Happy To Wallabag
date: 2016-12-05 22:00
tags: wallabag 
category: News, Tutorial
slug: trigger-happy-to-wallabag
status: Published


As you may already know, TriggerHappy is able to propagate data from any source of data to any service that consumes that data.

Since several weeks now, I see a lot of tweets of people asking to the team of wallabag how to feed its wallabag instance,
and the team replying "we don't do that but external services exist to do the job like TriggerHappy".


Example (in French)

<blockquote class="twitter-tweet" data-lang="fr"><p lang="fr" dir="ltr"><a href="https://twitter.com/sylv_in">@sylv_in</a> Bonjour. Aujourd&#39;hui ça n&#39;est pas possible avec IFTTT pour nous. Mais vous pouvez utiliser <a href="https://t.co/x4VpdmBBkG">https://t.co/x4VpdmBBkG</a> de <a href="https://twitter.com/foxxmask">@foxxmask</a>.</p>&mdash; wallabag (@wallabagapp) <a href="https://twitter.com/wallabagapp/status/804286336471597056">1 décembre 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>


On my side, I thought of a solution since a lot of time, making a dedicated version of TriggerHappy for Wallabag
Something very very very light.

So this week-end during the night of saturday, I made [TriggerHappy To Wallabag](https://github.com/foxmask/th2w) (th2w).
I used the same them of Wallabag, thus you will not be lost with the UI (at least I hope:)

This project just does 2 things : 

* Grabbing data from RSS/Atom Feeds
* Pushing the data to a Wallabag instance.


Introduction
============

As it's a python project, I'm sorry for PHP fan but if you don't enjoy that language, continue the path somewhere else :)
So, I will detail the way to install from scratch :
 
* creating a virtualenv
* cloning the source code
* settings the database
* starting the project
* Recursives jobs
* Creating a new trigger
* Running read and publish commands

Creating a virtualenv 
=====================

We will say we start from scratch from `/home/foxmask/`

```bash
virtualenv --pytyhon=/usr/bin/python35 my_th2w
cd $_
source bin/activate
```

Cloning the source code
=======================

get the sources from the github repository :

```bash
git clone https://github.com/foxmask/th2w.git
```

then install the dependencies :

```bash
pip install -r requirements.txt
```

Settings the database
=====================

```python
python manage.py migrate           # this will create a Sqlite3 database
python manage.py createsuperuser   # and reply to the questions
```

for example

```python
Username (leave blank to use 'foxmask'): 
Email address: toto@tata.com
Password: 
Password (again): 
Superuser created successfully.
```


Settings your Wallabag instance
===============================

in the `th2w/settings.py` file, set the parameters that fit your needs :
 
```python

WALLABAG_SECRET = {
    'username': '',
    'password': '',
    'client_id': '',
    'client_secret': '',
    'host': '',  # url without the final / eg http://foo.com not http://foo.com/
}
```
Check that the variable `DEBUG` is set to `False` at the beginning of this file.


Starting the project
====================

```python
python manage.py runserver
```

Now you can open your browser and go to http://127.0.0.1:8000/ to start using the application


Recursives jobs
===============

the 2 commands to execute, manually:

```python
python manage.py read
python manage.py publish
```

or from the crontab:

```bash
10,25,41,55 * * * * . /home/foxmask/my_th2w/bin/activate && cd /home/foxmask/my_th2w/th2w/ && ./manage.py read 
*/15 * * * * . /home/foxmask/my_th2w/bin/activate && cd /home/foxmask/my_th2w/th2w/ && ./manage.py publish
```


Creating a new trigger
======================


Connection
----------

![login](https://blog.trigger-happy.eu/static/th2w_login.png)


Create the trigger
------------------

Empty list

![empty list of triggers](https://blog.trigger-happy.eu/static/th2w_list.png)

Creation

![Creation of a trigger](https://blog.trigger-happy.eu/static/th2w_create_trigger.png)

List of triggers

![list of triggers](https://blog.trigger-happy.eu/static/th2w_list2.png)

Running read and publish commands
=================================


```bash
foxmask@localhost$ ./manage.py read
INFO foxmask - FoxMaSk Blog - 2 new data
foxmask@localhost$ ./manage.py publish
INFO foxmask - FoxMaSk Blog - 2 new data

```

Content before
![list of triggers](https://blog.trigger-happy.eu/static/wallabag_instance_before.png)

Content after
![list of triggers](https://blog.trigger-happy.eu/static/wallabag_instance_after.png)


The final word
==============

Now, if the complete project TriggerHappy was too much for your needs, just have fun with this one ;)
 
