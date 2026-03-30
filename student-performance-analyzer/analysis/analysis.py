 # Performance anlysis logic   
 # Performance analyser based on the number of problems solved with accuracy and time taken by the student.
 # Also focus on the strength , weaknessses and give recommendations for the students. 

def analyze(data):
    problems = data.get("problems_solved", 0)
    correct = data.get("correct_submissions", 0)
    time = data.get("time_taken", 0)

    accuracy = correct / problems if problems > 0 else 0

    score = (accuracy * 60) + (problems * 2)

    # ranking of students based on their score

    if score > 80:
        level = "Advanced"
    elif score > 50:
        level = "Intermediate"
    else:
        level = "Beginner"

    strengths = []
    weaknesses = []
    recommendations = []


        # showing the strength of the student 

    if accuracy >= 0.75:
        strengths.append("High accuracy in problem solving")
    if problems >= 10:
        strengths.append("Consistent practice")

        # showing the weaknesses of the student 

    if accuracy < 0.6:
        weaknesses.append("Low accuracy")
    if problems < 5:
        weaknesses.append("Insufficient practice")

        # recommendation for the students based on their accuracy and time taken

    if accuracy < 0.75:
        recommendations.append("Focus on understanding concepts before solving")
    if problems < 10:
        recommendations.append("Increase daily problem-solving count")
    if time > 180:
        recommendations.append("Work on time optimization")

    return {
        "summary": {
            "score": round(score, 2),
            "accuracy": round(accuracy, 2),
            "level": level,
            "performance_tag": "🔥 Excellent" if score > 80 else "👍 Good" if score > 50 else "⚠️ Needs Improvement"
        },       # performance tag based on their score, accuracy and level 
        "strengths": strengths,
        "weaknesses": weaknesses,
        "recommendations": recommendations
    }


if __name__ == "__main__":
    sample_data = {
        "problems_solved": 20,       # write the no. of problems solved by the student
        "correct_submissions": 10,   # write the no. of problems correctly solved by the student
        "time_taken": 250          # write the time taken (in seconds) to solve the problems 
    }

    result = analyze(sample_data)

    import json
    print(json.dumps(result, indent=4))