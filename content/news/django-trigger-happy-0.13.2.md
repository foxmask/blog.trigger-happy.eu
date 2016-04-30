title: Django Trigger Happy 0.13.2
date: 2016-04-30 21:15
tags: django, wallabag, release
category: News
slug: django-trigger-happy-0.13.2
summary: Django Trigger Happy 0.13.2 is released ! Happy download !
status: Published


So, Here comes a small update of this open source clone of IFTTT, allowing to orchestrate data retrieval and publishing, while exploiting our own Internet services (like Twitter to name one). Just to stay the master and control our data without having to give our access permissions to anyone (services provider)

In celebration program :


* **New service Integration** 

  * [**Wallabag**](https://www.wallabag.org). "a 'read it later' opensource project". Yes you read well : WALLABAG ! 

    Thus now, we are able to store any web page to our own wallabag account, or better to our own wallabag instance (when we can host wallabag on one of our own server ). That way we can stop using Pocket, as wallabag can replace with all the pros you can imagine ;)

    This adds a toy to the list of keys ring : Twitter, Evernote, RSS, Readability, Pocket, Trello, Pelican. 

    Technically, I made the [python API for wallabag](https://github.com/foxmask/wallabag_api), and so I could make the service integration smoothly ;)

* **Notice**
  
  Since I dropped Celery and Python RQ, I face some very anoying performances issues related to ... Evernote... Something like, 1 time on 5, Python went in timeout... To compare the behavior, and try to isolate the source of the problem, I created the same triggers, but instead of creating note to Evernote, creating posts to Pocket. And here, everything go fast, no bottle neck at all, no timeout, all is perfect.


* **Installation**

 * I invite you to come and read the small [QuickStart guide](http://trigger-happy.readthedocs.org/en/latest/quickstart.html), which could be summarize by this commands :

```python
    pyvenv myhomy
    cd myhomy
    pip install django_th
    cd django_th
    python manage.py migrate
```

 * in case you already have installed the project, just do 

```python
    pip install wallabag_api
    pip install -U django_th
    python manage.py migrate
```


Happy Download, Happy installation :)
