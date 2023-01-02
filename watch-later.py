#USER CONFIG

WATCH_LATER_HTML = 'wl.html' # Path to watch later html file
TXT_FILE = 1 # 0 = no, 1 = yes
CSV_FILE = 0 # 0 = no, 1 = yes

#IMPORT LIBRARIES

from bs4 import BeautifulSoup
import csv


#FUNCTIONS DEFINITIONS

def parse_html(htmlfile):
    page = open(htmlfile, 'r', encoding='utf-8')
    soup = BeautifulSoup(page, 'html.parser')
    links = soup.find_all('a', class_='yt-simple-endpoint style-scope ytd-playlist-video-renderer')

    data = {}

    for link in links:
        x, y = (link['href'], link['title'])
        data[x] = y

    print("HTML Page Parsed Successfully")

    return data

def write_to_txt(data):
    with open('watchlater.txt', 'w', encoding='utf-8') as f:
        for key, value in data.items():
            f.write(f"{key} : {value}\n")
    
    print("TXT File Created Successfully")

def write_to_csv(data):
    with open('watchlater.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Title','Link'])
        for key, value in data.items():
            writer.writerow([value, key])
    
    print("CSV File Created Successfully")

if __name__ == '__main__':
    
    data = parse_html(WATCH_LATER_HTML)

    if TXT_FILE == 1:
        write_to_txt(data)
    
    elif CSV_FILE == 1:
        write_to_csv(data)

    elif TXT_FILE == 0 and CSV_FILE == 0:
        print("Enter valid option")
    