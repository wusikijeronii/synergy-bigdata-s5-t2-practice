# Задание 5 - База данных интернет-магазина

База данных интернет-магазина, включающая информацию о товарах, клиентах, доставке, скидках и заказах.

## Что реализовано

* клиенты
* товары
* скидки
* доставка
* заказы
* состав заказов

## Аналитика

### Выручка по товарам

```sql
SELECT
    p.name,
    SUM(oi.quantity) AS total_sold,
    SUM(oi.quantity * oi.item_price) AS total_revenue
FROM order_items oi
JOIN products p ON p.id = oi.product_id
GROUP BY p.name
ORDER BY total_revenue DESC;
```

### Самые активные клиенты

```sql
SELECT
    c.full_name,
    COUNT(o.id) AS total_orders
FROM orders o
JOIN customers c ON c.id = o.customer_id
GROUP BY c.full_name
ORDER BY total_orders DESC;
```

### Статистика по категориям

```sql
SELECT
    p.category,
    SUM(oi.quantity) AS total_units_sold,
    SUM(oi.quantity * oi.item_price) AS total_revenue
FROM order_items oi
JOIN products p ON p.id = oi.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;
```

### Потенциально популярные товары

```sql
SELECT
    p.name,
    SUM(oi.quantity) AS total_sold
FROM order_items oi
JOIN products p ON p.id = oi.product_id
GROUP BY p.name
ORDER BY total_sold DESC
LIMIT 5;
```

## Используемые технологии

* СУБД: PostgreSQL 18.3
* ОС: Manjaro Linux (Arch-based)

## Файл

* `ecommerce.sql` - дамп базы данных

## Примечание

Решение выполнено в учебных целях в упрощённом виде.
