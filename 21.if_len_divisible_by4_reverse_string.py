'''Write a Python function to reverses a string if its length is a multiple of
4'''
def rev(a):
    if len(a)%4==0:
        return reversed(a)
    else:
        return a 
x=rev("abcd")
print("".join(x))
        
