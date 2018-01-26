import django
from  django.shortcuts import render_to_response,render
from django.http import HttpResponse,HttpResponseRedirect
from books.models import Book,Staff,Company,Plan
from django.core.mail import send_mail,EmailMessage
from django.template import RequestContext,loader,Context
from mysite.forms import ContactForm
import smtplib 
from django.conf import settings
import codecs

def search_form(request):
    return render_to_response('search_form.html')

def search(request): 
    errors = []
    if 'q' in request.GET:
        b = request.GET['q']
        if not b:
            errors.append('Enter a book name!')
        elif len(b) > 20 :
            errors.append('Pls Enter a shorter name!')
        else:
            books = Book.objects.filter(title__icontains=b)
            return render_to_response('search_results.html',
                                  {'books':books,'query':b})
    return render_to_response('search_form.html',{'error':errors})


def contactt(request):
    send_mail('subject','message',settings.EMAIL_HOST_USER,['zwt467875460@gmail.com'],fail_silently = False)
    return HttpResponseRedirect('/contact/thanks')
def contact(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
            request.POST['subject'],
            request.POST['message'],
            'zwt467875460@gmail.com',
            [request.POST.get('email')],
            fail_silently = False
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial = {'email':'zwt467875460@gmail.com'}        )
    context = {'form':form}
    return render(request,'contact_form.html',context)
def thanks(request): 
     return HttpResponse('thanks!')







def shift(request):
    
   
    monday_staff = [str(item) for item in Staff.objects.exclude(plan=1)]

    #another way
    #tu = Plan.objects.get(Not_avaliable_day=2)
    #tuesday_staff = tu.staff_set.all() 

    tuesday_staff = [str(item) for item in Staff.objects.exclude(plan=2)]
    wednesday_staff = [str(item) for item in Staff.objects.exclude(plan=3)]
    thursday_staff = [str(item) for item in Staff.objects.exclude(plan=4)]
    friday_staff = [str(item) for item in Staff.objects.exclude(plan=5)]
    saturday_staff = [str(item) for item in Staff.objects.exclude(plan=6)]
    sunday_staff = [str(item) for item in Staff.objects.exclude(plan=7)]
    



    t = loader.get_template('shiftform.html')
    c = Context({
        'monday_staff':monday_staff,
        'tuesday_staff':tuesday_staff,
        'wednesday_staff':wednesday_staff,
        'thursday_staff':thursday_staff,
        'friday_staff':friday_staff,
        'saturday_staff':saturday_staff,
        'sunday_staff':sunday_staff,
    })
      
    return HttpResponse(t.render(c))

'''for i in range(7):
        
        day[i] = [str(item) for item in Staff.objects.exclude(plan=i)]

    c = Context({
        'monday_staff':day[0],
        'tuesday_staff':day[1],
        'wednesday_staff':day[2],
        'thursday_staff':day[3],
        'friday_staff':day[4],
        'saturday_staff':day[5],
        'sunday_staff':day[6],
    })
      
    
    return HttpResponse(t.render(c))'''
    
 
