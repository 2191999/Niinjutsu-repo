import smtplib

host="smtp.gmail.com"
port=587
userName="jainsaloni221@gmail.com"
password="22salonijain"
from_email = userName
to_list=["hmehta675@gmail.com"]

email_conn = smtplib.SMTP(host,port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(userName,password)
email_conn.sendmail(from_email, to_list, "Hii Mr. Abhishek.i Hope u r fine.")
email_conn.quit()


from smtplib import SMTP

xyz= SMTP(host,port)
xyz.ehlo()
xyz.starttls()
xyz.login(userName,password)
xyz.sendmail(from_email, to_list, "Hii Mr. Harsh.i Hope u r fine.")
xyz.quit()

from smtplib import SMTP, SMTPAuthenticationError, SMTPException
xyz= SMTP(host,port)
xyz.ehlo()
xyz.starttls()
try:
    xyz.login(userName,"hjjkcdse")
    xyz.sendmail(from_email, to_list, "Hii Mr. Harsh.i Hope u r fine.")
except:
    print("an error occured")
xyz.quit()
