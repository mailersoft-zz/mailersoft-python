import urllib, urllib2, json

class MailerSoft:
    MAILER_SERVER_URI = 'https://api.mailersoft.com/api/v1/messages/'
    api_key = ''
    from_name = ''
    from_email = ''
    variables = dict()
    mail_id = 0
    recipient_email = ''
    recipient_name = ''
    type = ''
    language = ''

    def __init__(self, apiKey):
        self.set_api_key(apiKey)

    def set_recipient(self, email, name=None):
        self.recipient_email = email
        if name:
            self.recipient_name = name
        return self

    def set_api_key(self, api_key):
        self.api_key = api_key
        return self

    def set_from_name(self, name):
        self.from_name = name
        return self

    def set_from_email(self, email):
        self.from_email = email
        return self

    def set_variables(self, variables):
        if isinstance(variables, dict):
            for name, value in variables.items():
                self.set_variable(name, value)
        return self

    def set_variable(self, name, value):
        self.variables[name] = value
        return self

    def set_mail(self, id):
        self.mail_id = id
        return self

    def set_type(self, type):
        self.type = type
        return self

    def set_language(self, code):
        self.language = code
        return self

    def send(self):
        data = {
            'fromName': self.from_name,
            'fromEmail': self.from_email,
            'recipientName': self.recipient_name,
            'recipientEmail': self.recipient_email,
            'apiKey': self.api_key,
            'type': self.type,
            'variables': self.variables,
            'mailId': self.mail_id,
            'language': self.language
        }
        return urllib2.urlopen(self.MAILER_SERVER_URI, data=urllib.urlencode(data)).read()