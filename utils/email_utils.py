import sendgrid
from sendgrid.helpers.mail import *
import os

def send_otp_mail(to_mail,otp,from_mail):
    
    sg=sendgrid.SendGridAPIClient(api_key=os.environ.get("SENDGRID_API_KEY"))
    from_mail=Email(os.environ.get('FROM_EMAIL'))
    subject="Your OTP Code"
    content=Content("text/plain",f"Hey there,\nYour OTP code is {otp}. The validity of this otp exists only within the timeframe of 6 minutes from generation. Please do not share it with anyone .\n Regards")
    mail=Mail(from_mail,to_mail,subject,content)
    response=sg.client.mail.send.post(request_body=mail.get())
    return response.status_code
    