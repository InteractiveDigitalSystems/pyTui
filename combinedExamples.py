import npyscreen

class App(npyscreen.NPSAppManaged):
    def onStart(self):
        #add forms to the application
        self.addForm('MAIN', FirstForm, name="main")
        self.addForm('SECOND', SecondForm, name="second")
        self.addForm('THIRD', ThirdForm, name="third")
    def change_form(self, name):
        self.switchForm(name)
        self.resetHistory()
      
class FirstForm(npyscreen.ActionFormMinimal):
    def create(self):
        self.add(npyscreen.TitleText, w_id="txt", name = "Text:", value= "try presseing ctrl + T" )
        self.add(Selector, id="selector", name="Select", values=['slider example', 'buttons'], relx=3)
        self.add_handlers({"^T": self.switch})
        self.add_handlers({"^W": self.pop})
        self.add_handlers({"^Q": self.die})
    def switch(self, *args, **keywords):
        self.get_widget("txt").value = "try ctrl + W :-)"
    def pop(self, *args, **keywords):
        self.get_widget("txt").value = "GREAT JOB"
    def die(self, *args, **keywords):
        npyscreen.notify_confirm("CTRL + Q exits the application!", title="CTRL + Q", wrap=True, wide=True, editw=1)
        self.parentApp.change_form(None)

class SecondForm(npyscreen.ActionFormMinimal):
    def create(self):
        self.add(npyscreen.TitleText, name = "Text:", value= "Press ^T to change screens" )
        self.add(MySlider, w_id="slider1", out_of=100)
        self.add(npyscreen.TitleText, w_id="sliderValue", name = "slide value:", value=self.get_widget("slider1").value )

    def on_ok(self):
        print(self.get_widget("slider1").value)
        self.parentApp.change_form(None)

class ThirdForm(npyscreen.ActionFormMinimal):
    def create(self):
        #self.add(npyscreen.Button, w_id="btn", name="Button Example")
        self.add(npyscreen.ButtonPress, name="Button Example", when_pressed_function=self.btn_press)
    def on_ok(self):
        self.parentApp.change_form(None)
    def btn_press(self):
        npyscreen.notify_confirm("You pressed the button :-)", title="Button Press", wrap=True, wide=True, editw=1)



class Selector(npyscreen.MultiLineAction):

    def actionHighlighted(self, act_on_this, key_press):
        print("act_on_this:")
        print( act_on_this)
        if act_on_this == 'slider example':
            self.parent.parentApp.change_form('SECOND')
        if act_on_this == 'buttons':
            self.parent.parentApp.change_form('THIRD')

class MySlider(npyscreen.TitleSlider):

    def when_value_edited(self):
        self.parent.get_widget("sliderValue").value = str(self.value)
        

app = App()
app.run()