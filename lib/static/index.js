//////////////////////////////////////////
// グローバル変数
//////////////////////////////////////////

//////////////////////////////////////////
// 読み込み時実行
//////////////////////////////////////////
$(function() {
    // 書込ボタン押下時イベント
    $('#postBtn').click(function(e) {
        postBtnClickEvent();
    });
    // 更新ボタン押下時イベント
    $('#updateBtn').click(function(e) {
        updateDisplay();
    });
    // 読み込み時に過去の書き込みを表示させる
    postTextDisplay("", "", "", "", "");
    // 3秒毎に画面を更新
    setInterval('updateDisplay()',3000);
});
//////////////////////////////////////////
// 「書込」ボタン押下時イベント
//////////////////////////////////////////
function postBtnClickEvent(){
    // 名前の取得
    let nm = "無名";
    let name = document.getElementById("name");
    if (name.value != "") {
        nm = name.value;
    }
    // 時間の取得
    // JST は UTC の9時間後
    let date = new Date(Date.now() + ((new Date().getTimezoneOffset() + (9 * 60)) * 60 * 1000));
    let yyyymmdd = date.getFullYear() + '/' + ('0' + (date.getMonth() + 1)).slice(-2) 
        + '/' + ('0' + date.getDate()).slice(-2);
    let hhmmss = ('0' + date.getHours()).slice(-2) + ':' 
        + ('0' + date.getMinutes()).slice(-2) + ':' + ('0' + date.getSeconds()).slice(-2);
    let milliSeconds = ('0' + date.getMilliseconds()).slice(-2);

    // 書込テキスト取得
    let input = document.getElementById("inputText");
    let text = input.value;
    // 書込が行われている場合のみ処理を実施
    if (text != "") {
        $("#output").empty();
        postTextDisplay(yyyymmdd, hhmmss, milliSeconds, nm, text);
        // テキストエリアのクリア
        input.value = '';
    }
}
//////////////////////////////////////////
// 「書込」を取得し、画面に反映する
//////////////////////////////////////////
function postTextDisplay(yyyymmdd, hhmmss, milliSeconds, nm, text){

    dateInfoList = [yyyymmdd, hhmmss, milliSeconds, nm, text];
    // jsonに変換
    dateInfoListJSON = JSON.stringify(dateInfoList);

    // サーバー送受信
    jQuery.ajaxSetup({async: false});
    jQuery.ajax({
        type: "POST",
        url: "/get_post_text",
        data: dateInfoListJSON,
        contentType: "application/json",
        success: function(obj) {
            obj.data.map(function(arr) {
                let yyyymmdd = arr[0];
                let hhmmss = arr[1];
                let strDate = yyyymmdd + ' ' + hhmmss;
                let name = arr[3];
                let text = arr[4];
                text=text.replace(/\n/g,'<br>') // gフラグオプションで、全ての改行コードを置換
                let title = "日時：" + strDate + "　名前：";
                let output = document.getElementById("output");
                output.insertAdjacentHTML('beforeend', "<div class=\"thread\">" + title + "<font color=\"green\"><b>" + name + "<font color=\"green\"><b></div>");
                output.insertAdjacentHTML('beforeend', "<div class=\"comment\">" + text + "</div>");
                output.insertAdjacentHTML('beforeend', "<br>");
            });
        },
        error: function(obj) {
            console.log("サーバー通信 失敗");
        }
    });
    jQuery.ajaxSetup({async: true});
}
//////////////////////////////////////////
// 画面更新
//////////////////////////////////////////
function updateDisplay(){
    $("#output").empty();
    postTextDisplay("", "", "", "", "");
}