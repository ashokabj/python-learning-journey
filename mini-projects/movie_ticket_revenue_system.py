# Movie Ticket Revenue System

tickets = {
    "Avengers": 120,
    "Leo": 85,
    "Kantara": 150,
    "KGF": 95
}

ticket_prices = {}

print("\n---------- Movie Ticket Prices ----------")

for movie in tickets:
    price = int(input(f"Enter the ticket price for {movie} --> "))
    ticket_prices[movie] = price

revenue = 0
total_revenue = 0
highest_revenue = 0
movie_name = ""

print("\n---------- Revenue of Each Movie ----------")

for movie, ticket_sold in tickets.items():

    revenue = ticket_prices[movie] * ticket_sold

    total_revenue += revenue

    if revenue > highest_revenue:
        highest_revenue = revenue
        movie_name = movie

    print(f"{movie} --> Rs {revenue}")

print(f"\nHighest revenue movie: {movie_name} (Rs {highest_revenue})")
print(f"Total revenue of all movies: Rs {total_revenue}")