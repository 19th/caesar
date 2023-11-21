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

w = """
1. Encrypt text
2. Decrypt text
3. Bruteforce all rotations
Choose mode: """
mode = int(input(w))

if mode == 1:
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Encrypted: " + encrypt(text, rotation))
elif mode == 2:
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Decrypted: " + decrypt(text, rotation))
elif mode == 3:
  print("Bruteforcing...")
  print("But I don't know how to do it, sorry ¯\_(ツ)_/¯")
