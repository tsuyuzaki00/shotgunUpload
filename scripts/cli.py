import os
import sys

from shotgun_api3 import Shotgun

def main():
    target_dir = "images"
 
    url = "https://engiscriptstest.shotgunstudio.com/"
    script_name = "myuploader"
    api_key = "hwdoZvfavf0(lzzdetntdsmal"
 
    # Shotgunインスタンスの取得
    shotgun = Shotgun(url, script_name=script_name, api_key=api_key)
 
    # 対象プロジェクト
    project_id = 122
    project = {"type": "Project", "id": project_id}
 
    # 対象のエンティティをバージョン、ファイルへリンクするフィールドをsg_uploaded_movieとします
    entity_type = "Version"
    for _file in os.listdir(target_dir):
 
        # ファイル名と同じ名前のバージョン名と、所属するプロジェクトの情報を持たせます
        entity_data = {"code": _file, "project": project}
 
        # バージョンエンティティを作成します
        version = shotgun.create(entity_type, entity_data)
 
        # versionにはどのようなデータが入っているでしょうか？
        print(version)
    return 0
 
 
if __name__ == "__main__":
    sys.exit(main())