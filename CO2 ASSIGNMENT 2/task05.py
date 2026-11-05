# Q5 - Canteen orders, parameters and scope
def add_item_buggy(item, order=[]):
    order.append(item)
    return order

def add_item(item, order=None):
    if order is None:
        order = []
    order.append(item)
    return order

def calculate_bill(amount, gst_rate=0.05):
    gst = amount * gst_rate
    total = amount + gst
    return total, gst

global_count = 0

def demonstrate_global():
    global global_count
    global_count += 1
    return global_count

def outer():
    message = "outer"
    def inner():
        nonlocal message
        message = "changed by inner"
    inner()
    return message

if __name__ == "__main__":
    print(add_item_buggy("Tea"), add_item_buggy("Vada"))
    print("Shared defaults:", add_item_buggy.__defaults__)
    print(add_item("Tea"), add_item("Vada"))
    print("Customer orders:")
    for customer_items in (["Tea", "Vada"], ["Coffee"], ["Juice", "Samosa"]):
        order = []
        for item in customer_items:
            add_item(item, order)
        print(order)
    total, gst = calculate_bill(200)
    print(f"Total={total:.2f}, GST={gst:.2f}")
    print("Global:", demonstrate_global())
    print("Nonlocal:", outer())

    # A local variable exists only inside its function.
    def local_example():
        local_value = 10
        return local_value
    print("Local:", local_example())
