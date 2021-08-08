from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail


def index(request):
    if request.method == "POST":
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')

        data = {
            'subject':subject,
            'email': email, 
            'message':message
        }
        message = '''
        New Message:{}

        From:{}
        '''.format(data['message'], data['email'])

        send_mail(data['subject'], message, '', ['shakil.cse.uoda@gmail.com'])
       
    return render(request, 'sendmail.html', {})
