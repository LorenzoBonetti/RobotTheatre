import json

from src.ScriptWriter import ScriptWriter

filename="test"
scenename="testscene"
scriptwriter=ScriptWriter(filename)
scriptwriter.write_scene_name(scenename)