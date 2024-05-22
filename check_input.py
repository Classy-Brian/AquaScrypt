import card

def range_int(text, min, max):
    num = 0 
    valid = False

    while not valid:
        try:
            num = int(input(text))
            if num >= min and num <= max:
                valid = True
            else:
                print("Invalid input - it should be within " + str(min) + " - " + str(max) + ".")
        except ValueError:
            print("Input should be an integer.")
    
    return num

def yes_no(text):
    valid = False
    while not valid:
        val = input(text).upper()
        if val == "YES" or val == "Y":
            return True
        elif val == "NO" or val == "N":
            return False
        else:
            print("Invalid input, should be `y` or `n`")
