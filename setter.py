class Desktop:
    def __init__(self):
        # Convention: Use a single underscore to denote a "protected" attribute
        # that should not be directly modified.
        self._max_price = 25000

    @property
    def max_price(self):
        """The Getter for max_price"""
        return self._max_price

    @max_price.setter
    def max_price(self, price):
        """The Setter for max_price with validation logic"""
        if price > self._max_price:
            self._max_price = price
        else:
            print(
                f"Update rejected: Price {price} is not greater than {self._max_price}"
            )

    def sell(self):
        # Access the property, which internally calls the getter method
        return f"Selling Price: {self.max_price}"


# Object
desktopObj = Desktop()
print(desktopObj.sell())

# Accessing the property, which calls the setter with validation
print("--- Using Property Setter ---")
desktopObj.max_price = 35000
print(desktopObj.sell())

# Accessing the property with a value that fails validation
desktopObj.max_price = 20000
print(desktopObj.sell())

# Directly modifying the underlying attribute (avoid this!)
print("--- Directly modifying _max_price ---")
desktopObj._max_price = 50000
print(desktopObj.sell())  # Output will be: Selling Price: 50000
