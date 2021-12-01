from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending'

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox') 
  chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument('--headless')
  driver = webdriver.Chrome(options=chrome_options)
  return driver

def get_videos(driver):  
  VIDEO_DIV_TAG = 'ytd-video-renderer'
  driver.get(YOUTUBE_TRENDING_URL)
  videos = driver.find_elements(By.TAG_NAME, VIDEO_DIV_TAG)
  return videos


if __name__ == "__main__":
  print('Creating driver')
  driver = get_driver()

  print('Fetching trending videos')
  videos = get_videos(driver)

  print(f'Found {len(videos)} videos')


  print('Parsing the first video')
  # title, url, thumbnail_url, channel, views, uploaded, description
  video = videos[0]
  title_tag = video.find_element(By.ID, 'video-title')
  title = title_tag.text
  
  url = title_tag.get_attribute('href')

  thumbnail_tag = video.find_element(By.TAG_NAME, 'img')
  thumbnail_url = thumbnail_tag.get_attribute('src')

  channel_div = video.find_element(By.CLASS_NAME, 'ytd-channel-name')
  channel_name = channel_div.text

  description = video.find_element(By.ID, 'description-text').text
  print('Title:', title)
  print('URL:', url)
  print('Thumbnail URL:', thumbnail_url)
  print('Channel Name:', channel_name)
  print('Description:', description)

