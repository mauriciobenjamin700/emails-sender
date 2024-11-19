from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def format_email(from_email: str, to_email: str, subject: str, body: str) -> MIMEMultipart:
    """
    Formata conteúdo para formar um email

    - Args:
        - from_email (str): Email do remetente
        - to_email (str): Email do destinatário
        - subject (str): Assunto do email
        - body (str): Corpo do email

    - Returns:
        - MIMEMultipart: Email formatado para envio
    """
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    return msg