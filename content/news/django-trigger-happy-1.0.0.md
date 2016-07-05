title: Django Trigger Happy 1.0.0
date: 2016-07-03 18:15
tags: django, release, pushbullet, todoist, instapush
category: News
slug: django-trigger-happy-1.0.0
summary: Django Trigger Happy 1.0.0 is released ! Happy download !
status: Published

Since three years of incubating, time came to release the version 1

Whats new ?
===========
Here are the new services supported that are now part of the keyring :

* Pushbullet
* Instapush
* Todoist

The keyring now contains :

* Twitter
* Evernote
* Wallabag
* Pocket
* Readability
* Pushbullet
* Instapush
* Todoist
* Pelican
* Github
* RSS
* Trello


Improvements under the hood :
=============================

* Until today, all the services werent fully usable as they all consumed data but not provided them. For exemple you could create à note in Evernote to create an issue on github but could not get issue from github and create à note in Evernote. Now all the combinaison with those 11, 5 services is possible. The missing 0.5 is for Trello who is not able to provide filtered data yet but can receive everything.
* to be DRY : reducing a lot of code of each service and moving the auth to the main mother class.

Cosmestics :
============

the render of the list of triggers changed by dropping the blue of buttons to edit the services, which, with the time, tired  your eyes.

I also added the icons of each known service by the set of picture from [http://fontawesome.io](http://fontawesome.io) , in that buttons.


Tests of services :
===================

In the meantime i tried a lot of services, but :
* some do not have api -> Google Keep
* make you pay to use their service -> pushOver, diigo. As a fresoftware developper, ethically, i could not resign myself to support services that you have to pay to use them. A special case  : todoist, but here, the service provides enough "Free" parts that we can use which justifies its support.
* some are too slow with the browser and do not support postgresql -> paperwork

As a fishman, i fished a lot but didnt find a lot of nice fish. But that permits to learn new ways to fish and improve my fishing rod.

What next ?
===========

Version 1 :
-----------

Fixes and new services could be added, like yours and mine :)

Version 2 :
-----------

This version could change the face of the project, with, for instance, Angularjs as front with DRF on top of Trigger-happy to deliver the API access, plus many async* stuff in background. Right now nothing is written in the marble and is still widly open for suggestions you could make.

So stay tune, and have fun !

Last thing :
============

Now, you can 'come in' the service ! How ? On [Trigger Happy](https://trigger-happy.eu), click on "come in" in the top of the page and enjoy.

