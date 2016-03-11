title: Django Trigger Happy 0.12.1
date: 2016-03-09 21:15
tags: python, django, release
category: News
slug: django-trigger-happy-0.12.1
summary: Django Trigger Happy 0.12.1 is released ! Happy download !
status: Published


Like explained [sooner this day](django-trigger-happy-0.12.0-regression.html), a regression has been located with the Twitter service. So this release just concerns this little fix.


So, this will do the job :

```python

pip install -U django-th

```
then do

```python 

python manage.py migrate

```

to finish the update process.
