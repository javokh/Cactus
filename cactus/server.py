import os
import sys

import SimpleHTTPServer
import SocketServer

# See: https://github.com/koenbok/Cactus/issues/8
# class Server(SocketServer.ForkingMixIn, SocketServer.TCPServer):
# 	allow_reuse_address = True

class Server(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	allow_reuse_address = True

class RequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	
	def send_error(self, code, message=None):
		
		if code == 404:
			self.path = '/error.html'
			return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
		
		return SimpleHTTPServer.SimpleHTTPRequestHandler.send_error(
			self, code, message=None)
	
	def log_message(self, format, *args):
		sys.stdout.write("%s\n" % format%args)

	def log_request(self, code='', size=''):
		try:
			self.log_message('%s %s %s', str(code), 
				self.requestline.split(' ')[0], 
				self.requestline.split(' ')[1])
		except:
			pass