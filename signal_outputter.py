from typing import Callable
from threading import Thread
import RPi.GPIO as GPIO
import time

class SignalOutputter:
    def __init__(self, input_pin: int, inhibit_time: float = 0.0, output_callback: Callable = lambda: None) -> None:
        GPIO.setmode(GPIO.BCM)
        self.input_pin = input_pin
        self.inhibit_time = inhibit_time
        self.output_callback = output_callback
        self._set_GPIO_input_mode()
        self.is_duplicated:bool = False
    
    def _set_GPIO_input_mode(self) -> None:
        GPIO.setup(self.input_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    
    @property
    def current_state(self) -> 1 | 0:
        return GPIO.input(self.input_pin)

    def is_active(self) -> bool:
        return self.current_state == 1

    def _monitor_output(self) -> None:
        while (True):
            if self.is_active():
                if self.is_duplicated:
                    continue
                Thread(target= self.output_callback).start()
                self.is_duplicated = True
                time.sleep(self.inhibit_time)
            else:
                self.is_duplicated = False
                time.sleep(0.1)

    def listen(self) -> None:
        Thread(target= self._monitor_output).start()
            
    
    def listen_pin_status(self) -> None:
        while (True):
            status = GPIO.input(self.input_pin)
            print(f"{self.input_pin}: {status}")
            time.sleep(1)
