""" module helps to send message """

import smtplib


def send_email():
    """function receives datas and sand message to receiver"""
    print("Please input some information")
    topic = input("Topic of the message:  ")
    body = input("Text:  ")
    sender = input("Your email:  ")
    sender_password = input("Password:  ")
    message = f"Topic: {topic} \n\n{body}"
    receiver = input("Email of receiver:  ")
    smtp_server = input("smtp server:  ")
    with smtplib.SMTP(smtp_server, 587) as server:
        server.starttls()
        server.login(sender, sender_password)
        server.sendmail(sender, receiver, message)


if __name__ == "__main__":
    send_email()
