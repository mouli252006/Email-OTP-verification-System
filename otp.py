import qrcode
import random
import time
import smtplib
from email.message import EmailMessage

SENDER_EMAIL = "moulikavinjamuri@gmail.com"
APP_PASSWORD = "vvcy nmeq xnpm mbty"
OTP_EXPIRY = 180  # seconds

otp = random.randint(100000, 999999)
otp_time = time.time()

receiver = input("Enter email to receive OTP: ")

msg = EmailMessage()
msg["Subject"] = "QR Login OTP"
msg["From"] = SENDER_EMAIL
msg["To"] = receiver
msg.set_content(
    # f"Session ID: {session_id}\n"
    f"Your OTP is {otp}. Valid for {OTP_EXPIRY} seconds."
)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(SENDER_EMAIL, APP_PASSWORD)
    server.send_message(msg)

print("✅ OTP sent to email")


entered_otp = input("Enter OTP: ")

if time.time() - otp_time > OTP_EXPIRY:
    print("❌ OTP expired")
elif  entered_otp == str(otp):
    print("✅ Verification successful")
else:
    print("❌ Verification failed")