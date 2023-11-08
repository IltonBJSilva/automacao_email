import requests
import re
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print('Automação iniciada...')
time.sleep(2)
print('')

with open('curriculo.txt','r',encoding='utf-8') as arquivo2:
    curriculo = arquivo2.read()

print('Iniciando o envio de emails para empresas...')
time.sleep(2)
print('')
print('.')
print('.')
print('.')
print('')

# Ler a lista de e-mails de um arquivo
with open('lista-de-emails.txt', 'r') as arquivo_emails:
    lista_emails = arquivo_emails.read().splitlines()

# Configuração inicial para o envio
fromaddr = "iltonbatista2018@gmail.com"  # Insira seu e-mail aqui




s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(fromaddr, "ynqu exaj vsuw qeru")  # Insira a senha do seu Gmail aqui

# Iterar pela lista de e-mails e enviar e-mails
for toaddr in lista_emails:
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "CURRICULO"
    body = curriculo
    msg.attach(MIMEText(body, 'plain')) 
    
    s.sendmail(fromaddr, toaddr, msg.as_string())
    print(f'E-mail para {toaddr} enviado com sucesso!')

# Encerrar a conexão SMTP
s.quit()

            
print('')
print('.')
print('.')
print('.')
print('')
print('Automação concluida com sucesso!')