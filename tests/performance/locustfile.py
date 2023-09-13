from locust import HttpUser, task


class PerfTest(HttpUser):
    @task
    def index(self):
        self.client.get("/")

    @task
    def profiles_index(self):
        self.client.get("/profiles/")

    @task
    def get_a_profile(self):
        self.client.get("/profiles/HeadlinesGazer/")

    @task
    def lettings_index(self):
        self.client.get("/lettings/")

    @task
    def get_a_letting(self):
        self.client.get("/lettings/1/")

    # erreurs 404
    @task
    def get_worng_url(self):
        self.client.get("/UnknownUrl/")

    @task
    def get_wrong_profile(self):
        self.client.get("/profiles/NotExistsInDatabase/")

    @task
    def get_wrong_letting(self):
        self.client.get("/lettings/150/")
