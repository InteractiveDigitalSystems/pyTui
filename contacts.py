#  Contacts.py 
#  Example by Ebbe Vang - feb 2021

from npyscreen import *

class TuiApp(NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", ContactsForm, name="..:: Contacts ::.." )
        self.setNextForm(None)

class ContactsForm(Form):
    def create(self):
        self.add(TitleFixedText, id="title", name="Add Contacts", hidden=False)
        self.edit()



if (__name__ == "__main__"):
    app = TuiApp().run()



