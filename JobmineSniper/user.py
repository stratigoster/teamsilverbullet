from encrypt import *
import cPickle as pickle

class User:
  def __init__(self):
    self.username = ''
    self.password = ''
    self.email = ''

  def save(self, fileName, passkey):
    data = pickle.dumps(self)
    data = encrypt(data, passkey)
    o = open(fileName, 'w')
    o.write(data)

def loadUser(fileName, passkey):
  o = open(fileName, 'r')
  data = o.read()
  data = decrypt(data, passkey)
  return pickle.loads(data)
