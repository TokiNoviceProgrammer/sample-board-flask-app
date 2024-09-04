from flask import jsonify, render_template, request

import constant

# 内部資材
import query

# 固定値
cons = constant.constant()


@query.define_table.app.route("/SampleSiteCh")
def index():
    return render_template("index.html")


@query.define_table.app.route("/get_post_text", methods=["POST"])
def get_post_text():
    # フロントからの取得値
    json_data = request.json
    json_data_list = list(json_data)
    yyyymmdd = json_data_list[0]
    hhmmss = json_data_list[1]
    milliSeconds = json_data_list[2]
    nm = json_data_list[3]
    text = json_data_list[4]
    # 登録
    if yyyymmdd != "":
        query.add_post(yyyymmdd, hhmmss, milliSeconds, nm, text)
    # 表示内容取得し、フロントへ返却
    coords = query.get_t_post()

    return jsonify({"data": coords})


if __name__ == "__main__":
    query.define_table.app.run(host="0.0.0.0", port=5000, debug=True)
