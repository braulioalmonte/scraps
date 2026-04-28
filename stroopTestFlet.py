#Inspired by the game OLDTV and by the actual stroop test.
import asyncio
import flet as ft
import random
class Countdown(ft.Text):
    def __init__(self, seconds):
        super().__init__()
        self.seconds = seconds

    def did_mount(self):
        self.running = True
        self.page.run_task(self.update_timer)

    def will_unmount(self):
        self.running = False

    async def update_timer(self):
        while self.seconds and self.running:
            mins, secs = divmod(self.seconds, 60)
            self.value = "{:02d}:{:02d}".format(mins, secs)
            self.update()
            await asyncio.sleep(1)
            self.seconds -= 1

def main(page: ft.Page):
    #Variables
    combinations = {
    0: [
        (ft.Colors.RED, "Red"),
        (ft.Colors.BLUE, "Blue"),
        (ft.Colors.CYAN_ACCENT, "Cyan"),
        (ft.Colors.PURPLE, "Purple"),
        (ft.Colors.GREEN, "Green"),
        (ft.Colors.YELLOW, "Yellow"),
        (ft.Colors.ORANGE, "Orange"),
    ],
    1: [
        (ft.Colors.RED, "Blue"),
        (ft.Colors.RED, "Cyan"),
        (ft.Colors.RED, "Purple"),
        (ft.Colors.RED, "Green"),
        (ft.Colors.RED, "Yellow"),
        (ft.Colors.RED, "Orange"),
        (ft.Colors.BLUE, "Red"),
        (ft.Colors.BLUE, "Cyan"),
        (ft.Colors.BLUE, "Purple"),
        (ft.Colors.BLUE, "Green"),
        (ft.Colors.BLUE, "Yellow"),
        (ft.Colors.BLUE, "Orange"),
        (ft.Colors.CYAN_ACCENT, "Red"),
        (ft.Colors.CYAN_ACCENT, "Blue"),
        (ft.Colors.CYAN_ACCENT, "Purple"),
        (ft.Colors.CYAN_ACCENT, "Green"),
        (ft.Colors.CYAN_ACCENT, "Yellow"),
        (ft.Colors.CYAN_ACCENT, "Orange"),
        (ft.Colors.PURPLE, "Red"),
        (ft.Colors.PURPLE, "Blue"),
        (ft.Colors.PURPLE, "Cyan"),
        (ft.Colors.PURPLE, "Green"),
        (ft.Colors.PURPLE, "Yellow"),
        (ft.Colors.PURPLE, "Orange"),
        (ft.Colors.GREEN, "Red"),
        (ft.Colors.GREEN, "Blue"),
        (ft.Colors.GREEN, "Cyan"),
        (ft.Colors.GREEN, "Purple"),
        (ft.Colors.GREEN, "Yellow"),
        (ft.Colors.GREEN, "Orange"),
        (ft.Colors.YELLOW, "Red"),
        (ft.Colors.YELLOW, "Blue"),
        (ft.Colors.YELLOW, "Cyan"),
        (ft.Colors.YELLOW, "Purple"),
        (ft.Colors.YELLOW, "Green"),
        (ft.Colors.YELLOW, "Orange"),
        (ft.Colors.ORANGE, "Red"),
        (ft.Colors.ORANGE, "Blue"),
        (ft.Colors.ORANGE, "Cyan"),
        (ft.Colors.ORANGE, "Purple"),
        (ft.Colors.ORANGE, "Green"),
        (ft.Colors.ORANGE, "Yellow"),
    ]
        }
    lives = 0
    gameRunning = False
    color = ""
    word = ""
    #Functions
    def addSeconds():
        countDownText.seconds += 1
    
    def substractSeconds():
        countDownText.seconds -= 5
    
    def substractLife():
        nonlocal lives
        lives+=1
        if lives <= 3:
            livesRow.controls[lives-1].icon = ft.Icons.HEART_BROKEN
            livesRow.controls[lives-1].color = ft.Colors.RED

    def gameOver():
        nonlocal gameRunning, color, word
        color = ""
        word = ""
        gameRunning = False
        stroopText.value = "Color"
        stroopText.color = ft.Colors.WHITE
        startButton.disabled = False

    def checkAnswer(e: ft.KeyDownEvent):
        nonlocal lives, color, word
        if gameRunning and (e.key in ["A", "D"]):
            correct = color == word.lower() #lower here because color constants on flet are written in lowercase
            if (e.key == "A" and correct) or (e.key == "D" and not correct):
                feedbackText.value = "Correct!"
                correctText.data+=1
                correctText.value = f"Correct: {correctText.data}"
                addSeconds()
            else:
                incorrectText.data +=1
                incorrectText.value = f"Incorrect: {incorrectText.data}"
                feedbackText.value = "Incorrect!"
                substractSeconds()
                substractLife()
        if lives < 3:
            nextColor()
        elif lives >= 3:
            gameOver()

    async def startGame(e):
        nonlocal gameRunning, lives
        await listener.focus()
        lives = 0
        gameRunning = True
        startButton.disabled = True
        livesRow.controls = [ft.Icon(icon=ft.Icons.FAVORITE) for i in range(3)]
        correctText.data = incorrectText.data = 0
        correctText.value = f"Correct: {correctText.data}"
        incorrectText.value = f"Incorrect: {incorrectText.data}"
        nextColor()

    def nextColor():
        nonlocal color, word
        color, word = random.choice(random.choice(combinations))
        stroopText.color = color
        stroopText.value = word

    #Page Setup
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.height = 500
    page.window.width = 500
    page.title = "Stroop Test Minigame"

    #Controls
    listener = ft.KeyboardListener(content=ft.Text(),on_key_down=checkAnswer)
    stroopText = ft.Text(value="Color", size=50, data=len(combinations[0])-1)
    feedbackText = ft.Text(value="")
    correctText = ft.Text(value="Correct: 0", data = 0)
    incorrectText = ft.Text(value="Incorrect: 0", data = 0)

    countDownText =  Countdown(120)
    startButton = ft.Button("Start Game", on_click=startGame)

    timerRow = ft.Row(controls=[countDownText, feedbackText], alignment=ft.MainAxisAlignment.CENTER)
    livesRow = ft.Row(controls=[ft.Icon(icon=ft.Icons.FAVORITE) for i in range(3)], alignment=ft.MainAxisAlignment.CENTER)

    instructionText = ft.Text(value="Press Left for correct\nPress Right for incorrect", size=20)
    mainColumn = ft.Column(controls=[stroopText,
                                     livesRow, 
                                     ft.Row(controls=[correctText, 
                                                      startButton, 
                                                      incorrectText],
                                            alignment=ft.MainAxisAlignment.CENTER), 
                                     instructionText], 
                           alignment=ft.MainAxisAlignment.START, 
                           horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    page.add(timerRow, mainColumn, listener)

ft.run(main=main)