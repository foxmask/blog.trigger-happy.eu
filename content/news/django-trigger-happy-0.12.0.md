title: Django Trigger Happy 0.12.0
date: 2016-03-03 21:30
tags: python, django, release
category: News
slug: django-trigger-happy-0.12.0
summary: Django Trigger Happy 0.12.0 is released ! Happy download !
status: Published


So, Here comes a small update of my little project, micro ESB (the open source clone of IFTTT), allowing to orchestrate data retrieval and publishing, while exploiting your own Internet services (like Twitter to name one). Just to stay the master and crontrol your data without having to give your access permissions to anyone (services provider)

In celebration program :


* **New service Integration** 

  * **Pelican**. "is a static website generator". This adds a toy to the list of keys ring : Twitter, Evernote, RSS, Readability, Pocket, Trello. Thus now, we are able to generate post in the pelican content folder from whatever service that will make you happy ;) The idea behind this is to do something like [paper.li](http://paper.li), which generates your daily journal for you without moving a finger.



* **Technical improvements**

  * Still Django 1.8.x (naturally) because I don't have time to play with (each release of) 1.9.x and having to modify the settings (that drop parms), nor change my module that use the class like Logger for example. So for the moment I play the stability.


* **Performances**

  * As I'm never satisfied of what I produce (like I said in August 2015), I decide to, defenetly, drop Celery from the project, and replace it by [Python-RQ](http://python-rq.org). Why ? because, without any apparent reason, Celery, suddendly, stops to work without complaining of anything. No error log nothing nowhere. The system is widely sized so it's not a matter of system resources... And most of all, RQ and Redis work fine altogether.


* **Simplicity**

  * with the RQ integration, you can see that this paste on how I feel with code of the project, I like things are as simple as possible. That way I found that the doc was to long to launch the application from scratch, that's why I made a [QuickStart guide](http://trigger-happy.readthedocs.org/en/latest/quickstart.html), and dropping Celery, finally, permits to keep things to install, short and clear.


And tommorow ? [some new service and ideas](https://github.com/foxmask/django-th/wiki) are planned.


* **Not so many things**

  * as you can read, there are not many things, new things ... But I experienced a lot, and a lot of different things, and a lot of differents way. It took me a while to be ready for this new version.


* **Installation**

 * if you plan to use the project inside another application, then :

```python
    pip install django_th
```

  * if not, you can directly clone the repository of the project inside a virtualenv and then follow the [QuickStart guide](http://trigger-happy.readthedocs.org/en/latest/quickstart.html).


**Thanks !**

Thank [to the new 100 stargazers](https://github.com/foxmask/django-th/stargazers) the project gained since I made a post on HackerNews.
I hope the big companies that are interested in the project, will find it fun, as fun as I have the pleasure to code it, squirm it, experiment it and build it.

Happy Download, Happy installation :)

