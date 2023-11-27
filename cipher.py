ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(text, offset):
  result = ""
  for character in text:
    if (ALPHABET.find(character) == -1):
      result += character
    else:
      result += (ALPHABET[(ALPHABET.find(character) + offset) % len(ALPHABET)])
  return result

def decrypt(text, offset):
  result = ""
  for character in text:
    if (ALPHABET.find(character) == -1):
      result += character
    else:
      result += (ALPHABET[(ALPHABET.find(character) - offset) % len(ALPHABET)])
  return result