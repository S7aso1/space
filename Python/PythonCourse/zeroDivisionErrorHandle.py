def division():
    res = 5/0
    return res

def divFunction():
    try:
        div = division()
        print(div)

    except ZeroDivisionError: 
        print("Please do not divide by Zero!!!")

divFunction()