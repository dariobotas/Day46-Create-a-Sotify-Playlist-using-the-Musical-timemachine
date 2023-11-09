import requests

from bs4 import BeautifulSoup
#from selenium import webdriver

URL = "https://www.billboard.com/charts/hot-100/"

if __name__ == '__main__':
    #year_to_travel = input("Wich year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")

    url_scrap = f"{URL}2000-08-12"#{year_to_travel}"
    #print(url_scrap)
    
    #driver = webdriver.Edge()
    #driver.get(url_scrap)
    response = requests.get(url_scrap)
    website_html = response.text
    #soup = BeautifulSoup(driver.page_source, "html.parser")
    soup = BeautifulSoup(website_html, "html.parser")
    #print(soup.body.contents)
    #driver.quit()
    title_and_song_li_tags = soup.find_all("li", class_="lrv-u-width-100p")
    uls = [ul for ul in title_and_song_li_tags]
    
    """ Songs List """
    h3_songs = [h3.find_all('h3') for h3 in uls]
    #print(h3_songs[::2])
    songs = []#[song.get_text() for song in h3_songs if len(song) != 0]
    for song in h3_songs:
        music = song.text
        songs.append(str(music))
    print(songs)
    """ Artists List """
    span_artists = [span.find_all('span', class_="a-font-primary-s") for span in uls]
    artists = [artist.get_text() for artist in span_artists if len(artist) != 0]
    print(f"Songs: {len(h3_songs[::2])}- Artists: {len(span_artists[::2])}")
    print(f"Songs: {len(songs)}- Artists: {len(artists)}")
    print([f"Song/Artist: {songs[i]} - {artists[i]}" for i in range(len(songs))])
    #titles_and_songs = [title for title in uls_inside_lis]
    #rest=[title.find_all("h3") for title in titles_and_songs]
    #print(rest[0].getText())
    #titles = soup.find_all("h3", id="title-of-a-story", class_="c-title")f"Title/Artist: {title.find_all("h3").getText()} - {title.find_all("span").getText()}"
    #print([title.getText().replace("\n", "").replace("\t","") for title in titles])
    
    #body_content = soup.body.contents
    #with open("billboard.txt", mode="w") as file:
    #    for line in body_content:
    #        file.write(f"{line}\n")
    #print(soup.prettify())