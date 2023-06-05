from database import (input_data, 
                        view_every_entry, 
                        view_single_entry,
                        modify_entry)

menu = """
Welcome to the Diary room, press
1) To insert new entries into the diary
2) View all entries in the diary
3) View single entry in the diary
4) To modify entries in the diary
5) To delete entries from the diary
6) Exit
"""

def add_entry():
    """
    Function that adds new entries to our diary by inputing
    the date an event occured, the topic and the event.
    """
    date = input("On what day did the event occur? (YYYY-MM-DD): ")
    topic = input("What's the topic? ")
    event = input("What is on your mind? ")
    input_data(date, topic, event)

def view_all_diary():
    """
    Function that displays all the records in our diary
    """
    print(view_every_entry())

def view_single_topic():
    """
    Function that requests for the topic you want to display
    """
    topic = input("What topic do you want to view? ")
    data = view_single_entry(topic)
    title = data[0][3]
    date = data[0][1]
    event = data[0][4]
    display = f"""
    Topic: {title}
    Date: {date}
    Event: {event}
    """
    print(display)
    # print(data)



def edit_diary():
    """
    Function that requests for the topic you want to modify
    """
    topic = input("What topic do you want to modify? ")
    new_date = input("Enter the new date: ")
    new_topic = input("Enter the new topic:  ")
    new_event = input("Enter the new event: ")
    modify_entry(topic, new_date, new_topic, new_event)


def delete_entry():
    pass


while True:
    print(menu)
    user_input = input()
    if user_input == '1':
        add_entry()
    elif user_input == '2':
        view_all_diary()
    elif user_input == '3':
        view_single_topic()
    elif user_input == '4':
        edit_diary()
    elif user_input == '5':
        delete_entry()
    elif user_input == '6':
        print('Thank You and Good Bye!\n')
        break
    else:
        print("Invalid Input\n")