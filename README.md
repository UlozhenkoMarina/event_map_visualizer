# event_map_visualizer
# Events Map Visualizer 🌍

MVP веб-додаток для відображення подій на інтерактивній мапі з можливістю фільтрації та додавання нових подій.

## 🚀 Функціонал

* 📍 Відображення подій на карті (React-Leaflet)
* 📝 Додавання нових подій через форму
* 🔎 Фільтрація подій:

  * по категорії
  * по даті
* 📋 Список подій
* ⚡ REST API для CRUD операцій

## 🛠️ Технології

### Backend

* FastAPI
* PostgreSQL
* SQLAlchemy (ORM)
* Pydantic (валідація)
* Uvicorn

### Frontend

* React
* Material UI
* React-Leaflet (карта)

### Testing

* Pytest (планується)

---

## 📂 Структура проєкту

```
project/
├── backend/
│   ├── app/
│   │   ├── models/
│   │   │   ├── orm/
│   │   │   └── schemas/
│   │   ├── crud/
│   │   ├── routes/
│   │   ├── database/
│   │   └── main.py
│   └── tests/
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── EventList.js
│   │   │   ├── EventForm.js
│   │   │   └── EventMap.js
│   │   └── api/
│   └── package.json
```

---


## 📌 Статус проєкту

🟡 Prototype (MVP в процесі розробки)

Планується:

* Додати тести (Pytest)
* Авторизація користувачів
* Збереження улюблених подій
* Аналітика


