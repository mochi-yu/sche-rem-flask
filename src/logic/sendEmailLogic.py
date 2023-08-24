import smtplib
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText

from setting import *


def send_emails(sendAdresses: list[str], mailTitle: str, mailBody: str):
    smtp_server = "smtp.gmail.com"
    port = 587

    server = smtplib.SMTP(smtp_server, port)

    server.starttls()

    login_address = GMAIL_ADDRESS #送信元のメールアドレス
    login_password = GMAIL_APP_PASS #パスワードを入力

    server.login(login_address, login_password)

    message = MIMEMultipart()

    message["Subject"] = mailTitle #送信タイトル
    message["From"] = GMAIL_ADDRESS #送信元のメールアドレス
    message["To"] = ",".join(sendAdresses) #送信先メールアドレス

    text = MIMEText("") #文章絵お入力
    message.attach(text)

    server.send_message(message)

    server.quit()