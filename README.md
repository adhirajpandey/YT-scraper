# YT-scraper

# Description

This Script allows you to generate structured txt and csv file of Youtube Subscriptions as well as Youtube Watch Later Playlist videos of a user.

This Script uses saved html file of your subscriptions/watch-later page and BeautifulSoup to parse it structurally to implement the objective.
  
# Requirements

- python3
- pip3
- BeautifulSoup
- csv

# Usage

1. Go to `https://www.youtube.com/feed/channels` OR `https://www.youtube.com/playlist?list=WL`(make sure you are logged in) and scroll to bottom of the page.
2. Save html of the page by right-clicking in browser window and select `save as` to download it in your computer.
3. Clone this project `git clone https://github.com/adhirajpandey/YT-scraper` and cd into it `cd YT-subscriptions-scraper`
4. Install Requirement `pip install bs4`
5. Modify `subs.py` or `watch-later.py to modify the path of your saved html file of your page.
6. Run Script
7. Check directory for the output.
8. Edit `clear-playlist.py` as per your need and run it to clear your playlists.

# Sample

1. Download html
  ![htmlpagedwnld](https://user-images.githubusercontent.com/87516052/202515640-75bd0d38-a43f-4dd1-93e3-5010377badc6.png)

2. Clone 
    ![clone](https://user-images.githubusercontent.com/87516052/202512245-2bde5e7e-d9da-45f1-ae03-bf0b75ee4125.png)

3. Install Requirement
    ![installreq](https://user-images.githubusercontent.com/87516052/202512408-2234a80c-2dc1-4a4e-9727-f86cfb970887.png)

4. Edit main.py
    ![editmain](https://user-images.githubusercontent.com/87516052/202512492-5d053a2e-6cd5-415e-b74f-858f79a8f715.png)    

5. Execute main.py
    ![execute](https://user-images.githubusercontent.com/87516052/202512606-d8cdd426-34c9-4797-b9d4-2923280ce72c.png)

6. Generated Files
    ![filesgen](https://user-images.githubusercontent.com/87516052/202512703-9a17bf16-e9dc-4cd0-a8ef-0e62dd86b32a.png)

7. Text File Sample
    ![txtsample](https://user-images.githubusercontent.com/87516052/202512862-821b37c3-7f4b-4ea3-b6cb-e3169914809b.png)

8. CSV File Sample
    ![csvsample](https://user-images.githubusercontent.com/87516052/202512951-866fae34-c3e7-4cc0-8776-0ae90de8c371.png)
