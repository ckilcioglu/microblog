from flask_mail import Message
from app import mail, app
from flask import render_template
from threading import Thread
from flask_babel import _


def send_email_async(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_email_async, args=(app, msg)).start()
