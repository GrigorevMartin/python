import random # импорт библеотеки
def get_question (): #задаём функцию по созданию вопроса
    with open('questions.txt', 'r', encoding='utf-8') as f:     #открываем файл с вопросами на чтение
        question_list = f.read().splitlines()   #задаём переменную и разбиваем по строчкам
    number_question = random.randrange(0, len(question_list))   # выбираем случайную строку массива
    question_answer = str(question_list[number_question])   #создаём вопрос уже в виде полноценной строки
    for i in range(0, len(question_answer)):    #создаём цикл от 0 до длинны ответа
        if question_answer[i] == ';':   #создаём условие если текущий символ равен знаку разделителя
            question=question_answer[0:i]   #создаём новую переменную которая содержит вопрос
            answer = question_answer[i + 1:len(question_answer)]    #задаём новою переменную которая содержит ответ
    return answer, question    #возвращает вопрос и ответ

#закрываем ответ от учасника звёздочами
answer, question = get_question()   #две переменные передаём в функцию
print(question)  #выводим вопрос
current_view = []   #задаём пустой массив
for i in range (0,len(answer)):  #пускаем цикл от нуля до длинны ответа
    current_view.append('*')    #заполняем массив звёздочками
print(''.join(current_view))    #склеиваем копию списка в строку

while True:    #создаём цикл с условием
    user = input('Введите букву или назовите слово:')   #создаём переменную куда мы будем писать слово или выбранную букву
    if user == answer:  #запускаем первую проверку  на полный ответ
        print('вы правильно назвали слово!');break  #выводем если игрок сразу ответил полностью
    if (user in answer ):   #если переменная ввода пользовотеля находится в масиве
        print('есть такая буква!')  #выводим подтверждение
        for i in range(0,len(answer)):  #создаём цикл который будет работать от 0 до длинны ответа
            if answer[i] == user: #если текущее значение массиву равно вводу пользователя
                current_view[i] = user # присвоение ответа игрока к текущему состоянию массива
                user_answer=''.join(current_view)   #склеиваем текщий массив в одну строчку
    else:#если первые два условия не выполнились
        print('такой буквы нет')#то пишем что такой буквы нету
    if user_answer == answer:#проверка на победу
        print('вы правильно назвали все буквы!');break  #победное оповещение
    print(user_answer)  #выводим ответ игрока