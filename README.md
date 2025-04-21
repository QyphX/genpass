# Genpass
A simple and customizable password generator written in Python.  
Quickly create secure passwords from the command line with options for length, character types, and clipboard copy.

> ⚠️ This script uses `pbcopy` and works only on **macOS** by default.
---
## 📦 Features
- Generate strong, random passwords
- Customize with letters, numbers, and symbols
- Automatically copy to clipboard (macOS)
- Optionally display password in terminal

---
## 📥 Installation
Clone the repository:

```
$ git clone https://github.com/QyphX/genpass.git
$ cd genpass
```

Make sure you have Python installed.

---
## 🚀 Usage
Run the script from the terminal: 

```
$ python3 genpass.py [options]
```

### Options
| Flag | Description |
|------|-------------|
`-l`, `--length`| Length of the password (default: 25)
`-a`, `--ascii`| Include ASCII letters (A-Z, a-z)
`-n`, `--numbers`| Include numbers (0-9)
`-s`, `--simbols`| Include symbols `(!@#$%...)`
`-p`, `--print`| Print the generated password in the terminal

> If you don't provide any character set flags, the password will include letters, numbers and symbols by default.

---
## 🧪 Examples
Generate a 16-character password with letters and numbers:
```
$ python3 genpass.py -l 16 -a -n
```

Generate a 30-character password with all types of characters and print it:
```
$ python3 genpass.py -l 30 -a -n -s -p
```

Generate a default password (25 characters, includes everything), copied silently to clipboard:
```
$ python3 genpass.py
```

---

## ⚠️ Compatibility
This script uses the pbcopy command, which only works on macOS.
If you're using Windows or Linux, consider modifying the script to use `pyperclip`.

---
## 🛠️ Contributing
Pull requests are welcome!
For major changes, please open an issue first to discuss what you'd like to improve or modify.
