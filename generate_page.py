from pathlib import Path
from html import escape

ORGANIZATION = {
    "title": "Университет «Синергия»",
    "full_name": (
        "Автономная некоммерческая организация высшего образования "
        "«Московский университет „Синергия“»"
    ),
    "short_name": "Университет «Синергия»",
    "legal_form": "Автономная некоммерческая организация высшего образования",
    "location": "г. Москва",
    "description": (
        "Университет «Синергия» — негосударственная образовательная организация, "
        "реализующая программы среднего профессионального, высшего, дополнительного "
        "и бизнес-образования. Обучение проводится в очном, очно-заочном, заочном "
        "и дистанционном форматах."
    ),
    "activities": [
        "реализация программ среднего профессионального образования;",
        "подготовка бакалавров, специалистов и магистров;",
        "реализация программ аспирантуры и дополнительного образования;",
        "организация дистанционного обучения;",
        "научная, методическая и просветительская деятельность;",
        "содействие практике и трудоустройству обучающихся.",
    ],
}

FONT_OPTIONS = [
    ("brand", "Фирменный вариант", "Arial, Helvetica, sans-serif"),
    ("inter", "Inter", "'Inter', Arial, sans-serif"),
    ("roboto", "Roboto", "'Roboto', Arial, sans-serif"),
    ("open-sans", "Open Sans", "'Open Sans', Arial, sans-serif"),
    ("montserrat", "Montserrat", "'Montserrat', Arial, sans-serif"),
    ("pt-sans", "PT Sans", "'PT Sans', Arial, sans-serif"),
]


def build_font_buttons() -> str:
    buttons = []
    for css_class, label, _ in FONT_OPTIONS:
        active = " active" if css_class == "brand" else ""
        buttons.append(
            f'<button class="font-button{active}" '
            f'data-font="{escape(css_class)}">{escape(label)}</button>'
        )
    return "\n".join(buttons)


def build_activity_items() -> str:
    return "\n".join(
        f"<li>{escape(item)}</li>" for item in ORGANIZATION["activities"]
    )


def generate_html(output_path: str = "index.html") -> Path:
    page = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta
        name="description"
        content="Информация об Университете Синергия — базе практической подготовки"
    >
    <title>{escape(ORGANIZATION["title"])}</title>

    <!-- Пять дополнительных вариантов шрифтов -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link
        href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Montserrat:wght@400;500;600;700;800&family=Open+Sans:wght@400;500;600;700&family=PT+Sans:wght@400;700&family=Roboto:wght@400;500;700;900&display=swap"
        rel="stylesheet"
    >

    <link rel="stylesheet" href="styles.css">
</head>
<body class="font-brand">
    <header class="hero">
        <div class="hero__decoration hero__decoration--one"></div>
        <div class="hero__decoration hero__decoration--two"></div>

        <nav class="navigation container" aria-label="Навигация по странице">
            <a class="brand" href="#about" aria-label="Университет Синергия">
                <span class="brand__symbol">S</span>
                <span>
                    <strong>СИНЕРГИЯ</strong>
                    <small>Университет</small>
                </span>
            </a>
            <a class="navigation__link" href="#about">Об организации</a>
        </nav>

        <div class="hero__content container">
            <p class="eyebrow">Кейс-задача № 5 · Практическая подготовка</p>
            <h1>Наименование организации, на базе которой Вы проходите практическую подготовку</h1>
            <p class="hero__organization">{escape(ORGANIZATION["title"])}</p>
            <a class="primary-button" href="#about">Подробнее об организации</a>
        </div>
    </header>

    <main>
        <section class="font-panel" aria-labelledby="font-title">
            <div class="container">
                <div>
                    <p class="section-label">Типографика</p>
                    <h2 id="font-title">Выберите вариант шрифта</h2>
                    <p>
                        Основной вариант стилизован под современную типографику
                        официальных цифровых материалов университета. Дополнительно
                        представлены пять распространённых шрифтов с поддержкой кириллицы.
                    </p>
                </div>
                <div class="font-buttons" role="group" aria-label="Выбор шрифта">
                    {build_font_buttons()}
                </div>
                <p class="current-font">
                    Активный шрифт: <strong id="current-font-name">Фирменный вариант</strong>
                </p>
            </div>
        </section>

        <section class="about container" id="about">
            <div class="about__heading">
                <p class="section-label">Об организации</p>
                <h2>{escape(ORGANIZATION["title"])}</h2>
                <p>{escape(ORGANIZATION["description"])}</p>
            </div>

            <div class="facts">
                <article class="fact-card">
                    <span class="fact-card__number">01</span>
                    <h3>Полное наименование</h3>
                    <p>{escape(ORGANIZATION["full_name"])}</p>
                </article>

                <article class="fact-card">
                    <span class="fact-card__number">02</span>
                    <h3>Организационно-правовая форма</h3>
                    <p>{escape(ORGANIZATION["legal_form"])}</p>
                </article>

                <article class="fact-card">
                    <span class="fact-card__number">03</span>
                    <h3>Территориальное размещение</h3>
                    <p>
                        Головная организация находится в {escape(ORGANIZATION["location"])}.
                        Образовательные услуги также оказываются дистанционно.
                    </p>
                </article>
            </div>
        </section>

        <section class="activities">
            <div class="container activities__grid">
                <div>
                    <p class="section-label section-label--light">Основная деятельность</p>
                    <h2>Образовательные услуги и направления работы</h2>
                </div>
                <ul class="activity-list">
                    {build_activity_items()}
                </ul>
            </div>
        </section>

        <section class="digital container">
            <div class="digital__card">
                <div>
                    <p class="section-label">Цифровая образовательная среда</p>
                    <h2>Обучение без территориальных ограничений</h2>
                </div>
                <p>
                    В образовательном процессе используются личные кабинеты студентов
                    и абитуриентов, электронные учебные материалы, онлайн-тестирование,
                    вебинары, электронные библиотечные системы и дистанционные
                    образовательные технологии.
                </p>
            </div>
        </section>
    </main>

    <footer>
        <div class="container footer__content">
            <p>Учебный проект по практике</p>
            <p>© 2026 · Университет «Синергия»</p>
        </div>
    </footer>

    <script src="script.js"></script>
</body>
</html>
"""
    output = Path(output_path)
    output.write_text(page, encoding="utf-8")
    return output


if __name__ == "__main__":
    result = generate_html()
    print(f"HTML-страница создана: {result.resolve()}")
