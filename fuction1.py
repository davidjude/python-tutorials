#positional argument
from sre_constants import RANGE


def name(myname,myname2):
    print(myname,myname2)
name("David","jude")
#named argument
def surname(myname3,myname2,myname):
    print(myname,myname3,myname2)
surname(myname="David",myname2="jude",myname3="luke")
#abituary argument
def subject(*args):
    print(args)
    for i in args:
        print(i)
subject("math","english","biology","history")

def house(**kwargs):
   print(kwargs)
house(name="shool",name1="church",name2="market")



#assignment read geek for geek python functions
#w3schools reelpython

#create a python function that mul
def product(number1,number2):
    a=number1 * number2
    return a
ans=product(10,20)

def sub(number1,number2):
    a=number1 - number2
    print(a)
sub(ans, 50)