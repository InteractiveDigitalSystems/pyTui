#  Contacts.py 
#  Example by Ebbe Vang - feb 2021

from npyscreen import *

# the Application
class TuiApp(NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', ContactsForm)
        self.addForm('ALLCONTACTS', ListContacts)
    def changeForm(self, name):
        self.setNextForm("ALLCONTACTS")
        self.switchForm("ALLCONTACTS")
        self.resetHistory();    
        
        

# the Form being displayed in the Application
class ContactsForm(Form):
    def create(self):
        self.add(TitleFixedText, id="title", name="Please Choose an option" )
        self.add(Selector, id="selector", name="Select", values=['first', 'second'], relx=3)
    def activate(self):
        self.edit()
        self.parentApp.setNextForm(None)

# form to show all contacts
class ListContacts(Form):
    
    contacts = ['Liv', 'Mikkel']

    def create(self):
        self.add(MultiLine, id="allContacts", values=self.contacts)

    def activate(self):
        self.edit()
        self.parentApp.setNextForm(None)


# widget inherrited from MultiLineAction
class Selector(MultiLineAction):
    def actionHighlighted(self, act_on_this, key_press):
        #self.parent.parentApp.setNextForm("ALLCONTACTS")
        #print(act_on_this)
        #self.parent.parentApp.switchForm("ALLCONTACTS")
        self.parent.parentApp.changeForm('ALLCONTACTS')
        
        
        

if (__name__ == "__main__"):
    app = TuiApp().run()



