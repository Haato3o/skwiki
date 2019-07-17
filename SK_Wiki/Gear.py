from requests import request
from bs4 import BeautifulSoup

Wiki    = 'http://wiki.spiralknights.com/'
Media   = 'http://media3.spiralknights.com/wiki-'

class Gear:
    def __init__(self, Name):
        '''
            :param Name: Weapon/Armor/Shield name
        '''
        self.Pretty_Name: str = Name
        self.Name: str = Name.title().replace(" ", "_").replace("'S","'s")
        self.URL: str = f"{Wiki}{self.Name}".replace("Of", "of").replace("The_", "the_")
        self.Wiki_Content = request('get', self.URL)

    def Description(self):
        '''
            Returns Item description
            :return: String
        '''
        try:
            content = self.Wiki_Content.text
            HTMLParser = BeautifulSoup(content, 'html.parser')
            HTMLParser.find(alt="stats")
            Description = HTMLParser.find(id="Description").find_next("p").get_text()
            return Description
        except:
            return None

    def Image(self):
        '''
            Returns Item image
            :return: String
        '''
        try:
            content = self.Wiki_Content.text
            HTMLParser = BeautifulSoup(content, "html.parser")
            HTMLParser.find(alt="stats")
            Image_Candidates:list = HTMLParser.find_all("img")
            # Loops through images and return the one with Equipped in the name
            # This is necessary since some reskinned weapons have slightly different wiki pages
            for img in Image_Candidates:
                Image = img.get("src")
                if Image.split("-")[1] == "Equipped.png":
                    break
            Image = list(Image)
            Image.remove("/")
            return f"{Media}{''.join(Image)}"
        except:
            return None

    def Status(self):
        '''
            Returns item status
            :return: String
        '''
        try:
            content = self.Wiki_Content.text
            HTMLParser = BeautifulSoup(content, "html.parser")
            Status = list(str(HTMLParser.find(alt="stats").get("src")))
            Status.remove("/")
            return f"{Media}{''.join(Status)}"
        except:
            return None

    def Tier(self):
        '''
            Returns item tier
            :return: String
        '''
        try:
            content = self.Wiki_Content.text
            HTMLParser = BeautifulSoup(content, "html.parser")
            HTMLParser.find(alt="stats")
            for html_tag in HTMLParser.find("td").find_all_next("td"):
                if html_tag.get_text() == "":
                    continue
                elif html_tag.get_text().strip()[0] in ["★", "☆"]:
                    Tier = html_tag.get_text().strip()
                    break
            return Tier.split("\n")[0]
        except:
            return None
