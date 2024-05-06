import tkinter as tk
from AdafruitMotor import AdafruitMotor
from AdafruitRover import AdafruitRover

class RoverControllerApp:
    def __init__(self, main, rover):
        self.master = main # Create the tkinter main window
        self.rover = rover # Create the rover instance
        
        # Create directional buttons
        self.btn_forward = self.create_button("Forward", self.rover.forward)
        self.btn_backward = self.create_button("Backward", self.rover.backward)
        self.btn_left = self.create_button("Left", self.rover.left)
        self.btn_right = self.create_button("Right", self.rover.right)
        
        # Bind button press and release events
        self.master.bind('<KeyPress>', self.on_key_press)
        self.master.bind('<KeyRelease>', self.on_key_release)
        
        # Dictionary to store pressed buttons
        self.pressed_buttons = {}
    
    def create_button(self, text, command):
        # Create tkinter buttons with the specified text and commands
        button = tk.Button(self.master, text=text, command=command, width=10)
        button.pack() # Pack the button into the GUI
        return button # Return the created button
    
    def on_key_press(self, event):
        # Event handler for key press
        key = event.keysym
        if key in self.pressed_buttons:
            return
        self.pressed_buttons[key] = True # Add key press to the dictionary
        self.execute_commands() # Execute rover command based on the key press
    
    def on_key_release(self, event):
        # Event handler for key release
        key = event.keysym
        if key in self.pressed_buttons:
            del self.pressed_buttons[key] # Remove released key from dictionary
        if not self.pressed_buttons:
            # If no keys are pressed, stop the rover
            self.rover.stop() 
    
    def execute_commands(self):
        # Execute methods from rover class based on buttons pressed
        if 'Up' in self.pressed_buttons:
            self.rover.forward()
        if 'Down' in self.pressed_buttons:
            self.rover.backward()
        if 'Left' in self.pressed_buttons:
            self.rover.left()
        if 'Right' in self.pressed_buttons:
            self.rover.right()

if __name__ == "__main__":
    root = tk.Tk() # Create tkinter root window
    root.title("Rover Does Stuff") # Set window title

    # Create instances of the motor class
    front_left = AdafruitMotor(1)
    front_right = AdafruitMotor(2)
    back_left = AdafruitMotor(3)
    back_right = AdafruitMotor(4)

    # Create an instance of the rover class
    rover = AdafruitRover(front_left, front_right, back_left, back_right)
    
    # Create RoverControllerApp instance
    app = RoverControllerApp(root, rover)
    
    # Enter the tkinter main event loop
    root.mainloop()