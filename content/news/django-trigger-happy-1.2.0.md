title: Django Trigger Happy 1.2.0
date: 2016-12-22 16:00
tags: django, release
category: News
slug: django-trigger-happy-1.2.0
summary: Django Trigger Happy 1.2.0 released !
status: Published


This will be a short, very short message, but with a lot of fun [I had (have a look at the 'bameda' in the bottom of the article)](https://foxmask.trigger-happy.eu/post/2016/11/26/trigger-happy-two-weeks-after-strong-storm/).

New feature :
=============

* [#155](https://github.com/foxmask/django-th/issues/155) [Taiga](https://taiga.io/) and [Slack](https://slack.com/) services are now supported, through their respectives WebHooks... and [Mattermost](https://about.mattermost.com/) too, as this project uses the same API of Slack. 
* [#162](https://github.com/foxmask/django-th/issues/162) You can now use the project with Docker. If you are familiar with docker, you can just follow [the README_docker file](https://github.com/foxmask/django-th/blob/master/README_docker.md) I made.

Improvements :
==============

Update of all the (old) requirements, except django still in 1.8.x

Contributions :
---------------

* typo fixing [#156](https://github.com/foxmask/django-th/pull/156) by Kenny John Jacob

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

