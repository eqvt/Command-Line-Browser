import sys
import os
import glob

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# write your code here


def saveToFile(name):
    with open(f".\\{directory}\\{name}.txt", 'w') as file:
        if name == "bloomberg.com":
            file.write(bloomberg_com)
        elif name == "nytimes.com":
            file.write(nytimes_com)

        saved_tabs.append(name[:name.find('.')])


def check_saved_tabs(name):
    try:
        open(f".\\{directory}\\{name}.txt", 'r')
    except:
        return False
    return True


def read_saved_tabs(name):
    for name in glob.glob(f"{directory}/*"):
        found_file = name
    with open(f".\\{found_file}", 'r') as file:
        print(file.read())


def check_validity_of_url(url):
    result = False
    if "." not in url:
        if url not in saved_tabs:
            print("error")
            return True
    return result


saved_tabs = []
args = sys.argv
if len(args) != 2:
    print("Too many arguments!!")
else:
    directory = args[1]
    if not (os.path.isdir(directory)):
        os.makedirs(directory)
    while True:
        chosen_url = input()
        if "." not in chosen_url:
            if chosen_url not in saved_tabs:
                print("error")
        if chosen_url == "exit":
            break
        elif ".com" in chosen_url:
            if check_saved_tabs(chosen_url) == False:
                saveToFile(chosen_url)
                read_saved_tabs(chosen_url)
        elif chosen_url in saved_tabs:
            read_saved_tabs(chosen_url)
