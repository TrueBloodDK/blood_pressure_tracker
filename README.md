# Blood Pressure Tracker
## Функциональность
- Регистрация и авторизация пользователей
- Создание записей давления (систолическое, диастолическое, пульс)
- Просмотр последней записи
- Статистика за сутки и месяц (среднее, минимум, максимум)
- REST API с токен-авторизацией
- Веб-интерфейс для работы с данными

## Установка и запуск

### 1. Клонировать репозиторий
```bash
git clone https://github.com/TrueBloodDK/blood_pressure_tracker.git
cd blood_pressure_tracker
```

### 2. Создать и активировать виртуальное окружение
```bash
python -m venv venv
source venv/bin/activate  # Linux (В зависимости от шела нужно будет активировать activate.fish или activate.zsh)
venv\Scripts\activate     # Windows
```

### 3. Установить зависимости
```bash
pip install -r requirements.txt
```

### 4. Создать базу данных PostgreSQL
```sql
CREATE USER tracker WITH PASSWORD 'пароль';
CREATE DATABASE blood_pressure_db OWNER tracker;
GRANT ALL PRIVILEGES ON DATABASE blood_pressure_db TO tracker;
```

### 5. Настроить переменные окружения 
Создать файл `.env` в заполнить его по примеру `.env.example`:

```env
SECRET_KEY=твой_секретный_ключ
DEBUG=True

DB_NAME=blood_pressure_db
DB_USER=твой_пользователь
DB_PASSWORD=твой_пароль
DB_HOST=localhost
DB_PORT=5432
```
### 6. Применить миграции
```bash
python manage.py migrate
```

### 7. Создать суперпользователя
```bash
python manage.py createsuperuser
```

### 8. Запустить сервер
```bash
python manage.py runserver
```

## Использование
### Веб-интерфейс
В графическом виде можно начать работу просто перейдя на корневой энпдоинт: `http://127.0.0.1:8000
### REST API
Все API запросы требуют токен-авторизацию:
```markdown
Authorization: Token ваш_токен
```

#### Получить токен
```
POST /api/auth/token/
````
```json
{
    "username": "пользователь",
    "password": "пароль"
}
```

#### Создать запись
````
POST /api/records/create/
````
```json
{
    "systolic": 120,
    "diastolic": 80,
    "pulse": 70
}
```

#### Посмотреть статистику
```
GET /api/records/latest/
GET /api/records/statistics/?period=day
GET /api/records/statistics/?period=month
```
