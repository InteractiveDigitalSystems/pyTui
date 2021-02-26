import npyscreen

class App(npyscreen.NPSAppManaged):
    def onStart(self):
        #add forms to the application
        self.addForm('MAIN', FirstForm, name="main")
        self.addForm('SECOND', SecondForm, name="second")
    def change_form(self, name):
        self.switchForm(name)
        self.resetHistory()
      
class FirstForm(npyscreen.ActionFormMinimal):
    def create(self):
        self.add(npyscreen.TitleText, name = "Text:", value= "Press ^T to change screen" )
        self.add(Selector, id="selector", name="Select", values=['first', 'second'], relx=3)
        self.add_handlers({"^T": self.switch})

    def switch(self, *args, **keywords):
        self.parentApp.change_form(None)

class SecondForm(npyscreen.ActionFormMinimal):
    def create(self):
        self.add(npyscreen.TitleText, name = "Text:", value= "Press ^T to change screens" )
    
    def on_ok(self):
        self.parentApp.change_form(None)

class Selector(npyscreen.MultiLineAction):

    def actionHighlighted(self, act_on_this, key_press):
        self.parent.parentApp.change_form('SECOND')


app = App()
app.run()