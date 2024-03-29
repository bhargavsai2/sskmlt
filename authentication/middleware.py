# Author: Integra
# Dev: Partha(Ref)

import hashlib, re, sys, inspect
from datetime import datetime 

from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.utils.translation import activate
from django.utils.deprecation import MiddlewareMixin

# class If_Session_Idle_Timeout:
#     '''middleware that checks for session idle timeout'''
#     def process_request(self, request):
#         path = request.get_full_path()
#         temp_path=request.path
#         try:
#             try:
#                  last_activity=request.session['last_touch']
#             except:
#                  request.session['last_touch'] = datetime.now()
#                  last_activity = request.session['last_touch']
#             now=datetime.now()
#             expiry_time=settings.SESSION_TIMEOUT
#             if (now-last_activity).total_seconds() > expiry_time:
#                 logout(request)
#                 return HttpResponseRedirect('/login/')
#             else:
#                 request.session['last_touch']=datetime.now()
#                 return
#         except:
#             return HttpResponseRedirect('/login/')


    

class LoginRequired(MiddlewareMixin):

    def process_request(self, request):
        if request.user.is_authenticated():
            if request.path == "/login/":
                return HttpResponseRedirect("/")
        else:
            if request.path == "/login/" or request.path == '/register/':
                return
            return HttpResponseRedirect('/login/')
