title: Trigger Happy : Setup Instapush service
date: 2016-09-09 21:00
tags: django, instapush
category: Tutorial
slug: trigger-happy-instapush
summary: This article explain how to setup Instapush with Trigger Happy and then never miss a thing with a rain of notifications ;)
status: Published


To use Instapush on TriggerHappy :

3 steps 
=======

Part 1 Instapush
----------------

![Dashboard](https://blog.trigger-happy.eu/static/Instapush_dashboard.png)

* on [instapush.im](http://instapush.im) create an account 
* from TriggerHappy.eu, [edit your instapush service](https://trigger-happy.eu/th/service/) and in the "User token" field enter the "User token" you have from your dashboard on the tab "&lt;/&gt; Info"
* on [instapush.im](http://instapush.im) dashboard, select the tabs "APPS" , then "+ Add Application" and enter a title for this app	

![The Apps](https://blog.trigger-happy.eu/static/Instapush_dashboard_apps.png)

* then on the page of your app select "+Add events" and fill the field like below for example 

![New event](https://blog.trigger-happy.eu/static/Instapush_dashboard_app_new_event.png)

* now with this new event, click on tab "Basic Info" and get the App ID and App Secret infos

![Application details](https://blog.trigger-happy.eu/static/Instapush_dashboard_app_details.png)


Part 2 Trigger Happy
--------------------

once all of that is done, create a trigger :

* select Twitter as Provider
* fill the field like you want, for example in screen put @foxxmask
* select instapush as Consumer
* fill the field with the App ID and App Secret you got earlier, fill the "event name" and "tracker name" you saw in the example earlier in the example "mestweets" and "message"
* save it

Part 3 Instapush on your smartphone 
-----------------------------------

Get it from the store, then connect your account.


End
---

and now ... wait my tweet :)

![The tweets](https://blog.trigger-happy.eu/static/instapush_tweets.png)


And tada

![Notifications](https://blog.trigger-happy.eu/static/Instapush_notif.png)


no it's not Twitter notification but Instapush notification



Have Fun !
