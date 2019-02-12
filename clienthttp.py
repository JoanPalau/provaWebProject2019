from urllib.request import urlopen
import bs4

class ClientWeb(object):
    """"Client web per la web de la EPS"""
    def __init__(self):
        super(ClientWeb, self).__init__()
        pass

    def run(self):
        # descaregar-me html
        html = self.descarregar_html()
        # buscar activitats
        activitats = self.buscar_activitats(html)

        # imprimir resultat
        print(activitats)

    def descarregar_html(self):
        f = urlopen("http://www.eps.udl.cat/ca/")
        html = f.read()
        f.close()
        return html

    def buscar_activitats(self, html):
        arbre = bs4.BeautifulSoup(html, features="lxml")
        activitats = arbre.find_all("div", "featured-links-item")
        return activitats

if __name__ == "__main__":
    c = ClientWeb()
    c.run()
