# MVC Pattern Implementation 2
from abc import ABC, abstractmethod

class Model:
    def __init__(self):
        self.data = {}
    
    def get_data(self):
        return self.data
    
    def set_data(self, key, value):
        self.data[key] = value

class View:
    def display(self, data):
        print(f"Displaying data: {data}")

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def update_data(self, key, value):
        self.model.set_data(key, value)
        self.view.display(self.model.get_data())

# Usage
model = Model()
view = View()
controller = Controller(model, view)
controller.update_data("test", "value")
