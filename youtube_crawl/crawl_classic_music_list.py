import time
from chrome_webdriver import driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
from tqdm import tqdm

music_dict = {"index": [], "ytid" : [], "periods" : []}

classic_music_youtube = [
{ "periods" : "romantic" ,   "url" : "https://www.youtube.com/playlist?list=PLrn-3oc_hSryG-PcVAX-xXdf0eR_f4thl", "num" : 714},
{ "periods" : "classical",   "url" : "https://www.youtube.com/playlist?list=PLrn-3oc_hSry7_6AHoRT6-1bpoqK5-mHt", "num" : 714},
{ "periods" : "baroque",     "url" : "https://www.youtube.com/playlist?list=PLrn-3oc_hSryDgTE6uD0_UcD7FQGdiVuj", "num" : 714},
{ "periods" : "renaissance", "url" : "https://www.youtube.com/playlist?list=PLrn-3oc_hSrw6wJISwPIddw6pmXLWRe3E", "num" : 714},
{ "periods" : "medieval",    "url" : "https://www.youtube.com/playlist?list=PLrn-3oc_hSrwHfAzBj9Zr-2lEOo7Lxnsj", "num" : 648},
{ "periods" : "modernism",   "url" : "https://www.youtube.com/playlist?list=PLrn-3oc_hSry5JkAW8Uz2Wq4ATg6MJ6OI", "num" : 545} ]

for playlist in classic_music_youtube:
    periods = playlist['periods']
    url = playlist['url']
    num = playlist['num']
    
    driver.get(url=url)
    time.sleep(1)

    # Scroll Down for Crawlling
    actions = driver.find_element(By.CSS_SELECTOR, 'body')
    for i in range(200):
        actions.send_keys(Keys.PAGE_DOWN)

    print(f"{periods} crawlling...")
    for i in tqdm(range(1,num+1)):
        xpath = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-playlist-video-list-renderer/div[3]/ytd-playlist-video-renderer['+str(i)+']/div[2]/div[1]/div/h3/a'
        tmp = driver.find_element(by=By.XPATH, value=xpath)
        youtube_full_url = tmp.get_attribute("href")
        youtube_id = youtube_full_url.split('watch?v=')[-1].split('&list=')[0]

        # print(" ======= Index :", i-1)
        # print("Full url :", youtube_full_url)
        # print("Youtube ID :", youtube_id)

        music_dict["index"].append(i)
        music_dict["ytid"].append(youtube_id)
        music_dict["periods"].append(periods)

df = pd.DataFrame.from_dict(music_dict, orient='columns')
df.to_csv('classical_music_ytid.csv', index=False)