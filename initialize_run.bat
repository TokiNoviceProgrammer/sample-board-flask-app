@echo off
chcp 65001
rem ###############################################################
rem # 起動bat(dbファイルを作り直すところから実行する)
rem ###############################################################

rem ###############################################################
rem # 処理実行
rem ###############################################################

set PYTHONDONTWRITEBYTECODE=1

echo %date% %time% %dbファイル作成
cd lib
python create_table.py
cd ..

echo %date% %time% %実行
python app.py

rem エラーチェック
if %errorlevel% neq 0 (
    echo %date% %time% 異常終了しました。
    exit /B %errorlevel%
)

echo %date% %time% 正常終了しました。