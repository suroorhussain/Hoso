import argparser
import application_control

def get_channels():
    return raw_input("Please enter the channels seperated by commas: ").split(',')

def get_msg():
    return raw_input("Please enter your status update: ")


if argparser.args.message is not None:
    message = argparser.args.message
else:
    message = get_msg()

if argparser.args.channels is not None:
    selected_channels = argparser.args.channels
else:
    selected_channels = get_channels() 

user = application_control.login('terminal_user', 'password')
while True:
    application_control.select_channels(selected_channels, user)
    try:
        user.send_message(message, application_control.selected_channels)
    except Exception as e:
        print "The following errors occured\n {}".format(e)
        
    c = raw_input("Would you like to make another update? (y/n): ")

    if c == 'y':
        print "1.use same channels \t 2.select new channels"
        action = raw_input('>>>')
        if action == '1':
            print "posting to {}".format(','.join(application_control.selected_channels))
        elif action == '2':
            selected_channels = get_channels()

        message = get_msg()
    else:
        break

for channel in user.registered_channels:
    user.remove_channel(channel)

application_control.logout(user)
            
