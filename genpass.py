import random
import string
import argparse
import subprocess # PBCOPY ONLY WORKS ON MAC (PYPERCLIP TO USE ON OTHER OS)

def generate_password(length, show=False, letters=False, numbers=False, simbols=False):
  # Include all the characters for default
  if not (letters or numbers or simbols):
    characters = string.ascii_letters + string.digits + string.punctuation
  else:
    characters = ''
    if letters:
      characters += string.ascii_letters

    if numbers:
      characters += string.digits

    if simbols:
      characters += string.punctuation

  password = ''.join(random.choice(characters) for i in range(length))

  if show:
    print(password)
  else:
    print("Password generated successfully")
  
  return password

def copy_password(password):
  subprocess.run("pbcopy", text=True, input=password)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(
    prog='PasswordGenerator',
    description='Generate secure passwords with customizable character sets'
  )
  parser.add_argument('-l', '--length', type=int, default=25, help="Password length (default: 25)")
  parser.add_argument('-n', '--numbers', action="store_true",help="Include numbers in the password" )
  parser.add_argument('-s', '--simbols', action="store_true",help="Include symbols in the password" )
  parser.add_argument('-a', '--ascii', action="store_true",help="Include letters in the password" )
  parser.add_argument('-p', '--print', action="store_true", help="Print the password in the terminal")

  args = parser.parse_args()

  password = generate_password(
    length=args.length,
    letters=args.ascii,
    numbers=args.numbers,
    simbols=args.simbols,
    show=args.print
  )

copy_password(password)

# This scirpt was created by QyphX