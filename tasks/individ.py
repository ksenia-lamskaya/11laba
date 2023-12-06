#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def help1():
    """"
    Функция для вывода списка команд
    """
    # Вывести справку о работе с программой.
    print("Список команд:\n")
    print("add - добавить маршрут;")
    print("list - вывести список маршрутов;")
    print("select <тип> - вывод на экран пунктов маршрута, используя номер маршрута;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")


def add1():
    """"
    Функция для добавления информации о новых маршрутах
    """
    # Запросить данные о маршруте.
    name = input("Название начального пункта маршрута:  ")
    name2 = input("Название конечного пункта маршрута: ")
    number = int(input("Номер маршрута: "))

    # Создать словарь.
    i = {'name': name, 'name2': name2, 'number': number}

    return i


def error1(command):
    """"
    функция для неопознанных команд
    """
    print(f"Неизвестная команда {command}")


def list(point):
    """"
    Функция для вывода списка добавленных маршрутов
    """
    # Заголовок таблицы.
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
    '-' * 4,
    '-' * 30,
    '-' * 20,
    '-' * 8
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
            "№",
            "Начальный пункт.",
            "Конечный пункт",
            "№ маршрута"
        )
    )
    print(line)

    # Вывести данные о всех маршрутах.
    for idx, i in enumerate(point, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                idx,
                i.get('name', ''),
                i.get('name2', ''),
                i.get('number', '')
            )
    )
    print(line)


def select(point):
    """""
    Функция для получения маршрута по его номеру
    """
    # Разбить команду на части для выделения номера маршрута.
    parts = input("Введите значение: ")
    # Проверить сведения работников из списка.

    # Проверить сведения.
    flag = True
    for i in point:
        if i['number'] == int(parts):
            print("Начальный пункт маршрута - ", i["name"])
            print("Конечный пункт маршрута - ", i["name2"])
            flag = False
            break
    if flag:
        print("Маршрут с таким номером не найден")


def main():
    """"
    Главная функция программы.
    """
    print("Список команд:\n")
    print("add - добавить маршрут;")
    print("list - вывести список маршрутов;")
    print("select <тип> - вывод на экран пунктов маршрута, используя номер маршрута;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")
    # Список маршрутов.
    point = []
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()
        # Выполнить действие в соответствие с командой.

        match command:
            case 'exit':
                break

            case 'add':
                # Добавить словарь в список.
                i = add1()
                point.append(i)
                # Отсортировать список в случае необходимости.
                if len(point) > 1:
                    point.sort(key=lambda item: item.get('number', ''))

            case 'list':
                list(point)

            case 'select':
                select(point)

            case 'help':
                help1()

            case _:
                error1(command)


if __name__ == '__main__':
    main()