from pick import pick


# insert following code into Menu class
def navigate_menu():
    """
    Makes navigation of menu possible
    :return: chosen menu option (starts with 1)
    """
    options = ['[Play Game]', '[Quit]']
    option, index = pick(options, indicator='> ')
    # insert function for quit button
    print(' You have chosen ' + option)
    return index+1
