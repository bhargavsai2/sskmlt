import os
import pytz
import re
from datetime import date,datetime
from wordnik import *

from django.conf import settings
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.conf import settings
from django.utils import six
from django.utils.crypto import constant_time_compare, salted_hmac
from django.utils.http import base36_to_int, int_to_base36

from authentication.models import PPVProfile

def send_mail(**kwargs):
    if 'attachment' in kwargs:
        file_name=kwargs['attachment']
    else:
        file_name=False
    from_email = settings.EMAIL_HOST_USER
    email_list = kwargs['email_list']
    subject = kwargs['subject']
    message = kwargs['body']
    msg = EmailMessage(subject=subject,to=email_list)
    msg.template_name = 'billing_template'
    msg.use_template_subject = False
    msg.use_template_from = True
    msg.global_merge_vars = { 
        'content' : message,
    }
    if file_name:
        msg.attach_file(file_name)
    msg.send()        
    if file_name and os.path.isfile(file_name):
        os.system("rm "+file_name)
