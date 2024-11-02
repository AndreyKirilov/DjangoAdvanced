from django.http import HttpResponseForbidden
from django.utils.timezone import localtime
from datetime import time


class SetTimeRestriction:
    start_time = time(9, 0)
    end_time = time(17, 0)
    forbidden_message = 'This website is available only from 9am to 5pm.'

    def dispatch(self, request, *args, **kwargs):
        current_time = localtime().time()

        if not (self.start_time <= current_time <= self.end_time):
            return HttpResponseForbidden(self.forbidden_message)

        return super().dispatch(request, *args, **kwargs)
