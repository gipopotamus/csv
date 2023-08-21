
## Документация по API

API предоставляет следующие эндпоинты:

1. **Загрузка файла**:
   - URL: `/api/upload`
   - Метод: POST
   - Параметры: `file` (тип файла): CSV-файл для загрузки

2. **Список файлов**:
   - URL: `/api/files`
   - Метод: GET

3. **Данные файла**:
   - URL: `/api/files/<filename>`
   - Метод: GET
   - Параметры:
     - `filters` (необязательный): Фильтры в формате `column:value,column:value`
     - `sort_by` (необязательный): Столбец для сортировки

4. **Удаление файла**:
   - URL: `/api/files/<filename>`
   - Метод: DELETE

## Развертывание приложения

1. Установите Docker, если он еще не установлен.

2. Склонируйте репозиторий с кодом:

   ```bash
   git clone https://github.com/yourusername/kaggle-parser.git
   ```

3. Перейдите в папку проекта:

   ```bash
   cd kaggle-parser
   ```

4. Соберите и запустите Docker-контейнер:

   ```bash
   docker build -t kaggle-parser .
   docker run -p 5000:5000 kaggle-parser
   ```

5. Ваше приложение будет доступно по адресу `http://localhost:5000`.

Примечание: Папка uploads будет создана автоматически при первой загрузке файла, если она отсутствует.


