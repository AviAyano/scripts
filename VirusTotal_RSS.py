import requests
import time
import json
import csv
import feedparser

def api():
    api_key = '8f4b2c50b9a2aa70971752338635d0c8dcb380aacf6e51c25fda4d603296bb86'
    return api_key
def menu():
    print("""
    1. Search hash
    2. RSS feed - Date & Title
    3. RSS feed - Full report
    4. Exit the program""")
    time.sleep(1)
def select():
    answer = input("Would you like to...\n1.Continue.\n2.Return to menu.")
    return answer
def error():
    print("\nERROR - please select a valid choice from the menu. ")
def errors():
    print("\nERROR - No matches found !\nAre you looking for advanced malware searching capabilities? \nVT Intelligence can help https://www.virustotal.com/gui/intelligence-overview")
def exit():
    time.sleep(1)
    print("\nThank you..see you next time!\n")
def main():
    url_temp ="https://www.virustotal.com/api/v3/files"
    do_continue = True
    while do_continue:
        menu()
        user_select = input("\nPlease choose an option : ")
        if user_select == '1':
            answer = select()
            if answer in ["Continue", "1"]:
                indicator = input("\nEnter your Hash please : ")
                headers = {
                    "Accept": "application/json",
                    "x-apikey": api()
                }
                url = url_temp +"/" + indicator
                response = requests.request("GET", url, headers=headers)
                try:
                    response_json = json.loads(response.content)
                    if response_json["data"]["attributes"]["last_analysis_stats"]["malicious"]>= 50 or  response_json["data"]["attributes"]["last_analysis_results"]["Microsoft"]["category"] == "malicious":
                        if "Check_Point" in response_json["data"]["attributes"]["last_analysis_results"] :
                            if response_json["data"]["attributes"]["last_analysis_results"]["Check_Point"]["category"] == "malicious":
                                print("Malicious!   [ included Check Point engine. ]")
                        else:
                            print("Malicious.")
                    else:
                        print("Undetected.")
                except Exception:
                    errors()
        elif user_select == '2':
            answer = select()
            if answer in ["Continue", "1"]:
                check_point_feed = feedparser.parse("https://research.checkpoint.com/feed/")
                entry = check_point_feed.entries[1]
                print(" Research Date:",entry.published,"\n","Research Title:",entry.title)
        elif user_select == '3':
            answer = select()
            if answer in ["Continue", "1"]:
                check_point_feed = feedparser.parse("https://research.checkpoint.com/feed/")
                entry = check_point_feed.entries[1]
                if "IOCs" in entry.keys():
                    columns = ['Date', 'Title', 'Ioc_Type', 'IOC']
                    data = entry.IOCs
                    with open('iocs.csv', 'w', encoding='UTF8', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow(columns)
                        writer.writerow(data)
                print(entry.keys())
                print(" Summary Report:\n",entry.summary)
        elif user_select == '4':
            exit()
            do_continue = False
        else:
            error()

main()