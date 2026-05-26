def calculate_revenue(ticket_price, tickets_sold):
    return ticket_price * tickets_sold


avengers_revenue = calculate_revenue(250, 200)

leo_revenue = calculate_revenue(200, 190)

kgf_revenue = calculate_revenue(300, 500)

total_revenue = (
    avengers_revenue
    + leo_revenue
    + kgf_revenue
)

print(f"Revenue of Avengers: {avengers_revenue}")

print(f"Revenue of Leo: {leo_revenue}")

print(f"Revenue of KGF: {kgf_revenue}")

print(f"Total Revenue: {total_revenue}")