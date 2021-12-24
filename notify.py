import smtplib
from twilio.rest import Client
import os

tw_id = "AC405565638eb21752d664f91e7c1c16ce"
tw_tkn = "3685d4c70f1f0aa0cef968c2c586d4d2"
tw_no = "+19256432125"
my_no = "+919491654127"
my_mail = "mailme.anonymous.1@gmail.com"
mail_pasd = "mailme1997"

class Notification():

    def __init__(self):
        self.client = Client(tw_id, tw_tkn)

    def sms(self, msg2, link):
        msg = self.client.messages.create(
            body=f"{msg2}\n{link}",
            from_=tw_no,
            to=my_no
        )
        print(msg.sid, msg.status)

    def snd_email(self, nms, email_s, msg2, link):
      with smtplib.SMTP("smtp.gmail.com:587") as cntn:
        cntn.ehlo()
        cntn.starttls()
        cntn.login(user=my_mail, password=mail_pasd)
        try:
          for eml in range(len(email_s)):
            cntn.sendmail(from_addr=my_mail,
                          to_addrs=email_s[eml],
                          msg=f"Subject:New Low Price Flight! {nms[eml]}\n\n{msg2}\n{link}".encode('utf-8')
                          )
            print(cntn)
        except:
          print("You've Given an invalid Gmail")