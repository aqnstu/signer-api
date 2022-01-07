"""отправка почты"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.message import EmailMessage
from os.path import basename
from configs import email


class NSTUSender:
    """Класс обертка для отправки почты через Exchange"""
    def __init__(self, server, port, login, passw):
        self._server = server
        self._port = port
        self._login = login
        self._passw = passw
        self._s = None
        self.start()

    def start(self):
        self._s = smtplib.SMTP(self._server, self._port)
        self._s.starttls()
        self._s.login(email.MAIL_LOGIN, email.MAIL_PASS)

    def quit(self):
        self._s.quit()

    def send_html(self, subj, message, html_message, sfrom, sto, files=None):
        """Отправка сообщения в формате html"""
        m = EmailMessage()
        m["From"] = sfrom
        m["Subject"] = subj
        m["To"] = sto
        m.set_content(message)
        m.add_alternative(html_message, subtype='html')
        for f in files or []:
            with open(f, "rb") as fil:
                part = MIMEApplication(
                    fil.read(),
                    Name=basename(f)
                )
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
            m.attach(part)
        self._s.send_message(m)
        del m

    def send(self, subj, message, sfrom, sto, files=None):
        """Отправка сообщения"""
        msg = MIMEMultipart()
        msg['From'] = sfrom
        msg['To'] = sto
        msg['Subject'] = subj
        msg.attach(MIMEText(message, 'html'))

        for f in files or []:
            with open(f, "rb") as fil:
                part = MIMEApplication(
                    fil.read(),
                    Name=basename(f)
                )
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
            msg.attach(part)
        self._s.sendmail(sfrom, sto, msg.as_string())
        del msg

    @classmethod
    def get_default_sender(cls):
        """возврат объекта отправителя с параметрами по умолчанию"""
        return cls(email.MAIL_SERVER, email.SMTP_PORT, email.MAIL_LOGIN, email.MAIL_PASS)


