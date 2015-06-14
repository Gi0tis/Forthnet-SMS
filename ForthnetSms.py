import mechanize
import cookielib
import getpass
import ssl
from ssl import PROTOCOL_SSLv23, PROTOCOL_SSLv3, CERT_NONE, SSLSocket


#SSL compatibility 
def monkey_wrap_socket(sock, keyfile=None, certfile=None,
	server_side=False, cert_reqs=CERT_NONE,
	ssl_version=PROTOCOL_SSLv23, ca_certs=None,
	do_handshake_on_connect=True,
	suppress_ragged_eofs=True, ciphers=None):
	ssl_version=ssl.PROTOCOL_TLSv1
	return SSLSocket(sock, keyfile=keyfile, certfile=certfile,
	server_side=server_side, cert_reqs=cert_reqs,
	ssl_version=ssl_version, ca_certs=ca_certs,
	do_handshake_on_connect=do_handshake_on_connect,
	suppress_ragged_eofs=suppress_ragged_eofs,
	ciphers=ciphers)

ssl.wrap_socket = monkey_wrap_socket

#User input
print "What's your email?"
username = raw_input()
print "What's your password?"
password = getpass.getpass()

#Browser
br = mechanize.Browser()
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-agent', 'Mozilla/5.0')]
r = br.open('https://www-old.forthnet.gr/secure/websms/default.aspx')

#Authentication
br.select_form(nr=0)
br.form['Username'] = username
br.form['Password'] = password
br.submit()

#SMS sending
br.select_form(nr=0)
print "Phone Number to send an sms:"
number = raw_input()
br.form['txtTo'] = number

print "SMS Text:"
message = raw_input()
br.form['txtMessage'] = message
br.submit()
print "SMS sent."

#History
smsThisMonthPage = br.open ('https://www-old.forthnet.gr/secure/websms/History.aspx')
smsHTML = smsThisMonthPage.read()
index = smsHTML.find('/ 50')
print "You have sent",smsHTML[(index-3):index],"out of 50 free SMS this month"