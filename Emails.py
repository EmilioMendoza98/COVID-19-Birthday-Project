import smtplib
import ssl
import os

#### Make sure you set environment variables for the email and password of your account and restart your computer ####


class Email:
    def __init__(self, EnvironmentVariableEmail, EnvironmentVariablePass):
        self.Email = os.environ.get(EnvironmentVariableEmail)
        self.Pass = os.environ.get(EnvironmentVariablePass)
        self.port = 465 # for ssl
        self.smtp_server = "smtp.gmail.com"
        self.message = "Subject: Covid-19 Contact Tracing\n\nYou may have been in close contact with someone who has tested positive with Covid-19\nFor More information on what to do please call your local health department immediately"
        self.context = ssl.create_default_context()

    def sendEmail(self, emails):
        for email in emails:
            with smtplib.SMTP_SSL(self.smtp_server, self.port, context=self.context) as server:
                server.login(self.Email, self.Pass)
                server.sendmail(self.Email, email, self.message)

    def getLatestMessage(self):
        pass