import urllib, urllib2, cookielib

username = raw_input('Username:')
password = raw_input('Password:')

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
login_data = urllib.urlencode({'userid' : username, 'pwd' : password})
opener.open('https://quest.pecs.uwaterloo.ca/psp/SS/?cmd=login', login_data)
select_data = urllib.urlencode({'SSR_DUMMY_RECV1$sels$0' : 1})
resp = opener.open('https://quest.pecs.uwaterloo.ca/psc/SS/ACADEMIC/HRMS/c/SA_LEARNER_SERVICES.SSR_SSENRL_LIST.GBL', select_data)

o = file('x.html', 'w')
o.write(resp.read())
