def word_counts(text):
    words = text.lower().split()
    result = {}
    for word in words:
        word = word.strip(".,!?;:")
        if not word:
            continue
        result[word] = result.get(word, 0) + 1
    return result


def common_topics(first, second):
    return sorted(set(first) & set(second))


def all_topics(first, second):
    return sorted(set(first) | set(second))


def totals_by_category(records):
    total = {}
    for record in records:
        category = record["category"]
        amount = record["amount"]
        total[category] = total.get(category, 0) + amount
    return total


def titles_in_category(records, category):
    total = []
    for record in records:
        if record["category"] == category:
            total.append(record["title"])
    return total


def alphabet_sort(totals):
    for total in sorted(totals):
        print(f"{total}: {totals[total]}")


def get_sorted(records):
    totals = totals_by_category(records)
    result = list(totals.items())
    return sorted(result, key=lambda x: (-x[1], x[0]))
