import random
from locust import HttpUser, between, task, TaskSet, constant
from pyquery import PyQuery

class ContactSection(TaskSet):
    wait_time = constant(1)

    @task
    def submit_contact_form(self):
        self.client.post("/contact", {
            "name": "A user",
            "email": "inputtext@example.com",
            "message": "This is a test message."
         })
    @task
    def exit_contact(self):
        self.interrupt()

class MainPage(TaskSet):
    wait_time = constant(5)

    @task
    def visit_home(self):
        self.client.get("/")

    @task
    def exit_main(self):
        self.interrupt()

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)
    tasks = [MainPage]
    host = "https://tlab.co.id"
