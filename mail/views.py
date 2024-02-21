from django.shortcuts import render,HttpResponse

# Create your views here.
from django.core.mail import send_mail

def send_email_view(request):
    send_mail(
            'Hello from Django',
            'This is a test email from Django.',
            'jaswantevaishnavi@gmail.com',
            ['sawalakhevaishnavi@gmail.com'] , # List of recipient email addresses
        
        fail_silently= False,

        
    )
    
   

    
    return HttpResponse('Email sent successfully!')





