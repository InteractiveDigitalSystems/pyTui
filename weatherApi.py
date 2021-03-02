import npyscreen
from npyscreen.wgtitlefield import TitleText
import requests


class App(npyscreen.NPSAppManaged):
    def onStart(self):
        # add forms to the application
        self.addForm('MAIN', FirstForm, name="Get weather")


class FirstForm(npyscreen.ActionFormMinimal):
    def create(self):
        self.add(npyscreen.TitleText, w_id="textfield",
                 name="Enter city:")
        self.add(npyscreen.ButtonPress, name="Get coordinates!",
                 when_pressed_function=self.btn_press)

    def btn_press(self):
        form_input = self.get_widget("textfield").value
        url = "https://www.metaweather.com/api/location/search/?query=" + form_input
        resp = requests.get(url=url)
        if resp.text == '[]':
            npyscreen.notify_confirm(
                "Search returns null", title="Hi", wrap=True, wide=True, editw=1)
            return
        resp = resp.json()
        url = "https://www.metaweather.com/api/location/" + str(resp[0]['woeid'])
        resp = requests.get(url=url)
        resp = resp.json()
        # https://www.metaweather.com/api/location/44418/
        weather = resp['consolidated_weather'][0]['weather_state_name']
        message = f'Weather is {weather}'
        npyscreen.notify_confirm(
            message, title="Hi", wrap=True, wide=True, editw=1)

    def on_ok(self):
        self.parentApp.switchForm(None)


app = App()
app.run()
