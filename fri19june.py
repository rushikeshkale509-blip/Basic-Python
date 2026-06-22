'''import qrcode
data = "https://www.youtube.com"
img = qrcode.make(data)
img.save("qrcode.png")
print("qr code generated")'''



'''import qrcode
data="https://www.youtube.com"
qr=qrcode.QRCode()
qr.add_data(data)
qr.make()
qr.print_ascii()'''

'''import smtplib
from email.message import EmailMessage

msg=EmailMessage()

msg["Subject"]="Python Test Mail"
msg["From"]="rushikeshkale509@gmail.com"
msg["To"]="prathmeshnavale900@gmail.com"


msg.set_content("RUSHIKESH ANKUSH KALE")

server=smtplib.SMTP("smtp.gmail.com",587)

server.starttls()

server.login(
    "rushikeshkale509@gmail.com",
    "dqqx kvhq dauk dcsp"
)
server.send_message(msg)

print("email send successfully")

server.quit()'''


import random
import smtplib
from email.message import EmailMessage

otp=random.randint(100000,999999)

msg=EmailMessage()

msg["Subject"]="Python Test Mail"
msg["From"]="rushikeshkale509@gmail.com"
msg["To"]=input("enter your email id: ")


msg.set_content(f"Your OTP is: {otp}")

server=smtplib.SMTP("smtp.gmail.com",587)

server.starttls()

server.login(
    "rushikeshkale509@gmail.com",
    "dqqx kvhq dauk dcsp"
)
server.send_message(msg)

print("OTP send successfully")

server.quit()

attempts=1

while attempts<=1:
    n=int(input("enter otp,only 1 attempts allowed "))
    if n==otp:
        print("login succesfully ")
        break
    else:
        print("invalid otp")
        attempts+=1

