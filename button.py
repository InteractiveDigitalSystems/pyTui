import npyscreen

class App(npyscreen.NPSAppManaged):
    def onStart(self):
        #add forms to the application
        self.addForm('MAIN', FirstForm, name="main")
        
        
      
class FirstForm(npyscreen.ActionFormMinimal):
    def create(self):
        self.add(npyscreen.ButtonPress, name="Button Example", when_pressed_function=self.btn_press)
    def btn_press(self):
        npyscreen.notify_confirm("You clicked the button. that will trigger a function in the code where anything can happen", title="CLICK!!!", wrap=True, wide=True, editw=1)

    def on_ok(self):
        self.parentApp.switchForm(None)
      
app = App()
app.run()