# Enviar e-mail

#input: receiver email address, assunto, mensagem

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def send_email(to, me, subject, body, my_password):
    s = smtplib.SMTP(host="smtp-mail.outlook.com", port="587")
    s.starttls()
    s.login(me, my_password)

    msg = MIMEMultipart()
    msg['From'] = str(me)
    msg['To'] = str(to)
    msg['Subject'] = str(subject)

    message = str(body)

    msg.attach(MIMEText(message, 'plain'))

    s.send_message(msg)
    del msg


para = input('E-mail para: ')
assunto = input('Assunto: ')
corpo = input('Corpo do e-mail: ')
de = input('Seu e-mail: ')
senha = input('Senha:')

send_email(para, de, assunto, corpo, senha)