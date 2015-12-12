from sys import argv

message = ''
     
def get_message():

    if len(argv) == 1:
        message = raw_input('enter message: ') 
    else:
       message = argv[1]
  
    return message

