import npyscreen

def simple_function ( *arguments):
    form = npyscreen.Form( name='hello world', lines=6, columns=40)
    form.edit()

npyscreen.wrapper_basic(simple_function)