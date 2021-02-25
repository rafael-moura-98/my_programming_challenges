from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def send_email(to, me, subject, body, my_password):
    """Simple function to deliver e-mail. Currently, the origin of the messagem must come from an outlook email.
    
    
    Parameters
    ----------
    to: str
        Email address of whom is receiving

    me: str
        Email address of whom is sending

    subject: str
        Subject of the message

    body: str
        Body message of the email.

    my_password: str
        Password of the account that is sending the message.
    
    """

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