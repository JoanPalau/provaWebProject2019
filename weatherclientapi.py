from urllib.request import urlopen
import json
import pprint

class ClientWeb(object):
    """"Client web per obtenir la temperatura de Lleida"""
    def __init__(self):
        super(ClientWeb, self).__init__()
        pass

    def run(self):
        # descaregar-me html
        data = self.do_request()
        # print(data)
        # buscar activitats
        data = self.process_weather(data)
        # imprimir resultat
        print(data)

    def do_request(self):
        f = urlopen("http://api.openweathermap.org/data/2.5/find?q=Lleida&units=metric&APPID=eceb0dc81e2deb91fc62eb578ecd0180&mode=json&lang=ca")
        data = f.read()
        f.close()
        return data

    def process_weather(self, html):
        dic = json.loads(html)
        # pprint.pprint(dic)
        temp = dic['list'][0]['main']['temp']
        weather = dic['list'][0]['weather'][0]['description']
        return (str(temp)+" and "+weather)


if __name__ == "__main__":
    c = ClientWeb()
    c.run()
