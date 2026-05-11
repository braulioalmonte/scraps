import flet as ft
import random

def main(page: ft.Page):
    def rotateText(e):
        testText.rotate = ft.Rotate(angle=random.randint(1,360))
        print(testText.rotate.angle)
    testText = ft.Text("⏩", size=100, animate_rotation=ft.Animation(duration=ft.Duration(seconds=10), 
                                                                    curve=ft.AnimationCurve.EASE_OUT_EXPO))
    rotateButton = ft.Button("Spin the wheel!", on_click=rotateText)
    
    page.add(testText,rotateButton)

ft.run(main=main)