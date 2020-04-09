from src.ScriptWriter import ScriptWriter

filename = "test.xml"

scriptwriter = ScriptWriter(filename)
scriptwriter.new_opera("Romeo e Giulietta")
scriptwriter.new_scene('0')
scriptwriter.new_scene('1')
scriptwriter.new_scene('0')
scriptwriter.new_section('0', '0')
scriptwriter.new_section('0', '1')
