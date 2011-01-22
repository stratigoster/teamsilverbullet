import urllib, urllib2, cookielib

username = raw_input()
password = raw_input()

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
login_data = urllib.urlencode({'userid' : username, 'pwd' : password})
opener.open('https://quest.pecs.uwaterloo.ca/psp/SS/?cmd=login', login_data)

print 'Logged in'

resp = opener.open('https://quest.pecs.uwaterloo.ca/psc/SS/ACADEMIC/HRMS/c/SA_LEARNER_SERVICES.SSR_SSENRL_LIST.GBL')

select_data = urllib.urlencode({
  'ICAction': 'DERIVED_SSS_SCT_SSR_PB_GO',
  'DERIVED_SSTSNAV_SSTS_MAIN_GOTO$24$': 9999,
  'SSR_DUMMY_RECV1$sels$0' : 0,
  'DERIVED_SSTSNAV_SSTS_MAIN_GOTO$68$': 9999,
})

print 'loaded term selection page'

resp = opener.open('https://quest.pecs.uwaterloo.ca/psc/SS/ACADEMIC/HRMS/c/SA_LEARNER_SERVICES.SSR_SSENRL_LIST.GBL', select_data)

print 'schedule open'

o = file('x.html', 'w')
o.write(resp.read())
