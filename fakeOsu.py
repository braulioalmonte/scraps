import flet as ft
import random

def main(page: ft.Page):

    #functions
    def makeJump(e):
        jumpingButton.top = random.randint(0,400)
        jumpingButton.left = random.randint(0,400)
        nextJumpingButton.disabled = False
        jumpingButton.disabled = True
        jumpingButton.bgcolor = ft.Colors.GREY
        nextJumpingButton.bgcolor = ft.Colors.YELLOW_100

        jumpingButton.data+=1
        changeBgColor(jumpingButton.data)
        countPoints()

    def makeNextJump(e):
        nextJumpingButton.top = random.randint(0,400)
        nextJumpingButton.left = random.randint(0,400)
        jumpingButton.disabled = False
        nextJumpingButton.disabled = True
        nextJumpingButton.bgcolor = ft.Colors.GREY
        jumpingButton.bgcolor = ft.Colors.BLUE_100

        nextJumpingButton.data+=1
        changeBgColor(nextJumpingButton.data)
        countPoints()

    def countPoints():
        pointsText.data+=1
        pointsText.value = f"Points: {pointsText.data}"

    def changeBgColor(jumps):
        colorsList = [ft.Colors.PURPLE_100, 
                      ft.Colors.RED_100, 
                      ft.Colors.GREEN_100, 
                      ft.Colors.ORANGE_100]
        
        areaContainer.bgcolor = colorsList[jumps%4]

    def countMiss(e):
        missesText.data +=1
        missesText.value = f"Misses: {missesText.data}"

    #page setup
    page.window.resizable = False
    page.window.maximizable = False
    page.window.width = 510
    page.window.height = 650

    #controls
    areaContainer = ft.Container(height=500, width=500, bgcolor=ft.Colors.PURPLE_100, on_click=countMiss)
    jumpingButton = ft.Button(data=0, width=100, height=100, content="1", top=0, left=0, on_click=makeJump, bgcolor=ft.Colors.BLUE_100, color=ft.Colors.BLACK)
    nextJumpingButton = ft.Button(disabled=True, data=2, width=100, height=100, content="2", top=250, left=250, on_click=makeNextJump, bgcolor=ft.Colors.GREY, color=ft.Colors.BLACK)
    pointsText = ft.Text(value="Points: 0", data=0)
    missesText = ft.Text(value="Misses: 0", data=0)
    areaStack = ft.Stack(height=500, width=500,controls=[areaContainer,nextJumpingButton, jumpingButton])
    
    page.add(areaStack, pointsText, missesText)

ft.run(main=main)