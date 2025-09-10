def positive_feedback_percentage(ratings):
    if not ratings:
        return 0.0
    positive = sum(1 for r in ratings if r >= 4)
    return (positive / len(ratings)) * 100
ratings = list(map(int, input("Enter ratings (1-5) space separated: ").split()))
percentage = positive_feedback_percentage(ratings)
print(f"Positive Feedback: {percentage:.1f}%")
