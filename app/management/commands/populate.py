from datetime import datetime, timedelta
from random import randint
import string
import pytz

from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


from app.models import User,Activity

from app.helper import random_pk, TIMEZONES


class Command(BaseCommand):
    help = "Create random users and activity periods"

    def get_id(self):
        return random_pk()

    def get_real_name(self):
        return get_random_string()

    def get_tz(self):
        random_index = randint(0,len(TIMEZONES)-1)
        return  TIMEZONES[random_index]

    def get_start_time(self):
        return datetime.now()

    def get_end_time(self):
        #random day after start time
        end_time = self.get_start_time() + timedelta(randint(1,100))
        return end_time

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for _ in range(total):
            kwargs = {
                'user_id': self.get_id(),
                'real_name': self.get_real_name(),
                'tz': self.get_tz(),
            }
            user = User.objects.create(**kwargs)
            activities = []
            for _ in range(total):
                kwargs={
                    'user': user,
                    'start_time': self.get_start_time(),
                    'end_time': self.get_end_time(),
                }
                activity = Activity(**kwargs)
                activities.append(activity)

            Activity.objects.bulk_create(activities)

        self.stdout.write(self.style.SUCCESS('Data successfully created'))