import json

#class to write the script in a json file
class ScriptWriter:
    def __init__(self, filename):  # initializes the writer for the script file
        print("New writer created for the file: %s", filename)
        self.filename = filename

    def write_in_file(self, what_to_write):# writes a dictionary in the json file
        json_object = json.dumps(what_to_write, indent=4)
        with open(self.filename, "w") as outfile:
            outfile.write(json_object)

    def write_scene_name(self, scenename): #writes the scene name in the json file
        dictionary = {"scenename": scenename}
        self.write_in_file(dictionary)

