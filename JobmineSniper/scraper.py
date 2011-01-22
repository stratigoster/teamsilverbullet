import urllib, urllib2, cookielib

username = raw_input()
password = raw_input()

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
login_data = urllib.urlencode({'userid' : username, 'pwd' : password})
opener.open('https://jobmine.ccol.uwaterloo.ca/servlets/iclientservlet/ES/?cmd=login', login_data)

print 'Logged in'

resp = opener.open('https://jobmine.ccol.uwaterloo.ca/servlets/iclientservlet/ES/?ICType=Panel&Menu=UW_CO_STUDENTS&Market=GBL&PanelGroupName=UW_CO_APP_SUMMARY&RL=&target=main0&navc=3523')

o = file('x.html', 'w')
o.write(resp.read())
