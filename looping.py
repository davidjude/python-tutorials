from cgi import print_environ


count = 0
for number in range(1,10):
    if number  %  2 ==  0:
        count += 1
        print(number)
    for  numbers in range(1, 10):
     print(f"we have {count} even numbers")
