


# MailerSoft Transactional email API

Official Python wrapper for MailerSoft Transactional emails

## Sample usage

	#!/usr/bin/python
	# -*- coding: latin-1 -*-

	from mailerloop import MailerLoop

	mailer = MailerLoop('120d2e6c9d130e82bcf5567b5b527680')
	mailer.set_mail( 4015 )
	mailer.set_recipient('tomas@talandis.lt', 'Tomas Talandis')
	vars = {
	    'banner' : 'BanerisCia',
	    'clientFullName' : 'KlientasKlientauskas',
	    'piguAddress' : 'http://www.pigu.lt/',
	    'orderId' : '1231231',
	    'questionnaireHash' : 'asdasdasd'
	    }
	mailer.set_variables(vars)
	res = mailer.send()
	print( res )