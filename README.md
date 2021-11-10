# amass_backend

This project was built due to influence of a community I was leading at the moment. I wanted to create a platform where you can get information about particular
events that we held, rsvp for the event, pay for the event and get a confirmation of the ticket and add it to your calendar.

The project was built using Django and Django Rest Framework.

The project is divided into different applications:

The Accounts Appication, uses tokenization to authenticate users who would like to login/sign up for the event.
I also incorporated serializers that convert complex data such as querysets to python native datatypes that can be rendered in JSON OR XML.
I used the class methid decorator that receives self as the implicit first argument and you can use its properties inside the method,
also it has access to every attribute.

When using DRF we can combine logic for a set of related views in a single class called viewsets. Viewsets provide actions such as .list() and .create()
Two advantages of using this is repeated logic can be combined into a single class and we can only specfy the queryset once. Viewsets uses routers meaning we do
not need to deal with wiring up our Urls configurations ourselves.

I used celery as a worker to send emails and redis as its broker. The celery tasks are like python functions called using celery.


