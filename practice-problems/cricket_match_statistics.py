scores = [45, 78, 12, 99, 34, 67]

highest_score = scores[0]
low_scores = []

print("\n========== Match Score Analysis ==========")

for score in scores:
    print(f"Player scored: {score}")

    if score > highest_score:
        highest_score = score

    if score < 50:
        low_scores.append(score)

print(f"\nHighest Score: {highest_score}")
print(f"Low scores: {low_scores}")
print(f"Total players: {len(scores)}")