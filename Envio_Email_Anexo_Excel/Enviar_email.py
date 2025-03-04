import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os
from listas.lista_departamentos import lista_departamentos

USUARIO_PATH = "C:\\restante_do_caminho\\usuario.txt"
SMTP_SERVER = 'smtp.outlook.com'
SMTP_PORT = 587

def obter_credenciais():
    if os.path.exists(USUARIO_PATH):
        with open(USUARIO_PATH, "r") as f:
            users = f.read().splitlines()
        for user in users:
            email, password = user.split(":")
            return email, password
    return None, None

def criar_mensagem(from_address, to_address, subject, body, attachment_path):
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    if os.path.isfile(attachment_path):
        with open(attachment_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachment_path))
            msg.attach(part)
    else:
        print(f"Arquivo {attachment_path} não encontrado.")
    return msg

def Enviar_email():
    email, password = obter_credenciais()
    if not email or not password:
        print("Credenciais não encontradas.")
        return

    from_address = email
    to_address = str(lista_departamentos())
    subject = input("Informe o assunto do e-mail: ")
    os.system('cls')
    body = input('Informe sua mensagem: ')
    os.system('cls')
    nome_arquivo = input('Informe o nome do arquivo: ')
    os.system('cls')
    attachment_path = f'C:\\restante_do_caminho\\{nome_arquivo}.xlsx'

    msg = criar_mensagem(from_address, to_address, subject, body, attachment_path)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(email, password)
            server.sendmail(from_address, to_address, msg.as_string())
        print('Email enviado com sucesso.')
    except Exception as e:
        print(f"Falha ao enviar email: {e}")

if __name__ == "__main__":
    Enviar_email()