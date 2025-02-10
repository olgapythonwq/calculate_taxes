1. Создайте проект, используя poetry, создайте структуру проекта и напишите тесты для функции 
`calculate_taxes`. Отправьте код на GitHub.

2. Используя TDD-методологию, напишите функцию `calculate_tax`, которая принимает два аргумента:
 
- `price` — цена товара (`float`);
- `tax_rate` — налоговый процент (`float`).
Функция должна вычислять стоимость товара с учетом налога и возвращать результат (`float`).

Требования:

- Если цена товара `price` не положительная, функция должна возбуждать исключительную ситуацию `ValueError`
 с сообщением «Неверная цена».
- Если `tax_rate` меньше нуля, больше или равен `100%`, функция должна возбуждать исключительную ситуацию `ValueError`
 с сообщением «Неверный налоговый процент».
Пример использования:
```python
result = calculate_tax(100, 10)
assert result == 110.0

result = calculate_tax(50, 5)
assert result == 52.5
```
Функцию добавьте в текущий проект из первого задания. Отправьте код на GitHub.

3. Используя TDD-методологию, доработайте функцию `calculate_tax`:
 Добавьте в функцию возможность вычислять цену товара с учетом скидки. Скидка передается в виде аргумента, выраженного 
 в процентах. Если скидки нет, значение равно 0. Функция должна вернуть стоимость товара с учетом налога и скидки 
 (скидка берется от цены с учетом налога).
 Добавьте возможность округления результата до заданной точности (двух знаков после запятой по умолчанию).
 Добавьте обработку исключительной ситуации, возникающей при передаче аргументов типа, отличного от `int` или `float`.
 Все новые параметры должны быть только именованными. Позиционными функция может принимать только два параметра: цену 
 и налог.