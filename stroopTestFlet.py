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
    colors = [ft.Colors.RED,
              ft.Colors.BLUE,
              ft.Colors.CYAN_ACCENT,
              ft.Colors.PURPLE,
              ft.Colors.GREEN,
              ft.Colors.YELLOW,
              ft.Colors.ORANGE]
    
    colorWords = ["Red", "Blue", "Cyan", "Purple", "Green", "Yellow", "Orange"]
    indexes = []
    lives = 0
    gameRunning = False

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
        nonlocal gameRunning
        gameRunning = False
        stroopText.value = "Color"
        stroopText.color = ft.Colors.WHITE
        startButton.disabled = False

    def checkAnswer(e: ft.KeyDownEvent):
        print(e.key)
        nonlocal lives
        if gameRunning and (e.key in ["A", "D"]):
            correct = indexes[0] == indexes[1]
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
        nonlocal gameRunning
        nonlocal lives
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
        nonlocal indexes
        indexes = [random.randint(0,stroopText.data),random.randint(0,stroopText.data)]
        stroopText.color = colors[indexes[0]]
        stroopText.value = colorWords[indexes[1]]

    #Page Setup
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.height = 500
    page.window.width = 500

    #Controls
    listener = ft.KeyboardListener(content=ft.Text(),on_key_down=checkAnswer)
    stroopText = ft.Text(value="Color", size=50, data=len(colors)-1)
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