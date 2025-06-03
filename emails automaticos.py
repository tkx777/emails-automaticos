# Importando as bibliotecas necessárias
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os # Para buscar variáveis de ambiente (mais seguro para senhas) e caminhos de arquivo

email_remetente = '' #email que enviara dentro nos ""
senha_remetente = ''.replace(" ", "") #senha dos email dentro ''

# coloque os emails das pessoas que iram receber nos [] com '' e saparando com ,
emails_destinatarios = [
    'email1@gmail.com'.
    'email2@gmail.com'
    
]

assunto_email = 'Reporte Automático - Informativos de Publicações B3 (Múltiplos Anexos)'

# --- Conteúdo do E-mail caso saiba basico html pode mudar a msg que vai no email---
corpo_email_html = """
<html>
  <body>
    <p>AOBAA, BOM</p>
    <p>Segue o reporte automático com os informativos de manuais da B3.</p>
    <p>Este e-mail contém múltiplos anexos.</p>
    <p>e-maili enviado automatcamente nao responder por favor.</p>
    <p>Atenciosamente,<br> Python REPORT</p>
  </body>
</html>
"""

# --- Anexos (Múltiplos Arquivos) ---
pasta_pdfs = 'E:/AULA/Aula Python/REPORT/pdfs/' # caminho onde ficaram os pdfs caso tiver 

#colocar o nome dos pdf dentro dos [] utilize ''para eescrever o nome e separe com ,
nomes_dos_arquivos_pdf = [
    
]

lista_arquivos_anexar = [os.path.join(pasta_pdfs, nome_arquivo) for nome_arquivo in nomes_dos_arquivos_pdf]

# --- Criação da Mensagem ---
mensagem = MIMEMultipart("alternative")
mensagem['From'] = email_remetente
mensagem['To'] = ", ".join(emails_destinatarios) # Junta a lista de e-mails com vírgula para o cabeçalho
mensagem['Subject'] = assunto_email

# Adiciona o corpo do e-mail em formato HTML
parte_html = MIMEText(corpo_email_html, 'html')
mensagem.attach(parte_html)

# Adiciona os anexos
arquivos_anexados_com_sucesso = 0
for caminho_completo_arquivo in lista_arquivos_anexar:
    try:
        if os.path.exists(caminho_completo_arquivo):
            nome_arquivo_para_anexo = os.path.basename(caminho_completo_arquivo)
            with open(caminho_completo_arquivo, 'rb') as anexo: 
                parte_anexo = MIMEBase('application', 'octet-stream')
                parte_anexo.set_payload(anexo.read())
            encoders.encode_base64(parte_anexo)
            parte_anexo.add_header(
                'Content-Disposition',
                f'attachment; filename="{nome_arquivo_para_anexo}"', 
            )
            mensagem.attach(parte_anexo)
            print(f"Anexo '{nome_arquivo_para_anexo}' adicionado com sucesso.")
            arquivos_anexados_com_sucesso += 1
        else:
            print(f"Aviso: Arquivo de anexo '{caminho_completo_arquivo}' não encontrado. Não será anexado.")
    except Exception as e:
        print(f"Erro ao tentar anexar o arquivo '{caminho_completo_arquivo}': {e}")

if arquivos_anexados_com_sucesso == 0 and len(lista_arquivos_anexar) > 0:
    print("Nenhum arquivo foi anexado. Verifique os caminhos e nomes dos arquivos.")
elif arquivos_anexados_com_sucesso < len(lista_arquivos_anexar):
    print(f"{arquivos_anexados_com_sucesso} de {len(lista_arquivos_anexar)} arquivos foram anexados.")


# --- Envio do E-mail ---
try:
    contexto_ssl = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto_ssl) as servidor_smtp:
        print("Conectando ao servidor SMTP...")
        servidor_smtp.login(email_remetente, senha_remetente)
        print("Login realizado com sucesso!") 
        
        # A função sendmail aceita uma lista de destinatários diretamente
        servidor_smtp.sendmail(
            email_remetente, emails_destinatarios, mensagem.as_string()
        )
        print(f"E-mail enviado com sucesso para: {', '.join(emails_destinatarios)}!")

except smtplib.SMTPAuthenticationError:
    print("Erro de autenticação. Verifique seu e-mail e senha (ou senha de app).")
    print("As senhas de app do Gmail geralmente não contêm espaços.")
    print("Para o Gmail, pode ser necessário 'Permitir acesso a app menos seguro' ou usar uma 'Senha de App'.")
except smtplib.SMTPServerDisconnected:
    print("Servidor desconectado. Verifique sua conexão ou as configurações do servidor SMTP.")
except smtplib.SMTPConnectError:
    print("Não foi possível conectar ao servidor SMTP. Verifique o endereço do servidor e a porta.")
except ConnectionRefusedError:
     print("Conexão recusada. Verifique se o servidor SMTP está ativo e se não há firewall bloqueando.")
except Exception as e:
    print(f"Ocorreu um erro ao enviar o e-mail: {e}")

