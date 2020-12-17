import os
import sys

from shotgun_api3 import Shotgun

def main():
    target_dir = "images"
 
    url = "https://engiscriptstest.shotgunstudio.com/"
    script_name = "myuploader"
    api_key = "hwdoZvfavf0(lzzdetntdsmal"
 
    # Shotgunインスタンスの取得
    sg = Shotgun(url, script_name=script_name, api_key=api_key)
 
    # 対象プロジェクト
    project_id = 122
    project = sg.find_one('Project', [['name', 'is', "testProject"]])
    field = sg.schema_field_read('Asset').keys()
    #print(project)
    #print(field)

    result = sg.find("Version", [], ['project'])
    #print(result)

    sg.close()

    # 対象のエンティティをバージョン、ファイルへリンクするフィールドをsg_uploaded_movieとします
    file = os.listdir(target_dir)
 
    # バージョンエンティティを作成します
    # code = アセット名
    # project = どのプロジェクトの中に作るか {type : Project, id : num }指示
    version = sg.create("Version", {"code": "hogehoge",
    "project": { "type": "Project", "name": "testProject" , "id": project_id },
    "description" : "testtest"
    #"sg_sequence":{"id": 1454, "name": "hogehoge", "type": "Asset"}
    })
 
    # versionにはどのようなデータが入っているでしょうか？
    #print (version)
    return 0

if __name__ == "__main__":
    sys.exit(main())