import json
import time
import threading
import Emails

open("database.json", "a")


class Machine:
    def __init__(self):
        self.name = ""
        self.email = ""
        self.date = ""
        self.accurate = ""
        self.data = ""
        self.statusChecker = ""
        self.CovidList = {}
        self.CovidCases = 0
        self.emailSent = False
        self.emailList = []

    def main(self):
        th = threading.Thread(target=self.CovidStatusChecker)  # Create new thread
        th.start()  # Start thread
        self.name = input("Please enter your name (first and last): ")
        self.email = input("Please enter your email address: ")
        print("Did you enter in the information below correctly? ")
        print(f"Full Name : {self.name} \nEmail : {self.email}")
        self.accurate = input("Is this information accurate? (Y:N): ")
        if self.accurate.lower() == "y":
            self.logInfo(self.name, self.email)
        else:
            self.main()

    def logInfo(self, name, email):
        with open('database.json', "r") as f:
            self.data = json.load(f)  # load json file
        toAppend = {name: {"name": name, "email": email, "date": time.strftime("%m/%d/%Y, %H"), "Covid-19": False}}
        self.data.update(toAppend)  # Append the dictionary
        with open('database.json', 'w') as f:
            json.dump(self.data, f)

    def CovidStatusChecker(self):
        with open('database.json', "r") as f:
            self.data = json.load(f)  # load json file
        for key in self.data:
            if self.data[key]["Covid-19"]:
                toAppendCovid = {self.data[key]["name"]: self.data[key]}
                self.CovidList.update(toAppendCovid)
                self.CovidCases += 1

        if self.CovidCases >= 1:
            for key in self.data:
                for case in self.CovidList:
                    if self.CovidList[case]["date"] == self.data[key]["date"]:
                        self.emailList.append(self.data[key]["email"])
            self.sendEmail(email)

    def sendEmail(self, emailController):
        emailController.sendEmail(self.emailList)


email = Emails.Email("EMAIL_USER", "EMAIL_PASSW")
machine = Machine()
machine.main()
