import requests

class TelegramHandler:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id
        self.base_url = f'https://api.telegram.org/bot{self.token}/sendMessage'

    def send_notification(self, message):
        payload = {
            'chat_id': self.chat_id,
            'text': message,
        }
        response = requests.post(self.base_url, data=payload)
        return response.status_code, response.json()

    def notify_new_listing(self, listing):
        message = f'New listing: {listing}'
        return self.send_notification(message)

    def notify_price_change(self, item, old_price, new_price):
        message = f'Price Change for {item}: {old_price} -> {new_price}'
        return self.send_notification(message)

    def notify_offer_sent(self, offer):
        message = f'Offer sent: {offer}'
        return self.send_notification(message)

    def notify_error(self, error_message):
        message = f'Error: {error_message}'
        return self.send_notification(message)
