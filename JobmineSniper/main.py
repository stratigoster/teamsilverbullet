from Tkinter import *
from user import *
from scraper import *
from threading import Thread

class JobmineSniper(Frame):
    def check(self):
      i = 0
      while self.go:
        self.label.config(text = str(i))
        i += 1
        page = self.scraper.getApplicationPage()
        #newStatus = self.parser.getAppStatus(page)
        #if user.appStatus != newStatus:
        #  pass
    def startLoop(self):
      self.scraper = Scraper(self.user)
      self.thread = Thread(target=self.check)
      self.go = True
      self.thread.start()
    def stopLoop(self):
      self.go = False
      if self.thread:
        self.thread.join()
      self.label.config(text = 'stopped')
    def loginInfo(self):
      pass
    def notifyInfo(self):
      pass

    def createWidgets(self):
        self.login = Button(self)
        self.login["text"] = "Credentials..."
        self.login["command"] = self.loginInfo
        self.login.pack()

        self.notify = Button(self)
        self.notify["text"] = "Notify me..."
        self.notify["command"] = self.notifyInfo
        self.notify.pack()

        self.label = Label(self)
        self.label["text"] = "Nothing's happened"
        self.label.pack()

        self.start = Button(self)
        self.start["text"] = "Start"
        self.start["fg"] = "green"
        self.start["command"] = self.startLoop

        self.start.pack(side=LEFT, fill=X)

        self.stop = Button(self)
        self.stop["text"] = "Stop",
        self.stop["fg"] = "red"
        self.stop["command"] = self.stopLoop

        self.stop.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master, width=200, height=200)
        self.pack_propagate(0)
        self.pack()
        self.createWidgets()
        self.thread = False
        self.user = loadUser('user.txt', '1234')

root = Tk()
root.resizable(0, 0)
app = JobmineSniper(master=root)
app.mainloop()
