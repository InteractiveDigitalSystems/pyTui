from typing import Text
import npyscreen

class App(npyscreen.NPSAppManaged):
    def onStart(self):
        #add forms to the application
        self.addForm('MAIN', FirstForm, name="main")
        
        
      
class FirstForm(npyscreen.ActionFormMinimal):
    def create(self):
        self.add(npyscreen.Slider, w_id="slider1", out_of=100)
    def on_ok(self, name):
        self.switchForm(name)
      
app = App()
app.run()