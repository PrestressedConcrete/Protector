from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import hashlib

def encode(input: str) -> str:
    encoded = hashlib.sha256(input.encode()).hexdigest()
    return encoded

class Protector(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Password field
        self.password = TextInput(password=True, hint_text='Enter password', size_hint=(1, 0.2))
        self.layout.add_widget(self.password)

        # Input field
        self.input = TextInput(hint_text='Enter a word', size_hint=(1, 0.2))
        self.layout.add_widget(self.input)

        # Encode button
        self.encode_btn = Button(text='Encode', on_press=self.encode, size_hint=(1, 0.2))
        self.layout.add_widget(self.encode_btn)

        # Output field
        self.output = TextInput(readonly=True, size_hint=(1, 0.2))
        self.layout.add_widget(self.output)

        return self.layout

    def _encode(self, password: str, input: str):
        # Simple encoding using SHA-256 hashing
        # Concatenate password and input, then hash
        if encode(password) != "483029d526219f816e8e8f6a9de07b422633dba180ffc26faac22862a017519f":
            raise Exception()

        password = password.split()[0]
        input = input.split()[0]
        combined = password + input
        encoded = encode(combined)

        if len(input)%3==0:
            encoded = encoded[-10:]
            encoded = encoded[3:].upper() + '@' + encoded[3:6] + '#'+ encoded[6:].upper()
        elif len(input)%3==1:
            encoded = encoded[-10:]
            encoded =  '@' + '#'+ encoded[3:] + encoded[3:6].upper() + encoded[6:].upper()
        else:
            encoded = encoded[-10:]
            encoded = encoded[6:] + '@' + encoded[6:7].upper() + '#'+ encoded[7:].upper()

        if encoded.upper() == encoded:
            encoded = encoded + 'b'
        if encoded.lower() == encoded:
            encoded = encoded + 'B'
        
        
        return encoded

    def encode(self, instance):
        encoded_text = self._encode(self.password.text, self.input.text)
        self.output.text = encoded_text

if __name__ == '__main__':
    Protector().run()
