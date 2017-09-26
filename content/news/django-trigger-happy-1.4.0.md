title: Trigger Happy 1.4.0
date: 2017-09-26 22:00
tags: django, release, tumblr
category: News
slug: django-trigger-happy-1.4.0
summary: Django Trigger Happy 1.4.0 released !
status: Published


New feature :
=============

* New service Tumblr supported
* Data Digest that permits to get your grabbed data each, day, week, month if you want.
for that, just set digest_event to True 

```
DJANGO_TH = {
    # paginating
    'paginate_by': 5,

    # this permits to avoid "flood" effect when publishing
    # to the target service - when limit is reached
    # the cache is kept until next time
    # set it to 0 to drop that limit
    'publishing_limit': 0,
    # number of process to spawn from multiprocessing.Pool
    'processes': 1,
    'services_wo_cache': ['th_instapush', ],
    # number of tries before disabling a trigger
    # when management commands run each 15min
    # with 4 'tries' this permit to try on 1 hour
    'failed_tries': 2,  # can exceed 99 - when
    # if you want to authorize the fire button for EACH trigger
    'fire': False,
    'digest_event': True,
}
```

Django and Python Update
========================

* Django 1.11.x
* Python 3.6.x

Improvements and bug fix
========================

* several little fixes here and there


Installation and Update :
=========================

Once you did 

```python
pip install -U django_th 
```

finish by

```python
python manage.py migrate
```
to update the database

Notice
======
As this release do a step from django 1.8.x to 1.11.x, I strongly suggest to have a look at the doc and use 


```python
python manage.py check --deploy
```

to see what's going on
