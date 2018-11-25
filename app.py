from flask import Flask, request
from message import VkApi


api = VkApi(('59b5aae9f38581c646d872db46f62b5fa79b481f377074542cbaeaccf3ac3c6d022e9f878e9c8f3889b23'))


app = Flask(__name__)


@app.route('/vk/', methods=['POST'])
def vk():
    message = request.get_json()

    if message.get('type') == 'confirmation':
        return 'da004b1c'

    if message.get('type') == 'message_new':
        api.message(
            message.get('object').get('from_id'), 
            message.get('object').get('text')
        )

    return 'Ok'
