title: Trigger Happy 1.5.0 "Hacktoberfest"
date: 2017-10-27 16:00
tags: django, release, mastodon, reddit, hacktoberfest
category: News
slug: django-trigger-happy-1.5.0-hacktoberfest
summary: Trigger Happy 1.5.0 aka "Hacktoberfest" has been released !
status: published

Introduction:
=============

This month, a wonderful event was launched, named [Hacktoberfest](http://hacktoberfest.digitalocean.com/).

This Hacktoberfest allowed us to win T-Shirt once we did 4 accepted PR. The primary goal was not to win anything (really?:) but, contributing to an open source project, by picked up issues from github, tagged "hacktoberfest".

This event was a great moment with a lot of exchanges with a lot of contributors, more than ever before in the story of the project.  

As I already [explained](https://blog.trigger-happy.eu/hacktoberfest-2017.html), I did not expect anything from anyone, and opened a little bucket of issues, and surprisingly, contributions came as if it rained cat and dogs :)


I deeply address a warm thanks for all of them.

* [Koalie](https://github.com/koalie)
* [CrazyLlama](https://github.com/CrazyLlama)
* [Logan1x](https://github.com/Logan1x)
* [h-chauhan](https://github.com/h-chauhan)
* [RishabhJain2018](https://github.com/RishabhJain2018)
* [denvaar](https://github.com/denvaar)
* [alonisser](https://github.com/alonisser)
* [Pal0r](https://github.com/Pal0r)
* [scomert](https://github.com/scomert)
* [pohzipohzi](https://github.com/pohzipohzi)


2 specials thanks to:

* h-chauhan who integrated the new Reddit module and fix several issues
* Koalie for all the doc reviewing  

Now the 'menu' :)

New feature :
=============

* New service [Reddit](https://reddit.com) supported

Thus you can get data from a subreddit of your choice and push them wherever you want
You can also create a post in the subreddit you want, with the data coming from anywhere.

* New service [Mastodon](https://joinmastodon.org/) supported

Thus you can get data from a Mastodon instance, and push them on Twitter for example, or even in the over side, from Twitter to Mastodon
and with the images if the "toot"/"tweet" embeded one(s)


[![Mastodon](https://blog.trigger-happy.eu/static/mastodon.png)](https://joinmastodon.org/)



As usual, when you want to use such a service, you need to register an application.
In return, the service will then provides you the consumer key+secret you will put in the `.env` file (see below)

Improvements:
=============

UI:
---

* A rework of the page of the service management has been done and instead of having a form "all in one" for every service, that causes confusion, each service now has a form with just its required fields

Settings:
---------

* You can now setup trigger-happy without editing `th_settings.py` at all

Just create a `.env` (by copying `env.sample`) and set the value of the services you use.
In the documentation, for each [supported service](http://trigger-happy.readthedocs.io/en/latest/services.html), you can follow the steps to register an application, by reading "Registering a key" 

Installation and administation
------------------------------

* Installation now add fixtures to enable all the provided services
* The project now collects stats about the health of the triggers to avoid to impact the core by failing over and over again with weak triggers
* Administration : fix the edition of the services, fix the filters list on the service and triggers page.

Documentation:
-------------

I hope you will enjoy the doc as I spent a lot of time to detail how each of them can be activated, disabled, how to request key, how to use them as provider and consumer and so on. So now the doc is splitted in 4 guides:

* installation guide
* an administration guide
* user guide
* docker guide

Others:
-------
* Several little fixes here and there


Installation and Update :
=========================

for an new installation
-----------------------

```python
pip install django_th 
python manage.py loaddata initial_services
python manage.py migrate
```

for an update do 
----------------

```python
pip install -U django_th
python manage.py migrate
```

As there are 2 new services, you will need to enable the 2 new services [from the admin panel](http://127.0.0.1:8000/admin/django_th/servicesactivated/)


![Services](https://raw.githubusercontent.com/foxmask/django-th/master/docs/installation_guide/admin_service_list.png)
Console access: ![Services](http://127.0.0.1:8000/admin/django_th/servicesactivated/)


![Adding a Service](https://raw.githubusercontent.com/foxmask/django-th/master/docs/installation_guide/admin_service_details.png)
Console access: ![Adding a service](http://127.0.0.1:8000/admin/django_th/servicesactivated/add/)


