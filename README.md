# Генератор HTML-страницы об Университете «Синергия»

Учебный проект для кейс-задачи № 5.

Программа на Python генерирует HTML-страницу с заголовком:

> «Наименование организации, на базе которой Вы проходите практическую подготовку»

На странице размещена информация об Университете «Синергия», добавлены CSS-стили и интерактивное переключение между основным и пятью дополнительными вариантами шрифта.

## Варианты шрифтов

1. Основной фирменный вариант — системный гротеск `Arial / Helvetica`;
2. Inter;
3. Roboto;
4. Open Sans;
5. Montserrat;
6. PT Sans.

Дополнительные шрифты загружаются через Google Fonts. При отсутствии интернета используются системные резервные шрифты.

## Файлы проекта

```text
.
├── generate_page.py
├── index.html
├── styles.css
├── script.js
├── README.md
└── .gitignore
```

## Запуск программы

Для генерации страницы необходим Python 3.9 или новее.

```bash
python generate_page.py
```

После выполнения будет создан или обновлён файл `index.html`.

Для просмотра страницы откройте `index.html` в браузере.

Также можно запустить локальный сервер:

```bash
python -m http.server 8000
```

Затем открыть в браузере:

```text
http://localhost:8000
```

## Публикация на GitHub

```bash
git init
git add .
git commit -m "Add Synergy University HTML page generator"
git branch -M main
git remote add origin https://github.com/USERNAME/synergy-html-generator.git
git push -u origin main
```

После публикации в качестве ответа на задание можно указать ссылку:

```text
https://github.com/USERNAME/synergy-html-generator
```

## Публикация через GitHub Pages

В репозитории откройте:

`Settings → Pages → Deploy from a branch → main / root`

После этого страница будет доступна по адресу:

```text
https://USERNAME.github.io/synergy-html-generator/
```
