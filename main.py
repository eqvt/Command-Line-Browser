import sys
import os
import glob
import requests

args = sys.argv

if len(args) != 2:
    print("Too many arguments!!")
else:
    directory = args[1]
    if not (os.path.isdir(directory)):
        os.makedirs(directory)


def saveToFile(name):
    with open(f".\\{directory}\\{name[8:]}.txt", 'w', encoding='utf8', errors='replace') as file:
        r = requests.get(name)
        file.write(r.text)
        saved_tabs.append(name[8:name.find('.')])


def read_saved_tabs(name):
    for x in glob.glob(f"{directory}/*"):
        if name[8:] in x:
            found_file = x
    with open(f".\\{found_file}", 'r', encoding='utf8', errors='replace') as file:
        print(file.read())


chosen_url = ""
last_url = ""
saved_tabs = []
history = []

while chosen_url != 'exit':
    chosen_url = input()
    if chosen_url == 'back':
        if len(history):
            try:
                history.pop()
                last = history.pop()
                read_saved_tabs(last)
                continue
            except:
                continue

    elif len(saved_tabs) and chosen_url in saved_tabs:
        read_saved_tabs(chosen_url)
        history.append(chosen_url)

    elif ".com" in chosen_url:
        if chosen_url.startswith("https") == False:
            chosen_url = "https://" + chosen_url
        saveToFile(chosen_url)
        read_saved_tabs(chosen_url)
        history.append(chosen_url)

    else:
        print("error")
