#  Contacts.py 
#  Example by Ebbe Vang - feb 2021

from npyscreen import *

# the Application
class TuiApp(NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', ContactsForm)
        self.addForm('ALLCONTACTS', ListContacts)
    def changeForm(self, name):
        self.switchForm('ALLCONTACTS')
        self.resetHistory(); 
    def change_forms(self, name):
        # Switch forms.  NB. Do *not* call the .edit() method directly (which 
        # would lead to a memory leak and ultimately a recursion error).
        # Instead, use the method .switchForm to change forms.
        self.switchForm(name)
        
        # By default the application keeps track of every form visited.
        # There's no harm in this, but we don't need it so:        
        self.resetHistory()
        
# the Form being displayed in the Application
class ContactsForm(Form):
    def create(self):
        self.add(TitleFixedText, id="title", name="Please Choose an option" )
        self.add(Selector, id="selector", name="Select", values=['first', 'second'], relx=3)
        self.add_handlers({"^T": self.change_form})
    def change_form(self, *args, **keywords):
        self.parentApp.changeForm('ALLCONTACTS')

# form to show all contacts
class ListContacts(Form):
    
    contacts = ['Liv', 'Mikkel']

    def create(self):
        self.add(MultiLine, id="allContacts", values=self.contacts)

    def activate(self):
        self.parentApp.setNextForm(None)

# widget inherrited from MultiLineAction
class Selector(MultiLineAction):
    def actionHighlighted(self, act_on_this, key_press):
        #self.parent.parentApp.setNextForm("ALLCONTACTS")
        #print(act_on_this)
        #self.parent.parentApp.switchForm("ALLCONTACTS")
        #self.parent.change_form()
        self.parent.parentApp.switchForm('ALLCONTACTS')
        
        
        

if (__name__ == "__main__"):
    app = TuiApp() # create application instance
    app.run() # Run application



