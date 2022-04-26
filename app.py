from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.lang.builder import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.network.urlrequest import UrlRequest
from kivy.properties import StringProperty
#Config.set('graphics', 'width', '360')
#Config.set('graphics', 'height', '720')
Config.set('kivy','window_icon','Cattura.png')

kv = '''
Home:

<Home>:
    Label:
        text: "SpaceNAO"
        font_name: "mandalore.ttf"
        font_size: 100
        pos_hint: {"center_x":0.5, "center_y":0.9}
    #Label:
        #text: "Telecomando: "+root.telecomando
        #pos_hint: {"center_x":0.2, "center_y":0.75}
    #Slider:
        #id: prog_bar
        #pos_hint: {'center_x':0.7, 'center_y':0.75}
        #size_hint: dp(0.5), dp(.4)
        #value: 2
        #step: 1
        #min: 2
        #max: 3
        #on_value: root.change_telecomando(self.value)
    Button:
        text:"A"
        background_color: 255/255, 51/255, 51/255, 1
        size_hint: 0.4, 0.2
        pos_hint: {"center_x":0.5, "center_y":0.6}
        on_press: root.invio('A')
    Button:
        text:"B"
        background_color: 0/255, 0/255, 255/255, 1
        size_hint: 0.4, 0.2
        pos_hint: {"center_x":0.5, "center_y":0.4}
        on_press: root.invio('B')
    Button:
        text:"C"
        background_color: 51/255, 255/255, 51/255, 1
        size_hint: 0.4, 0.2
        pos_hint: {"center_x":0.5, "center_y":0.2}
        on_press: root.invio('C')
'''



class Home(FloatLayout):
    telecomando = StringProperty("2")

    #def change_telecomando(self, value):
    #    self.telecomando = str(value)
    #    print(value)

    def invio(self, risposta):
        #UrlRequest("http://192.168.1.69:8081", req_body=str(self.telecomando)+"2;"+str(risposta))
        UrlRequest("http://192.168.1.69:8081", req_body="3;"+str(risposta))

    

class MainApp(App):
    def build(self):
        return Builder.load_string(kv)


if __name__ == '__main__':
    MainApp().run()
