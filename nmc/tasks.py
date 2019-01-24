from __future__ import absolute_import, unicode_literals

# from .celery import app
from celery.schedules import crontab
from splinter import Browser
from nmc.models import Schedule
from django.contrib.auth.models import User

from celery import Celery

app = Celery("tests", broker="amqp://", backend="amqp://", include=["nmc.tasks"])


def put_call_request(mob, c_code="+91"):
    url = "https://www.twilio.com/voic"
    mob = c_code + str(mob)

    with Browser() as browser:
        browser.visit(url)
        inp = browser.find_by_xpath('//input[@role="number"]')
        btn = browser.find_by_xpath('//button[text()="Call my phone"]')
        inp.first.value = mob
        btn.first.click()


@app.task
def work(sender):
    # Get all users.
    users = User.objects.all()
    for user in users:
        # Get all Schedules for a user.
        schedules = Schedule.objects.filter(uid=user.id)
        for sch in schedules:
            sender.add_periodic_task(
                crontab(hour=int(sch.hr), minute=int(sch.mn)),
                put_call_request.delay(user.mobile),
            )


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Executes everyday at 12:00 a.m.
    sender.add_periodic_task(
        crontab(hour=0, minute=0, day_of_week="mon-fri"), work.delay(sender)
    )


# @app.task
# def add(x, y):
#     return x + y


# @app.task
# def mul(x, y):
#     return x * y


# @app.task
# def xsum(numbers):
#     return sum(numbers)
