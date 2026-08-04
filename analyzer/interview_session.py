questions = []

current_question = 0


def set_questions(new_questions):
    global questions, current_question

    questions = new_questions
    current_question = 0


def get_current_question():
    global questions, current_question

    if current_question >= len(questions):
        return "✅ Interview completed."

    return questions[current_question]


def next_question():
    global questions, current_question

    current_question += 1

    if current_question >= len(questions):
        return "✅ Interview completed."

    return questions[current_question]