from bs4 import BeautifulSoup
import requests

class Hosue:
    final2 = ''
    def __init__(self, type_house, state):
        self.type_house = type_house
        self.state = state
    
    def owner(self):
        global price_p
        global final2
        final = ''
        URL = f'https://www.redfin.com/state/{self.state.capitalize()}'
        URL2 = f'https://www.nerdwallet.com/mortgages/mortgage-rates/{self.state}'
        URL3 = f"https://www.usbank.com/home-loans/mortgage/mortgage-rates/{self.state}.html"

        headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}

        page = requests.get(URL, headers=headers)
        page2 = requests.get(URL2, headers=headers)
        page3 = requests.get(URL3, headers=headers)


        soup =  BeautifulSoup(page.content, 'html.parser')
        soup2 =  BeautifulSoup(page2.content, 'html.parser')
        soup3 =  BeautifulSoup(page3.content, 'html.parser')

        try:
            price = soup.find(class_="statePageDescription text-base headerOffset").get_text()
            price_p = price.replace("$", "")
            price_o = price_p.replace(",", "")
            for i in price_o:
                if i.isdigit():
                    final = final + i
            Hosue.final2 = int(final[5:11])
            print(Hosue.final2)
        except:
            price = "the stae that you are loking for does not exist"
            print("nopr")

        mortage = soup2.find(class_="_13J6Bq").get_text()
        mortage2 = mortage.replace("%", "")
        mortage3 = float(mortage2)
        pay_30 = Hosue.final2 / 100 * mortage3
        Hosue.pay_30f = Hosue.final2 + pay_30
        print(Hosue.pay_30f)
        Hosue.month = Hosue.pay_30f / 360


    def renter(self):
        URL = f'https://www.homesnacks.com/cities/average-rent-in-{self.state}/'

        headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}

        page = requests.get(URL, headers=headers)


        soup =  BeautifulSoup(page.content, 'html.parser')
        try:
            price = soup.find(class_="statistic-box-inner").get_text()
        except:
            price = "the state that you are looking for does not exist"
        print(price)
p1 = Hosue("buying", "texas")
p1.owner()
print(p1.pay_30f)