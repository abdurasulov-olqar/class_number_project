class Number:
    def __init__(self, value: int):
        self.value = value


    def get_number(self):
        """
        Returns the number.

        returns: int
        """
        return self.value

    def is_odd(self):
        """
        Returns True if the number is odd, otherwise False.

        returns: bool

        """
        return self.value % 2 == 1

    def is_even(self):
        """
        Returns True if the number is even, otherwise False. 

        returns: bool
        """
        return self.value % 2 == 0

    def is_prime(self):
        """
        Returns True if the number is prime, otherwise False.

        returns: bool
        """
        prime = True
        for i in range(2, self.value):
            if self.value % i == 0:
                prime = False
        return prime

    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        l = []
        for i in range(1, self.value+1):
            if self.value % i == 0:
                l.append(i)
        
        return l

    def get_length(self):
        """
        Returns the number of digits in the number.

        returns: int
        """
        
        digits = []
        i = abs(self.value)
        while i > 0:
            n = i%10
            digits.append(n)
            i = i // 10 
        return len(digits)

    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        s = 0
        i = abs(self.value)
        while i > 0:
            n = i%10
            s = s+n
            i = i // 10 
        return s

    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        digits = []
        i = abs(self.value)
        while i > 0:
            n = i%10
            digits.append(n)
            i = i // 10 
        num = 0    
        power = len(digits)-1
        for digit in digits:
            num+= digit * (10**power)
            power = power-1

        return num

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        return number.get_reverse() == self.value

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        
        digits = []
        i = abs(self.value)
        if i== 0:
            return [0]
        while i > 0:
            n = i%10
            digits.append(n)
            i = i // 10 
        return digits[-1:]

    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        return max(number.get_digits())

    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        return min(number.get_digits())

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        
        return number.get_sum()/number.get_length()

    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        pass

    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        pass

    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.

        returns: dict
        """
        pass
    

# Create a new instance of Number
number = Number(8758736498)
# print(number.get_number())
# print(number.is_even())
# print(number.is_prime())
# print(number.get_divisors())
# print(number.get_length())
# print(number.get_sum())
# print(number.get_reverse())
# print(number.is_palindrome())
# print(number.get_digits())
# print(number.get_max())
print(number.get_min())