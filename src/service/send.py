from email.mime.multipart import MIMEMultipart
from smtplib import SMTP


def send_email(smtp_server: str, smtp_port: str, from_email: str, password: str, to_email: str, msg: MIMEMultipart):
    """
    Envia um email para um email de destino

    - Args:
        - smtp_server (str): Servidor SMTP
        - smtp_port (str): Porta do SMTP
        - from_email (str): Email do remetente
        - password (str): Senha do remetente
        - to_email (str): Email do destinatário
        - msg (MIMEMultipart): Email formatado para envio

    - Returns:
        - None
    """
    try:
        """
        Cria uma instância do objeto SMTP e conecta ao servidor SMTP especificado pelo endereço (smtp_server) e porta (smtp_port).
        """
        server = SMTP(smtp_server, smtp_port)
        """
        Inicia a comunicação TLS (Transport Layer Security) para criptografar a conexão ao servidor SMTP, garantindo a segurança dos dados transmitidos.
        """
        server.starttls()
        """
        Faz login no servidor SMTP usando o endereço de email (from_email) e a senha (password).
        """
        server.login(from_email, password)
        """
        Envia o email usando o método sendmail do objeto SMTP.
            from_email: O endereço de email do remetente.
            to_email: O endereço de email do destinatário.
            msg.as_string(): Converte o objeto de mensagem (msg) para uma string f
        """
        server.sendmail(from_email, to_email, msg.as_string())
        """
        Encerra a conexão com o servidor SMTP.
        """
        server.quit()
        
        print("Email enviado com sucesso!")
    except Exception as e:
        print(f"Falha ao enviar email: {e}")