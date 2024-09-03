"""Task 6 - Calculations: greedy and dynamic algorithms"""

from constants import ITEMS


def get_best_item_for_greedy(balance):
    """Max calories/cost from ITEMS SET <= balance"""
    res = None
    filtered_items = {k: v for k, v in ITEMS.items() if v["cost"] <= balance}
    if filtered_items:
        res = max(
            filtered_items,
            key=lambda k: (filtered_items[k]["calories"] / filtered_items[k]["cost"]),
        )
    return res


def get_best_item_for_dynamic(balance):
    """Max calories from ITEMS SET <= balance"""
    res = None
    filtered_items = {k: v for k, v in ITEMS.items() if v["cost"] <= balance}
    if filtered_items:
        res = max(
            filtered_items,
            key=lambda k: (filtered_items[k]["calories"]),
        )
    return res


def greedy_algorithm(budget):
    """Select dishes with best calories / cost"""
    dishes = {}
    while budget > 0:
        dish = get_best_item_for_greedy(budget)
        if dish:
            budget -= ITEMS.get(dish)["cost"]
            item = dishes.get(dish)
            dishes[dish] = item + 1 if item else 1
        else:
            budget = 0
    return dishes if dishes else None


def dynamic_programming(budget):
    """Calculate coins set for change"""
    memo = {}
    if budget == 0:
        return None
    dish = get_best_item_for_dynamic(budget)
    if dish:
        if budget - ITEMS.get(dish)["cost"] == 0:
            return {dish: 1}
        memo = dynamic_programming(budget - ITEMS.get(dish)["cost"])
        item = memo.get(dish)
        memo[dish] = item + 1 if item else 1
    return memo


if __name__ == "__main__":
    BUDGET = 537
    print(f"Results for budget = {BUDGET}:")
    print(f"{greedy_algorithm(BUDGET) = }")
    print(f"{dynamic_programming(BUDGET) = }")
