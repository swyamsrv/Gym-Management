# Project on GYM MANAGEMENT


import time
import os
from os import path


def page1():
    """The First Viewed Page!!"""
    i = 0
    while i not in range(1, 6):
        print("CHOOSE YOURS CHOICE!")
        if i in range(1, 6):  # Termination Condition
            break
        elif i not in range(1, 6):  # Input Data
            i = int(input('Admit -> 1\nRetrieve -> 2\nAlready Exist -> 3\nLeave Membership -> 4\nExit -> 5\n'))
            time.sleep(2)
    return i


def page2():
    """This Function takes the name of the user!"""
    member = input("**********Enter the name of the person**********\n")
    member = member.title()
    return member


def directory_creation():

    """If we want to confirm that a given path points to a directory, we can use the 'os.path.dir()',
        'os.mkdirs(name)': This function creates a new directory labeling with the given name."""

    if os.path.isdir('C:Users//My_GYM'):  # Detect the path of the directory
        return
    else:
        os.makedirs('C:Users//My_GYM')


def admit(name):

    yes_no = input('Are you Sure you want to add {}, In your GYM\n'
                   'Enter (Y) for "YES" & (N) for "NO"->'.format(name))
    global i
    i = 0
    if yes_no[0].lower() == 'y':
        file_creation(name)
    elif yes_no[0].lower() == 'n':
        return
    else:
        print('\nPlease enter a valid response\n')
        admit(name)  # Recursion if wrong option was choose!!


def file_creation(nam):

    """This function will create a file specific to that person who had joined the gym"""

    fil = open('C:Users//My_GYM//{}.txt'.format(nam.lower()), 'w+')
    time.sleep(3)
    print('{} has been admitted in our Gym successfully\n'.format(nam))


def retrieve(_name):

    """This Funcrtion will provide you the details of the person in the gym!!"""
    yes_no = input('Do you want to Retrieve the details of {}?\n'
                   'Enter (Y) for "YES" & (N) for "NO"->'.format(_name))
    global i
    i = 0
    if yes_no[0].lower() == 'y':
        file_retrieval(_name)
    elif yes_no[0].lower() == 'n':
        return
    else:
        print('\nPlease enter a valid response\n')
        admit(_name)


def file_retrieval(nam):

    """This funcrtion will provoide you the details of the required person!!!"""

    if os.path.isfile('C:Users//My_GYM//{}.txt'.format(nam.lower())):
        time.sleep(2)
        fil = open('C:Users//My_GYM//{}.txt'.format(nam.lower()), 'r')
        print(fil.read())
    else:
        print('No Data Found\nPlease Enter a Valid name\nTry Again\n')


def exist(_name):
    """This function is for the Members of the GYM who needs to add the details of diet and Exercise"""

    if os.path.isfile('C:Users//My_GYM//{}.txt'.format(_name.lower())):
        exe_diet = 0
        while exe_diet not in range(1, 3):
            exe_diet = int(input('What do you wanna conclude\nExercise -> 1\n\rDiet ->2\n'))
            if exe_diet in range(1, 3):
                break
            elif exe_diet != 1 or exe_diet != 2:
                print('Please Enter a valid option\n')
        return exe_diet  # Either value 1 or 2!!
    else:
        print("This Person is not our gym\n")
        return


def file_edit(nam, exe_diet):

    """Main task of adding up the data is done by this function only!!"""

    global i
    i = 0
    fil = open('C:Users//My_GYM//{}.txt'.format(nam.lower()), 'a')
    tim = getdate()  # Use to grab the correct time at which he or she took a diet or Exercise!!
    if exe_diet == 1:
        fil.write('--------------------------------------------------\n'
                  'Exercise:\n{}:-> {}\n'
                  '--------------------------------------------------\n'.format(tim, exercise()))
    if exe_diet == 2:
        fil.write('--------------------------------------------------\n'
                  'Diet: \n{}:-> {}\n'
                  '--------------------------------------------------\n'.format(tim, food()))
    fil.close()


def getdate():
    """Will provide the current time"""
    import datetime
    t = str(datetime.datetime.now())
    return t[:16]  # 2022-07-14 02:32 -> In this form


def exercise():
    """Exercise done by person!"""
    _exe = input("Enter the EXERCISE you've done\n")
    return _exe


def food():
    """Diet taken by person """
    _food = input("Enter the Diet you've taken \n")
    return _food


def leave_gym(nam):
    """The Person who wants to leave the GYM!!"""
    global i
    i = 0
    if os.path.isfile('C:Users//My_GYM///{}.txt'.format(nam.lower())):
        os.remove('C:Users//My_GYM///{}.txt'.format(nam.lower()))
        print('{} has left your Gym\n'.format(nam.title()))
    else:
        print('This person is not in our gym\n')
    print('Your Record has been updated\n')


if __name__ == '__main__':

    print('Hello! This is your GYM Management\n')
    i = 0
    while i not in range(1, 6):
        i = page1()
        if i == 5:
            break  # Exit Condition

        member_name = page2()
        directory_creation()  # This will create a folder only for initial process
        if i == 1:
            admit(member_name)
        elif i == 2:
            retrieve(member_name)
        elif i == 3:   # For the members of the GYM!
            exe_diet = exist(member_name)
            file_edit(member_name, exe_diet)
        elif i == 4:
            leave_gym(member_name)

    print('Thank you\n')








