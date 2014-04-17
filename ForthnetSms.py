import mechanize
import cookielib
import getpass

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
br.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:28.0) Gecko/20100101 Firefox/28.0')]
r = br.open('https://www-old.forthnet.gr/secure/webSMS/login.aspx?ReturnUrl=%2fsecure%2fwebsms%2fdefault.aspx&xss_mode=l')


#Authentication
br.select_form(nr=0)
br.form['Username'] = username
br.form['Password'] = password
br.submit()

#SMS sending
br.select_form(nr=0)

print "Phone Number:"
number = raw_input()
br.form['txtTo'] = number

print "Sms Text:"
message = raw_input()
br.form['txtMessage'] = message

br.submit()

