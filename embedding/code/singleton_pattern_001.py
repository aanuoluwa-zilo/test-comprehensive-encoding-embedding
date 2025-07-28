# Singleton Pattern Implementation 1
class Singleton1:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self.data = {}
            self._initialized = True
    
    def add_data(self, key, value):
        self.data[key] = value
    
    def get_data(self, key):
        return self.data.get(key)

# Usage
singleton1 = Singleton1()
singleton2 = Singleton1()
print(singleton1 is singleton2)  # True
