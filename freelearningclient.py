from urllib.request import urlopen
import bs4
import argparse

class ClientWeb(object):
    """"Client web per la web de la EPS"""
    def __init__(self):
        super(ClientWeb, self).__init__()
        pass
    '''
    def get_args(self):
        parser = argparse.ArgumentParser()
        parser.parse_args()
        parser.add_argument("link", type=str, help="link to the web")
        args = parser.parse_args()
        return args.link
    '''
    def run(self):
        #parsejar arguments
        #link = self.get_args()
        # descaregar-me html
        link = "https://www.packtpub.com/packt/offers/free-learning/"
        html = self.descarregar_html(link)
        # buscar activitats
        #timer = self.buscar_activitats(html)
        # imprimir resultat
        print(html)

    def descarregar_html(self, link):
        f = urlopen(link)
        html = f.read()
        f.close()
        return html

if __name__ == "__main__":
    c = ClientWeb()
    c.run()
