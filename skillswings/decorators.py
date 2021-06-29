
from django.shortcuts import redirect

from courses.models import Course


PROFILE_URL = 'profile'


def redirect_loggedin_user(func=None, redirect_url=PROFILE_URL):
    def login_checker(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return func(request, *args, **kwargs)
    return login_checker


def enrolled_user_only(func=None, redirect_url='/'):
    def check_enrollment(request, *args, **kwargs):
        course_id = kwargs.get('idc')
        if course_id:
            course = Course.objects.get(id=course_id)
            if request.user.is_authenticated and course in request.user.profile.course.all():
                return func(request, *args, **kwargs)
            else:
                return redirect(redirect_url)
        else:
            return redirect(redirect_url)
    return check_enrollment
