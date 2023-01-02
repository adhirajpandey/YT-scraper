#USER CONFIG

SUBSCRIPTIONS_HTML = 'subs.html' # Path to subscriptions html file
TXT_FILE = 1 # 0 = no, 1 = yes
CSV_FILE = 1 # 0 = no, 1 = yes

#IMPORT LIBRARIES

from bs4 import BeautifulSoup
import csv


#FUNCTION DEFINITIONS

#function to get html file of subscriptions page and return data of channels as a list
def parsehtml(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    channel_data = soup.find_all("div", class_="style-scope ytd-channel-renderer")
    
    channel_names = []
    
    #loop to filter becuase of multiple entries of same data
    for i in range(0, len(channel_data), 11):
        channel_names.append(channel_data[i])
    
    print("Data parsed Successfully")
    
    return channel_names

#function to take channel data(channel_names) and write extracted subscriptions data to a text file(subscriptions.txt)
def write_txt_file(channel_names):
    with open('.//subscriptions.txt', 'w', encoding='utf-8') as f:
        for i in range(0, len(channel_names)):
            
            #defining required attributes
            name = channel_names[i].find("yt-formatted-string", id="text").text
            subs = channel_names[i].find("span", id="subscribers").text
            videos = channel_names[i].find("span", id="video-count").text
            description = channel_names[i].find("yt-formatted-string", id="description").text
            link = channel_names[i].find("a", id="main-link").get('href')
            
            f.write(f"Channel Name: {name}\n")
            f.write(f"Subscribers: {subs}\n")
            f.write(f"Videos: {videos}\n")
            f.write(f"Description: {description}\n")
            f.write(f"Link: {link}\n")
            f.write("\n==============================================================\n")
    
    print("Data written to subscriptions.txt")

#function to take channel data(channel_names) and write extracted subscriptions data to a csv file(subscriptions.csv)
def write_csv_file(channel_names):
    with open('subscriptions.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Channel Name', 'Subscribers', 'Videos', 'Description', 'Link'])
        for i in range(0, len(channel_names)):
            
            #defining required attributes
            name = channel_names[i].find("yt-formatted-string", id="text").text
            subs = channel_names[i].find("span", id="subscribers").text
            videos = channel_names[i].find("span", id="video-count").text
            description = channel_names[i].find("yt-formatted-string", id="description").text
            link = channel_names[i].find("a", id="main-link").get('href')
            
            writer.writerow([name, subs, videos, description, link])
    
    print("Data written to subscriptions.csv")



#MAIN PROGRAM

if __name__ == "__main__":
    
    html = open(SUBSCRIPTIONS_HTML, encoding='utf-8').read()

    channel_names = parsehtml(html)

    if TXT_FILE == 1:
        write_txt_file(channel_names)
    
    if CSV_FILE == 1:
        write_csv_file(channel_names)
    
    if TXT_FILE == 0 and CSV_FILE == 0:
        print("Enter valid option")
    
    print("Program executed successfully")

