from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

host = "smtp.gmail.com"
port = 587
userName = "jainsaloni221@gmail.com"
password = "22salonijain"
from_email = userName
to_list = ["hmehta675@gmail.com"]

try:
    email_conn = smtplib.SMTP(host,port)
    email_conn.ehlo()
    email_conn.starttls()
    email_conn.login(userName, password)

    the_msg = MIMEMultipart("alternative")
    the_msg["Subject"] = "BE HAPPY"
    the_msg["From"] = from_email

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

   # print(the_msg.as_string())
   email_conn.sendmail(from_email, to_list, the_msg.as_string())
   email_conn.quit()
except smtplib.SMTPException:
    print("error sending message")
    
