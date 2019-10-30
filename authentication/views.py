# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate,login,logout
from .models import Profile, AccountEntry,Lorry,CustomerCosignee,CustomerConsigner
from django.http import HttpResponse
from django.core import serializers
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
import json
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q, Count
import xlsxwriter
import StringIO
import datetime
# Create your views here.
def accountentry(request,pk):
    lorries = Lorry.objects.all()
    consignees = CustomerCosignee.objects.all()
    consigners = CustomerConsigner.objects.all()
    if request.method == 'GET':
        if pk == '':
            return render(request,'accountentry.html',{'lorries':lorries,'consignees':consignees,'consigners':consigners})
        else:
            entry = AccountEntry.objects.get(pk=pk)
            return render(request,'accountentry.html',{'entry':entry,'lorries':lorries,'consignees':consignees,'consigners':consigners})
    else:
        # import pdb;pdb.set_trace()
        if pk == '':
            entry = AccountEntry()
        else:
            entry = AccountEntry.objects.get(pk=pk)
        if request.POST['collection_date'] == '':
            entry.collection_date = None
        else:
            collection_date = request.POST['collection_date']
            entry.collection_date = datetime.datetime.strptime(collection_date, '%m/%d/%Y').date()
        if request.POST['entry'] == '':
            entry.date = None
        else:
            date = request.POST['entry']
            entry.date=datetime.datetime.strptime(date, '%m/%d/%Y').date()
        if request.POST['paid_date'] == '':
            entry.paid_date = None
        else:
            paid_date = request.POST['paid_date']
            entry.paid_date = datetime.datetime.strptime(paid_date, '%m/%d/%Y').date()
        customer_consignee = request.POST['consignee']
        customer_consigner = request.POST['consigner']
        truck = request.POST['truck']
        if request.POST['tons'] != '':
            entry.tons = float(request.POST['tons'])
        if request.POST['freight'] != '':
            entry.freight = float(request.POST['freight'])
        if request.POST['advance'] != '':
            entry.advance = float(request.POST['advance'])
        if request.POST['balance'] != '':
            entry.balance = float(request.POST['balance'])
        if request.POST['hamali'] != '':
            entry.hamali = float(request.POST['hamali'])
        if request.POST['net_collection'] != '':
            entry.netcollection = float(request.POST['net_collection'])
        if request.POST['paid_balance'] != '':
            entry.paid_balance = float(request.POST['paid_balance'])
        entry.station= request.POST['station']
        entry.truck = Lorry.objects.get(truck_no=truck)
        entry.customer_consignee = CustomerCosignee.objects.get(customer_name=customer_consignee)
        entry.customer_consigner = CustomerConsigner.objects.get(customer_name=customer_consigner)
        entry.save()
        return HttpResponse(json.dumps({
                        'type': 'success',
                        'message': 'Account Entry Saved Successfully'
                    }))

class UserLogin(View):

    def get(self, request):
        return render(request,'login.html', {})

    def post(self, request):
    	# import pdb;pdb.set_trace()
        uname=request.POST.get('username')
        pwd=request.POST.get('password')
        user=authenticate(username=uname, password=pwd)
        if user is not None:
        	login(request, user)
        	return HttpResponseRedirect('/')
        else:	
        	return render(request,'login.html', {'error':'Invalid User'})
def create_lorry(request):
    # import pdb;pdb.set_trace()
    if request.method == 'GET':
        return render(request,'lorry.html')
    else:
        lorry = Lorry()
        lorry.truck_no = request.POST['truck_no']
        lorry.driver_name = request.POST['driver_name']
        lorry.driver_contact = request.POST['driver_contact']
        lorry.owner_name = request.POST['owner_name']
        lorry.owner_contact = request.POST['owner_contact']
        lorry.licence_id = request.POST['licence_id']
        lorry.save()    
        return render(request,'lorry.html',{'lorry':lorry})

def update_lorry(request,id=None):
    if request.method == 'GET':
        lorry = Lorry.objects.get(id=id)
        return render(request,'lorry.html',{'lorry':lorry})
    else:
        lorry = Lorry.objects.get(id=id)
        lorry.truck_no = request.POST['truck_no']
        lorry.driver_name = request.POST['driver_name']
        lorry.driver_contact = request.POST['driver_contact']
        lorry.owner_name = request.POST['owner_name']
        lorry.owner_contact = request.POST['owner_contact']
        lorry.licence_id = request.POST['licence_id']
        lorry.save()    
        return render(request,'lorry.html',{'lorry':lorry})

def create_consignee(request,id=None):
    if request.method == 'GET':
        try:
            customer = CustomerCosignee.objects.get(id=id)
        except:
            customer = []
        return render(request,'customer_consignee.html',{'customer':customer})
    else:
        try:
            customer = CustomerCosignee.objects.get(id=id)
        except:
            customer = CustomerCosignee()
        customer.customer_name = request.POST['customer_name']
        customer.address = request.POST['address']
        customer.contact  = request.POST['contact']
        customer.save()
        return render(request,'customer_consignee.html',{'customer':customer})

def create_consigner(request,id=None):
    if request.method == 'GET':
        try:
            customer = CustomerConsigner.objects.get(id=id)
        except:
            customer = []
        return render(request,'customer_consigner.html',{'customer':customer})
    else:
        try:
            customer = CustomerConsigner.objects.get(id=id)
        except:
            customer = CustomerConsigner()
        customer.customer_name = request.POST['customer_name']
        customer.address = request.POST['address']
        customer.contact  = request.POST['contact']
        customer.save()
        return render(request,'customer_consigner.html',{'customer':customer})

def consignees(request):
    customers = CustomerCosignee.objects.all()
    return render(request,'consignees.html',{'customers':customers})
