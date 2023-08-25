from flask import Flask, request, jsonify
from flask_cors import CORS
import database.db as db

from setting import *
from models.create_group_request_param import CreateGroupRequestParam
from models.submit_group_request_param import SubmitGroupRequestParam
from logic.makeNewGroupLogic import make_new_group_logic
from logic.getGroupInfoLogic import get_group_info_with_groupID_logic
from logic.submitScheduleLogic import submit_schedule_logic

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
        # スケジュールを登録
        requestParam = SubmitGroupRequestParam(**request.json)

        updatedGroupInfo = submit_schedule_logic(requestParam, groupId)

        for i in range(len(updatedGroupInfo.schedules)):
            updatedGroupInfo.schedules[i] = updatedGroupInfo.schedules[i].__dict__

        print(updatedGroupInfo.__dict__)

        return jsonify(updatedGroupInfo.__dict__), 200


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pong"}), 200

if __name__ == '__main__':
    db.init_db()
    app.run(debug=False, host='0.0.0.0', port=5001)