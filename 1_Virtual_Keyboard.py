from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window


class MyApp(App):              
    def change_to_upper_case(self, button):
        if button.text.islower():
            button.text = button.text.upper()

    def change_to_lower_case(self, button):
        if button.text.isupper():
            button.text = button.text.lower()


    def build(self):
    
        Window.size = (400, 600)
        
        # Set the window background color to magenta
        Window.clearcolor = (0, 0.5, 0, 0.1)  
        
        # Set the title of the window
        self.title = 'My Mobile'
        
        self.selected_input = None  # Track which input is selected

        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Input fields with labels
        input1_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))
        label1 = Label(text='User name:', size_hint=(0.3, 1))
        self.input1 = TextInput(
            hint_text='Enter username',
            multiline=False,
            font_size=20,
            size_hint=(0.7, None),
            height=40
        )
        
        
        self.input1.bind(focus=self.on_focus)
        input1_layout.add_widget(label1)
        input1_layout.add_widget(self.input1)

        input2_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))
        label2 = Label(text='Password:', size_hint=(0.3, 1))
        self.input2 = TextInput(
            hint_text='Enter password',
            multiline=False,
            password=True,
            font_size=20,
            size_hint=(0.7, None),
            height = 40
        )
        self.input2.bind(focus=self.on_focus)
        input2_layout.add_widget(label2)
        input2_layout.add_widget(self.input2)

        main_layout.add_widget(input1_layout)
        main_layout.add_widget(input2_layout)

        # Navigation buttons ==============================================
        nav_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))

        # Spacer at the beginning
        nav_layout.add_widget(Widget(size_hint_x=0.4))  # Horizontal spacer

        left_button = Button(text='<-', size_hint_x=0.1, background_color=(1, 1, 0, 1), bold=True)
        left_button.bind(on_press=self.move_cursor_left)
        nav_layout.add_widget(left_button)

        right_button = Button(text='->', size_hint_x=0.1, background_color=(1, 1, 0, 1), bold=True)
        right_button.bind(on_press=self.move_cursor_right)  # Corrected binding position
        nav_layout.add_widget(right_button)

        # Spacer at the end
        nav_layout.add_widget(Widget(size_hint_x=0.4))  # Horizontal spacer

        main_layout.add_widget(nav_layout)

        # Delete buttons =====================================================
        delete_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))

        # Spacer at the beginning
        delete_layout.add_widget(Widget(size_hint_x=0.4))  # Horizontal spacer

        del_left_button = Button(text='Del <-', size_hint_x=0.1)  # Delete left symbol
        del_left_button.bind(on_press=self.delete_left)
        delete_layout.add_widget(del_left_button)

        del_right_button = Button(text='-> Del', size_hint_x=0.1)  # Delete right symbol
        del_right_button.bind(on_press=self.delete_right)
        delete_layout.add_widget(del_right_button)

        # Spacer at the end
        delete_layout.add_widget(Widget(size_hint_x=0.4))  # Horizontal spacer

        main_layout.add_widget(delete_layout)

        # Message label
        self.message_label = Label(
            text='Messages will appear here.',
            size_hint=(1, 0.1),
            color=(1, 0, 0, 1),  # Red color
            font_size='20sp',    # Larger font size
            bold=True            # Bold text
        )
        main_layout.add_widget(self.message_label)

        # Keyboard layout
        self.keyboard_layout = GridLayout(cols=10, size_hint=(1, 0.6))

        # Create buttons for each letter
        self.buttons = []
        letters = 'abcdefghijklmnopqrstuvwxyz-., '
        for letter in letters:
            button = Button(text=letter)
            button.bind(on_press=self.on_button_press)
            self.keyboard_layout.add_widget(button)
            self.buttons.append(button)

        main_layout.add_widget(self.keyboard_layout)

        # Buttons Layout
        buttons_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)

        # Button to clear input texts
        clear_button = Button(text='Clear Inputs', size_hint=(None, None), size=(100, 50),
                              color=(0, 0, 1, 1), background_color=(1, 1, 1, 1))
        clear_button.bind(on_press=self.clear_inputs)
        buttons_layout.add_widget(clear_button)

        # Button to transmit the message
        transmit_button = Button(text='Transmit', size_hint=(None, None), size=(100, 50),
                                 color=(0, 0, 1, 1), background_color=(1, 1, 1, 1))
        transmit_button.bind(on_press=self.transmit)
        buttons_layout.add_widget(transmit_button)

        # Button to change text to uppercase
        uppercase_button = Button(text='Uppercase', size_hint=(None, None), size=(100, 50),
                                  color=(0, 0, 1, 1), background_color=(1, 1, 1, 1))
        uppercase_button.bind(on_press=self.change_all_buttons_to_uppercase)
        buttons_layout.add_widget(uppercase_button)

        # Button to change text to lowercase
        lowercase_button = Button(text='Lowercase', size_hint=(None, None), size=(100, 50),
                                  color=(0, 0, 1, 1), background_color=(1, 1, 1, 1))
        lowercase_button.bind(on_press=self.change_all_buttons_to_lowercase)
        buttons_layout.add_widget(lowercase_button)
        
        main_layout.add_widget(buttons_layout)

        return main_layout

    def on_focus(self, instance, value):
        if value:
            self.selected_input = instance
            self.message_label.text = f"{instance.hint_text} is focused."

    def on_button_press(self, instance):
        if self.selected_input:
            self.selected_input.insert_text(instance.text)
            self.message_label.text = f"Inserted '{instance.text}' into {self.selected_input.hint_text}"
        else:
            self.message_label.text = "No input selected."

    def move_cursor_left(self, instance):
        if self.selected_input:
            cursor_x, cursor_y = self.selected_input.cursor
            if cursor_x > 0:
                self.selected_input.cursor = (cursor_x - 1, cursor_y)

    def move_cursor_right(self, instance):
        if self.selected_input:
            cursor_x, cursor_y = self.selected_input.cursor
            if cursor_x < len(self.selected_input.text):
                self.selected_input.cursor = (cursor_x + 1, cursor_y)

    def delete_left(self, instance):
        if self.selected_input:
            cursor_x, cursor_y = self.selected_input.cursor
            if cursor_x > 0:
                text_before_cursor = self.selected_input.text[:cursor_x - 1]
                text_after_cursor = self.selected_input.text[cursor_x:]
                self.selected_input.text = text_before_cursor + text_after_cursor
                self.selected_input.cursor = (cursor_x - 1, cursor_y)

    def delete_right(self, instance):
        if self.selected_input:
            cursor_x, cursor_y = self.selected_input.cursor
            if cursor_x < len(self.selected_input.text):
                text_before_cursor = self.selected_input.text[:cursor_x]
                text_after_cursor = self.selected_input.text[cursor_x + 1:]
                self.selected_input.text = text_before_cursor + text_after_cursor
                self.selected_input.cursor = (cursor_x, cursor_y)

    def clear_inputs(self, instance):
        # Clear input texts
        self.input1.text = ''
        self.input2.text = ''

    def transmit(self, instance):
        # Retrieve input text and create message
        text1 = self.input1.text
        text2 = self.input2.text
        message = f"User name: {text1} \nPassword: {text2}"
        self.message_label.text = message

    def change_all_buttons_to_uppercase(self, instance):
        for button in self.buttons:
            self.change_to_upper_case(button)

    def change_all_buttons_to_lowercase(self, instance):
        for button in self.buttons:
            self.change_to_lower_case(button)

            
if __name__ == '__main__':
    MyApp().run()
