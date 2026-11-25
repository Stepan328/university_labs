from collections_lab import (
    word_counts, common_topics, all_topics,
    totals_by_category, titles_in_category, alphabet_sort, get_sorted
)

if __name__ == "__main__":
    #Задание 1
    assert word_counts("Python, python! SQL") == {"python": 2, "sql": 1}
    assert word_counts("!!!") == {}
    assert word_counts("") == {}


    counts = word_counts("Python, python! SQL, git, git")
    alphabet_sort(counts)
    print()

    #Задание 2
    assert common_topics(["python", "sql", "python"], ["sql", "git"]) == ["sql"]
    assert all_topics(["python", "sql", "python"], ["sql", "git"]) == ["git", "python", "sql"]
    assert common_topics([], ["sql", "git"]) == []
    assert all_topics([], ["sql", "git"]) == ["git", "sql"]

    #Задание 3
    table = {'title': 'Python', 'hours': 10}
    table['hours'] = 13
    table['completed'] = False
    data = (table['title'], table['hours'])
    title, hours = data
    print(f"title = {title}")
    print(f"hours = {hours}")
    print()


    #Индивидуальный вариант №15
    records = [
        {"title": "Закат у реки", "category": "пейзаж", "amount": 12},
        {"title": "Горные вершины", "category": "пейзаж", "amount": 18},
        {"title": "Улицы старого города", "category": "город", "amount": 10},
        {"title": "Фасады домов", "category": "город", "amount": 5},
        {"title": "Семейный портрет", "category": "портрет", "amount": 8}
    ]


    prov = [i.copy() for i in records]


    assert totals_by_category(records) == {"пейзаж": 30, "город": 15, "портрет": 8}
    assert totals_by_category([]) == {}
    assert titles_in_category(records, "пейзаж") == ["Закат у реки", "Горные вершины"]
    assert titles_in_category(records, "нет") == []
    assert titles_in_category([], "пейзаж") == []
    assert records == prov

    # Дополнительное задание
    expected_sorted = [("пейзаж", 30), ("город", 15), ("портрет", 8)]
    assert get_sorted(records) == expected_sorted

    # Вывод сводки по категориям
    totals = totals_by_category(records)
    print("Сводка по категориям (по алфавиту):")
    for cat in sorted(totals):
        print(f"  {cat}: {totals[cat]}")

    # Поиск категории, введённой пользователем
    user_category = input("Введите категорию для поиска: ").strip().lower()
    found_titles = titles_in_category(records, user_category)

    if found_titles:
        print(f"Найдены задания в категории '{user_category}': {found_titles}")
    else:
        print(f"В категории '{user_category}' ничего не найдено ([]).")

    print("Все проверки пройдены.")
