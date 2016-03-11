title: Django Trigger Happy 0.12.0 Regression
date: 2016-03-09 11:55
tags: python, django, release
category: News
slug: django-trigger-happy-0.12.0-regression
summary: Django Trigger Happy 0.12.0 regression because of Twitter service
status: Published


With the last release, I introduced a regression that I didnt notice when pushing to github.

This regression is about the model of the Twitter service.

If you ran the migrate command to add the new pelican service, in the meantime, ran a script that has nothing to do here :

```bash
localhost $ ./manage.py migrate
Operations to perform:
  Synchronize unmigrated apps: django_rq, staticfiles, messages, evernote, th_rss, django_js_reverse, gunicorn
  Apply all migrations: th_evernote, th_pelican, sessions, contenttypes, th_twitter, auth, th_readability, th_holidays, django_th, sites, admin, th_pocket, th_trello
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
  Installing custom SQL...
Running migrations:
  Rendering model states... DONE
  Applying th_pelican.0001_initial... OK
  Applying th_twitter.0003_auto_20160210_0953... OK
```

the last line should never happened

So to fix this, if you have a backup, restore it, it's better, otherwise: 
    
1) connect to your database and do :

```sql
select * from django_migrations where app = 'th_twitter'
 id |      app       |                 name                  |            applied            
----+----------------+---------------------------------------+-------------------------------
 23 | th_twitter     | 0001_initial                          | 2015-06-13 13:42:36.977958+02
 27 | th_twitter     | 0002_int_to_bigint                    | 2015-08-23 10:37:50.534353+02
 32 | th_twitter     | 0003_auto_20160210_0953               | 2016-03-09 11:30:31.083277+01
```

2) get the ID and delete all of them

3) delete the bad migration  `0003_auto_20160210_0953.py` from your installation (something like) lib/python3.4/site-packages/th_twitter/migrations/ 

4) then run the migration again to fix the migration history :

```bash
localhost$ ./manage.py migrate
Operations to perform:
  Synchronize unmigrated apps: staticfiles, gunicorn, messages, django_js_reverse, django_rq, th_rss, evernote
  Apply all migrations: sessions, th_trello, th_pocket, sites, auth, django_th, th_evernote, th_pelican, th_holidays, th_readability, admin, th_twitter, contenttypes
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
  Installing custom SQL...
Running migrations:
  Rendering model states... DONE
  Applying th_twitter.0001_initial... OK
  Applying th_twitter.0002_int_to_bigint... OK
```

5) If you have existing triggers related to twitter, and recreate them from the webpage.


I will release a 0.12.1 as soon as possible B.O.D


Apologies for the inconvenience
