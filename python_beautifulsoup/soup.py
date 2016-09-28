import re
from bs4 import BeautifulSoup

html_atag = """<html><body><p>Test html a tag example</p>
<a href="http://www. allitebook.com">Home</a>
<a href="http://www.allitebook.com/books">Books</a>
</body>
</html>"""

html_markup = """<div>
<ul id="students">
<li class="student">
<div class="name">Carl</div>
<div class="age">32</div>
</li>
<li class="student">
<div class="name">Lucy</div>
<div class="age">25</div>
</li>
</ul>
</div>"""

email_id_example = """<div>The below HTML has the information that has email ids.</div>
withoutdivemail@example.com
<div>divemail@example.com</div>
<span>spanemail@example.com</span>"""

#soup = BeautifulSoup(html_atag, "lxml")
#print(soup.a)

#soup = BeautifulSoup(html_markup, "lxml")
#student_entries = soup.find("ul")
#print(student_entries.li.div.string)

#soup = BeautifulSoup(email_id_example, "lxml")
#emailid_regexp = re.compile("\w+@\w+\.\w+")
#first_email_id = soup.find(text=emailid_regexp)
#all_email_id = soup.find_all(text=emailid_regexp)
#print(first_email_id)
#print(all_email_id)

