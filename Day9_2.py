from day6 import frmt_messeage
from file_mod import MessageUser


f_Names = ["shreya","surabhi","somil","sudha","subhash","shraddha"]
Amount = [120,152.0,148.55,456.66,555.2,123.12]

Messeage= """Hii {Name}!

Thank you for watcching the movie on {date}.
i hope you really feel happy after watching it.
i just want to remainder the cost of ticket was {Amount}.

Shreya
"""
frmt_messeage(f_Names,Amount)

obj=MessageUser()
obj.add_user("vinay",152.0)
obj.add_user("vijay",113.44)
obj.add_user("sumit",156.9)
obj.add_user("anand",159.8)
obj.add_user("vikas",185.0)
obj.get_detail()

print(obj.make_messsages())
