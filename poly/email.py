class EmailNotification:
    def send(self):
        print("Email notification sent.")
class SMSNotification:
    def send(self):
        print("SMS notification sent.")
def notify(obj):
    obj.send()
email=EmailNotification()
sms=SMSNotification()
notify(email)
notify(sms)