import npyscreen

class App(npyscreen.NPSAppManaged):
    def onStart(self):
        #add forms to the application
        self.addForm('MAIN', FirstForm, name="main")
      
class FirstForm(npyscreen.ActionFormMinimal):
    def create(self):
        self.add(npyscreen.TitleText, name="Press CTRL + T")
        self.add_handlers({"^T": self.handler})
    def handler(self, *args, **keywords):
        npyscreen.notify_confirm("Hey you pressed CTRL + T!", title="SHORTCUT!!!", wrap=True, wide=True, editw=1)

    def on_ok(self):
        self.parentApp.switchForm(None)
      
app = App()
app.run()