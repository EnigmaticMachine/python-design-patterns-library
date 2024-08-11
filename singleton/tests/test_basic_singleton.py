import pytest
from code_examples.basic_singleton import Singleton


def test_singleton_instance():
    # Create two instances of the Singleton class
    singleton1 = Singleton()
    singleton2 = Singleton()

    # Test if both instances are actually the same object
    assert singleton1 is singleton2, "Singleton instances are not the same!"


def test_singleton_value_persistence():
    # Create an instance and set a value
    singleton1 = Singleton()
    singleton1.set_value(100)

    # Create another instance and check if the value persists
    singleton2 = Singleton()
    assert (
        singleton2.get_value() == 100
    ), "Singleton value was not persistent across instances!"
