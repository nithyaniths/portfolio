from django.shortcuts import render,redirect
from django.core import mail
from django.contrib import messages
from myportfolio import settings

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
            subject=f'Email is from {name}',
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



        # if name and email and message and subject:  # Basic validation to ensure fields are not empty
        #     try:
        #         # Send an email
        #         send_mail(
        #             subject=subject,
        #             message=message,
        #             from_email=email,  # Use the sender's email from the POST data
        #             recipient_list=['nithyapramod97@gmail.com.com'],  # Replace with your email
        #         )
        #         messages.success(request, "Your message has been sent successfully!")
        #     except Exception as e:
        #         messages.error(request, f"An error occurred: {str(e)}")
        #     return redirect(home)  # Redirect to the same page or another
        # else:
        #     messages.error(request, "All fields are required!")
    return render(request, 'home.html')