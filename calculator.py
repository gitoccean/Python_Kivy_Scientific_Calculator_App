
"""
Created on Sun Oct 22 19:26:06 2023
A VERSATILE SCIENTIFIC CALCULATOR-APP
@author: Ali Hassan
mailto:garrison1855@gmail.com
https://github.com/gitoccean
"""
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

import math


# Window.size = (450,600)

Builder.load_file('calculator.kv')


# To extract a Subtext
def sub(tex, flag):
    b_point = tex.find(flag)
    # print(f'Found {flag} at: {b_point}')
    brackets = 0
    for i in range(b_point + len(flag)-1, len(tex)):
        if tex[i] == '(':
            brackets += 1
            print(f'Brackets at {str(brackets)}')
        if tex[i] == ')':
            brackets = brackets - 1
            print(f'Brackets at {str(brackets)}')
        if brackets == 0:
            e_point = i
            break
    print(f'Endpoint = {tex[e_point]}')
    subtex = tex[b_point + len(flag):e_point]
    return subtex


# THIS IS WHERE THE MAGIC HAPPENS:
def calculate(tex):
    global calcflag
    flags = ["ln(", "sin(", "cos(", "tan("]
    for flag in flags:
        # print(f'Searching for {flag}')
        if flag in tex:
            # print(f'found {flag}')
            subtex = sub(tex, flag)
            # print(f'Subtext is {subtex}')
            calcsub = calculate(subtex)
            if flag == "ln(":
                calcflag = str(math.log(float(calcsub)))
            if flag == "sin(":
                calcflag = str(math.sin(float(calcsub)))
            if flag == "cos(":
                calcflag = str(math.cos(float(calcsub)))
            if flag == "tan(":
                calcflag = str(math.tan(float(calcsub)))
            # print(f'Calc ln  = {ln}')
            tex = tex.replace(f'{flag}{subtex})', calcflag)
            # print(tex)
    try:
        sol = str(eval(tex))
        return sol
    except:
        return "ERROR"


class TheGrid(Widget):

    def testpress(self):
        data = self.input.text
        print(f'Works! {data}')

    def clear(self):
        self.ids.input.text = "0"

    def act(self, action):
        tex_old = self.ids.input.text
        if tex_old == "0" or "ERROR" in tex_old:
            tex_old = ""
            self.ids.input.text = f'{action}'
        else:
            self.ids.input.text = f'{tex_old}{action}'

    def dot(self):
        # print("GO")
        tex_old = self.ids.input.text
        if tex_old[len(tex_old) - 1].isdecimal():
            # print(tex_old[len(tex_old)-1])
            if len(tex_old) == 1:
                self.ids.input.text = f'{tex_old}.'
            for i in range(len(tex_old) - 1, -1, -1):
                # print("GO LOOP")
                # print(f'The I is {str(i)}')
                # print(tex_old[i])
                if i == 0:
                    # print("IS LAST")
                    self.ids.input.text = f'{tex_old}.'
                    break
                if (tex_old[i].isdecimal() == False) and (tex_old[i] != "."):
                    # print("Found OTHER")
                    self.ids.input.text = f'{tex_old}.'
                    break
                if tex_old[i] == ".":
                    # print("Found Dot")
                    break
        else:
            pass

    def remove(self):
        tex_old = self.ids.input.text
        tex_old = tex_old[:-1]
        self.ids.input.text = tex_old

    def equals(self):
        tex = self.ids.input.text
        sol = calculate(tex)
        self.ids.input.text = sol


class Scientific_Calculator_Ali_Hassan(App):
    def build(self):
        return TheGrid()


if __name__ == "__main__":
    app = Scientific_Calculator_Ali_Hassan()
    app.run()
