import dia

def hello_callback(data, flags):
    dia.message(2, "Hello, World!\n")
   
dia.register_callback("Hello World", "<Display>/Tools/Hello", hello_callback)