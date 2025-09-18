
Order to run the scripts in:

```
cd music_production_and_performance/django

rm db.sqlite3
rm -R theory_western/migrations

python manage.py makemigrations theory_western

python manage.py migrate

python scripts/populate_pitch_classes.py

python scripts/populate_fifths.py

python scripts/load_camelot_numbers.py
```
