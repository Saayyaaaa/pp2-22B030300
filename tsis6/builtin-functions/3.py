def reverse_string(string):
    r = ''.join(reversed(string))
    if string == r:
        return True
    return False

if reverse_string(input()):
    print("This string is polindrome")
else:
    print("This string is not polindrome")
