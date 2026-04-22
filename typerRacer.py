import flet as ft
import random
#import time

#TODO #1
#TODO: Make word color letter for letter as the user progresses the typing

#TODO #2
#TODO: Add a timer with a start button included
#TODO 2.1
#TODO: Make the start button focus on the text field once the user clicks it [DONE]

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
#TODO: Add an option to make the player choose the amount of words they want to type [DONE, 22/4/2026]

def main(page: ft.Page):

    #TODO #1
    # def checkLetter(e):
    #     for letter in word.value:
    #         pass
    #     pass

    async def focusTextField():
        await typeSpace.focus()

    async def gameSetup(e):
        typeSpace.disabled = False
        startButton.disabled = True
        mistakes.data = 0
        seenCount.data = 0
        mistakes.value = f"Mistakes: {mistakes.data} / {len(actualWords)}"
        seenCount.value = f"Words seen: {seenCount.data} / {len(actualWords)}"
        await focusTextField()
        chooseNextWord()

    def chooseNextWord():
        word.value = actualWords[seenCount.data]
    
    async def checkWord(e):
        seenCount.data+=1
        if typeSpace.value == word.value:
            resultText.value = "Correct!"
            seenCount.value = f"Words seen: {seenCount.data} / {len(actualWords)}"
            resultText.color = ft.Colors.GREEN
        else:
            mistakes.data +=1
            mistakes.value = f"Mistakes: {mistakes.data} / {len(actualWords)}"
            seenCount.value = f"Words seen: {seenCount.data} / {len(actualWords)}"
            resultText.value = "Incorrect!"
            resultText.color = ft.Colors.RED
        
        if seenCount.data >= len(actualWords):
            typeSpace.disabled = True
            finishText.value = "Finished!"
            finishText.color = ft.Colors.YELLOW_ACCENT_700
            startButton.disabled = False
        else:
            chooseNextWord()
            await focusTextField()
        accText.value = f"Accuracy: {100-((mistakes.data/len(actualWords))*100)}"
        typeSpace.value = ""

    def resizeWordList(e):
        nonlocal actualWords
        actualWords = words[:int(wordsAmount.value)]
        mistakes.value = f"Mistakes: {mistakes.data} / {len(actualWords)}"
        seenCount.value = f"Words seen: {seenCount.data} / {len(actualWords)}"

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
    actualWords = []

    pstitle = ft.Text("Python Type Master")
    typeSpace = ft.TextField(disabled=True, hint_text="Type the words as they appear", on_submit=checkWord)
    word = ft.Text()
    resultText = ft.Text()
    mistakes = ft.Text(f"Mistakes: 0 / {len(actualWords)}", data = 0)
    seenCount = ft.Text(f"Words seen: 0 / {len(actualWords)}", data = 0)
    accText = ft.Text("Accuracy: ")

    wordsAmount = ft.Dropdown(hint_text="Amount of words",
                              on_select=resizeWordList,
                              options=[
        ft.dropdown.Option(text=f"{str(int(len(words)*0.10))}"),
        ft.dropdown.Option(text=f"{str(int(len(words)*0.25))}"),
        ft.dropdown.Option(text=f"{str(int(len(words)*0.50))}"),
        ft.dropdown.Option(text=f"{str(int(len(words)*0.75))}"),
        ft.dropdown.Option(text=f"{str(int(len(words)))}")
    ])

    startButton = ft.Button(content="Start game", on_click=gameSetup)
    #resetButton = ft.ElevatedButton(text="Reset Game", on_click=gameReset)
    finishText = ft.Text()

    page.title = "Python Type Master"
    page.theme_mode = "LIGHT"

    page.window.height = 500
    page.window.width = 500

    page.add(pstitle, 
             typeSpace, 
             word, 
             mistakes,
             seenCount, 
             accText, 
             finishText, 
             resultText, 
             wordsAmount, 
             startButton)

ft.run(main=main)