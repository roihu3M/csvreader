
# csvreader

Запуск:
```
python main.py --files [FILES] --report {report}
```
Запуск тестов:
```
pytest --cov
```
Добавление новых отчётов:
1. В reports.py в классе Reports создайте новый метод для создания отчётов
2. В main.py добавьте новый метод в reports_dict:
```
reports_dict = {
    'example-report' : Reports.example_report
}

```


