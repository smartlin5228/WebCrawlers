import sys
import string
import re, random
import urllib, urllib2
import cookielib
import getpass

class Coursera(object):
	"""docstring for Coursera"""
	def __init__(self, url, user_name, password):
		self.login_url = "http://accounts.coursera.org/api/v1/login"
		self.url = url
		if user_name == "" or password == "":
			raise UserOrPwdNone("Username or password cannot be empty")
			sys.exit(2)
		else:
			self.user_name = user_name
			self.password = password
	def simulation_login(self):
		cookie = cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
		urllib2.install_opener(opener)
		form_data, request_header = self.structure_headers()
		req = urllib2.Request(self.login_url, data = form_data, headers = request_header)
		try:
			result = urllib2.urlopen(req)
		except urllib2.URLError, e:
			if hasattr(e, "code"):
				print "The server cannot process the request. Chekc your url and the error message"
				print "Error: code: %s" %e.code
			elif hasattr(e, "reason"):
				print "Failed to reach the server."
				print "Reason: %s" %e.reason
			sys.exit(2)
		if result.getcode() == 200 : 
			print "Login success."
	def structure_headers(self):
		form_data = urllib.urlencode({
			"email": self.user_name,
			"password": self.password,
			"webrequest": "true"
			})
		user_agent = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) "
			"AppleWebKit/537.36 (KHTML, like Gecko) "
			"Chrome/38.0.2125.111 Safari/537.36")
		XCSRF2Cookie = 'csrf2_token_%s' % ''.join(self.random_string(8))
		XCSRF2Token = ''.join(self.random_string(24))
		XCSRFToken = ''.join(self.random_string(24))
		cookie = "csrftoken=%s; %s=%s" % (XCSRFToken, XCSRF2Cookie, XCSRF2Token)
		request_header = {
			"Referer": "https://accounts.coursera.org/signin",
			"User-Agent": user_agent,
			"X-Requested-With": "XMLHttpRequest",
			"X-CSRF2-Cookie": XCSRF2Cookie,
			"X-CSRF2-Token": XCSRF2Token,
			"X-CSRFToken": XCSRFToken,
			"Cookie": cookie
		}
		return form_data, request_header
	def random_string(self, length):
		return ''.join(random.choice(string.letters + string.digits) for i in xrange(length))
	def get_links(self):
		try:
			result = urllib2.urlopen(self.url)
		except urllib2.URLError, e:
			if hasattrO(e, "code"):
				print "The server cannot process the request. Chekc your url and the error message"
				print "Error: code: %s" %e.code
			elif hasattr(e, "reason"):
				print "Failed to reach the server."
				print "Reason: %s" %e.reason
			sys.exit(2)
		content = result.read().decode("utf-8")
		print "Crawling success"
		down_links = re.findall(r'<a.*?href="(.*?mp4.*?)"', content)
		down_pdfs = re.findall(r'<a.*?href="(.*?pdf.*?)"', content)
		print "Matching results:"
		return down_links, down_pdfs
	def start_spider(self):
		self.simulation_login()
		down_links,down_pdfs = self.get_links()
		with open("coursera.html", "w+") as my_file:
			print "Length of the link", len(down_links)
			for link in down_links:
				print link
				try:
					my_file.write(link + "\n")
				except UnicodeError:
					sys.exit(2)
		with open("coursera.pdf", "w+") as my_file:
			print "Length of pdfs", len(down_pdfs)
			for pdf in down_pdfs:
				try:
					my_file.write(pdf + "\n")
				except UnicodeError:
					sys.exit(2)
		print "Coursera courses downloaded successfully"
class UserOrPwdNone(BaseException):
	"""docstring for UserOrPwdNone"BaseExceptionf __init__(self, arg):
		super(UserOrPwdNone,BaseException.__init__()
		self.arg = arg
	"""
def main():
	if len(sys.argv) != 2:
		print "Input which course you want to download"
		sys.exit(2)
	url = "http://class.coursera.org/{course}/lecture"
	user_name = raw_input("Email: >")
	password = getpass.getpass("Password: >")
	spider = Coursera(url.format(course = sys.argv[1]), user_name, password)
	spider.start_spider()
if __name__ == '__main__':
	main()