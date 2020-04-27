from src.ScriptWriterJSON import ScriptWriterJSON
from src.character_writer import CharacterWriterJSON
from src.scriptReader import ScriptReaderJSON

filenameJSON = "C:\\Users\Lorenzo\\Documents\POLIMI\\Magistrale\\TESI\\RobotTheatre\\files\\script.json"
character = "C:\\Users\Lorenzo\\Documents\POLIMI\\Magistrale\\TESI\\RobotTheatre\\files\\character.json"

# ScriptWriterJSON testing
jsonWriter = ScriptWriterJSON(filenameJSON)
jsonWriter.new_opera("Romeo and Juliet")
jsonWriter.add_new_character('Romeo', 'red', '50 to 100')
jsonWriter.add_new_character('Juliet', 'blue', '60 to 110')
jsonWriter.new_act(2)
jsonWriter.new_scene(2, 2)
emotion = {'happiness': 0.9, 'sadness': 0.1, 'anger': 0.2, 'fear': 0,
           'curiosity': 0.5}  # migh be a simple list, now dictionary for readability
jsonWriter.new_section(2, 2, 0, 'after_precedent', '', emotion)
jsonWriter.move_to(2, 2, 0, 'location', ('DR', 'N'))  # means position down right, orientation north
jsonWriter.new_section(2, 2, 1, 'after_actor', 'Romeo', emotion)
jsonWriter.move_to(2, 2, 1, 'actor', 'Romeo')
jsonWriter.speech(2, 2, 1, "O Romeo Romeo, wherefore art thou Romeo")
jsonWriter.move_arts(2, 2, 1, ['r_shoulder', 'l_shoulder', 'bust'])

jsonWriter.write_in_file()

# ChacracterWriter testin

characterWriter = CharacterWriterJSON(character)
characterWriter.new_character('Juliet')
characterWriter.movable_parts(['arm_dx', 'arm_sx', 'bust', 'body', 'face'])
characterWriter.emotion_weights({"happiness": 0.4, "sadness": 0.1, "anger": 0.2, "fear": 0.6, "curiosity": 1})
characterWriter.write_in_file()

# ScriptReader Testing
scriptReader = ScriptReaderJSON(filenameJSON)
if scriptReader.getTrigger(3, 2, 1) != None:
    print(scriptReader.getTrigger(3, 2, 1))

print(scriptReader.getTrigger(2, 2, 1))
