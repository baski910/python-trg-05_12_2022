def addnum(a,b):
    return a+b

def divnum(a,b):
    return a/b


# __name__ - returns __main__ in the current script
# __name__ - returns module name when imported in another script


#if __name__ == '__main__':
print("calling from module:",__name__) 
print("calling from module:",addnum(25,5))
print("calling from module:",divnum(25,5))