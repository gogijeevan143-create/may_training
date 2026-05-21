def demonstrate_mutable_default_bug():
    print("Part A - Buggy function output:")

    def add_item(item, cart=[]):
        cart.append(item)
        return cart

    print(add_item("apple"))
    print(add_item("banana"))
    print(add_item("milk", cart=["bread"]))
    print(add_item("eggs"))
    print(
        "Explanation: apple, banana, and eggs share the same default list because "
        "the default list is created only once when the function is defined.\n"
    )


def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart


def create_cart(owner, discount=0):
    return {"owner": owner, "items": [], "discount": discount}


def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({"name": name, "price": price, "qty": qty})


def update_price(price_tuple, new_price):
    try:
        price_tuple[1] = new_price
    except TypeError as error:
        # Tuples are immutable, so their existing elements cannot be changed.
        print("Tuple update failed:", error)


def calculate_total(cart):
    subtotal = 0
    for item in cart["items"]:
        subtotal += item["price"] * item["qty"]

    discount_amount = subtotal * cart["discount"] / 100
    return subtotal - discount_amount


def show_cart(cart):
    print(f"\nCart Owner: {cart['owner']}")
    print(f"Discount: {cart['discount']}%")
    print("Items:")

    if not cart["items"]:
        print("No items in cart.")
    else:
        for item in cart["items"]:
            print(f"- {item['name']}: Rs.{item['price']} x {item['qty']}")

    print(f"Final Total: Rs.{calculate_total(cart)}")


def main():
    demonstrate_mutable_default_bug()

    print("Part B - Fixed function output:")
    print(add_item("apple"))
    print(add_item("banana"))
    print(add_item("milk", cart=["bread"]))
    print(add_item("eggs"))

    print("\nPart C - Complete shopping cart:")
    aarav_cart = create_cart("Aarav", discount=10)
    diya_cart = create_cart("Diya")

    add_to_cart(aarav_cart, "Notebook", 60, qty=3)
    add_to_cart(aarav_cart, "Pen", 10, qty=5)
    add_to_cart(diya_cart, "Bag", 750)
    add_to_cart(diya_cart, "Pencil Box", 120, qty=2)

    update_price(("Notebook", 60), 70)

    show_cart(aarav_cart)
    show_cart(diya_cart)

    print("\nIndependent cart proof:")
    print("Aarav cart items:", aarav_cart["items"])
    print("Diya cart items:", diya_cart["items"])


if __name__ == "__main__":
    main()


# Discussion Answers:
# 1. discount=0 is safe because integers are immutable. cart=[] is dangerous
#    because a list is mutable and the same default list is reused in every
#    function call where no cart is provided.
#
# 2. Rebinding means making a variable name point to a new object, for example
#    x = [1, 2] followed by x = [3, 4]. Mutating means changing the same object,
#    for example x.append(3).
#
# 3. Mutable types: list, dict, set.
#    Immutable types: tuple, str, int.
#
# 4. Yes, if a list is passed into a function and the function mutates it,
#    the change is visible outside because both the outside variable and the
#    function parameter refer to the same list object.
