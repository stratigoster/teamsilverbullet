import urllib, urllib2, cookielib

username = raw_input()
password = raw_input()
class_number = raw_input()

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
login_data = urllib.urlencode({'userid' : username, 'pwd' : password})
opener.open('https://quest.pecs.uwaterloo.ca/psp/SS/?cmd=login', login_data)

print 'Logged in'
resp = opener.open('https://quest.pecs.uwaterloo.ca/psc/SS/ACADEMIC/SA/c/SA_LEARNER_SERVICES.UW_SSR_CLASS_SRCH.GBL')

print 'search page'

select_data = urllib.urlencode({
  'ICAction': 'UW_DERIVED_SR_SSR_PB_CLASS_SRCH',
  'CLASS_SRCH_WRK2_INSTITUTION$46$': 'UWATR',
  'CLASS_SRCH_WRK2_STRM$49$': 1111,
  'CLASS_SRCH_WRK2_SSR_OPEN_ONLY$chk': 'N',
  'CLASS_SRCH_WRK2_CLASS_NBR$109$': class_number,
  'DERIVED_SSTSNAV_SSTS_MAIN_GOTO$143$': 9999,
})

resp = opener.open('https://quest.pecs.uwaterloo.ca/psc/SS/ACADEMIC/SA/c/SA_LEARNER_SERVICES.UW_SSR_CLASS_SRCH.GBL', select_data)

print 'searched'

select_data = urllib.urlencode({
  'ICAction': 'UW_DERIVED_SR_SSR_CLASSNAME_LONG$0',
})

resp = opener.open('https://quest.pecs.uwaterloo.ca/psc/SS/ACADEMIC/SA/c/SA_LEARNER_SERVICES.UW_SSR_CLASS_SRCH.GBL', select_data)

print 'result'

o = file('x.html', 'w')
o.write(resp.read())
