def get_grade(score):
    """
    Determines the letter grade based on the given score (0-100).

    Args:
        score: The numerical score.

    Returns:
        The letter grade corresponding to the score.
    """

    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Get user input for the score
score = float(input("Enter the score (0-100): "))

# Calculate and print the grade
grade = get_grade(score)
print("Grade:", grade)