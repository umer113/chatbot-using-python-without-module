questions = {
    "I'm good, thanks for asking!": "How are you",
    "Yeah, what you want to know about ubit?": "I want to know about UBIT",
    "I suppose, everytime the admission opens at December.": "When will the admission open for UBIT",
    "there are only two fields in bachelors, computer science and software.": "How many fields are there in UBIT",
    "There are few scholarship offers in ubit": "Tell me about the scholarship programs at UBIT",
    "Each year in December, admissions reopen.": "Can you provide information on the admission requirements",
    "Admission criteria is the percentage of intermediate": "What is the criteria for the admission?",
    "What is the faculty-to-student ratio at UBIT?": "Can you provide information on the faculty-to-student ratio",
    "I heard UBIT has a strong focus on research. Is that true": "Tell me more about the research opportunities at UBIT.",
    "An admission form opens at Karachi University portal every year when admissions are announced": "How can I apply for admission to UBIT?",
    "What are the key features of the computer science program at UBIT?": "Tell me about the features of the computer science program",
    "Do you offer online courses or distance learning programs at UBIT?": "What are the options for online courses or distance learning",
    "Usually, the internship offers in jobfest.": "Tell me about the internship programs available",
    "Average class size is 85-90": "Can you provide information on the average class size",
    "Is there a campus tour available for prospective students?": "How can I schedule a campus tour at UBIT",
    "Are there any notable alumni from UBIT?": "Tell me about some notable alumni from UBIT",
    "What types of facilities and resources are available for students at UBIT?": "Describe the facilities and resources for students",
    "Morning admission ends around 15th December": "When are the admission deadlines for UBIT",
    "Is there a student council or student government at UBIT?": "Tell me about the student council or government",
    "How diverse is the student population at UBIT?": "Describe the diversity of the student population",
    "What support services are available for international students at UBIT?": "Tell me about support services for international students",
    "Are there any partnerships or collaborations with industry at UBIT?": "Describe the industry partnerships and collaborations",
    "Alumni network of UBIT is very strong": "What opportunities are there for alumni networking",
    "Are there any exchange programs for students at UBIT?": "Tell me about exchange programs and study abroad opportunities",
    "What majors or specializations are offered in the software field at UBIT?": "Provide information on majors in the software field",
    "How does UBIT support student success and career development?": "Describe the support for student success and career development",
    "What is the accreditation status of UBIT?": "Is UBIT accredited, and by which accrediting bodies",
    "Are there any research centers or labs at UBIT?": "Tell me about the research centers and labs",
    "What is the acceptance rate at UBIT?": "Can you provide information on the acceptance rate",
    "How is the campus life at UBIT?": "Describe the overall campus life and atmosphere",
    "What are the graduation requirements for UBIT?": "Can you provide information on graduation requirements",
    "Are there any special programs or initiatives for women in technology at UBIT?": "Tell me about programs for women in technology",
    "What is the average starting salary for UBIT graduates?": "Can you provide information on the average starting salary",
    "Is there a mentorship program for students at UBIT?": "Tell me about the mentorship opportunities",
    "How does UBIT stay updated with the latest trends in technology and education?": "Describe the approach to staying updated with trends",
    "Tell me about the admission interview process at UBIT.": "What is involved in the admission interview",
    "What types of student organizations or clubs are available at UBIT?": "Describe the student organizations and clubs",
    "Can you provide information on the financial aid options for students at UBIT?": "Tell me about financial aid options",
}


def keyword_suggestion(questions, user_input):
    most_close_matches = []
    highest_match = 0
    user_words = user_input.split()

    for key, value in questions.items():
        question_words = value.lower().split()
        common_words = set(user_words) & set(question_words)
        match_keyword = len(common_words)

        if match_keyword > highest_match:
            highest_match = match_keyword
            most_close_matches = [value]

        elif match_keyword == highest_match:
            most_close_matches.append(value)

    if len(most_close_matches) == 1:
        return most_close_matches[0]

    if highest_match > 0:
        return most_close_matches
    else:
        return None

print("Hello! I'm your chatbot. Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ").lower()

    if user_input in ["exit", "ex", "exit", "exiT"]:
        break

    matched_question = None
    for key, value in questions.items():
        if value.lower() == user_input:
            matched_question = key
            break

    if matched_question:
        print("Bot:", matched_question)
    else:
        suggestions = keyword_suggestion(questions, user_input)

        if suggestions:
            if type(suggestions) == list and len(suggestions) > 1:
                for suggestion in suggestions:
                    user_choice = input(f"Bot: Did you mean '{suggestion}'? (Yes/No): ").lower()
                    if user_choice == 'yes':
                        for key, value in questions.items():
                            if value == suggestion:
                                print("Bot:", key)
                                break
                        break
                else:
                    print("Bot: I'm not sure how to respond to that.")
            else:
                for key, value in questions.items():
                    if value == suggestions:
                        print("Bot:", key)
                        break
        else:
            print("Bot: I'm not sure how to respond to that.")
