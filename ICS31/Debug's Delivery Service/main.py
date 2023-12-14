from collections import namedtuple

Customer = namedtuple('Customer', 'name order')

Store = namedtuple('Store', 'name inventory')

item = namedtuple('item', 'name price')

def drone_delivery_service(customers, stores):
    """
    Print Instructions for Drone Delivery Service.

    :param customers: [Customer(str, {str: float})]
    :param stores: [Store(str, {str: [float, int]})]
    """
    customer_totals = {}  # Use this for part 4
    # Your Code goes here:

    # Part 1:
    # Part 1A: Assuming the list is sorted in decending price, calculate and print
    #           the average item price at each store in ascending price order (reverse the list).
    # Part 1B: If the list is out of order, print an error message.
    # stores = [Store(name='Albertsons', inventory={'Chips': [5.00, 10], 'Pizza': [12.00, 3]}),   
    #        Store(name='99-Cent Store', inventory={'Salsa': [1.00, 1]})]
    previous = 0
    for store in stores[::-1]:
        total = 0
        price = 0
        quantity = 0
        count = 0
        for item in store.inventory:
            price = store.inventory[item][0]
            quantity = store.inventory[item][1]
            total +=  price * quantity
            count += quantity
        average = total / count
        print(f'The average item at {store.name} costs ${average:.2f}')
        if previous > average:
            print('Error: Outdated information, quitting program...')
            break
        else:
            previous = average
    
    print()  # Visual break in output; not necessary to keep.

    # Part 2: print sorted customer order
    #       Jared wants 2 Chips, 100 Crisps.
    #       Shannon does not want anything.
    # customers = [Customer(name='Jared', order={'Chips': 2, 'Crisps': 100}),
    #          Customer(name='Shannon', order={}),
    #          Customer(name='Caio', order={'Fries': 1, 'Chips': 10})]
    # Jared wants 2 Chips, 100 Crisps.
    # Shannon does not want anything.
    # Caio wants 10 Chips, 1 Fries.
    # stores = [Store(name='Vons', inventory={'Cereal': [10.00, 10]}),
    #       Store(name='Trader Joes', inventory={'Chips': [9, 1]}),
    #       Store(name='Albertsons', inventory={'Chips': [5.00, 10], 'Pizza': [12.00, 3], 'Fries': [5.00, 1]}),
    #       Store(name='99-Cent Store', inventory={'Salsa': [1.00, 1]})]
    stores = stores[::-1]
    customer_totals = {}
    for customer in customers:
        sorted_key_orders = sorted(customer.order.keys())
        if len(sorted_key_orders) == 0:
            print(f'{customer.name} does not want anything.')
            continue
        for num in range(len(sorted_key_orders)):
            if num == 0 and len(sorted_key_orders) == 1:
                print(f'{customer.name} wants {customer.order[sorted_key_orders[num]]} {sorted_key_orders[num]}.')
            elif num == 0:
                print(f'{customer.name} wants {customer.order[sorted_key_orders[num]]} {sorted_key_orders[num]}, ', end = "")
            elif num == len(sorted_key_orders) - 1:
                print(f'{customer.order[sorted_key_orders[num]]} {sorted_key_orders[num]}.')
            else:
                print(f'{customer.order[sorted_key_orders[num]]} {sorted_key_orders[num]}, ', end = '')
        customer_totals[customer.name] = {}
        for i in range(len(sorted_key_orders)):
            item = sorted_key_orders[i]
            quantity = customer.order[sorted_key_orders[i]] #사야함
            total_purchased = 0
            for store in stores:
                total_purchased = 0
                if store.name not in customer_totals[customer.name].keys():
                    customer_totals[customer.name][store.name] = 0
                else:
                    pass
                if item in store.inventory and store.inventory[item][1] != 0:
                    if quantity != 0 and quantity <= store.inventory[item][1]:
                        total_purchased = quantity
                        store.inventory[item][1] = store.inventory[item][1] - total_purchased
                        quantity -= total_purchased
                        print(f'\tPurchased {total_purchased} {item} at {store.name} for ${store.inventory[item][0] * total_purchased:.2f}')
                        customer_totals[customer.name][store.name] = customer_totals[customer.name][store.name] + store.inventory[item][0] * total_purchased
                    elif quantity != 0 and quantity > store.inventory[item][1]:
                        total_purchased +=  store.inventory[item][1]
                        store.inventory[item][1] = 0
                        quantity -= total_purchased
                        print(f'\tPurchased {total_purchased} {item} at {store.name} for ${store.inventory[item][0] * total_purchased:.2f}')
                        customer_totals[customer.name][store.name] = store.inventory[item][0] * total_purchased
                    else:
                        continue
            if total_purchased != quantity and quantity != 0:
                print(f'\tAll stores were sold out of {item}; {customer.name} could not purchase {quantity} {item}')
    stores = sorted(stores,reverse=True)



    # Part 3 & 4 might involve code from part 2...

    # ----End here----

    return customer_totals, stores


if __name__ == '__main__':
    # Set submit_mode to False to be able to run this code in python tutor or development mode
    # Ensure it is set to True when submitting code
    submit_mode = True
    if submit_mode:
        drone_delivery_service(*eval(input()))
    else:
        print("THIS IS A TEST RUN - IF YOU ARE SEEING "
              "THIS IN SUBMIT MODE, SET submit_mode = True AND RERUN")
        drone_delivery_service(
            [Customer(name='Jared', order={'Chips': 2, 'Crisps': 100}),
             Customer(name='Shannon', order={}),
             Customer(name='Caio', order={'Fries': 1, 'Chips': 10})],
            [Store(name='Vons', inventory={'Cereal': [10.00, 10]}),
             Store(name='Trader Joes', inventory={'Chips': [9, 1]}),
             Store(name='Albertsons', inventory={'Chips': [5.00, 10], 'Pizza': [12.00, 3], 'Fries': [5.00, 1]}),
             Store(name='99-Cent Store', inventory={'Salsa': [1.00, 1]})])
