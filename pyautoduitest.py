import webbrowser
import os, sys, subprocess
import pyautogui
import keyboard
taskdone = False
while taskdone != True:
    if keyboard.is_pressed('left'):
        pyautogui.write("just like a basketball player trains their muscles so they focus on the game, you can train your muscles to type without much thinking about it.") 
        taskdone = True