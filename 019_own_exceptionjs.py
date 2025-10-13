class PaymentError(Exception):
    def __init__(self, account):
        self.account = account

class PaymentDeclinedError(PaymentError):
    def __init__(self, *args):
        super().__init__(self, args)

class PaymentTimeoutError(PaymentError):
    def __init__(self, *args):
        super().__init__(self, args)

try:
    process_payment(card, amount)
except PaymentError:
    send_notification_to_user()