title: Developpers
slug: developpers
page_order: 3

## How to get involved ?

the source code of the project is available on a [GitHub repository](https://github.com/foxmask/django-th), where you could fork it, make your improvments, create new services (with django module) like Twitter, FourSquare, Reddit etc... to expand the project

If you find some issues linked to the application, do not hesitate [open a ticket](https://github.com/foxmask/django-th/issues/new) and provide the maximum of details

## Existing Modules

the following services could be helpful to start your own module

* [Evernote](https://github.com/foxmask/django-th/tree/master/th_evernote)
* [GitHub](https://github.com/)
* [Pocket](https://github.com/foxmask/django-th/tree/master/th_pocket)
* [RSS](https://github.com/foxmask/django-th/tree/master/th_rss)
* [Readability](https://github.com/foxmask/django-th/tree/master/th_readability)
* [Trello](https://github.com/foxmask/django-th/tree/master/th_trello)
* [Twitter](https://github.com/foxmask/django-th/tree/master/th_twitter)

A skelton module intended to be cloned to make your own Trigger Happy module named [django-th-dummy](https://github.com/foxmask/django-th-dummy), permits, with very few new lines of code [to produce his little module home made with Trigger Happy - link in french](http://foxmask.trigger-happy.eu/post/2013/12/09/trigger-happy-comment-pondre-son-propre-module)

You can also use a projet I made that use [Ansible to bootstrap (dango-th-ansible)](https://github.com/foxmask/django-th-ansible) your ready to use module that will be able to be plugged to the others services TriggerHappy can handle

## Roadmap

You can follow it from [here](https://github.com/foxmask/django-th/issues/milestones)

Other majors features will be : 

Using [Autobahn](http://autobahn.ws) or anything else like that. This would speed up the handling process : in other words : being multiprocess/async with no blocking process.

Until version < 0.10.0 the process works great but is done in serial
