from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import socket
import os

SMTP_SERVER = 'smtp.outlook.com'
SMTP_PORT = 587
EMAIL = 'teste_email@outlook.com'
SENHA = 'testes_Senha'
TITULO = 'Acesso não autorizado'

def obter_ip_rede():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(('8.8.8.8', 80))
            return s.getsockname()[0]
    except Exception as e:
        print(f"Erro ao obter o IP da rede: {e}")
        return None

def criar_mensagem(from_address, to_address, subject, body):
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    return msg

def enviar_email(msg, smtp_username, smtp_password):
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(msg['From'], msg['To'], msg.as_string())
        print('Email enviado com sucesso.')
    except Exception as e:
        print(f"Falha ao enviar email: {e}")

def alerta():
    try:
        username = os.getlogin()
    except Exception as e:
        print(f"Erro ao obter o nome do usuário: {e}")
        username = "Desconhecido"

    network_ip_address = obter_ip_rede()
    if not network_ip_address:
        print("Não foi possível obter o IP da rede.")
        return

    body = (f'Uma tentativa de acesso foi detectada em um equipamento não autorizado. '
            f'IP do equipamento: {network_ip_address}. Usuário que tentou acesso: {username}')
    
    msg = criar_mensagem(EMAIL, EMAIL, TITULO, body)
    enviar_email(msg, EMAIL, SENHA)

if __name__ == "__main__":
    alerta()