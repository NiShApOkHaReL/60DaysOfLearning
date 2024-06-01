class MathUtility:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

# Call static methods
result1 = MathUtility.add(5, 3)
result2 = MathUtility.multiply(5, 3)

print(result1)  # Output: 8
print(result2)  # Output: 15
