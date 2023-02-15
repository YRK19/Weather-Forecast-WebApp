import smtplib
import ssl


def send_email(message):
    """Build a server to send an e-mail to admin(receiver)"""
    host = "smtp.gmail.com"
    port = 465

    # Server credentials
    username = "testcode019@gmail.com"
    password = "urmeiognugamgnks"

    receiver = "testcode019@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
