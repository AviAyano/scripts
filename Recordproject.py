# -*- coding: utf-8 -*-

import time
import sys
import copy
from termcolor import cprint
print_red_bold = lambda x: cprint(x, 'red', attrs=['bold'])
print_bold = lambda x: cprint(x, attrs=['bold'])

class Format:
    end = '\033[0m'
    underline = '\033[4m'

def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

def input_style(name):
    return name.strip().lower().title()

def introduction_print():
    typingPrint("Hello & Welcome...\n")
    time.sleep(1)
    typingPrint("This is Tech Career's record list project...\n")
    time.sleep(1)

def pos_update_massage(ans):
    print_bold("\nThe record has been successfully {}!".format(ans))
    print_bold("\nCurrent playlist :")

def neg_update_massage(ans1):
    print_bold("\nNo {} to the playlist was made!!".format(ans1))

def Error_Select():
    print_red_bold("\nERROR - Please select a valid choice From the Menu!! ")

def Error_print2():
    print_red_bold(Format.underline + "\nUser Error:" + Format.end)
    print_red_bold("please enter a valid (int) number! above zero!!")
    print_red_bold("or insert 0, to return to the Playlist menu..\n")

def Error_print(ans):
    print_red_bold(Format.underline + "\nUser Error:" + Format.end)
    print_red_bold("Please Enter a valid number between 1-{}".format(ans))
    print_red_bold("or insert 0, to return to the Playlist menu..\n")

def print_function(name):
    print_bold("\nYou have chosen to {} record('s).\n".format(name))
    print("Would you like to...\n1.Continue.\n2.Return to top menu.")
    print("Insert Your choice:  ",end="")
    ans = input_style(input())
    if ans == "1":
        print_bold("...")
    elif ans == "2":
        print_bold("...")
    else:
        Error_Select()
    return ans

def no_playlist():
    print_red_bold("No playlist available!!")

def search_engine(musician_name, record_name, playlist):
    playlist_key = repr([musician_name, record_name])
    if playlist_key in playlist.keys():
        return True
    else:
        return False

def playlist_status(empty_print_string,print_string,playlist):
     if not playlist:
        print_bold(empty_print_string)
     else:
        print(print_string, playlist)

def add_record(musician_name, record_name, Record_Quantity, playlist):
    playlist_key = repr([musician_name, record_name])
    playlist_copy = copy.deepcopy(playlist)
    old_record_quantity = playlist_copy.get(playlist_key)
    if not search_engine(musician_name, record_name, playlist_copy):
        playlist_copy.update({repr([musician_name, record_name]): Record_Quantity})
        pos_update_massage("added")
        print(playlist_copy)
    elif search_engine(musician_name, record_name, playlist_copy):
        if Record_Quantity != old_record_quantity:
            playlist_copy.update({playlist_key: Record_Quantity})
            pos_update_massage("updated")
            print(playlist_copy)
        elif Record_Quantity == old_record_quantity:
            neg_update_massage("update")
    return playlist_copy

def delete_record(musician_name, record_name, amount_to_delete, playlist):
    playlist_key = repr([musician_name, record_name])
    while search_engine(musician_name, record_name, playlist):
        deleted_records = playlist.get(playlist_key) - amount_to_delete
        if deleted_records == 0:
            playlist.pop(playlist_key)
            if not playlist:
                print_bold("\nPlaylist deleted!!")
                print_bold("Please create a new playlist.")
            elif playlist:
                print_bold("\nThe Record(s) Has been deleted From the playlist")
                print_bold("\nCurrent playlist:")
                print(playlist)
            break
        else:
            Quantity_update(musician_name, record_name, deleted_records,amount_to_delete ,playlist)
            print_bold("\n{} Record(s) Had been deleted !\nCurrent playlist:  ".format(amount_to_delete))
            print(playlist)
        break
    return playlist

def search_by_name(musician_name, record_name, playlist):
    playlist_key = repr([musician_name, record_name])
    if search_engine(musician_name, record_name, playlist):
        print_bold("\nThe requested record:")
        print(playlist_key, ":", playlist[playlist_key])
    else:
        print_bold("\nThe entered record does not exist in the playlist!\n")

def Update_Name(new_musician_name, new_record_name, Record_Quantity, playlist):
    new_key = repr([new_musician_name, new_record_name])
    playlist.update({new_key: Record_Quantity})
    return playlist

def name_status(flag,new_key,record_quantity,playlist ):
    if flag:
        print_bold("\nThe name has been updated successfully!! ")
        print_bold("Updated Record's Name: ")
        print("{", '"', new_key, ":", record_quantity, '"', "}", sep="")
    else:
        print_red_bold(Format.underline + "\nUser Error:" + Format.end)
        print_red_bold("\nThe name already exists in the playlist!!")
        print_red_bold("Key elements (i.e, record name & and musician's name) must be unique")

def Quantity_update(musician_name, record_name, new_record_quantity, old_record_quantity, playlist):
    playlist_key = repr([musician_name, record_name])
    if new_record_quantity == old_record_quantity:
        print_bold("\nNo quantity update has been made")
        print_bold("Current Record Quantity: ")
        print("{", '"', [musician_name, record_name], '"', ":", old_record_quantity, "}",
              sep="")
    else:
        print_bold("\nRecord quantity updated successfully!\n")
        print_bold("updated Record Quantity: ")
        print("{", '"', [musician_name, record_name], '"', ":", new_record_quantity, "}",
              sep="")
    return playlist.update({playlist_key: new_record_quantity})

