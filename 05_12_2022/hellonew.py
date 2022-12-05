# __all__ to restrict the functions to be imported
__all__ = ['addnum','divnum'] # only these 2 functions are imported when 'from hellonew import *' directive is used

def addnum(a,b):
    return a+b

def divnum(a,b):
    return a/b

def sayHello():
    print("helloworld")