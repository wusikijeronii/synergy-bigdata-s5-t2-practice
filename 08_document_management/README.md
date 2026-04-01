# Задание 8 - Система учета корреспонденции

Программа для учета входящей и исходящей корреспонденции.

## Что делает
- читает данные о документах из CSV-файла
- выводит информацию об отправителях и получателях
- показывает направление документа
- показывает статус отправки или получения
- выводит простую статистику

## Формат CSV

```csv
document_id,document_type,subject,sender,recipient,direction,status,date
1,Letter,Contract,Company A,Company B,Incoming,Received,2026-04-01
2,Invoice,Payment,Company B,Company A,Outgoing,Sent,2026-04-02
```

## Запуск
```sh
python3 document_management.py documents.csv
```