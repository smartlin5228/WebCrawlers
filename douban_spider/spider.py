import string
import re
import urllib2

class DouBanSpider(object):
	""" Top 100 movies from douban.com"""
	def __init__(self):
		self.page = 1
		self.cur_url = "http://movie.douban.com/top250?start={page}&filter=&type="
		self.datas = []
		self._top_num = 1
		print "Douban Spider is ready to crawl data.."

	def get_page(self, cur_page):
		""" Craw data from webpage based on the page number"""
		url = self.cur_url
		try:
			my_page = urllib2.urlopen(url.format(page = (cur_page - 1) * 25)).read().decode("utf-8")
		except urllib2.URLError, e:
			if hasattr(e, "code"):
				print "The server couldn't process the request"
				print "Error code: %s" % e.code
			elif hasattr(e, "reason"):
				print "Failed to reach server, check url again"
				print "Reason, %s" % e.reason
		return my_page
	def find_title(self, my_page):
		"""return url for the webpage"""
		temp = []
		movie_items = re.findall(r'<span.*?class="title">(.*?)</span>', my_page, re.S)
		for index, item in enumerate(movie_items):
			if item.find("&nbsp") == -1:
				temp.append("Top" + str(self._top_num) + " " + item)
				self._top_num += 1
		self.datas.extend(temp)
	def start_spider(self):
		while self.page <= 4:
			my_page = self.get_page(self.page)
			self.find_title(my_page)
			self.page += 1
def main() :
	print """
		###############################
			Simple Douban Crawler
			Version: 0.0.1
			Date: 2014-12-04
		###############################
	"""
	my_spider = DouBanSpider()
	my_spider.start_spider()
	for item in my_spider.datas :
		print item
	print "result..."

if __name__ == '__main__':
	main()