@echo off
chcp 65001
rem ###############################################################
rem # キャッシュを削除するbat
rem ###############################################################

rem ###############################################################
rem # 処理実行
rem ###############################################################

rem キャッシュの削除
rmdir /s /q __pycache__
rmdir /s /q lib\__pycache__

rem エラーチェック
if %errorlevel% neq 0 (
    echo %date% %time% 異常終了しました。
    exit /B %errorlevel%
)

echo %date% %time% 正常終了しました。