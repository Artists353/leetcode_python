class Solution:
    def mySqrt(self, x: int, precision=0.00001) -> int:
        if x < 0:
            return "Нельзя найти действительный корень для отрицательного числа"
        guess = x / 2.0 # Начальное приближение
        while abs(guess * guess - x) > precision:
            guess = (guess + x / guess) / 2.0 # Формула Ньютона 
        if float(guess):
            return int(guess)
    
soliution = Solution()
print(soliution.mySqrt(8))  # Пример использования