def Total_amount(playlist):
    print("\nThe total Quantity of copies available is : ", sum(playlist.values()))
    print("shared between:", len(playlist), "Record('s)")

def Sorted_Playlist(playlist):
    for key, value in sorted(playlist.items()):
        print(key, value)

def Exit():
    time.sleep(1)
    typingPrint("\nThank you..see you next time!\n")
    typingPrint("The Program will shut itself in 3..")
    time.sleep(1)
    typingPrint("2..")
    time.sleep(1)
    typingPrint("1..")
    time.sleep(1)
    print("\nGood Bye!")

def Top_menu():
    print_bold(Format.underline + "\nPlaylist Menu:" + Format.end)
    print_bold("""
    1. Add/update a record
    2. Delete a record
    3. Search by name
    4. Update record's name
    5. Update quantity of copies 
    6. Total copies available
    7. Sorted Playlist (A-Z)
    8. Exit the program""")
    time.sleep(1)

introduction_print()
def main():
    playlist = {}
    do_continue = True
    while do_continue:
        Top_menu()
        user_select = input_style(input("\nplease choose an option From The Playlist Menu: "))
        if user_select == '1':
            ans = print_function("add/update")
            if ans in ["Continue", "1"]:
                playlist_status("To add a record, please enter the following details!\n"," current playlist:\n",playlist)
                musician_name = input_style(input("Please insert the Musician's name: "))
                record_name = input_style(
                    input("Please insert the record's name: "))
                if playlist:
                    search_by_name(musician_name, record_name, playlist)
                while True:
                    try:
                        record_quantity = int(input("Please insert the Record's Quantity: "))
                        if record_quantity == 0:
                            neg_update_massage("addition")
                            break
                        elif record_quantity < 0:
                            raise ValueError
                    except ValueError:
                        Error_print2()
                    else:
                        playlist = add_record(musician_name, record_name, record_quantity, playlist)
                        break

        elif user_select == '2':
            if playlist:
                ans = print_function("delete")
                if ans in ["Continue", "1"]:
                    print("Current playlist:\n", playlist)
                    musician_name = input_style(input("Please insert the Musician's name: "))
                    record_name = input_style(input("\nPlease insert the record's name: "))
                    search_by_name(musician_name, record_name, playlist)
                    playlist_key = repr([musician_name, record_name])
                    old_record_amount = playlist.get(playlist_key)
                    if search_engine(musician_name, record_name, playlist):
                        while True:
                            try:
                                amount_to_delete = int(
                                    input("\nPlease enter the amount of records you want to delete: "))
                                if amount_to_delete == 0:
                                    neg_update_massage("deletion")
                                    break
                                elif amount_to_delete < 0 or amount_to_delete > old_record_amount :
                                    raise ValueError
                            except ValueError:
                                Error_print(old_record_amount)
                            else:
                                delete_record(musician_name, record_name, amount_to_delete, playlist)
                                break
            else:
                no_playlist()

        elif user_select == '3':
            if playlist:
                ans = print_function("search")
                if ans in ["Continue", "1"]:
                    musician_name = input_style(input("Please insert the Musician's name: "))
                    record_name = input_style(
                        input("\nPlease insert the record's name: "))
                    search_by_name(musician_name, record_name, playlist)
            else:
                no_playlist()

        elif user_select == '4':
            if playlist:
                ans = print_function("update the name of a")
                if ans in ["Continue", "1"]:
                    print("Current playlist:\n", playlist)
                    musician_name = input_style(input("Please insert the Musician's name: "))
                    record_name = input_style(input("\nPlease insert the record's name: "))
                    search_by_name(musician_name, record_name, playlist)
                    old_playlist_key = repr([musician_name, record_name])
                    if search_engine(musician_name, record_name, playlist):
                        new_record_name = input_style(input("\nPlease insert the Record's new name: "))
                        new_key = repr([musician_name, new_record_name])
                        record_quantity = playlist.get(old_playlist_key)
                        if new_key not in playlist:
                            playlist[new_key] = playlist.pop(old_playlist_key)
                            name_status(True,new_key, record_quantity, playlist)
                        else:
                            name_status(False,new_key, record_quantity, playlist)
            else:
                no_playlist()

        elif user_select == '5':
            if playlist:
                ans = print_function("Update quantity to")
                if ans in ["Continue", "1"]:
                    print("The Current Playlist:", playlist)
                    musician_name = input_style(input("Please insert the Musician's name: "))
                    record_name = input_style(input("\nPlease insert the record's name: "))
                    search_by_name(musician_name, record_name, playlist)
                    playlist_key = repr([musician_name, record_name])
                    old_record_quantity = playlist.get(playlist_key)
                    if search_engine(musician_name, record_name, playlist):
                        while True:
                            try:
                                new_record_quantity = int(input("Please enter the new quantity of records : "))
                                if new_record_quantity < 0:
                                   raise ValueError
                                elif new_record_quantity == 0:
                                    print_bold("No quantity update was made\n")
                                    break
                            except ValueError:
                                Error_print2()
                            else:
                                Quantity_update(musician_name, record_name, new_record_quantity,old_record_quantity, playlist)
                                break
            else:
                no_playlist()

        elif user_select == '6':
            if playlist:
                print_bold(" current playlist:\n")
                print(playlist)
                Total_amount(playlist)
            else:
                no_playlist()

        elif user_select == '7':
            if playlist:
                print_bold(Format.underline + " Sorted Playlist:\n" + Format.end)
                Sorted_Playlist(playlist)

            else:
                no_playlist()

        elif user_select == '8':
            Exit()
            do_continue = False

        else:
            Error_Select()

main()





