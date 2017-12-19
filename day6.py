import datetime

f_Names = ["shreya","surabhi","somil","sudha","subhash","shraddha"]
Amount = [120,152.0,148.55,456.66,555.2,123.12]

Messeage= """Hii {Name}!

Thank you for watcching the movie on {date}.
i hope you really feel happy after watching it.
i just want to remainder the cost of ticket was {Amount}.

Shreya
"""

def frmt_messeage(names,amounts):
    new_messeage=[]
    if len(names)==len(amounts):
         i=0
         today=datetime.date.today()
         text='{today.day}/{today.month}/{today.year}'.format(today=today)
         for name in names:
             new_amount="%.2f" %(Amount[i])
             new_messeage=Messeage.format(
                 Name=name,
                 date=text,
                 Amount=new_amount
                 )
             i+=1
             print(new_messeage)
             
                 
frmt_messeage(f_Names,Amount)
