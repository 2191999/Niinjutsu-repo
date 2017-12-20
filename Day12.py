from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import datetime


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

host = "smtp.gmail.com"
port = 587
userName = "jainsaloni221@gmail.com"
password = "22salonijain"
from_email = userName
to_list = ["hmehta675@gmail.com"]

class MessageUser():
    user_details=[]
    email_details=[]
    message=[]
    base_message="""hii {name}!
Thank you for the purchase on {date}.
i hope you are excited about using it.
Just as a reminder the purchase total was RS-/{total}.

Shreya
"""
    
    def add_user(self,name,amount):
        name=name[0].upper()+name[1:].lower()
        amount="%2f"%(amount)
        detail={
                 "name":name,
                 "amount":amount,
        }
        today=datetime.date.today()
        date_text='{today.day}/{today.month}/{today.year}'.format(today=today)
        detail["date"]=date_text
        self.user_details.append(detail)

    def get_detail(self):
        return self.user_details
    def make_messsages(self):
        if len(self.user_details) > 0:
              for detail in self.get_detail():
                  name = detail["name"]
                  date = detail["date"]
                  amount = detail["amount"]
                  message = self.base_message
                  new_message = message.format(
                      name=name,
                      date=date,
                      total=amount
                      )
                  user_email = detail.get("email")
                  if user_email:
                      user_data = {
                          "email": user_email'
                          "message": new_message
                          }
                      self.email_details.append(user_data)
                   else:
                       self.message.append(new_message)
              return self.message 
        return []
    def send_email(self):
        self.make_messages()
        if len(self.make_messages) > 0:
            for detail in self.email_messages:
                user_email = detail["email"]
                user_message = detail["message"]
                try:
                    email_conn = smtplib.SMTP(host,port)
                    email_conn.ehlo()
                    email_conn.starttls()
                    email_conn.login(userName, password)
    
                    the_msg = MIMEMultipart("alternative")
                    the_msg["Subject"] = "BE HAPPY"
                    the_msg["From"] = from_email
                    the_msg["To"] = to_list[0]
                    plain_txt = "Checking Whether u r happy or not"
                    html_txt = """\
                        <html>
                          <head></head>
                          <body>
                             <p>hey!<br>
                                Testing this mail <b>message</b>.Made by <a href="http://joincfe.com">TeamCFE</a>.
                             </p>
                          </body>
                        </html>
                        """

                        part_1 = MIMEText(plain_txt, "plain")
                        part_2 = MIMEText(html_txt, "html")

                        the_msg.attach(part_1)
                        the_msg.attach(part_2)
                        email_conn.sendmail(from_email, to_list, the_msg.as_string())
                        email_conn.quit()
                    except smtplib.SMTPException:
                        print("error sending message")
                 return True
             return False



obj=MessageUser()
obj.add_user("vinay",152.0)
obj.add_user("vijay",113.44)
obj.add_user("sumit",156.9)
obj.add_user("anand",159.8)
obj.add_user("vikas",185.0)
obj.get_detail()

obj.make_messsages()


