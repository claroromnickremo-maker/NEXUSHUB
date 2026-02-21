from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, DictProperty
import os


class NexusHubRoot(BoxLayout):
    status = StringProperty("Idle")
    features = DictProperty({
        "Auto Aim": False,
        "Wallhack": False,
        "Speed": False,
        "Radar": False,
    })

    def toggle_feature(self, feature, value):
        self.features[feature] = value
        self.status = f"{feature} {'enabled' if value else 'disabled'}"
        print(self.status)

    def apply_button(self):
        self.status = "Applied settings: " + ", ".join(
            f"{k}:{'ON' if v else 'OFF'}" for k, v in self.features.items()
        )
        print(self.status)

    def simulate_action(self, name):
        self.status = f"Simulated: {name}"
        print(self.status)


class NexusHubApp(App):
    def build(self):
        # Title and optional icon (place icon.png here)
        self.title = "N.E.X.U.SHUB"
        icon_path = os.path.join(os.path.dirname(__file__), "icon.png")
        if os.path.exists(icon_path):
            self.icon = icon_path
        return Builder.load_file("nexus.kv")


if __name__ == "__main__":
    NexusHubApp().run()
