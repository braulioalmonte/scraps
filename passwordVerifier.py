import flet as ft

def main(page: ft.Page):
    #functions
    conditions = {"upperCase":{"text":"Password must include at least 1 uppercase letter", 
                               "status":False},
                  "lowerCase":{"text":"Password must include at least 1 lowercase letter", 
                               "status":False},
                  "numbers":{"text":"Password must include at least 1 number", 
                               "status":False},
                  "symbols":{"text":"Password must include at least 1 special character", 
                               "status":False},
                  "evenSum":{"text":"The sum of all numbers in the password must be an even number", 
                               "status":False},
                  }
    
    def checkConditions(e):
        pass

    def updateConditions():
        pass

    #page setup
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.height = 500
    page.window.width = 500
    page.title = "Password Verifier"

    #controls
    passwordTextField = ft.TextField(hint_text="Write your password here:", on_change=checkConditions)

    page.add(passwordTextField)

ft.run(main=main)