import xml.etree.ElementTree as ET


# class to write the script in a XML file
class ScriptWriterXML:
    opera_level = 0
    scene_level = 1

    def __init__(self, filename):  # initializes the writer for the script file
        print("New writer created for the file:", filename)
        self.filename = filename

    def new_opera(self, operaname):
        root = ET.Element('opera')
        root.attrib['name'] = operaname
        tree = ET.ElementTree(root)
        tree.write(self.filename)

    def new_scene(self, scenenumber):  # writes the scene name in the json file
        tree = ET.parse(self.filename)
        root = tree.getroot()
        #check file
        for child in root:
            if child.attrib["number"] == scenenumber:
                print("ERROR: your scene already exists")
                return
        #write in file
        new_scene = ET.SubElement(root, 'scene')
        new_scene.attrib['number'] = scenenumber
        tree.write(self.filename)

    def new_section(self, scenenumber, sectionnumber):
        tree = ET.parse(self.filename)
        root = tree.getroot()
        #check file
        found = False
        for child in root:
            if child.attrib["number"] == scenenumber:
                found = True
                for child1 in child:
                    if child1.attrib["number"] == sectionnumber:
                        print("ERROR: your section already exists")
                        return
        #write in file
        if found:
            sceneindex=int(scenenumber)
            new_section = ET.SubElement(root[sceneindex], 'section')
            new_section.attrib['number'] = sectionnumber
            tree.write(self.filename)
        else:
            print("ERROR: scene does not exists")
