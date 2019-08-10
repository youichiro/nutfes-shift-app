## Setup

```bash
mysql -u root -p
> create database nutfes_shift_app;
```

```bash
git clone this.repository
cd this.repository
python manage.py migrate
python manage.py init_db
python manage.py member_registration
python manage.py shift_registration 
python manage.py timetable_registration
python manage.py loaddata fixtures/01_manual.yaml
python manage.py create_shift_data_json
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