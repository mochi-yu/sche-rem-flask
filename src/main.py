from flask import Flask, request, jsonify
from flask_cors import CORS
import database.db as db

from setting import *
from models.create_group_request_param import CreateGroupRequestParam
from logic.makeNewGroupLogic import make_new_group_logic
from logic.getGroupInfoLogic import get_group_info_with_groupID_logic

app = Flask(__name__)
CORS(app)

groups = []

@app.route('/group', methods=['POST'])
def groupInfo():
    print(request.method)
    if request.method == 'POST':
        # 新しいグループを作成
        newGroup = CreateGroupRequestParam(**request.json)

        createdGroupInfo = make_new_group_logic(newGroup)
        # print(createdGroupInfo.__dict__)

        return jsonify(createdGroupInfo.__dict__), 200
    else:
        return 404


@app.route('/group/<string:groupId>', methods=['GET', 'POST'])
def groupWithGroupID(groupId):
    if request.method == 'GET':
        # groupIdで指定したグループの情報を取得
        groupInfo = get_group_info_with_groupID_logic(groupId)

        for i in range(len(groupInfo.schedules)):
            groupInfo.schedules[i] = groupInfo.schedules[i].__dict__

        print(groupInfo.__dict__)

        return jsonify(groupInfo.__dict__), 200
    elif request.method == 'POST':
        data = request.json
        # groupIdに基づいて対応するグループを探す処理を行う
        for existing_group in groups:
            if existing_group["groupId"] == groupId:
                # ここで日程回答の処理を行う
                # dataに含まれる情報を使って処理を行うことを想定
                response_data = {
                    "userName": data["userName"],
                    "userMailAddress": data["userMailAddress"],
                    "scheduleInfo": data["scheduleInfo"]
                }
                existing_group["responses"].append(response_data)
                return jsonify(existing_group), 200
        return jsonify({"message": "Group not found"}), 404


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pong"}), 200

if __name__ == '__main__':
    db.init_db()
    app.run(debug=False, host='0.0.0.0', port=5001)