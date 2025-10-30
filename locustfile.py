import random
from locust import HttpUser, between, task
from pyquery import PyQuery

class UserBehavior(HttpUser):
    host = "https://dev-redesign.juru.id"
    wait_time = between(1, 3)

    @task(5)
    def index_page(self):
        response = self.client.get("")
        doc = PyQuery(response.content)
        link_elements = doc(".main-footer__menus nav.footer-menu a")
        self.toc_urls = [
            l.attrib["href"] for l in link_elements]

    def on_start(self):
        self.wait()
        self.index_page()
        self.url_on_current_page = self.toc_urls

    @task(10)
    def load_page(self):
        url = random.choice(self.toc_urls)
        r= self.client.get(url)
        pq = PyQuery(r.content)
        link_elements = pq("nav.footer-menu a")
        self.url_on_current_page = [
            l.attrib["href"] for l in link_elements
            ]
    @task(15)
    def load_subpage(self):
        if not self.url_on_current_page:
            return
        url = random.choice(self.url_on_current_page)
        self.client.get(url)