def consigners(request):
    customers = CustomerConsigner.objects.all()
    return render(request,'consigners.html',{'customers':customers})
def lorries(request):
    lorries = Lorry.objects.all()
    return render(request,'lorries.html',{'lorries':lorries})
def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

def dashboard(request):
    # if request.user.role == 'Administartor':
    date = datetime.datetime.now().date()
    entries = AccountEntry.objects.filter(date=date)
    return render(request,'dashboard.html',{'entries':entries})


class UserView(View):
    def post(self,request):
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        contact = request.POST['contact']
        role = request.POST['role']
        user = PPVProfile.objects.get(username=request.user.username)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.contact = contact
        if role != '':
            user.role = role
        user.save()
        return HttpResponse(json.dumps({
                        'type': 'success',
                        'message': 'User saved successfully'
                    }))

    def get(self, request):
        user = PPVProfile.objects.get(username=request.user.username)
        return render(request,'myaccount.html',{'user':user})

  

def users(request):
    users = PPVProfile.objects.all()
    return render(request,'userslist.html',{'users':users})    

def view_userdetails(request, user_id):
    # attempt to get the user object based on id number
    try:
        user = PPVProfile.objects.get(id=user_id)
    except:
        user = None
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        contact = request.POST['contact']
        role = request.POST['role']
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.contact = contact
        if role != '':
            user.role = role
        user.save()
        return HttpResponse(json.dumps({
                        'type': 'success',
                        'message': 'User saved successfully'
                    }))        
    return render(request,'myaccount.html',{'user':user})        


def register(request):
    if request.method == 'POST':
        username = request.POST['ldap_username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone =  request.POST['phone']
        email = request.POST['email']
        manager_email =  request.POST['manager_email']
        user = PPVProfile.objects.create()
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.phone = phone
        user.email = email
        user.escalation_email = manager_email
        user.save()
        return render(request,'register.html',{'success':True})
    return render(request,'register.html',{'success':False})    


def entries(request):
    entries = AccountEntry.objects.all()
    return render(request,'entries.html',{'entries':entries})


def report(request):
    if request.method == 'POST':
        # import pdb;pdb.set_trace()
        if request.POST['start_date'] == '':
                start_date = None
        else:
            start_date = request.POST['start_date']
            start_date = datetime.datetime.strptime(start_date, '%m/%d/%Y').date()
        if request.POST['end_date'] == '':
                end_date = None
        else:
            end_date = request.POST['end_date']
            end_date = datetime.datetime.strptime(end_date, '%m/%d/%Y').date()
        if start_date and end_date:
            entries = AccountEntry.objects.filter(date__gte=start_date,
            date__lt=end_date + datetime.timedelta(days=1))
        elif start_date:
            entries = AccountEntry.objects.filter(date__gte=start_date)
        elif end_date:
            entries = AccountEntry.objects.filter(date__lt=end_date + datetime.timedelta(days=1))
        else:
            entries = AccountEntry.objects.all()
        html = render_to_string('report_table.html',{'entries':entries})
        return HttpResponse(html)
    return render(request,'report.html')


@csrf_exempt
def download_report(request):
    # import pdb;pdb.set_trace()
    data = request.POST
    start_date = json.loads(data['start_date'])
    end_date = json.loads(data['end_date'])
    if start_date == '':
        start_date = None
    else:
        start_date = datetime.datetime.strptime(start_date, '%m/%d/%Y').date()
    if end_date == '':
            end_date = None
    else:
        end_date = datetime.datetime.strptime(end_date, '%m/%d/%Y').date()
    if start_date and end_date:
        entries = AccountEntry.objects.filter(date__gte=start_date,
        date__lt=end_date + datetime.timedelta(days=1))
    elif start_date:
        entries = AccountEntry.objects.filter(date__gte=start_date)
    elif end_date:
        entries = AccountEntry.objects.filter(date__lt=end_date + datetime.timedelta(days=1))
    else:
        entries = AccountEntry.objects.all()
    from django.utils import timezone
    time_audit = timezone.now()
    time_stamp = time_audit.strftime("%Y_%m_%d")
    file_name = 'audit_report_'+time_stamp+'.xlsx'
    results = list(entries.values_list('truck__truck_no','customer_consignee__customer_name','customer_consigner__customer_name','date','tons','freight','advance','balance','hamali','netcollection','collection_date','paid_date','paid_balance','station'))
    response = HttpResponse(content_type='application/openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename='+file_name
    output = StringIO.StringIO()
    wb = xlsxwriter.Workbook(output)
    ws = wb.add_worksheet('worksheet')
    columns = ['Truck No','Consignee','Consigner','Entry Date','Tons','Freight','Advance','Balance','Hamali','Net Collection','Collection Date','Paid Date','Paid Balance','Station']
    #Writing columns
    for idx,col in enumerate(columns):
        ws.write(0, idx, col)

    #Writing rows data
    for rowidx,result in enumerate(results):
        for idx, val in enumerate(result):
            if idx == 6:
                try:
                    val = timezone.localtime(val).strftime('%a %b %d %H:%M%p %Y')
                except:
                    pass
            ws.write(rowidx+1, idx, val.__str__())

    wb.close()
    response.write(output.getvalue())
    return response

# def show_users(request):
#     import pdb;pdb.set_trace()
#     users = PPVProfile.objects.all()
#     json = serializers.serialize('json', users,fields=['username','first_name','last_name','email'])
#     return HttpResponse(son, content_type='application/json')


# def process_postpatch_excel(request):
    
#     py_date = datetime.datetime(*xlrd.xldate_as_tuple(sheet.cell(0,0),xx.datemode))
#     

