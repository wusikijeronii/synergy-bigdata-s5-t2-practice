# Практическое задание - База данных учета продаж
## Реализация

В рамках задания была разработана реляционная база данных с использованием PostgreSQL.

### Структура базы данных

База данных включает следующие таблицы:

* **categories** - категории товаров
* **products** - товары
* **sales** - продажи

Связи:

* product → category
* sale → product

## SQL-запрос для анализа

```sql
SELECT
    EXTRACT(DOW FROM s.sale_date) AS weekday_num,
    TRIM(TO_CHAR(s.sale_date, 'Day')) AS weekday,
    c.name AS category,
    SUM(s.quantity) AS total_units_sold,
    SUM(s.quantity * p.price) AS total_revenue
FROM sales s
JOIN products p ON p.id = s.product_id
JOIN categories c ON c.id = p.category_id
GROUP BY
    EXTRACT(DOW FROM s.sale_date),
    TO_CHAR(s.sale_date, 'Day'),
    c.name
ORDER BY
    weekday_num,
    c.name;
```

## Используемые технологии

* СУБД: PostgreSQL 18.3
* ОС: Manjaro Linux (Arch-based)

## Файлы
* `sales_accounting.sql` - дамп базы данных
