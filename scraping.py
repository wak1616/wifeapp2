from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import os

def get_all_spotify_podcasts():
    chrome_options = Options()
    # Runs Chrome in headless mode (no GUI)
    chrome_options.add_argument("--headless")
    # Disables GPU acceleration - helps with headless mode stability
    chrome_options.add_argument("--disable-gpu")
    # Disables the sandbox for running in certain environments (like Docker)
    chrome_options.add_argument("--no-sandbox")
    # Helps prevent memory issues in Docker/Linux. Uses /tmp instead of /dev/shm
    chrome_options.add_argument("--disable-dev-shm-usage")
    # Sets a specific user agent to look like a regular browser to help the host from blocking.
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
    
    # Add binary location if set in environment
    if os.environ.get('GOOGLE_CHROME_BIN'):
        chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
    
    chrome_driver_path = os.environ.get('CHROMEDRIVER_PATH', 'chromedriver')
    service = Service(executable_path=chrome_driver_path)
    
    # Pass the service object to Chrome
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Sets a standard desktop resolution to ensure consistent rendering of responsive websites.
    driver.set_window_size(1920, 1080)

    # Initialize results dictionary (which will be a dictionary of lists of dictionaries)
    results = {
        'top_podcasts': [],
        'top_episodes': [],
        'health_fitness': []
    }

    try:
        # Get Top Podcasts
        print("Getting Top Podcasts...")
        driver.get("https://podcastcharts.byspotify.com/")
        results['top_podcasts'] = scrape_current_page(driver)

        # Get Top Episodes
        print("\nGetting Top Episodes...")
        category_dropdown = driver.find_element("id", "categoryDropdown")
        category_dropdown.click()
        time.sleep(2)
        episodes_button = driver.find_element("xpath", "//span[contains(text(), 'Top Episodes')]")
        episodes_button.click()
        time.sleep(2)
        results['top_episodes'] = scrape_current_page(driver)

        # Get Top Health & Fitness Podcasts
        print("\nGetting Health & Fitness...")
        category_dropdown = driver.find_element("id", "categoryDropdown")
        category_dropdown.click()
        time.sleep(2)
        fitness_button = driver.find_element("xpath", "//span[contains(text(), 'Health & Fitness')]")
        fitness_button.click()
        time.sleep(2)
        results['health_fitness'] = scrape_current_page(driver)

    finally:
        driver.quit()

    return results

def scrape_current_page(driver):
    # Scroll page
    print("Scrolling page...")
    # Scroll down and then back up to trigger lazy loading
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)

    # Get the page source
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    podcast_items = soup.find_all('div', class_="Show_show__jq9gl Show_show__default__2x1b_")
    
    podcast_list = []
    
    if podcast_items:
        for item in podcast_items[:10]:  #For Top 10 Podcasts
            img = item.find('img') if item else None
            title = img['alt'] if img else None
            rank = item.find('div', class_="Rank_rank__75HTS Rank_rank__default__YGig9 text-lg md:text-3xl") if item else None
            link = item.find('a') if item else None
            episode_div = item.find('div', class_="mt-1 md:mt-0 w-full lg:w-3/4 text-left text-sm md:text-xl md:pt-1 leading-tight md:leading-none text-accent0") if item else None
            episode = episode_div.get_text().strip().replace('…', '') if episode_div else None

            podcast_info = {
                'episode': episode if episode else 'No episode',
                'title': title if title else 'No title',
                'rank': rank.text.strip() if rank else 'No rank',
                'image': img['src'] if img else 'No image',
                'link': link['href'] if link else 'No link'
            }
            
            # Add to list
            podcast_list.append(podcast_info)
            
            # Print for debugging
            print("\nPodcast:")
            print(f"Episode: {podcast_info['episode']}")
            print(f"Title: {podcast_info['title']}")
            print(f"Rank: {podcast_info['rank']}")
            print(f"Image: {podcast_info['image']}")
            print(f"Link: {podcast_info['link']}")
            print("-" * 40)
            
    return podcast_list  # Returns a list of dictionaries

if __name__ == "__main__":
    all_podcasts = get_all_spotify_podcasts()
    print("\nAll results:")
    print(f"Top Podcasts: {len(all_podcasts['top_podcasts'])} items")
    print(f"Top Episodes: {len(all_podcasts['top_episodes'])} items")
    print(f"Health & Fitness: {len(all_podcasts['health_fitness'])} items")
