# 「Pipfile」ファイルから仮想環境を構築（Windowsコマンドプロンプト）
```
set PIPENV_VENV_IN_PROJECT=1
set PIPENV_SKIP_LOCK=1
pipenv install
```
※`pipenv`がインストールされていない場合は事前に以下のコマンドでインストールする
```
pip install pipenv
```
## 注意事項
`pipenv install`実行時に以下のような警告が出た場合は、インストールされているPythonのバージョンと`Pipfile`ファイルのバージョンを合わせた後、再度実行すること
```
Warning: Python 3.9 was not found on your system...
Neither 'pyenv' nor 'asdf' could be found to install Python.
```
![image](https://github.com/TokiNoviceProgrammer/competitive-programming/assets/119168264/2de4d2f5-7657-4edd-bd34-854ee8162236)

# 仮想環境をアクティブにする
```
.venv\Scripts\activate
```
PowerShellにて以下のエラーが発生する場合がある
```
& : このシステムではスクリプトの実行が無効になっているため、ファイル C:\competitive-programming\.venv\Scrip 
ts\Activate.ps1 を読み込むことができません。詳細については、「about_Execution_Policies」(https://go.microsoft.com/fwlink/?LinkID=135170 
発生場所 行:1 文字:3
+ & c:/Users/tdcsoft/Desktop/local/competitive-programming/.venv/Script ...
+   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : セキュリティ エラー: (: ) []、PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```
上記のエラー発生時は、以下のコマンドを実行する
```
powershell -ExecutionPolicy RemoteSigned
```

# コード整形(実行例)
```
isort app.py
black app.py
```
