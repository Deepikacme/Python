class EmailService:
    def send(self):
        print("Confirmation email sent")
class Order:
    def confirm(self, email):
        email.send()
Order().confirm(EmailService())