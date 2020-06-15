from django.core.mail import send_mail

send_mail(
    subject='That’s your subject',
    message='That’s your message body',
    from_email='shrinivaschowdhary97@gmail.com',
    recipient_list=['2015bcs017@sggs.ac.in',],
    fail_silently=False,
)