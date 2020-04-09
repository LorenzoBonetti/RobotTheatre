import json
import os


class ScriptWriterJSON:
    # initializes the jsonWriter
    # filename: the name of the file to write on
    def __init__(self, filename):
        print("New writer created for the file:", filename)
        self.filename = filename
        if os.path.isfile(filename):  # if the file already exists loads the dictionary stored in the file
            self.dictionary = json.load(open(filename))
        else:
            self.dictionary = {}
            self.dictionary['characters'] = []

    # writes the dictionary in the json file
    def write_in_file(self):
        with open(self.filename, "w") as outfile:
            json.dump(self.dictionary, outfile)

    def add_new_character(self, name):
        for character in self.dictionary['characters']:
            if character == name:
                print("ERROR: character:", name, " already exist")
                return
        self.dictionary['characters'].append(name)

    # writes the name of the opera
    def new_opera(self, opera_name):
        self.dictionary['opera'] = opera_name

    # initializes a new act
    def new_act(self, act_number):
        act_name = 'act:' + str(act_number)
        if self.dictionary.keys().__contains__(act_name):
            print("ERROR: act:", act_number, " already exist")
            return
        scenes = {}
        self.dictionary[act_name] = scenes

    # initializes a new scene
    def new_scene(self, act_number, scene_number):
        scene_name = 'scene:' + str(scene_number)
        act_name = 'act:' + str(act_number)
        if self.dictionary[act_name].__contains__(scene_name):
            print("ERROR: scene:", scene_number, " already exist")
            return
        sections = {}
        self.dictionary[act_name][scene_name] = sections

    # initializes a new section
    def new_section(self, act_number, scene_number, section_number):
        scene_name = 'scene:' + str(scene_number)
        act_name = 'act:' + str(act_number)
        section_name = 'section:' + str(section_number)
        if self.dictionary[act_name][scene_name].__contains__(section_name):
            print("ERROR: section:", section_number, " already exist")
            return
        actions = {}
        self.dictionary[act_name][scene_name][section_name] = actions
