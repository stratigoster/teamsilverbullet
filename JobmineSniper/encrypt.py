from Crypto.Cipher import Blowfish

def encrypt(text, key):
  obj = Blowfish.new(key)
  while len(text) % 8:
    text += chr(0)
  return obj.encrypt(text)

def decrypt(code, key):
  obj = Blowfish.new(key)
  text = obj.decrypt(code)
  while text[-1] == chr(0):
    text = text[:-1]
  return text
