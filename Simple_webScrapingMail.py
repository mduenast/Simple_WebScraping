import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import mail_settings
from Simple_webScraping import Simple_WebScraping

class Simple_webScrapingMail(object):
    def __init__(self):
        self.fromaddr = mail_settings.fromaddr
        self.password = mail_settings.password
        self.toaddr = mail_settings.toaddr
        self.smtp_server = mail_settings.smtp_server
        self.smtp_port = mail_settings.smtp_port

    def send_notification(self,body_message,mime_type,subject):
        """
        Send notification about the book of the day
        :param body_message:
        :param mime_type:
        :param subject:
        :return:
        """
        msg = MIMEMultipart()
        msg['From'] = self.fromaddr
        msg['To'] = self.toaddr
        msg['Subject'] = subject

        body = body_message
        msg.attach(MIMEText(body, mime_type))

        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.starttls()
        server.login(self.fromaddr, self.password)
        text = msg.as_string()
        server.sendmail(self.fromaddr, self.toaddr, text)
        server.quit()

if __name__ == "__main__":
    simple_webscraping = Simple_WebScraping("https://www.packtpub.com/packt/offers/free-learning")
    simple_webscraping.main()

    simple_web_scraping_mail = Simple_webScrapingMail()
    simple_web_scraping_mail.send_notification(simple_webscraping.main(),"plain","free book of the day")