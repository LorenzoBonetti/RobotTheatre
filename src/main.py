from src.ScriptWriterJSON import ScriptWriterJSON
from src.character_writer import CharacterWriterJSON

filenameJSON = "C:\\Users\Lorenzo\\Documents\POLIMI\\Magistrale\\TESI\\RobotTheatre\\files\\script.json"
character = "C:\\Users\Lorenzo\\Documents\POLIMI\\Magistrale\\TESI\\RobotTheatre\\files\\character.json"

# ScriptWriterJSON testing
jsonWriter = ScriptWriterJSON(filenameJSON)
jsonWriter.new_opera("Romeo and Juliet")
jsonWriter.add_new_character('Romeo')
jsonWriter.add_new_character('Juliet')
jsonWriter.new_act(2)
jsonWriter.new_scene(2, 2)
emotion = {'happiness': 0.9, 'sadness': 0.1, 'anger': 0.2, 'fear': 0,
           'curiosity': 0.5}  # migh be a simple list, now dictionary for readability
jsonWriter.new_section(2, 2, 0, 'after_precedent', '', emotion)
jsonWriter.new_movement(2, 2, 0, 'location', ['DR', 'N'], ['body'])  # means position down right, orientation north
jsonWriter.new_section(2, 2, 1, 'after_actor', 'Romeo', emotion)
jsonWriter.new_movement(2, 2, 1, 'actor', 'Romeo', ['arm_dx', 'arm_sx', 'bust', 'body'])
jsonWriter.new_movement(2, 2, 1, 'actor', 'Romeo', 'O Romeo, Romeo, wherefore are thou Romeo?')
jsonWriter.write_in_file()

# ChacracterWriter testin

characterWriter = CharacterWriterJSON(character)
characterWriter.new_character('Juliet')
characterWriter.movable_parts(['arm_dx', 'arm_sx', 'bust', 'body', 'face'])
characterWriter.write_in_file()
