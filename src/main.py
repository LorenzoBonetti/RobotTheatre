from src.ScriptWriterJSON import ScriptWriterJSON
from src.ScriptWriterXML import ScriptWriterXML

filenameXML = "test.xml"
filenameJSON="test_json.json"

scriptwriter = ScriptWriterXML(filenameXML)
scriptwriter.new_opera("Romeo e Giulietta")
scriptwriter.new_scene('0')
scriptwriter.new_scene('1')
scriptwriter.new_scene('0')
scriptwriter.new_section('0', '0')
scriptwriter.new_section('0', '1')


jsonWriter=ScriptWriterJSON(filenameJSON)
jsonWriter.new_opera("Romeo and Juliet")
jsonWriter.add_new_character('Romeo')
jsonWriter.add_new_character('Juliet')
jsonWriter.new_act(1)
jsonWriter.new_scene(1,1)
jsonWriter.new_section(1,1,0)
jsonWriter.write_in_file()