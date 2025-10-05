from pyscript import display, document

# PROJECT/main.py
# This module exposes `create_order` to the HTML page so the ordering form can
# build a summary of selected menu items and customer details. It is intentionally
# client-side only: in a real application you'd send the order to a server.

__all__ = ["create_order"]  # <-- the HTML page can call create_order via py-click

# Price table: keys match the checkbox `id` attributes in the HTML order form.
# Prices are in Philippine pesos (₱) for display purposes.
PRICES = {
    "goo_spaghetti": 150,
    "live_chicken": 250,
    "chocolate_milkshake": 120,
    "human_salad": 130,
    "toe_fries": 75,
}


def create_order(evt=None):
    """Build and display an order summary.

    Steps:
    1. Inspect each checkbox (by id) and add selected items to the order.
    2. Read customer name, address and contact fields from the form.
    3. Format a multi-line summary and display it in the page using PyScript's
       `display(..., target=...)` helper.
    """
    total = 0
    items = []

    # 1) Collect selected items and compute total
    for item_id, price in PRICES.items():
        el = document.getElementById(item_id)
        if el and el.checked:
            # create a nicer title for display (e.g. 'Goo Spaghetti')
            items.append((item_id.replace("_", " ").title(), price))
            total += price

    # 2) Read customer details (provide 'N/A' defaults if fields are empty)
    name = (document.getElementById("cust_name").value or "").strip() or "N/A"
    address = (document.getElementById("cust_address").value or "").strip() or "N/A"
    contact = (document.getElementById("cust_contact").value or "").strip() or "N/A"

    # 3) Build the human-readable summary
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

    # Display the summary in the page. The page's CSS uses pre-wrap so newlines
    # render as line breaks.
    display(f"{summary}", target="order-summary")
