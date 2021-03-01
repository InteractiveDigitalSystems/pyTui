import npyscreen
from npyscreen.wgtitlefield import TitleText

class App(npyscreen.NPSAppManaged):
    def onStart(self):
        #add forms to the application
        self.addForm('MAIN', FirstForm, name="main")
        
        
      
class FirstForm(npyscreen.ActionFormMinimal):
    def create(self):
        self.add(npyscreen.TitleText, w_id="textfield", name="Enter your name:")
        self.add(npyscreen.ButtonPress, name="OK", when_pressed_function=self.btn_press)
    def btn_press(self):
        message = f'Hi {self.get_widget("textfield").value}' 
        npyscreen.notify_confirm(message, title="Hi", wrap=True, wide=True, editw=1)

    def on_ok(self):
        self.parentApp.switchForm(None)
      
app = App()
app.run()