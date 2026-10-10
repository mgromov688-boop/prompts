# Знаки сервисов · откуда взят каждый (10.10.2026)

Ни один знак не перерисован. Однотонные файлы — те же пути, что в первоисточнике, без заливки: цвет задаёт
страница (`currentColor` / CSS-маска). Реестр для кода и будущей живой обложки — `logos.json` рядом.

| Файл | Знак | Первоисточник | Как получен | Фирменный цвет |
|---|---|---|---|---|
| `anthropic.svg` | Anthropic | anthropic.com | simple-icons 16.34.0 (CC0, пути с сайта бренда) | `#191919` |
| `claude.svg` | Claude | claude.ai | simple-icons 16.34.0 | `#D97757` |
| `openai.svg` | OpenAI | openai.com | simple-icons **13** (в версиях 14+ убран по требованию бренда) | `#000000` (монохром у бренда) |
| `google.svg` | Google «G» однотонный | partnermarketinghub.withgoogle.com | simple-icons 16.34.0 | 4 цвета, см. ниже |
| `google_color.svg` | Google «G» цветной | Google, файл Wikimedia Commons `Google_"G"_logo.svg` | загружен как есть | ⚠️ по брендбуку Google «G» показывается в цвете; однотонный вариант допускается, когда цвет недоступен. **С 10.10 на странице гайда стоит он** (Максим: «Гугл оригинальный значек оставь»), без перекраски |
| `googlegemini.svg` | Google Gemini | gemini.google.com | simple-icons 16.34.0 | `#8E75B2` (у бренда градиент) |
| `n8n.svg` | n8n | n8n.io/press | simple-icons 16.34.0 | `#EA4B71` |
| `huggingface.svg` | Hugging Face | huggingface.co/brand | simple-icons 16.34.0 | `#FFD21E` |
| `kaggle.svg` | Kaggle | kaggle.com/brand-guidelines | simple-icons 16.34.0 | `#20BEFF` |
| `nvidia.svg` | NVIDIA | nvidia.com | simple-icons 16.34.0 | `#76B900` ⚠️ брендбук NVIDIA: знак зелёный либо чёрный/белый — однотонный на бумаге допустим |
| `coursera.svg` | Coursera | about.coursera.org/press | simple-icons 16.34.0 | `#0056D2` |
| `stepik_original.svg` | Stepik | stepik.org `/static/classic/ico/favicon.svg` | загружен как есть | `#222222` |
| `stepik.svg` | Stepik однотонный | из `stepik_original.svg` | два пути знака, белый путь стал вырезом (`evenodd`); прямоугольник clipPath отброшен | — |
| `elementsofai_original.svg` | Elements of AI | шапка elementsofai.com | инлайновый SVG знака, без изменений путей | `#4844A3` |
| `elementsofai.svg` | Elements of AI однотонный | из `elementsofai_original.svg` | те же два круга без заливки | — |
| `deeplearningai_original.png` | DeepLearning.AI (знак + надпись) | deeplearning.ai `/dlai/assets/dlai-logo.png`, 2677×601, RGBA | загружен как есть; SVG у них нет | коралловый, HEX не замерял |

**Чего нет и почему:** Harvard CS50 — простого знака у курса нет (герб Гарварда на 16 px не читается, у CS50 своего
знака на сайте нет), поэтому у строки CS50P знак не ставится. Знак DeepLearning.AI на странице показан CSS-маской
по левому квадрату PNG (знак занимает x 24–348, y 134–458 из 2677×601), сам файл не обрезан.

Обновить: `node ../../fetch_logos.js` и `node ../../fetch_logos2.js` (папка v2).
