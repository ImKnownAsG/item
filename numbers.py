class Num:
    _precision = .00001
        
    def abs(x):
        result = x
        if type(x) == str:
            try:
                x = float(x)
            except:
                x = x
        if type(x) == int or type(x) == float: 
            try:
                if x < 0:
                    result = x * -1
            except:
                print(f'something bad happened')
                result = 0
        else:
            raise TypeError('Not a valid type')
        return result
    def pow(b, e):
        result = 1
        if e != 0:
            result = b
            count = 1
            while count < Num.abs(e):
                result = result * b 
                count = count + 1
        if e < 0:
            result = 1 / result
        
        return result
    
    def ceil(x):
        return int(x) + 1

    def sqrt_joe(x):
        if x > 0:
            guess = x/2.0
            diff = x - Num.pow(guess, 2.0)
            while Num.abs(diff) > Num._precision:
                if diff < 0:
                    guess = guess/2.0
                else:
                    guess = guess * 1.5
                diff = x - pow(guess, 2.0)
        elif x == 0:
            guess = 0
        else:
            raise 'complex numbers not implemented yet'
        
        return guess
        
    def sqrt(x):
        if x < 0:
            if x == 0:
                guess == 0
            else:
                raise ValueError('Complex numbers not implemented yet')
        else:
            #establish initial high and low guesses, start guessing with the high value
            for _ in range(Num.ceil(x)):
                if pow(_, 2) < x:
                    lowGuess = _
                else:
                    highGuess = _
                    break
            
            guess = highGuess 
            
            #check how close our current guess is and guess again if it is too far off
            while abs(pow(guess, 2) - x) > Num._precision:
                #if current guess is too high
                if Num.pow(guess, 2) > x:
                    #new guess is halfway between current guess and lowGguess
                    guess = lowGuess + ((guess - lowGuess) * .5)
                    
                else:
                    guess = highGuess - ((highGuess - guess) * .5)
                
                #if the new guess is still too high set it to highGuess to define a new upper bound
                if Num.pow(guess, 2) > x:
                    highGuess = guess
                #otherwise use it as the new lower bound
                else:
                    lowGuess = guess
            
            #the logic above can create a very ugly decimal, much of which is unnecessary
            #starting from the integer value and adding decimal places, find the value of
            #guess with the least decimal places that satisfies the _precision requirement
            refGuess = int(guess)
            #as a way of truncating the decimals, guess is multiplied by a power of 10,
            #the int value is returned, then that int is divided by the same power of 10
            thisPow = 0 
            
            while abs(pow(refGuess, 2) - x) > Num._precision:
                #refPlus and refMin are attempts to get around the floating point inaccuracies...a failed attempt
                refPlus = int((refGuess + Num._precision) * Num.pow(10, thisPow)) / Num.pow(10, thisPow)
                refMin = int((refGuess - Num._precision) * Num.pow(10, thisPow)) / Num.pow(10, thisPow)
                print(f'refPlus, refMin: {refPlus}, {refMin}')
                print(f'Num.pow(refPlus, 2), Num.pow(refMin, 2): {Num.pow(refPlus, 2)}, {Num.pow(refMin, 2)}')
                if Num.pow(refPlus, 2) == x:
                    refGuess = refPlus
                elif Num.pow(refMin, 2) == x:
                    refGuess = refMin
                else:
                    refGuess = int(guess * Num.pow(10, thisPow)) / Num.pow(10, thisPow)
                    thisPow += 1
                    
        print(f'guess, refGuess: {guess}, {refGuess}')
        return refGuess
                
    def pi():
        sign = -1
        deno = 3
        result = 1
        while 1/deno > Num._precision:
            result += sign/denom
            sign *= -1
            denom += 2
        result *= 4
        return result
    
    def factI(n):
        result = 1
        for _+ in range(1, n + 1):
            result *= _
        return result
    
    def factR(n):
        if N < 2:
            return 1
        else:
            return n * factR(n - 1)
    
        
    def fib():
        

class Complex:
    real = 0
    imag = 0

