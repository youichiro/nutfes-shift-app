## Setup

MySQLのデータベースを作成

```bash
mysql -u root -p
> create database nutfes_shift_app;
```

クローン&ライブラリのインストール

```bash
git clone git@github.com:youichiro/nutfes-shift-app.git
cd nutfes-shift-app
pip install -r requirements.txt
```

データベースの設定

```bash
cp config/local_settings_example.py config/local_settings.py
# config/local_settings.pyにMySQLの設定を穴埋めする
```

マイグレート&データの登録

```bash
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser

# config/constants.pyの初期値を確認する
python manage.py init_db

# 名簿スプレッドシートをexcel形式でダウンロードし，static/xlsx/members.xlsxに保存する
# apps/shift/scripts/member_register.pyの設定を確認する
python manage.py member_registration

# シフトスプレッドシートをexcel形式でダウンロードし，static/xlsx/shift.xlsxに保存する
# split_xlsx.pyでシート別のexcelファイルを作成する
python split_xlsx.py -f static/xlsx/shift.xlsx -o static/xlsx
 
# apps/shift/scripts/shift_register.pyの設定を確認する
python manage.py shift_registration

# タイムテーブルスプレッドシートをexcel形式でダウンロードし，static/xlsx/timetable.xlsxに保存する
# apps/timetable/scripts/timetable_register.pyの設定を確認する 
python manage.py timetable_registration

python manage.py loaddata fixtures/01_manual.yaml
python manage.py create_member_json
python manage.py create_shift_data_json
python manage.py create_my_shift_data_json
python manage.py create_timetable_data_json
```

起動
```bash
gunicorn config.wsgi:application -b 0.0.0.0:8001 --daemon
```

停止
```bash
pkill gunicorn
```
