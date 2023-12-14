def get_ticket_sales():
    ticket_sales = {}
    total_revenue = 0.0
    
    while True:
        ticket_class = input("Введіть клас місць (A, B або C) або 'end' для завершення: ").upper()

        if ticket_class == 'END':
            break

        price_per_ticket = float(input(f"Введіть ціну за квиток для класу {ticket_class}: "))
        tickets_sold = int(input(f"Введіть кількість проданих квитків для класу {ticket_class}: "))

        revenue = price_per_ticket * tickets_sold
        ticket_sales[ticket_class] = revenue
        total_revenue += revenue

    return ticket_sales, total_revenue

def display_revenue(ticket_sales, total_revenue):
    print("Дохід за кожним класом місць:")
    for ticket_class, revenue in ticket_sales.items():
        print(f"{ticket_class}: {revenue}")

    print(f"\nЗагальний дохід: {total_revenue}")
ticket_sales, total_revenue = get_ticket_sales()
display_revenue(ticket_sales, total_revenue)
