import datetime

class MessageUser():
    user_details=[]
    message=[]
    base_message="""hii {name}!
Thank you for the purchase on {date}.
i hope you are excited about using it.
Just as a reminder the purchase total was RS-/{total}.

Shreya
"""
    
    def add_user(self,name,amount):
        name=name[0].upper()+name[1:].lower()
        new_amount="%2f"%(amount)
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
    def make_msssages(self):
        if len(self.user_details) > 0:
              for detail in self.user_detail():
                  name=detail["name"]
                  date=detail["date"]
                  amount=detail["amount"]
                  message=self.base_msg
                  new_message=base_message.format(
                      name=name,
                      date=date_text,
                      total=new_amount
                      )
                  self.message.append(new_message)
                return self.message
            return []



obj=Messageuser()
obj.add_user("vinay",152.0)
obj.add_user("vijay",113.44)
obj.add_user("sumit",156.9)
obj.add_user("anand",159.8)
obj.add_user("vikas",185.0)
obj.get_details()
          
          
