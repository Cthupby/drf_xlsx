# DRF xlsx app
### Приложение для обработки файлов xlsx на Django Rest Framework

```
1. эндпоинт для обработки файла bills.xlsx

В базу писать только валидные счета. Счет считается валидным, если выполнены все условия:
    • значение sum является числом
    • в service не пусто ( пусто так же считается, если вместо текста знак “-”)
    • корректная дата (дата считается корректной, если есть день, месяц и год).
    • №(номер счет) тип  int
    • client_name, client_org не пустые

2. эндпоинт со списком счетов с возможностью фильтровать по организации, клиенту.
```

## Установка и использование

1. Необходимо скачать проект  
2. Создать и активировать виртуальное окружение  
   ```python -m virualenv venv```  
   ```source ./venv/bin/activate```
3. Установить рекомендуемые библиотеки  
  ```pip install -r requirements.txt```
4. Запустить миграции базы данных и запустить проект  
  ```python manage.py migrate```  
  ```python manage.py runserver```  
