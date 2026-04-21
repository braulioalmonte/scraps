import flet as ft
import random
#import time

#TODO #1
#TODO: Make word color letter for letter as the user progresses the typing

#TODO #2
#TODO: Add a timer with a start button included
#TODO 2.1
#TODO: Make the start button focus on the text field once the user clicks it

#TODO #3
#TODO: Add different modes 
#TODO: Survival [add seconds to a timer to survive, make the words longer as the player progresses, when the player loses, display the amount of words written]
#TODO: Time Trial [type x amount of words and measure the time and stop once the amount of max words and tries is the same]

#TODO: #4
#TODO: Fix mistakes and tries count [DONE] 10/16/2024, Solution: Using data property of both objects
#TODO: as a middle man variable to pass around and make the count

#TODO #5
#TODO: Add a percentage of accuracy that updates in real time [DONE]

#TODO #6
#TODO: Add an option to make the player choose the amount of words they want to type [WIP, 25/10/2024]

def main(page: ft.Page):

    #TODO #1
    # def checkLetter(e):
    #     for letter in word.value:
    #         pass
    #     pass

    def gameSetup(e):
        typeSpace.disabled = False
        startButton.disabled = True
        typeSpace.focus()
        page.update()

    def chooseNextWord():
        word.value = words[seenCount.data]
        page.update()
    
    def checkWord(e):
        seenCount.data+=1
        if typeSpace.value == word.value:
            resultText.value = "Correct!"
            seenCount.value = f"Words seen: {seenCount.data} / {len(words)}"
            resultText.color = ft.Colors.GREEN
        else:
            mistakes.data +=1
            mistakes.value = f"Mistakes: {mistakes.data} / {len(words)}"
            seenCount.value = f"Words seen: {seenCount.data} / {len(words)}"
            resultText.value = "Incorrect!"
            resultText.color = ft.Colors.RED
        
        if seenCount.data >= len(words):
            typeSpace.disabled = True
            finishText.value = "Finished!"
            finishText.color = ft.Colors.YELLOW_ACCENT_700
            startButton.disabled = False
        else:
            chooseNextWord()
            typeSpace.focus()
        accText.value = f"Accuracy: {100-((mistakes.data/len(words))*100)}"
        typeSpace.value = ""
        page.update()

    words = ['write', 'carro', 'mesa', 'black', 'beach', 
            'marco', 'punto', 'corto', 'raton', 'feliz', 
            'puente', 'blanco', 'plant', 'world', 'luz', 
            'bread', 'negro', 'silla', 'sweet', 'white', 
            'nieve', 'dulce', 'stone', 'apple', 'libro', 
            'paz', 'earth', 'gente', 'sunny', 'dance', 'table', 
            'rojo', 'teach', 'dream', 'fruta', 'pizza', 'space', 
            'house', 'laugh', 'young', 'baker', 'cloud', 'mundo', 
            'jelly', 'grito', 'carry', 'smile', 'book', 'brave', 'banco']

    random.shuffle(words)

    pstitle = ft.Text("Python Type Master")
    typeSpace = ft.TextField(disabled=True,hint_text="Type the words as they appear", on_submit=checkWord)
    word = ft.Text()
    resultText = ft.Text()
    mistakes = ft.Text(f"Mistakes: 0 / {len(words)}", data = 0)
    seenCount = ft.Text(f"Words seen: 0 / {len(words)}", data = 0)
    accText = ft.Text("Accuracy: ")

    wordsAmount = ft.Dropdown(hint_text="Amount of words",options=[
        ft.dropdown.Option(text=f"{str(int(len(words)*0.10))}"),
        ft.dropdown.Option(text=f"{str(int(len(words)*0.25))}"),
        ft.dropdown.Option(text=f"{str(int(len(words)*0.50))}"),
        ft.dropdown.Option(text=f"{str(int(len(words)*0.75))}"),
        ft.dropdown.Option(text=f"{str(int(len(words)))}"),
    ])

    startButton = ft.ElevatedButton(text="Start game", on_click=gameSetup)
    #resetButton = ft.ElevatedButton(text="Reset Game", on_click=gameReset)
    finishText = ft.Text()

    page.title = "Python Type Master"
    page.theme_mode = "LIGHT"

    page.window.height = 500
    page.window.width = 500

    chooseNextWord()
    page.add(pstitle, typeSpace, word, mistakes, seenCount, accText, finishText, resultText, wordsAmount, startButton)

ft.app(target=main)