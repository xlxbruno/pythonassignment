values = "a,b"
a = 5
b = 7
if a == b :
    print("a and b are equal")
elif a > b:
    print("a is greater than b")
elif b > a:
    print("b is greater than a")
else:
    print("invalid")






Values=("a,b")
a = 12
b =8
s_um = a + b
d_iff = a - b
p_rod = a * b
quotien_t = a / b



if a == b:
    print("equal")
else :
    print("not equal")
if b == 0:
    print("error,division by zero")

else:
    print(s_um,d_iff,p_rod,quotien_t)

#BONUS

def palindrome (s):
    return s == s[::-1]
s = "level"
Output = palindrome(s)

if Output:
    print("Correct")
else :
    print("Invalid input")