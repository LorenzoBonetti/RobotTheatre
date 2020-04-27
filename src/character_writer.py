import json
import os


class CharacterWriterJSON:
    def __init__(self, filename):
        print("New writer created for the file:", filename)
        self.filename = filename
        if os.path.isfile(filename):  # if the file already exists loads the dictionary stored in the file
            self.dictionary = json.load(open(filename))

    # writes the dictionary in the json file
    def write_in_file(self):
        with open(self.filename, "w") as outfile:
            json.dump(self.dictionary, outfile)

    def new_character(self, character_name):
        self.dictionary['name'] = character_name

    def movable_parts(self, movable_parts):
        self.dictionary['movable_parts'] = movable_parts

    def emotion_weights(self, emotion_weights):
        self.dictionary['emotion_weights'] = emotion_weights
