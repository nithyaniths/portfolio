from django.shortcuts import render,redirect
from django.core import mail
from django.contrib import messages
from myportfolio import settings
import os
from django.http import FileResponse,Http404
def home(request):
    return render(request,'home.html')

def contact(request):
    if request.method == 'POST':
       
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject=request.POST.get('subject')


        from_email = settings.EMAIL_HOST_USER

        email_message = mail.EmailMessage(
            subject=f"Subject: {subject} (from {name})",
            body=f'User Email: {email}\nUser \n\n\nQuery:\n{message}',
            from_email=from_email,
            to=['nithyapramod97@gmail.com']  
        )
        try:
            email_message.send()
            messages.success(request, 'Your message has been sent successfully! Thank you.')
        except Exception as e:
            messages.error(request, f'An error occurred while sending the email: {e}')
        
        confirmation_message = mail.EmailMessage(
            subject='Thank you for contacting us',
            body=f'Hello {name},\n\nThank you for reaching out to us. We have received your message and will get back to you soon.',
            from_email=from_email,
            to=[email]
        )
        try:
            confirmation_message.send()
        except Exception as e:
            messages.error(request, f'An error occurred while sending the confirmation email: {e}')

    return redirect(home)


def download_resume(request):
    file_path = os.path.join('static', 'cv', 'Nithya.pdf')
    
    if os.path.exists(file_path):
        messages.success(request,"Message sent successfully")
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='Nithya.pdf')
       
    else:
        raise Http404("File not found")