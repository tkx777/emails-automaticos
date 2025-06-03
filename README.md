
Emails Automáticos

Este projeto permite o envio automático de e-mails personalizados com múltiplos anexos em PDF utilizando Python. Ideal para relatórios, envios periódicos e automação de comunicados.


Funcionalidades

Envio de e-mails para múltiplos destinatários  

Corpo do e-mail em HTML personalizável 

Suporte a múltiplos anexos (PDF ou outros arquivos) 

Configuração simples e segura com variáveis de ambiente 

Pré-requisitos 

Python 3.x 

Conta de e-mail (exemplo: Gmail)

Permissões adequadas para envio via SMTP (no Gmail, pode ser necessário gerar uma senha de app)

Instalação

Clone este repositório:

bash

git clone https://github.com/tkx777/emails-automaticos.git

cd emails-automaticos

Instale as dependências (opcional, pois usa apenas módulos da biblioteca padrão do Python):

bash

pip install -r requirements.txt

Configuração

Edite o arquivo principal do script:

Defina o e-mail e a senha do remetente.

Coloque os e-mails dos destinatários.

Altere o caminho da pasta com os PDFs, se desejar.

Insira os nomes dos arquivos para anexar.

Python

email_remetente = 'seuemail@gmail.com'

senha_remetente = 'sua_senha_app'

emails_destinatarios = ['destino1@email.com', 'destino2@email.com']

pasta_pdfs = 'CAMINHO/para/pdfs/'

nomes_dos_arquivos_pdf = ['arquivo1.pdf', 'arquivo2.pdf']

Por segurança, recomenda-se usar variáveis de ambiente para a senha.

Personalize o corpo do e-mail em HTML se desejar.

Como usar

Execute o script principal:

bash

python seu_script.py

Você verá mensagens no console indicando o andamento do envio e possíveis erros.

Observações

Para contas Gmail, pode ser necessário ativar "Acesso a apps menos seguros" ou criar uma senha de app.

Certifique-se de que os caminhos dos arquivos e anexos estão corretos.

Licença

Este projeto está sob a licença MIT.

Autor: rafael sena

E-mail: rafaelsena221@gmail.com
