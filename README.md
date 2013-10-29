# MailerSoft Transactional email API

Official Python wrapper for MailerSoft Transactional emails

## Sample usage

	#!/usr/bin/python
	# -*- coding: latin-1 -*-

	from mailersoft import MailerSoft

	mailer = MailerSoft('YOUR_MAILERSOFT_API_KEY')
	mailer.set_mail( 4015 )
	mailer.set_recipient('sample@recipient.com', 'Sample Recipient Name')
	vars = {
	    'sampleVariableName' : '1231231',
	    }
	mailer.set_variables(vars)
	res = mailer.send()
	print( res )