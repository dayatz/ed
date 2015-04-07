from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

class IsLoggedIn(object):
    def process_request(self, request):
        if not request.user.is_authenticated()\
                and not request.path == reverse('home'):
            return HttpResponseRedirect('/')