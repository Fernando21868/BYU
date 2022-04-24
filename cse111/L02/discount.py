from datetime import datetime

current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()

while True:
    price = float(input('Enter the price: '))
    if(price == 0):
        break
    quantity = int(input('Enter the quantity: '))

    subtotal = price*quantity

    day_of_week = 2

    if day_of_week == 1 or day_of_week == 2:
        if (50-subtotal) > 0:
            print(
                f'You should purchase at least 50 to receive the discount, here is what you need: {(50-subtotal):.2f}')
        else:
            discount_amount = (subtotal*0.10)
            subtotal = subtotal-discount_amount
            print(f'Discount amount: {discount_amount:.2f}')

    tax_amount = subtotal*0.06
    total = subtotal+tax_amount

    print(f'Sales tax amount: {tax_amount:.2f}')
    print(f'Total: {total:.2f}\n')
