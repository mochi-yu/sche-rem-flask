from flask import Flask, request, jsonify

app = Flask(__name__)

groups = []

@app.route('/group', methods=['GET', 'POST'])
def group():
    if request.method == 'GET':
        return jsonify(groups), 200
    elif request.method == 'POST':
        data = request.json
        new_group = {
            # ... グループ情報の生成
            "groupId": len(groups) + 1,
            "groupName": data["groupName"],
            "author": data["author"],
            "groupUsers": data["groupUsers"],
            "startDay": data["startDay"],
            "endDay": data["endDay"],
            "startHour": data["startHour"],
            "endHour": data["endHour"]  
        }
        groups.append(new_group)
        return jsonify(new_group), 200

# ダミーのデータベースとしてメモリ内のリストを使用
groups = []

# /group/{groupId} エンドポイントに対するGETとPOSTメソッドの処理を定義しています。
# GETメソッドでは、特定の groupId に対応するグループ情報を返します。POSTメソッドでは、特定の groupId に対応するグループに日程回答を追加します。

@app.route('/group/<string:groupId>', methods=['GET', 'POST'])
def group1(groupId):
    if request.method == 'GET':
        # groupIdに基づいて対応するグループを探す処理を行う
        for existing_group in groups:
            if existing_group["groupId"] == groupId:
                return jsonify(existing_group), 200
        return jsonify({"message": "Group not found"}), 404

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
    app.run(debug=False, host='0.0.0.0', port=5001)
