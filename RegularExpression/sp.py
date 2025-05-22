# -*- coding: utf-8 -*-
import re

text = "Hello world! User123 at 10:30AM on 2024-05-22.\nContact: user_01@example.com\tWebsite: https://example.com"

print("Original text:\n", text)
print("\n--- Special Sequences Demonstration ---\n")

# \d — Digits
print(r"\d  ->", re.findall(r"\d", text))

# \D — Non-digits
print(r"\D  ->", re.findall(r"\D", "123 abc"))

# \w — Word characters (letters, digits, underscore)
print(r"\w  ->", re.findall(r"\w", text))

# \W — Non-word characters (spaces, punctuation, etc.)
print(r"\W  ->", re.findall(r"\W", text))

# \s — Whitespace (spaces, tabs, newlines)
print(r"\s  ->", re.findall(r"\s", text))

# \S — Non-whitespace
print(r"\S  ->", re.findall(r"\S", "a b\tc"))

# \A — Beginning of string
print(r"\A  ->", re.findall(r"\AHello", text))

# \Z — End of string
print(r"\Z  ->", re.findall(r"com\Z", text))

# \b — Word boundary
print(r"\b  ->", re.findall(r"\bUser", text))

# \B — Not a word boundary
print(r"\B  ->", re.findall(r"\B123", text))

print("\n--- Done ---")
