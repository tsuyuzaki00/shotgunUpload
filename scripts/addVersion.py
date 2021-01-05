import json
import os
import sys

import requests
from shotgun_api3 import Shotgun

class IdentityError(Exception):
    pass

def base_dir():
    filepath = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(filepath)

def config_path():
    return os.path.join(base_dir(), "config", "config.json")

def get_config():
    with open(config_path(), "r") as fp:
        config = json.load(fp)
    return config

def find_unique(shotgun, entity_type, filters, fields):
    _entities = shotgun.find(entity_type, filters, fields)
    if not _entities:
        return None
    elif len(_entities) == 1:
        entity = _entities[0]
        return entity
    else:
        raise IdentityError

def main():
    config = get_config()

    shotgun_config = config["config"]
    url = shotgun_config["url"]
    script_name = shotgun_config["script_name"]
    api_key = shotgun_config["api_key"]
    target_dir = shotgun_config["target_dir"]
    project_id = shotgun_config["project_id"]
    user_id = shotgun_config["user"]

    shotgun_up = config["assetVersion00"]
    code = shotgun_up["code"]
    description = shotgun_up["description"]
    status = shotgun_up["sg_status_list"]
    link_asset_id = shotgun_up["link_asset"]
    link_task_id = shotgun_up["link_task"]

    sg = Shotgun(url, script_name=script_name, api_key=api_key)

    image = []

    target_list = os.listdir(target_dir)
    for file in target_list:
        if ".png" in file:
            image.append(file)

        version = sg.create("Version", {
            "project": { "type": "Project", "name": "testProject" , "id": project_id , "include_archived_projects": False},
            "entity": {"type": "Asset", "id": link_asset_id },
            "sg_task": {"type": "Task", 'id': link_task_id },
            "user": {"type": "HumanUser", 'id': user_id},
            "code": code,
            "description" : description,
            "sg_status_list": status,
            "sg_path_to_frames": image,
        })

        #sg.upload("Version", version["id"], os.path.join(target_dir, image), field_name = "sg_uploaded_movie", display_name = image)
        #sg.update("Version", version["id"], {"sg_status_list": status}, multi_entity_update_modes={"assets": "add"})

    return 0

if __name__ == "__main__":
    sys.exit(main())