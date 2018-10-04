from ReceteSorguPhase import ITSReceteSorgu
from UrunSorguPhase import ITSUrunSorgu
from LoginPhase import  ITSLogin
from locust import TaskSet, task,HttpLocust, seq_task

class ReceteTask(TaskSet):

    def on_start(self):
        self.recete = ITSReceteSorgu(self.client)

    @task(1)
    def recete_sorgu(self):
        self.recete.isLogon()
        if self.recete.account_login:
            self.recete.recete()
        else:
            self.recete.Login()

    @task(1)
    def recete_sorgu_sonucu(self):
        self.recete.isLogon()
        if self.recete.account_login:
            self.recete.recete_sorgu()
        else:
            self.recete.Login()

class UrunTask(TaskSet):

    def on_start(self):
        self.urun = ITSUrunSorgu(self.client)

    @task(1)
    def urun_sorgu(self):
        self.urun.isLogon()
        if self.urun.account_login:
            self.urun.urun()
        else:
            self.urun.Login()


    @task(1)
    def urun_sorgu_gtin_sn(self):
        self.urun.isLogon()
        if self.urun.account_login:
            self.urun.gtin_sn()
        else:
            self.urun.Login()


    @task(1)
    def urun_sorgu_urun_hareketleri(self):
        self.urun.isLogon()
        if self.urun.account_login:
            self.urun.get_urun_hareketleri()
        else:
            self.urun.Login()


    @task(1)
    def urun_sorgu_get_stakeholder(self):
        self.urun.isLogon()
        if self.urun.account_login:
            self.urun.get_stakeholder()
        else:
            self.urun.Login()

class LoginTask(TaskSet):
    tasks = { ReceteTask:1, UrunTask:1}

    def on_start(self):
        self.login = ITSLogin(self.client)

    @task(5)
    def login(self):
        self.login.Login()

class MyLocust(HttpLocust):
    task_set = LoginTask
    min_wait = 5000
    max_wait = 15000