
import random
def main():
    print("Welcome to the vocabulary quiz program.\n")
    file_name = input("Please enter a file name:")
    get_dict(file_name)
    name = input("Please enter your full name:")
    date = input("Please enter the date:")
    try:
        number_of_words = int(input("How many words would you like to be quizzed on?  "))
    except ValueError:
        print("Please Enter a valid integer")
    number_of_words = int(input("How many words would you like to be quizzed on?  "))





    quiz_dic = get_dict(file_name)


    incorrect, score = quiz_func(number_of_words,quiz_dic)
    output_file = input("Enter name for output file: ")

    make_quiz_file(name, date, incorrect, quiz_dic, output_file,score,number_of_words)
    print("Name:",name)
    print("Date:",date)
    for i in incorrect:
        translation = quiz_dic[i]
        print(i, end=" ")
        print(":", end=" ")
        print(*translation, sep=", ")
    print("score ", score,"out of",number_of_words)





def get_dict(file_name):

    quiz_dic = {}
    name_of_file= "words.txt"
    if file_name == name_of_file:
        infile = open("words.txt", "a")
        print("there were 10 entries found")

    else:
        print("The file name",file_name,"does not exist" "\n bye!")
        exit()


    infile = open(name_of_file, "r")
    line = infile.readline()
    while line:
        line = line.strip()
        word, translations = line.split(":")
        if "," in translations:
            t1, t2 = translations.split(",")

            quiz_dic[word] = [t1, t2]
        else:
            quiz_dic[word] = [translations]

        line = infile.readline()
    return quiz_dic



def quiz_func(number_of_words,quiz_dic):
    keys = []
    incorrect = []
    score = 0
    for key in quiz_dic:
        keys.append(key)
    get_length = len(quiz_dic)



    while (number_of_words>get_length) or (number_of_words == 0):
        print("Please choose a number between 1 and ",get_length)
        number_of_words = int(input("How many words would you like to be quizzed on?"))
    for i in range(0,number_of_words):
        index = random.randint(0,get_length-1)
        key=keys[index]
        print("English Word:", key)
        words1 = quiz_dic[key]

        len_words = len(words1)

        print("Enter", len_words,"equivalent English word(s).")
        user_answer = []
        count = 1

        while count<=len_words:
            print("word[",count,"]")
            answer = input(" ")
            user_answer.append(answer)
            count +=1

        result = check_user_answer(user_answer,words1)
        if result == True:
            print("Correct")
            score += 1
        else:
            print("incorrect")
            incorrect.append(key)
            score -= 1
    if score <= 0:
        score = 0
    return incorrect, score



def check_user_answer(user_answer, words1):

    if user_answer == words1:
        return True
    return False








def make_quiz_file(name,date,incorrect,quiz_dic, output_file,score,number_of_words):
    if len(output_file)>0:

        output_file = open(output_file,"w")

        for i in incorrect:
            if len(quiz_dic[i]) == 1:
                output_file.write(str(i) + ":" + str(quiz_dic[i][0]))
            else:
                output_file.write(str(i) + ":" + str(quiz_dic[i][0]) + ", " + str(quiz_dic[i][1]))
    else:
        print("Bye!")
        exit()















main()