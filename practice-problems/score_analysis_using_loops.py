scores = [45, 78, 92, 55, 38, 88, 70, 61, 49, 95]

passed = 0
failed = 0

for score in scores:
    if score >= 60:
        passed += 1
    else:
        failed += 1

total = len(scores)
pass_rate = (passed / total) * 100 if total > 0 else 0

print(f"Scores       : {scores}")
print(f"Total        : {total}")
print(f"Passed       : {passed}")
print(f"Failed       : {failed}")
print(f"Pass Rate    : {pass_rate:.2f}%")