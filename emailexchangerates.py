import emails
import os

toaddr = ["emendez@pbpost.com", "mstucka@pbpost.com", "asilverman@pbpost.com", "jwinans@pbpost.com"]

# toaddr = ["mstucka@pbpost.com", "stucka@gmail.com"]

emailuser = os.environ["GOOGLEADDRESS"]
emailpassword = os.environ["GOOGLEPASSWORD"]
emailname = os.environ["GOOGLENAME"]
emailfrom = emailname + " <" + emailuser + ">"

subject = "Currency exchange rate report"

filename = "ratereport.txt"

with open(filename, "r") as f:
    text = f.read()

message = emails.html(text=text, subject=subject, mail_from=emailfrom)
message.send(to=(toaddr), smtp={"host":"smtp.gmail.com", "port":465, "ssl":True, "user":emailuser, "password":emailpassword} )