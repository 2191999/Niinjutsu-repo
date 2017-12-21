import csv
import shutil
from tempfile import NamedTemporaryFile

def get_length(file_path):
    with open("Day14.csv","r") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        return len(reader_list)

def append_data(file_path, name, email):
    fieldnames = ["id", "name", "email", "amount", "sent", "date"]
    next_id = get_length(file_path)
    with open(file_path, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({
            "id": next_id,
            "name": name,
            "email": email,
            "amount": amount,
            "sent": "",
            "date": datetime.datetime.now()
            })
def edit_data(edit_id=None, email=None, amount=None, sent=None):
    filename = "Day14.csv"
    temp_file = NamedTemporaryFile(delete = False)

with open(filename, "w+") as csvfile, temp_file:
    reader = csv.DictReader(csvfile)
    fieldnames = ["id", "name", "email", "amount", "sent", "date"]
    writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
    writer.writeheader()
    for row in reader:
        if edit_id is not NONE:
            if int(row["id"])==int(edit_id):
                row["amount"] = amount
                row["sent"] = sent
            elif email is not None and edit_id is None:
                if str(row["email"]==str(email)):
                       row["amount"] = amount
                       row["sent"] = sent
            else:
                pass
            writer.writerow(row)
            shutil.move(temp_file.name, filename)
        return True 
    return False
          

edit_data(email="jainshreya219@gmail.com", amount=165, sent="")
