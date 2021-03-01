import npyscreen

class App(npyscreen.NPSAppManaged):
    def onStart(self):
        #add forms to the application
        self.addForm('MAIN', FirstForm, name="main")
        self.addForm('SECOND', SecondForm, name="second")
       
   
class FirstForm(npyscreen.ActionFormMinimal):
    def create(self):
        self.add(npyscreen.TitleText, w_id="txt", name = "This is the first Form!")
    def on_ok(self):        
        self.parentApp.switchForm('SECOND')


class SecondForm(npyscreen.ActionFormMinimal):
    def create(self):
        self.add(npyscreen.TitleText, w_id="txt", name = "This is the SECOND Form!")
       
    def on_ok(self):        
        self.parentApp.switchForm(None)

app = App()
app.run()