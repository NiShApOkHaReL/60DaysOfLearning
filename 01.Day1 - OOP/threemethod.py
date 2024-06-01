class Example:
    class_attr = "I am a class attribute"

    def __init__(self, instance_attr):
        self.instance_attr = instance_attr

    def instance_method(self):
        print(f"Instance attribute: {self.instance_attr}")
        print(f"Class attribute: {Example.class_attr}")

    @classmethod
    def class_method(cls):
        print(f"Class attribute: {cls.class_attr}")
        cls.class_attr = "Modified by class method"

    @staticmethod
    def static_method(arg1, arg2):
        print(f"Static method arguments: {arg1}, {arg2}")

# Create an instance
example_instance = Example("I am an instance attribute")

# Call instance method
example_instance.instance_method()
# Output:
# Instance attribute: I am an instance attribute
# Class attribute: I am a class attribute

# Call class method
Example.class_method()
# Output:
# Class attribute: I am a class attribute

# Call instance method again to see the effect
example_instance.instance_method()
# Output:
# Instance attribute: I am an instance attribute
# Class attribute: Modified by class method

# Call static method
Example.static_method("Argument 1", "Argument 2")
# Output:
# Static method arguments: Argument 1, Argument 2
