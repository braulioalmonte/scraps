#Inspired by the "Because of Mr. Terupt" book
import flet as ft

def main(page: ft.Page):
    #variables
    lettersToNumbers = {"abcdefghijklmnopqrstuvwxyz"[i-1] : i for i in range(1,27)}
    #functions
    def processWord(e):
        nonlocal lettersToNumbers
        wordSum = 0
        userWord = wordTextField.value.lower()
        for letter in userWord:
            wordSum+=lettersToNumbers[letter]
        if wordSum == 100:
            resultText.value = f"{userWord} is a dollar word!"
            resultText.color = ft.Colors.GREEN
        else:
            resultText.value = f"{userWord} is not a dollar word, it is worth {wordSum} cents"
            resultText.color = ft.Colors.RED

    #page setup
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    #controls
    #!i'll finish this later
    wordTextField = ft.TextField(hint_text="Write your word here: ", on_change=processWord)
    resultText = ft.Text(value="", size=20)

    page.add(wordTextField, resultText)

ft.run(main=main)