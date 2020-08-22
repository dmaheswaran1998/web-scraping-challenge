{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup as bs \n",
    "import requests\n",
    "from splinter import Browser\n",
    "from webdriver_manager.chrome import ChromeDriverManager \n",
    "import pandas as pd\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "# open chrome driver browser\n",
    "executable_path = {'executable_path':'/usr/local/bin/chromedriver'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "#URL of webpage to be scraped\n",
    "url =\"https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest\"\n",
    "\n",
    "# Retrieve page with the requests module\n",
    "browser.visit(url)\n",
    "\n",
    "#getting the browser html\n",
    "html=browser.html  \n",
    "soup=bs(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Celebrate Mars Reconnaissance Orbiter's Views From Above\n",
      "Marking its 15th anniversary since launch, one of the oldest spacecraft at the Red Planet has provided glimpses of dust devils, avalanches, and more.\n"
     ]
    }
   ],
   "source": [
    " # using find (not find_all) only for soup to get the first results \n",
    "\n",
    "results = soup.find('div', class_='list_text')\n",
    "\n",
    "news_title=results.find('div', class_='content_title').text\n",
    "news_p=results.find('div', class_='article_teaser_body').text\n",
    "print(news_title)\n",
    "print(news_p)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "time.sleep(5)\n",
    "#URL of second webpage to be scraped to be scraped\n",
    "url =\"https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars\"\n",
    "\n",
    "# Retrieve page with the requests module\n",
    "browser.visit(url)\n",
    "\n",
    "#using button feature to click on full image\n",
    "browser.click_link_by_partial_text('FULL IMAGE')\n",
    "\n",
    "browser.click_link_by_partial_text('more info')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "#using web-scraping to obtain the url of the image\n",
    "html=browser.html  \n",
    "soup=bs(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "image=soup.find('figure', class_='lede')\n",
    "image_1=image.find('a')\n",
    "image_url=image_1.attrs['href']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "featured_image_url=f\"https://www.jpl.nasa.gov{image_url}\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA09320_hires.jpg\n"
     ]
    }
   ],
   "source": [
    "print(featured_image_url)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Mars Facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "time.sleep(5)\n",
    "url=\"https://space-facts.com/mars/\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "tables = pd.read_html(url)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[                      0                              1\n",
      "0  Equatorial Diameter:                       6,792 km\n",
      "1       Polar Diameter:                       6,752 km\n",
      "2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
      "3                Moons:            2 (Phobos & Deimos)\n",
      "4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
      "5         Orbit Period:           687 days (1.9 years)\n",
      "6  Surface Temperature:                   -87 to -5 °C\n",
      "7         First Record:              2nd millennium BC\n",
      "8          Recorded By:           Egyptian astronomers,   Mars - Earth Comparison             Mars            Earth\n",
      "0               Diameter:         6,779 km        12,742 km\n",
      "1                   Mass:  6.39 × 10^23 kg  5.97 × 10^24 kg\n",
      "2                  Moons:                2                1\n",
      "3      Distance from Sun:   227,943,824 km   149,598,262 km\n",
      "4         Length of Year:   687 Earth days      365.24 days\n",
      "5            Temperature:    -153 to 20 °C      -88 to 58°C,                       0                              1\n",
      "0  Equatorial Diameter:                       6,792 km\n",
      "1       Polar Diameter:                       6,752 km\n",
      "2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
      "3                Moons:            2 (Phobos & Deimos)\n",
      "4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
      "5         Orbit Period:           687 days (1.9 years)\n",
      "6  Surface Temperature:                   -87 to -5 °C\n",
      "7         First Record:              2nd millennium BC\n",
      "8          Recorded By:           Egyptian astronomers]\n"
     ]
    }
   ],
   "source": [
    "print(tables)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Description</th>\n",
       "      <th>Value</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Equatorial Diameter:</td>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Polar Diameter:</td>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Orbit Distance:</td>\n",
       "      <td>227,943,824 km (1.38 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Orbit Period:</td>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Surface Temperature:</td>\n",
       "      <td>-87 to -5 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>First Record:</td>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Recorded By:</td>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Description                          Value\n",
       "0  Equatorial Diameter:                       6,792 km\n",
       "1       Polar Diameter:                       6,752 km\n",
       "2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       "3                Moons:            2 (Phobos & Deimos)\n",
       "4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       "5         Orbit Period:           687 days (1.9 years)\n",
       "6  Surface Temperature:                   -87 to -5 °C\n",
       "7         First Record:              2nd millennium BC\n",
       "8          Recorded By:           Egyptian astronomers"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = tables[2]\n",
    "df.columns = ['Description', 'Value']\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [],
   "source": [
    "table_html=df.to_html()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Mars Hemisphere"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/Users/dhanyamaheswaran/opt/anaconda3/lib/python3.7/site-packages/splinter/driver/webdriver/__init__.py:528: FutureWarning: browser.find_link_by_partial_text is deprecated. Use browser.links.find_by_partial_text instead.\n",
      "  FutureWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Cerberus Hemisphere Enhanced\n"
     ]
    }
   ],
   "source": [
    "#Cereberus Image\n",
    "#URL of second webpage to be scraped to be scraped \n",
    "time.sleep(5)\n",
    "url =\"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n",
    "\n",
    "# Retrieving the browser url\n",
    "browser.visit(url)\n",
    "\n",
    "#Getting the title for the Cereberus Hemisphere Enhanced\n",
    "\n",
    "#using button feature to click on full image\n",
    "browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')\n",
    "\n",
    "html=browser.html  \n",
    "soup=bs(html, 'html.parser')\n",
    "\n",
    "#Obtaining the title \n",
    "cereberus= soup.find('div', class_='content')\n",
    "cereberus_title= cereberus.find('h2').text\n",
    "print(cereberus_title)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg\n"
     ]
    }
   ],
   "source": [
    "cereberus_img= soup.find('div', class_='wide-image-wrapper')\n",
    "cereberus_img_url=cereberus_img.li.a.get('href')\n",
    "print(cereberus_img_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Schiaparelli Hemisphere Enhanced\n"
     ]
    }
   ],
   "source": [
    "#Schiaparelli Image\n",
    "#URL of second webpage to be scraped to be scraped \n",
    "time.sleep(5)\n",
    "url =\"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n",
    "\n",
    "# Retrieving the browser url\n",
    "browser.visit(url)\n",
    "\n",
    "#Getting the title for the Cereberus Hemisphere Enhanced\n",
    "\n",
    "#using button feature to click on full image\n",
    "browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')\n",
    "\n",
    "html=browser.html  \n",
    "soup=bs(html, 'html.parser')\n",
    "\n",
    "#Obtaining the title \n",
    "schiaparelli= soup.find('div', class_='content')\n",
    "schiaparelli_title= schiaparelli.find('h2').text\n",
    "print(schiaparelli_title)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg\n"
     ]
    }
   ],
   "source": [
    "schiaparelli_img= soup.find('div', class_='wide-image-wrapper')\n",
    "schiaparelli_img_url=schiaparelli_img.li.a.get('href')\n",
    "print(schiaparelli_img_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Syrtis Major Hemisphere Enhanced\n"
     ]
    }
   ],
   "source": [
    "#Syrtis Major Image\n",
    "#URL of second webpage to be scraped to be scraped \n",
    "time.sleep(5)\n",
    "url =\"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n",
    "\n",
    "# Retrieving the browser url\n",
    "browser.visit(url)\n",
    "\n",
    "#Getting the title for the Cereberus Hemisphere Enhanced\n",
    "\n",
    "#using button feature to click on full image\n",
    "browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')\n",
    "\n",
    "html=browser.html  \n",
    "soup=bs(html, 'html.parser')\n",
    "\n",
    "#Obtaining the title \n",
    "syrtis_major= soup.find('div', class_='content')\n",
    "syrtis_major_title= syrtis_major.find('h2').text\n",
    "print(syrtis_major_title)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg\n"
     ]
    }
   ],
   "source": [
    "syrtis_major_img= soup.find('div', class_='wide-image-wrapper')\n",
    "syrtis_major_img_url=syrtis_major_img.li.a.get('href')\n",
    "print(syrtis_major_img_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Valles Marineris Hemisphere Enhanced\n"
     ]
    }
   ],
   "source": [
    "#Valles Marineris Major Image\n",
    "#URL of second webpage to be scraped to be scraped \n",
    "time.sleep(5)\n",
    "url =\"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n",
    "\n",
    "# Retrieving the browser url\n",
    "browser.visit(url)\n",
    "\n",
    "#Getting the title for the Cereberus Hemisphere Enhanced\n",
    "\n",
    "#using button feature to click on full image\n",
    "browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')\n",
    "\n",
    "html=browser.html  \n",
    "soup=bs(html, 'html.parser')\n",
    "\n",
    "#Obtaining the title \n",
    "valles_marineris= soup.find('div', class_='content')\n",
    "valles_marineris_title= valles_marineris.find('h2').text\n",
    "print(valles_marineris_title)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg\n"
     ]
    }
   ],
   "source": [
    "valles_marineris_img= soup.find('div', class_='wide-image-wrapper')\n",
    "valles_marineris_img_url=valles_marineris_img.li.a.get('href')\n",
    "print(valles_marineris_img_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "metadata": {},
   "outputs": [],
   "source": [
    "hemisphere_image_urls=[\n",
    "    {'title': cereberus_title, \"img_url\": cereberus_img_url},\n",
    "    {'title':schiaparelli_title, \"img_url\":schiaparelli_img_url},\n",
    "    {'title':syrtis_major_title, \"img_url\":syrtis_major_img_url},\n",
    "    {'title':valles_marineris_title, \"img_url\":valles_marineris_img_url}\n",
    "]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': 'Cerberus Hemisphere Enhanced',\n",
       "  'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'},\n",
       " {'title': 'Schiaparelli Hemisphere Enhanced',\n",
       "  'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'},\n",
       " {'title': 'Syrtis Major Hemisphere Enhanced',\n",
       "  'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'},\n",
       " {'title': 'Valles Marineris Hemisphere Enhanced',\n",
       "  'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}]"
      ]
     },
     "execution_count": 138,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
