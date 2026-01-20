class Solution:
    def fizzBuzz(self, n: int):
        l=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                e="FizzBuzz"
            elif i%3==0:
                e="Fizz"
            elif i%5==0:
                e="Buzz"
            else:
                e=str(i)
            l.append(e)
        return l