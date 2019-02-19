from urllib.request import urlopen
import bs4

class ClientWeb(object):
    """"Client web per la web de la EPS"""
    def __init__(self):
        super(ClientWeb, self).__init__()
        pass

    def run(self):
        # descaregar-me html
        data = self.do_request()
        print(data)
        # buscar activitats
        data = self.process_weather(data)
        # imprimir resultat


    def do_request(self):

        f = urlopen("http://api.openweathermap.org/data/2.5/find?q=London&units=metric&APPID=eceb0dc81e2deb91fc62eb578ecd0180")
        data = f.read()
        f.close()
        return data

    def process_weather(self, html):
        arbre = bs4.BeautifulSoup(html, features="lxml")
        temperature = arbre.find("main")
        weather = arbre.find("weather")
        print(temperature["temp"] + " and " + weather["description"])
        return None

if __name__ == "__main__":
    c = ClientWeb()
    c.run()
