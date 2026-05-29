def ascii_to_char(ascii_code):
    return chr(ascii_code)

def char_to_ascii(char):
    return ord(char)

def main():
    ascii_code = int(input("ASCII kodi kiriting: "))
    char = ascii_to_char(ascii_code)
    print(f"Harf: {char}")
    print(f"ASCII kodi: {char_to_ascii(char)}")

if __name__ == "__main__":
    main()
```

```python
def ascii_to_char(ascii_code):
    return chr(ascii_code)

def char_to_ascii(char):
    return ord(char)

def main():
    char = input("Harf kiriting: ")
    ascii_code = char_to_ascii(char)
    print(f"Harf: {char}")
    print(f"ASCII kodi: {ascii_code}")

if __name__ == "__main__":
    main()
