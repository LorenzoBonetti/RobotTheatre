import json


class CharacterReaderJSON:

    def __init__(self, filename):
        self.data = json.load(open(filename))

    def get_name(self):
        return self.data.get('name', None)

    def get_movable_parts(self):
        return self.data.get('movable_parts', None)

    def get_emotion_weights(self):
        return self.data.get('emotion_weights', None)
