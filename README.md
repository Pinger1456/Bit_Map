# Создание README.md для проекта Bit_Map на GitHub
content = """
# Bit Map Message

## Overview
**Bit Map Message** is a Python program that displays a message using a bit map (pixel art) pattern. The program reads a multi-line string containing a bit map and overlays a message of the user's choice. Each character of the message is displayed in place of a non-empty character in the bit map, while spaces remain untouched.

This project is inspired by Al Sweigart's small Python projects, providing an easy-to-understand introduction to basic graphics and string manipulation.

## How It Works
- The program takes a multi-line string (bit map) where each `*` symbol represents a place where a character of the message should be displayed.
- The user inputs the message they want to display.
- The program loops through each character of the bit map and replaces `*` symbols with characters from the message, while spaces remain as spaces.
- The message repeats if it is shorter than the bit map.

