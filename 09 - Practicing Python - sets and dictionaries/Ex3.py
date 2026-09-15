""" Laura and Ana decided to go shopping together, but they created two different
shopping lists. They want a program that shows:

- Which items appear on both lists
- Which items are exclusive to Laura
- Which items are exclusive to Ana

Write a program that asks for the lists and displays the results of these comparisons.

Input Example:
Laura's list: milk, bread, coffee, sugar
Ana's list: bread, coffee, cookies, chocolate

Expected Output:
Items on both lists: bread, coffee
Items exclusive to Laura: milk, sugar
Items exclusive to Ana: cookies, chocolate """

laura_list = set(input("Enter the Laura's shopping list: ").split(', '))
ana_list = set(input("Enter the Ana's shopping list: ").split(', '))

common_items = laura_list.intersection(ana_list)
laura_exclusive_items = laura_list.difference(ana_list)
ana_exclusive_items = ana_list.difference(laura_list)

print(
    f"Items on both lists: {', '.join(sorted(common_items))}\n"
    f"Items exclusive to Laura: {', '.join(sorted(laura_exclusive_items))}\n"
    f"Items exclusive to Ana: {', '.join(sorted(ana_exclusive_items))}"
)
