import urllib, urllib2, cookielib

class Scraper:
  LOGIN_PAGE = 'https://jobmine.ccol.uwaterloo.ca/servlets/iclientservlet/ES/?cmd=login'
  INTERVIEW_PAGE = 'https://jobmine.ccol.uwaterloo.ca/servlets/iclientservlet/ES/?ICType=Panel&Menu=UW_CO_STUDENTS&Market=GBL&PanelGroupName=UW_CO_STU_INTVS&RL=&target=main0&navc=3523'
  APPLICATION_PAGE = 'https://jobmine.ccol.uwaterloo.ca/servlets/iclientservlet/ES/?ICType=Panel&Menu=UW_CO_STUDENTS&Market=GBL&PanelGroupName=UW_CO_APP_SUMMARY&RL=&target=main0&navc=3523'

  def __init__(self, user):
    self.cj = cookielib.CookieJar()
    self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
    login_data = urllib.urlencode({
      'userid' : user.username,
      'pwd': user.password,
    })
    self.opener.open(self.LOGIN_PAGE, login_data)

  def getInterviewPage(self):
    resp = self.opener.open(self.INTERVIEW_PAGE)
    return resp.read()

  def getApplicationPage(self):
    resp = self.opener.open(self.APPLICATION_PAGE)
    return resp.read()
