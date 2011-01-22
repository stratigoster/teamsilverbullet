from encrypt import *

class User:
  def __init__(self, passkey=''):
    self.passkey = passkey
    self.username = ''
    self.password = ''

  def load(self, fileName):
    o = open(fileName, 'r')
    self.username = decrypt(o.readline()[:-1], self.passkey)
    self.password = decrypt(o.readline()[:-1], self.passkey)
  
  def save(self, fileName):
    o = open(fileName, 'w')
    o.write(
        encrypt(self.username, self.passkey) + '\n' +
        encrypt(self.password, self.passkey) + '\n'
    )
