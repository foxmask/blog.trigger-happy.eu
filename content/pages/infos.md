title: Informations
slug: informations
page_order: 2

## What is this ?

"Trigger Happy" is a 🚂 bridge between internet services


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


![Trigger Happy architecture](https://raw.githubusercontent.com/foxmask/django-th/master/docs/th_esb.png)


## What services are available ?


* [Evernote](https://github.com/foxmask/django-th/tree/master/th_evernote),
* [Instapush](https://github.com/foxmask/django-th/tree/master/th_instapush),
* [GitHub](https://github.com/ifoxmask/django-th/tree/master/th_github), 
* [Mastodoon](https://github.com/foxmask/django-th/tree/master/th_mastodon),
* Mattermost,
* [Pelican](https://github.com/foxmask/django-th/tree/master/th_pelican),
* [Pocket](https://github.com/foxmask/django-th/tree/master/th_pocket),
* [PushBullet](https://github.com/foxmask/django-th/tree/master/th_pushbullet),
* [Reddit](https://github.com/foxmask/django-th/tree/master/th_reddit),
* [RSS](https://github.com/foxmask/django-th/tree/master/th_rss),
* [Slack](https://github.com/foxmask/django-th/tree/master/th_slack), 
* [Taiga](https://github.com/foxmask/django-th/tree/master/th_taiga), 
* [Todoist](https://github.com/foxmask/django-th/tree/master/th_todoist),
* [Trello](https://github.com/foxmask/django-th/tree/master/th_trello),
* [Tumblr](https://github.com/foxmask/django-th/tree/master/th_tumblr)
* [Twitter](https://github.com/foxmask/django-th/tree/master/th_twitter),
* [Wallabag](https://github.com/foxmask/django-th/tree/master/th_wallabag),


## Installing his/her own Trigger Happy instance


I invite you to read [the documentation](http://trigger-happy.readthedocs.org/en/latest/index.html) which details all you need. And if by some misfortune, you don't really know how to install it, come on [gitter](https://gitter.im/foxmask/django-th) to reach me (foxmask) and we could talk about that. I could already help someone to install the project, without any knowledge with python/django


## Using Trigger Happy without installing it

Just [login in](https://trigger-happy.eu/) to the Trigger Happy website.
It may happens that some features won't be available. This, to avoid the server to stop working correctly.

## How is this service born ?


Following setbacks with a service called IFTTT which made unreadable notes (because it did not handle accented characters UTF-8), the decision was made to launch a free alternative.


## a Technical Presentation 

[Trigger Happy](https://blog.trigger-happy.eu/pages/TriggerHappy.pdf)
