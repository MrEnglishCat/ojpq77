# ojpq77

## 🛠️ развертывание

### 1. Клонировать репозиторий:
```bash
git clone https://github.com/MrEnglishCat/ojpq77.git

cd yaon77

```

### 2. Дальше нужно установить на систему докер
https://docs.docker.com/engine/install/

### 3. После перехода в каталог проекта ```cd ojpq77``` 
нужно запустить сборку и запуск всех контейнеров через docker-compose.yml


```
docker compose up --build
```
## Ниже что связано с phpMyAdmin - нужно только для просмотра базы данных. Для работы самого приложения он не нужен. 
После запуска контейнеров можно сразу переходить к пункту 6. На страницу Flask app.

### 4. phpMyAdmin работает на порту 8080 

http://localhost:8080

Заходим в него. 
```aiignore
username = root
password = root
```

### 6. Адреса страниц:
    http://localhost:8080  - phpMyAdmin
    http://localhost:8081  - web app Django
    http://localhost:8082  - web app Django доступ через Nginx