Аргументы запуска. Собираем фикстуры, марки, и другую полезную информацию для отладки

--co
-k
-m
--markers
--fixtures
--durations=10
-l (--showlocals)
--setup-plan
Марки. Пропускаем тесты правильно

skip
xfail
uxefixtures
Параметризация. На тесте, на фикстуре. Переопределение параметров

pytest.mark.parametrize на тесте. Использование нескольких параметров
параметризация фикстуры.
indirect параметризация
ДЗ - github.com в мобильном и десктопном варианте.

Реализовать автотест для github.com, который заходит на страницу, ищет кнопку Sign In, и тыкает на нее (авторизоваться не нужно)

Нужно параметризовать тест различным размером окна браузера.

Обратите внимание, что для мобильной версии сайта потребуется другой автотест из-за изменения структуры локаторов.

Сделайте два варианта пропуска неподходящих параметров и тестов

Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
Переопределите параметр с помощью indirect
Сделайте разные фикстуры для каждого теста В чем преимущества и недостатки каждого из подходов?