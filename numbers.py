class Num:
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
            result = 'Not a valid type'
        return result

class Complex:
    real = 0
    imag = 0

y = '0'
    
print(f'Num.abs({y}): {Num.abs(y)}')
