import tkinter as tk
from AdafruitMotor import AdafruitMotor
from AdafruitRover import AdafruitRover
from ServoControl import ServoControl

class RoverControllerApp:
    def __init__(self, main, rover, servo):
        self.master = main
        self.rover = rover
        self.servo = servo

        self.camera_angle = 90  # Initial camera angle, assuming center position
        
        # Create directional buttons for the rover
        self.btn_forward = self.create_button("Forward", self.rover.forward)
        self.btn_backward = self.create_button("Backward", self.rover.backward)
        self.btn_left = self.create_button("Left", self.rover.left)
        self.btn_right = self.create_button("Right", self.rover.right)
        
        # Create camera control buttons
        self.btn_cam_left = self.create_button("Cam Left", lambda: self.move_camera(-10))
        self.btn_cam_right = self.create_button("Cam Right", lambda: self.move_camera(10))
        
        self.master.bind('<KeyPress>', self.on_key_press)
        self.master.bind('<KeyRelease>', self.on_key_release)
        self.pressed_buttons = {}

    def move_camera(self, angle_change):
        # Adjust camera angle within a safe range
        new_angle = max(0, min(180, self.camera_angle + angle_change))
        if new_angle != self.camera_angle:
            self.servo.set_servo_angle(new_angle)
            self.camera_angle = new_angle

    def on_key_press(self, event):
        key = event.keysym
        if key in self.pressed_buttons:
            return
        self.pressed_buttons[key] = True
        self.execute_commands()

    def on_key_release(self, event):
        key = event.keysym
        if key in self.pressed_buttons:
            del self.pressed_buttons[key]
        if not self.pressed_buttons:
            self.rover.stop()

    def execute_commands(self):
        if 'Up' in self.pressed_buttons:
            self.rover.forward()
        if 'Down' in self.pressed_buttons:
            self.rover.backward()
        if 'Left' in self.pressed_buttons:
            self.rover.left()
        if 'Right' in self.pressed_buttons:
            self.rover.right()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Rover Does Stuff")

    front_left = AdafruitMotor(1)
    front_right = AdafruitMotor(2)
    back_left = AdafruitMotor(3)
    back_right = AdafruitMotor(4)
    rover = AdafruitRover(front_left, front_right, back_left, back_right)

    servo = ServoControl(15)
    
    app = RoverControllerApp(root, rover, servo)
    root.mainloop()
