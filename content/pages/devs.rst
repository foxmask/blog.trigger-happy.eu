Developpers
===========
:slug: developpers
:page_order: 3

How to get involved ?
---------------------

the source code of the project is available on a `GitHub repository`_, where you could fork it, make your improvments, create new services (with django module) like Twitter, FourSquare, Reddit etc... to expand the project

If you find some issues linked to the application, do not hesitate `open a ticket`_ and provide the maximum of details

Existing Modules
----------------
the following services could be helpful to start your own module

* `Evernote`_
* `GitHub`_
* `Pocket`_
* `RSS`_
* `Readability`_
* `Trello`_
* `Twitter`_

A skelton module intended to be cloned to make your own Trigger Happy module named `django-th-dummy`_, permits, with very few new lines of code `to produce his little module home made with Trigger Happy (link in french)`_

You can also use a projet I made that use `Ansible to bootstrap (dango-th-ansible)`_ your ready to use module that will be able to be plugged to the others services TriggerHappy can handle

Roadmap
-------
You can follow it from `here`_

Other majors features will be : 

Using `Autobahn`_ or anything else like that. This would speed up the handling process : in other words : being multiprocess/async with no blocking process.

Until version < 0.10.0 the process works great but is done in serial


.. _GitHub: https://github.com/
.. _`GitHub repository`: https://github.com/foxmask/django-th
.. _`open a ticket`: https://github.com/foxmask/django-th/issues/new
.. _`django-th-dummy`: https://github.com/foxmask/django-th-dummy
.. _Evernote: https://github.com/foxmask/django-th/tree/master/th_evernote
.. _Pocket: https://github.com/foxmask/django-th/tree/master/th_pocket
.. _RSS: https://github.com/foxmask/django-th/tree/master/th_rss
.. _Readability: https://github.com/foxmask/django-th/tree/master/th_readability
.. _Trello: https://github.com/foxmask/django-th/tree/master/th_trello
.. _Twitter: https://github.com/foxmask/django-th/tree/master/th_twitter
.. _`to produce his little module home made with Trigger Happy (link in french)`: http://www.foxmask.info/post/2013/12/09/trigger-happy-comment-pondre-son-propre-module
.. _here: https://github.com/foxmask/django-th/issues/milestones
.. _Autobahn: http://autobahn.ws
.. _`Ansible to bootstrap (dango-th-ansible)`: https://github.com/foxmask/django-th-ansible
