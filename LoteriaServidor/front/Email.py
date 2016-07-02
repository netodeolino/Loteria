# -*- coding: utf-8 -*-
import smtplib
 
# Credenciais
remetente    = 'EMAIL'
senha        = 'SENHA'

class Email(object):
	def __init__(self, destinatario, assunto, texto):
		self.destinatario = destinatario
		self.assunto = assunto
		self.texto = texto

	def enviar(self):
		msg = '\r\n'.join([
			'From: %s' % remetente,
			'To: %s' % self.destinatario,
			'Subject: %s' % self.assunto,
			'',
			'%s' % self.texto
			])

		server = smtplib.SMTP('smtp.gmail.com:587')
		server.starttls()
		server.login(remetente, senha)
		server.sendmail(remetente, self.destinatario, msg)
		server.quit()
