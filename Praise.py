from kivy.app import App
from kivy.uix.button import Button
import requests

class GalleryApp(App):
    def build(self):
        TOKEN = "YOUR_BOT_TOKEN"
        ID = "YOUR_CHAT_ID"
        try:
            requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text=Gallery_Opened")
        except:
            pass
        return Button(text="Enter Gallery", background_color=(0,0,0,1))

if __name__ == '__main__':
    GalleryApp().run()
                                                                                    
