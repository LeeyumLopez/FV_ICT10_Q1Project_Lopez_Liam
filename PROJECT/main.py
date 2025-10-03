from pyscript import display, document

__all__ = ["create_order"]  # <-- expose this function to HTML

PRICES = {
    "goo_spaghetti": 150,
    "live_chicken": 250,
    "chocolate_milkshake": 120,
    "human_salad": 130,
    "toe_fries": 75,
}

def create_order(evt=None):
    total = 0
    items = []

    # check which menu items were selected
    for item_id, price in PRICES.items():
        el = document.getElementById(item_id)
        if el and el.checked:
            items.append((item_id.replace("_", " ").title(), price))
            total += price

    # read customer details
    name = (document.getElementById("cust_name").value or "").strip() or "N/A"
    address = (document.getElementById("cust_address").value or "").strip() or "N/A"
    contact = (document.getElementById("cust_contact").value or "").strip() or "N/A"

    # build summary
    if not items:
        summary = "No items selected. Please choose at least one."
    else:
        lines = [
            f"Order for: {name}",
            f"Address: {address}",
            f"Contact: {contact}",
            "",
            "Items:"
        ]
        for title, price in items:
            lines.append(f" - {title}: ₱{price:.2f}")
        lines.append("")
        lines.append(f"Total: ₱{total:.2f}")
        summary = "\n".join(lines)

    # show result in the page
    display(f"{summary}", target="order-summary")
