import json


class ScriptReaderJSON:

    def __init__(self, filename):
        self.data = json.load(open(filename))

    def check_existance(self, act_number, scene_number, section_number):
        scene_name = 'scene:' + str(scene_number)
        act_name = 'act:' + str(act_number)
        section_name = 'section:' + str(section_number)
        act = self.data.get(act_name, -1)
        if act == -1:
            print("ERROR: act:", act_number, " doesn't exist")
            return False
        scene = act.get(scene_name, -1)
        if scene == -1:
            print("ERROR: scene:", scene_number, " doesn't exist")
            return False
        section = scene.get(section_name, -1)
        if section == -1:
            print("ERROR: section:", section_number, " doesn't exist")
            return False
        return True

    def get_trigger(self, act_number, scene_number, section_number):
        scene_name = 'scene:' + str(scene_number)
        act_name = 'act:' + str(act_number)
        section_name = 'section:' + str(section_number)
        if self.check_existance(act_number, scene_number, section_number):
            return self.data.get(act_name, -1).get(scene_name, -1).get(section_name, -1).get('trigger', None)
        return None

    def get_emotion(self, act_number, scene_number, section_number):
        scene_name = 'scene:' + str(scene_number)
        act_name = 'act:' + str(act_number)
        section_name = 'section:' + str(section_number)
        if self.check_existance(act_number, scene_number, section_number):
            return self.data.get(act_name, -1).get(scene_name, -1).get(section_name, -1).get('emotion', None)
        return None

    def get_actions(self, act_number, scene_number, section_number):
        scene_name = 'scene:' + str(scene_number)
        act_name = 'act:' + str(act_number)
        section_name = 'section:' + str(section_number)
        if self.check_existance(act_number, scene_number, section_number):
            return self.data.get(act_name, -1).get(scene_name, -1).get(section_name, -1).get('actions', None)
        return None
