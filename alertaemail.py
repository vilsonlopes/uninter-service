import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv


load_dotenv()


def send_mail():

    email_address = os.getenv('EMAIL_ADDRESS')
    email_password = os.getenv('EMAIL_PASSWORD')
    email_cliente1 = os.getenv('EMAIL_CLIENTE1')

    contacts = ["vilsonlopes@yahoo.com.br"]

    msg = EmailMessage()
    msg['Subject'] = "Uninter Serviços"
    msg['From'] = email_address
    msg['To'] = ','.join(contacts)

    # The email body for recipients with non-HTML email clients.
    body_text = ""
    # The HTML body of the email.
    body_html = ('<html><body><h1 style="color: red">ATENÇAO!</h1><p>Houve mudanças na página de serviço da Uninter</p></body></html>')

    msg.set_content(body_html)
    # msg.add_alternative(body_text, subtype='text')
    msg.add_alternative(body_html, subtype='html')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(email_address, email_password)
            server.send_message(msg)
    except Exception as e:
        print(f'Erro ao enviar {e}')
    else:
        print('Email enviado com sucesso!')
