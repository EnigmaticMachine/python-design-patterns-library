class Singleton:

    _instance = None

    # __new__ Method: The __new__ method in Python is responsible for creating a new instance of a class.
    # It is called before __init__ and is the first step in the instance creation process.
    def __new__(cls):
        # If `_instance` is `None`, it means no instance has been created yet,
        # so `super(Singleton, cls).__new__(cls)` is called to create one.
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):  # Prevent reinitialization
            self.value = None
            self._initialized = True

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value
