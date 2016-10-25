title: Django Trigger Happy 1.1.0
date: 2016-10-25 16:00
tags: django, release
category: News
slug: django-trigger-happy-1.1.0
summary: Django Trigger Happy 1.1.0 is released ! Happy download !
status: Published


I enjoyed myself with 2 months of code atfer this summer. The result is that I played with Mock/Test that led to all the following details :


New feature :
=============

[#77](https://github.com/foxmask/django-th/issues/77) launch one trigger from its list of triggers 


Improvements :
==============


Core :
------

* forget to add templates to Manifest for v 1.0.0
* Many improvement with Unitests & Mock
* drop unused modules : th_holidays th_search 
* [#149](https://github.com/foxmask/django-th/issues/149) Triggers status of last execution
* [#145](https://github.com/foxmask/django-th/issues/145) Stop triggers that use a disabled service
* [#143](https://github.com/foxmask/django-th/issues/143) avoid error 500 when submitted twice the creation of a service

Modules :
---------

* **Evernote** : RateLimit is reached... does not return a evenote.api.client.Store 
* **Readability** : [#147](https://github.com/foxmask/django-th/issues/147) Drop support
* **Todoist** : regression with command line to 'recycle' data + an invalid import of TodoIst API
* **Twitter** : get tweets from a given search string - the tag field works also perfecly for searching purpose
* **Twitter** : set a longer size to store enorrrrmouuuusss token 
* **Twitter** : [#146](https://github.com/foxmask/django-th/issues/146) do a tweet with one tag


Contributions :
---------------

* typo fixing [#142](https://github.com/foxmask/django-th/pull/142) by Cyril Hou



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


Get involved :
==============

Feel free to use the project for your own needs on your own hosting provider or test it on https://trigger-happy.eu

If you want to see a new service to be included to the project: 2 solutions 

* 1 you have python skill and you then can use : https://github.com/foxmask/django-th-ansible to create a new module or fork the project from https://github.com/foxmask/django-th
* 2 you dont have python skill, the you can put suggestions about the project in comments .
* 3 you have python skill and dont have time to participate, so go to point 2 ;) (ok it's a third solution:)

