"""
Ask the user for a subject score. If it's above 90, congratulate him. If it's
between 50 and 90, suggest improvement. Otherwise, advise on retaking the
course.
"""
score_data = float(input("Enter your subject score: "))


if score_data > 90:
    print("Congratulations, Excellent performance.")
elif 50 <= score_data <= 90:
    print("Good effort, Keep working hard and you can improve further.")
else:
    print("You need to retake the course.Never give up.")