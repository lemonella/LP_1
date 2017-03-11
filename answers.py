def get_answer(question):
	#question = question.lower()
	answers = {'Привет!':"И тебе привет!", "Как твои дела?": "Хорошо", "Пойдем в кино сегодня?": "Неа"}
	return answers.get(question, '<нет такого вопроса>')

print(get_answer("Привет!"))