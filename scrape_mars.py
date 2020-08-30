from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    dictionary_mars = {}

    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)

    html = browser.html
    news_soup = bs(html, "html.parser")
    results = news_soup.select_one('ul.item_list')


    news_title=results.find('div', class_='content_title').text
    news_p=results.find('div', class_='article_teaser_body').text


    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)

    browser.click_link_by_partial_text('FULL IMAGE')

    browser.click_link_by_partial_text('more info')

    featured_image_html=browser.html  
    feature_image_soup=bs(featured_image_html, 'html.parser')

    image=feature_image_soup.find('figure', class_='lede')
    image_1=image.find('a')
    featured_image=image_1.attrs['href']

    feature_img_url=f"https://www.jpl.nasa.gov{featured_image}"

    time.sleep(2)
    table_url = "https://space-facts.com/mars/"
    tables = pd.read_html(table_url)
    
    
    df = tables[2]
    df.columns = ['Description', 'Value']
    
    table_html=df.to_html()
    table_html.replace('\n', '')

    
    Mars_moons_url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(Mars_moons_url) 
    mars_moons_html=browser.html  
    mars_moons_soup=bs(mars_moons_html, 'html.parser')
    mars_list=mars_moons_soup.find_all('div', class_='item')

    hemisphere_img_urls=[]
    for x in mars_list:
        browser.visit(Mars_moons_url) 
        mars_moons_html=browser.html  
        moon_heading=x.find('h3').text
        browser.click_link_by_partial_text(moon_heading)
        #obtaining the imag_ur;
        moon_img_html=browser.html  
        moon_img_soup=bs(moon_img_html, 'html.parser')
        moon_img=moon_img_soup.find('div', class_='wide-image-wrapper')
        moon_img_url=moon_img.li.a.get('href')
        #getting rid of the Enhanced heading to append to the dictionary
        moon_title=moon_heading.replace("Enhanced", "")
        moon_dict={
        "title":moon_title, "img_url":moon_img_url
        }
    
        hemisphere_img_urls.append(moon_dict)
    
    time.sleep(3)
    dictionary_mars={
    "news_title": news_title, 
    "news_p": news_p,
    "feature_url": feature_img_url,
    "table_string" : str(table_html),
    "hemisphere_img_url":hemisphere_img_urls
    }

    

    browser.quit()

    print(dictionary_mars)

    return(dictionary_mars)

