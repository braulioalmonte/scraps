#Inspired by https://cryptii.com/
import flet as ft

def main(page: ft.Page):
    #variables
    morseDict = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    ' ': ''
        }
    polarCenitDict = {"P": "C",
                      "O": "E",
                      "L": "N",
                      "A": "I",
                      "R": "T"}
    a1z26Dict = {"abcdefghijklmnopqrstuvwxyz"[i-1] : i for i in range(1,27)}

    #functions
    def processMessage(e):
        if codesDropdown.value == "Morse":
            nonlocal morseDict
            userMessage = messageTextField.value.upper()

            resultText.value = "".join(morseDict[letter]+"/" for letter in userMessage)
        elif codesDropdown.value == "A1Z26":
            pass
        
        elif codesDropdown.value == "Polar Cenit":
            pass

        elif codesDropdown.value == "Reverse":
            resultText.value = messageTextField.value[::-1]

    #page setup
    page.theme_mode = ft.ThemeMode.LIGHT

    #controls
    codesDropdown = ft.Dropdown(options=[ft.DropdownOption(text="Morse"),
                                         ft.DropdownOption(text="A1Z26"),
                                         ft.DropdownOption(text="Polar Cenit"),
                                         ft.DropdownOption(text="Reverse")])
    
    messageTextField = ft.TextField(hint_text="", on_change=processMessage)
    resultText = ft.Text("")

    page.add(codesDropdown,messageTextField, resultText)

ft.run(main=main)