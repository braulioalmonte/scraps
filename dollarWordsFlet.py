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
        try:
            for letter in userWord:
                wordSum+=lettersToNumbers[letter]
        except:
            resultText.value = "No numbers or spaces allowed"
        else:
            if wordSum == 0:
                resultText.value = ""
            elif wordSum == 100:
                resultText.value = f"{userWord} is a dollar word!"
                resultText.color = ft.Colors.GREEN
            else:
                resultText.value = f"{userWord} is not a dollar word, it is worth {wordSum} cents"
                resultText.color = ft.Colors.RED

    #page setup
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.height = 500
    page.window.width = 500
    page.title = "Dollar Words Checker"


    #controls
    #!i'll finish this later
    titleText = ft.Text("Dollar Words Checker", size=30)
    wordTextField = ft.TextField(hint_text="Write your word here: ", on_change=processWord)
    resultText = ft.Text(value="", size=20)

    page.add(titleText, wordTextField, resultText)

ft.run(main=main)