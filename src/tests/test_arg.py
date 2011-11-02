
def test_args(farg = None, *args, **kwargs ):
    print "formal arg:", farg
    
    print "args:", args 
    for arg in args:
        print "args:", arg

    print "kwargs:", kwargs
    for key in kwargs:
        print "kwargs: %s: %s" % (key, kwargs[key])
        

test_args(1, "two", 3)

test_args(farg=1, myarg2="two", myarg3=3)

args = ("two", 3)
test_args(1, *args)


kwargs = {"arg3": 3, "arg2": "two"}
test_args(1, **kwargs)

#Incluso los argumentos formales pueden ser enviados en la coleccion

kwargs = {"farg": 3, "arg2": "two"}
test_args( **kwargs)

