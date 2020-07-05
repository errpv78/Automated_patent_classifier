import requests
import bs4 as bs
import urllib.request

# url = "https://www.hbs.edu/faculty/Pages/profile.aspx?facId=6410"
# source = urllib.request.urlopen(url).read()
# soup = bs.BeautifulSoup(source, 'lxml')
#
# info = soup.find_all('div', attrs={'class':'contact-info'})
# print(info)
#
# [<div class="contact-info">
# <p><b>Unit</b>:
#                                                                         <a href="/faculty/units/strategy/Pages/default.aspx" xmlns:next="http://www.hbs.edu/">Strategy</a></p>
# <p class="sub-heading"><b>Contact:</b></p>
# <p>(617) 495-5082</p>
# <p><a href="contact.aspx?facId=6410">Send Email</a></p>
# </div>]


url = "https://www.wits.ac.za/staff/academic-a-z-listing/n/kantilalnaikwitsacza/"
source = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(source, 'lxml')

info = soup.find_all('table', attrs={'class':'profile-info'})
print(info)
