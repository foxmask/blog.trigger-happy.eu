title: Informations
slug: informations
page_order: 2

## What is this ?

As it exists tools to make his blog or website or even his own cloud system, "Trigger Happy" is a [free software](http://en.wikipedia.org/wiki/Free_software) that provides a micro [Enterprise service bus (ESB)](http://en.wikipedia.org/wiki/Enterprise_service_bus)


## How does it work ?


Trigger Happy enters in a new category of tools which permits to manage the connection between internet services, as a bridge between them, and will act from events triggered:

* on the web
* on your own "internet" accounts

Examples :

* When a news is published on a website, I want it to be stored in my Evernote or Pocket account to be read later, or published it on Twitter, or on my Facebook wall, etc...
* when I add a note to my Evernote account, I want to send it to my Pocket account also
* When a tweet about a specific subject is published, send it to my Pocket/Evernote/Whatever account
* etc…

All of this is widely inspired by the very great IFTTT service which permits that exchanges.


![Trigger Happy architecture](https://trigger-happy.eu/static/th_esb.png)


## What services are availables ?


You can make communicate with each other, the internet services [Evernote](https://github.com/foxmask/django-th/tree/master/th_evernote), [GitHub](https://github.com/), [Pocket](https://github.com/foxmask/django-th/tree/master/th_pocket), [PushBullet](https://github.com/foxmask/django-th/tree/master/th_pushbullet), [RSS](https://github.com/foxmask/django-th/tree/master/th_rss), [Readability](https://github.com/foxmask/django-th/tree/master/th_readability), [Todoist](https://github.com/foxmask/django-th/tree/master/th_todoist), [Trello](https://github.com/foxmask/django-th/tree/master/th_trello), [Twitter](https://github.com/foxmask/django-th/tree/master/th_twitter), [Pelican](https://github.com/foxmask/django-th/tree/master/th_pelican) and take advantage of all RSS feeds. Except RSS, you will have to own an account on each of this internet services.


## What If I wish to install "Trigger Happy" on my own ?


If you have [Python](http://python.org)/[Django](https://www.djangoproject.com/) skills, I invite you to read [the documentation](http://trigger-happy.readthedocs.org/en/latest/index.html) which details all of this

## How is this service born ?


Following setbacks with a service called IFTTT which made unreadable notes (because it did not handle accented characters UTF-8), the decision was made to launch a free alternative.

