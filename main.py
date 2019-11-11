'''
Bhargav Annem
Prueba por Verbos Pretéritos y Imperfectos
Professora Granados
12 October 2019
'''
import numpy as np
import random
import sys
from random import shuffle
import webbrowser

global score
score = 0
url = 'https://www.spanishdict.com/conjugate/'


# -------------------Definitions of Imperfect Verbs-----------------------
def andar():
    global score
    for x in range(1):
        andar_question = random.randint(0, 9)
        if andar_question == 0:
            ans1 = input("(Yo) \n")
            if ans1.upper() == andar_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            elif ans1.upper() != andar_conj_words["(Yo)"]:
                print("That is incorrect. The correct answer is ", andar_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('andar'))
                webbrowser.open_new

        elif andar_question == 1:
            ans1 = input("(Tú) \n")
            if ans1.upper() == andar_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", andar_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('andar'))

        elif andar_question == 2:
            ans1 = input("(Él) \n")
            if ans1.upper() == andar_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", andar_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('andar'))

        elif andar_question == 3:
            ans1 = input("(Ella) \n")
            if ans1.upper() == andar_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", andar_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('andar'))

        elif andar_question == 4:
            ans1 = input("(Usted) \n")
            if ans1.upper() == andar_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", andar_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('andar'))

        elif andar_question == 5:
            ans1 = input("(Nosotros) \n")
            if ans1.upper() == andar_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", andar_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('andar'))

        elif andar_question == 6:
            ans1 = input("(Vosotros) \n")
            if ans1.upper() == andar_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", andar_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('andar'))

        elif andar_question == 7:
            ans1 = input("(Ustedes) \n")
            if ans1.upper() == andar_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", andar_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('andar'))

        elif andar_question == 8:
            ans1 = input("(Ellos) \n")
            if ans1.upper() == andar_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", andar_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('andar'))

        else:
            ans1 = input("(Ellas) \n")
            if ans1.upper() == andar_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", andar_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('andar'))

    print("Current Score: ", score)


def caber():
    global score
    for x in range(1):
        caber_question = random.randint(0, 9)
        if caber_question == 0:
            ans2 = input("(Yo) \n")
            if ans2.upper() == caber_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", caber_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('caber'))

        elif caber_question == 1:
            ans2 = input("(Tú) \n")
            if ans2.upper() == caber_conj_words["(Tú)"]:
                print("That is correct\n")
                score += 1
            else:
                print("That is incorrect. The correct answer is ", caber_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('caber'))

        elif caber_question == 2:
            ans2 = input("(Él) \n")
            if ans2.upper() == caber_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", caber_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('caber'))

        elif caber_question == 3:
            ans2 = input("(Ella) \n")
            if ans2.upper() == caber_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", caber_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('caber'))
        elif caber_question == 4:
            ans2 = input("(Usted) \n")
            if ans2.upper() == caber_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", caber_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('caber'))
        elif caber_question == 5:
            ans2 = input("(Nosotros) \n")
            if ans2.upper() == caber_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", caber_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('caber'))
        elif caber_question == 6:
            ans2 = input("(Vosotros) \n")
            if ans2.upper() == caber_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", caber_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('caber'))
        elif caber_question == 7:
            ans2 = input("(Ustedes) \n")
            if ans2.upper() == caber_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score += 1
            else:
                print("That is incorrect. The correct answer is ", caber_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('caber'))
        elif caber_question == 8:
            ans2 = input("(Ellos) \n")
            if ans2.upper() == caber_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", caber_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('caber'))
        else:
            ans2 = input("(Ellas) \n")
            if ans2.upper() == caber_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", caber_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('caber'))
    print("Current Score: ", score)


def conducir():
    global score
    for x in range(1):
        conducir_question = random.randint(0, 9)
        if conducir_question == 0:
            ans3 = input("(Yo) \n")
            if ans3.upper() == conducir_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", conducir_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('conducir'))
        elif conducir_question == 1:
            ans3 = input("(Tú) \n")
            if ans3.upper() == conducir_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", conducir_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('conducir'))
        elif conducir_question == 2:
            ans3 = input("(Él) \n")
            if ans3.upper() == conducir_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", conducir_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('conducir'))
        elif conducir_question == 3:
            ans3 = input("(Ella) \n")
            if ans3.upper() == conducir_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", conducir_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('conducir'))
        elif conducir_question == 4:
            ans3 = input("(Usted) \n")
            if ans3.upper() == conducir_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", conducir_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('conducir'))
        elif conducir_question == 5:
            ans3 = input("(Nosotros) \n")
            if ans3.upper() == conducir_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", conducir_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('conducir'))
        elif conducir_question == 6:
            ans3 = input("(Vosotros) \n")
            if ans3.upper() == conducir_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", conducir_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('conducir'))
        elif conducir_question == 7:
            ans3 = input("(Ustedes) \n")
            if ans3.upper() == conducir_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", conducir_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('conducir'))
        elif conducir_question == 8:
            ans3 = input("(Ellos) \n")
            if ans3.upper() == conducir_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", conducir_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('conducir'))
        else:
            ans3 = input("(Ellas) \n")
            if ans3.upper() == conducir_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", conducir_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('conducir'))
    print("Current Score: ", score)


def dar():
    global score
    for x in range(1):
        dar_question = random.randint(0, 9)
        if dar_question == 0:
            ans4 = input("(Yo) \n")
            if ans4.upper() == dar_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", dar_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('dar'))
        elif dar_question == 1:
            ans4 = input("(Tú) \n")
            if ans4.upper() == dar_conj_words["(Tú)"]:
                print("That is correct\n")
                score += 1
            else:
                print("That is incorrect. The correct answer is ", dar_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('dar'))
        elif dar_question == 2:
            ans4 = input("(Él) \n")
            if ans4.upper() == dar_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", dar_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('dar'))
        elif dar_question == 3:
            ans4 = input("(Ella) \n")
            if ans4.upper() == dar_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", dar_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('dar'))
        elif dar_question == 4:
            ans4 = input("(Usted) \n")
            if ans4.upper() == dar_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", dar_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('dar'))
        elif dar_question == 5:
            ans4 = input("(Nosotros) \n")
            if ans4.upper() == dar_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", dar_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('dar'))
        elif dar_question == 6:
            ans4 = input("(Vosotros) \n")
            if ans4.upper() == dar_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", dar_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('dar'))
        elif dar_question == 7:
            ans4 = input("(Ustedes) \n")
            if ans4.upper() == dar_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", dar_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('dar'))
        elif dar_question == 8:
            ans4 = input("(Ellos) \n")
            if ans4.upper() == dar_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", dar_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('dar'))
        else:
            ans4 = input("(Ellas) \n")
            if ans4.upper() == dar_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", dar_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('dar'))
    print("Current Score: ", score)


def decir():
    global score
    for x in range(1):
        decir_question = random.randint(0, 9)
        if decir_question == 0:
            ans5 = input("(Yo) \n")
            if ans5.upper() == decir_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", decir_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('decir'))
        elif decir_question == 1:
            ans5 = input("(Tú) \n")
            if ans5.upper() == decir_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", decir_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('decir'))
        elif decir_question == 2:
            ans5 = input("(Él) \n")
            if ans5.upper() == decir_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", decir_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('decir'))
        elif decir_question == 3:
            ans5 = input("(Ella) \n")
            if ans5.upper() == decir_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", decir_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('decir'))
        elif decir_question == 4:
            ans5 = input("(Usted) \n")
            if ans5.upper() == decir_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", decir_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('decir'))
        elif decir_question == 5:
            ans5 = input("(Nosotros) \n")
            if ans5.upper() == decir_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", decir_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('andar'))
        elif decir_question == 6:
            ans5 = input("(Vosotros) \n")
            if ans5.upper() == decir_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", decir_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('decir'))
        elif decir_question == 7:
            ans5 = input("(Ustedes) \n")
            if ans5.upper() == decir_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", decir_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('decir'))
        elif decir_question == 8:
            ans5 = input("(Ellos) \n")
            if ans5.upper() == decir_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", decir_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('decir'))
        else:
            ans5 = input("(Ellas) \n")
            if ans5.upper() == decir_conj_words["(Ellas)"]:
                print("That is correct")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", decir_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('decir'))
    print("Current Score: ", score)


def estar():
    global score
    for x in range(1):
        estar_question = random.randint(0, 9)
        if estar_question == 0:
            ans6 = input("(Yo) ")
            if ans6.upper() == estar_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", estar_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('estar'))
        elif estar_question == 1:
            ans6 = input("(Tú) \n")
            if ans6.upper() == estar_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", estar_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('estar'))
        elif estar_question == 2:
            ans6 = input("(Él) \n")
            if ans6.upper() == estar_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", estar_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('estar'))
        elif estar_question == 3:
            ans6 = input("(Ella) \n")
            if ans6.upper() == estar_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", estar_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('estar'))
        elif estar_question == 4:
            ans6 = input("(Usted) \n")
            if ans6.upper() == estar_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", estar_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('estar'))
        elif estar_question == 5:
            ans6 = input("(Nosotros) \n")
            if ans6.upper() == estar_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", estar_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('estar'))
        elif estar_question == 6:
            ans6 = input("(Vosotros) \n")
            if ans6.upper() == estar_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", estar_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('estar'))
        elif estar_question == 7:
            ans6 = input("(Ustedes) \n")
            if ans6.upper() == estar_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", estar_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('estar'))
        elif estar_question == 8:
            ans6 = input("(Ellos) \n")
            if ans6.upper() == estar_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", estar_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('estar'))
        else:
            ans6 = input("(Ellas) \n")
            if ans6.upper() == estar_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", estar_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('estar'))
    print("Current Score: ", score)


def hacer():
    global score
    for x in range(1):
        hacer_question = random.randint(0, 9)
        if hacer_question == 0:
            ans7 = input("(Yo) \n")
            if ans7.upper() == hacer_conj_words["(Yo)"]:
                print("That is correct\n")
                score += 1
            else:
                print("That is incorrect. The correct answer is ", hacer_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('hacer'))
        elif hacer_question == 1:
            ans7 = input("(Tú) \n")
            if ans7.upper() == hacer_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", hacer_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('hacer'))
        elif hacer_question == 2:
            ans7 = input("(Él) \n")
            if ans7.upper() == hacer_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", hacer_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('hacer'))
        elif hacer_question == 3:
            ans7 = input("(Ella) \n")
            if ans7.upper() == hacer_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", hacer_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('hacer'))
        elif hacer_question == 4:
            ans7 = input("(Usted) \n")
            if ans7.upper() == hacer_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", hacer_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('hacer'))
        elif hacer_question == 5:
            ans7 = input("(Nosotros) \n")
            if ans7.upper() == hacer_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", hacer_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('hacer'))
        elif hacer_question == 6:
            ans7 = input("(Vosotros) \n")
            if ans7.upper() == hacer_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", hacer_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('hacer'))
        elif hacer_question == 7:
            ans7 = input("(Ustedes) \n")
            if ans7.upper() == hacer_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", hacer_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('hacer'))
        elif hacer_question == 8:
            ans7 = input("(Ellos) \n")
            if ans7.upper() == hacer_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", hacer_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('hacer'))
        else:
            ans7 = input("(Ellas) \n")
            if ans7.upper() == hacer_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", hacer_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('hacer'))
    print("Current Score: ", score)


def ir():
    global score
    for x in range(1):
        ir_question = random.randint(0, 9)
        if ir_question == 0:
            ans8 = input("(Yo) \n")
            if ans8.upper() == ir_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", ir_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('ir'))
        elif ir_question == 1:
            ans8 = input("(Tú) \n")
            if ans8.upper() == ir_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", ir_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('ir'))
        elif ir_question == 2:
            ans8 = input("(Él) \n")
            if ans8.upper() == ir_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", ir_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('ir'))
        elif ir_question == 3:
            ans8 = input("(Ella) \n")
            if ans8.upper() == ir_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", ir_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('ir'))
        elif ir_question == 4:
            ans8 = input("(Usted) \n")
            if ans8.upper() == ir_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", ir_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('ir'))
        elif ir_question == 5:
            ans8 = input("(Nosotros) \n")
            if ans8.upper() == ir_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", ir_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('ir'))
        elif ir_question == 6:
            ans8 = input("(Vosotros) \n")
            if ans8.upper() == ir_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", ir_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('ir'))
        elif ir_question == 7:
            ans8 = input("(Ustedes) \n")
            if ans8.upper() == ir_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", ir_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('ir'))
        elif ir_question == 8:
            ans8 = input("(Ellos) \n")
            if ans8.upper() == ir_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", ir_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('ir'))
        else:
            ans8 = input("(Ellas) \n")
            if ans8.upper() == ir_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", ir_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('ir'))
    print("Current Score: ", score)


def poder():
    global score
    for x in range(1):
        poder_question = random.randint(0, 9)
        if poder_question == 0:
            ans9 = input("(Yo) \n")
            if ans9.upper() == poder_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", poder_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('poder'))
        elif poder_question == 1:
            ans9 = input("(Tú) \n")
            if ans9.upper() == poder_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", poder_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('poder'))
        elif poder_question == 2:
            ans9 = input("(Él) \n")
            if ans9.upper() == poder_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", poder_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('poder'))
        elif poder_question == 3:
            ans9 = input("(Ella) \n")
            if ans9.upper() == poder_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", poder_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('poder'))
        elif poder_question == 4:
            ans9 = input("(Usted) \n")
            if ans9.upper() == poder_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", poder_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('poder'))
        elif poder_question == 5:
            ans9 = input("(Nosotros) \n")
            if ans9.upper() == poder_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", poder_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('poder'))
        elif poder_question == 6:
            ans9 = input("(Vosotros) \n")
            if ans9.upper() == poder_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", poder_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('poder'))
        elif poder_question == 7:
            ans9 = input("(Ustedes) \n")
            if ans9.upper() == poder_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", poder_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('poder'))
        elif poder_question == 8:
            ans9 = input("(Ellos) \n")
            if ans9.upper() == poder_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", poder_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('poder'))
        else:
            ans9 = input("(Ellas) \n")
            if ans9.upper() == poder_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", poder_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('poder'))
    print("Current Score: ", score)


def poner():
    global score
    for x in range(1):
        poner_question = random.randint(0, 9)
        if poner_question == 0:
            ans10 = input("(Yo) \n")
            if ans10.upper() == poner_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", poner_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('poner'))
        elif poner_question == 1:
            ans10 = input("(Tú) \n")
            if ans10.upper() == poner_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", poner_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('poner'))
        elif poner_question == 2:
            ans10 = input("(Él) \n")
            if ans10.upper() == poner_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", poner_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('poner'))
        elif poner_question == 3:
            ans10 = input("(Ella) \n")
            if ans10.upper() == poner_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", poner_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('poner'))
        elif poner_question == 4:
            ans10 = input("(Usted) \n")
            if ans10.upper() == poner_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", poner_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('poner'))
        elif poner_question == 5:
            ans10 = input("(Nosotros) \n")
            if ans10.upper() == poner_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", poner_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('poner'))
        elif poner_question == 6:
            ans10 = input("(Vosotros) \n")
            if ans10.upper() == poner_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", poner_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('poner'))
        elif poner_question == 7:
            ans10 = input("(Ustedes) \n")
            if ans10.upper() == poner_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", poner_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('poner'))
        elif poner_question == 8:
            ans10 = input("(Ellos) \n")
            if ans10.upper() == poner_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", poner_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('poner'))
        else:
            ans10 = input("(Ellas) \n")
            if ans10.upper() == poner_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", poner_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('poner'))
    print("Current Score: ", score)


def querer():
    global score
    for x in range(1):
        querer_question = random.randint(0, 9)
        if querer_question == 0:
            ans11 = input("(Yo) \n")
            if ans11.upper() == querer_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", querer_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('querer'))
        elif querer_question == 1:
            ans11 = input("(Tú) \n")
            if ans11.upper() == querer_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", querer_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('querer'))
        elif querer_question == 2:
            ans11 = input("(Él) \n")
            if ans11.upper() == querer_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", querer_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('querer'))
        elif querer_question == 3:
            ans11 = input("(Ella) \n")
            if ans11.upper() == querer_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", querer_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('querer'))
        elif querer_question == 4:
            ans11 = input("(Usted) \n")
            if ans11.upper() == querer_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", querer_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('querer'))
        elif querer_question == 5:
            ans11 = input("(Nosotros) \n")
            if ans11.upper() == querer_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", querer_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('querer'))
        elif querer_question == 6:
            ans11 = input("(Vosotros) \n")
            if ans11.upper() == querer_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", querer_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('querer'))
        elif querer_question == 7:
            ans11 = input("(Ustedes) \n")
            if ans11.upper() == querer_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", querer_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('querer'))
        elif querer_question == 8:
            ans11 = input("(Ellos) \n")
            if ans11.upper() == querer_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", querer_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('querer'))
        else:
            ans11 = input("(Ellas) \n")
            if ans11.upper() == querer_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", querer_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('querer'))
    print("Current Score: ", score)


def saber():
    global score
    for x in range(1):
        saber_question = random.randint(0, 9)
        if saber_question == 0:
            ans12 = input("(Yo) \n")
            if ans12.upper() == saber_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", saber_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('saber'))
        elif saber_question == 1:
            ans12 = input("(Tú) \n")
            if ans12.upper() == saber_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", saber_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('saber'))
        elif saber_question == 2:
            ans12 = input("(Él) \n")
            if ans12.upper() == saber_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", saber_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('saber'))
        elif saber_question == 3:
            ans12 = input("(Ella) \n")
            if ans12.upper() == saber_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", saber_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('saber'))
        elif saber_question == 4:
            ans12 = input("(Usted) \n")
            if ans12.upper() == saber_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", saber_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('saber'))
        elif saber_question == 5:
            ans12 = input("(Nosotros) \n")
            if ans12.upper() == saber_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", saber_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('saber'))
        elif saber_question == 6:
            ans12 = input("(Vosotros) \n")
            if ans12.upper() == saber_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", saber_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('saber'))
        elif saber_question == 7:
            ans12 = input("(Ustedes) \n")
            if ans12.upper() == saber_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", saber_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('saber'))
        elif saber_question == 8:
            ans12 = input("(Ellos) \n")
            if ans12.upper() == saber_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", saber_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('saber'))
        else:
            ans12 = input("(Ellas) \n")
            if ans12.upper() == saber_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", saber_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('saber'))
    print("Current Score: ", score)


def ser():
    global score
    for x in range(1):
        ser_question = random.randint(0, 9)
        if ser_question == 0:
            ans13 = input("(Yo) \n")
            if ans13.upper() == ser_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", ser_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('ser'))
        elif ser_question == 1:
            ans13 = input("(Tú) \n")
            if ans13.upper() == ser_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", ser_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('ser'))
        elif ser_question == 2:
            ans13 = input("(Él) \n")
            if ans13.upper() == ser_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", ser_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('ser'))
        elif ser_question == 3:
            ans13 = input("(Ella) \n")
            if ans13.upper() == ser_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", ser_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('ser'))
        elif ser_question == 4:
            ans13 = input("(Usted) \n")
            if ans13.upper() == ser_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", ser_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('ser'))
        elif ser_question == 5:
            ans13 = input("(Nosotros) \n")
            if ans13.upper() == ser_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", ser_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('ser'))
        elif ser_question == 6:
            ans13 = input("(Vosotros) \n")
            if ans13.upper() == ser_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", ser_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('ser'))
        elif ser_question == 7:
            ans13 = input("(Ustedes) \n")
            if ans13.upper() == ser_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", ser_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('ser'))
        elif ser_question == 8:
            ans13 = input("(Ellos) \n")
            if ans13.upper() == ser_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", ser_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('ser'))
        else:
            ans13 = input("(Ellas) \n")
            if ans13.upper() == ser_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", ser_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('ser'))
    print("Current Score: ", score)


def tener():
    global score
    for x in range(1):
        tener_question = random.randint(0, 9)
        if tener_question == 0:
            ans14 = input("(Yo) \n")
            if ans14.upper() == tener_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", tener_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('tener'))
        elif tener_question == 1:
            ans14 = input("(Tú) \n")
            if ans14.upper() == tener_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", tener_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('tener'))
        elif tener_question == 2:
            ans14 = input("(Él) \n")
            if ans14.upper() == tener_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", tener_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('tener'))
        elif tener_question == 3:
            ans14 = input("(Ella) \n")
            if ans14.upper() == tener_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", tener_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('tener'))
        elif tener_question == 4:
            ans14 = input("(Usted) \n")
            if ans14.upper() == tener_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", tener_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('tener'))
        elif tener_question == 5:
            ans14 = input("(Nosotros) \n")
            if ans14.upper() == tener_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", tener_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('tener'))
        elif tener_question == 6:
            ans14 = input("(Vosotros) \n")
            if ans14.upper() == tener_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", tener_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('tener'))
        elif tener_question == 7:
            ans14 = input("(Ustedes) \n")
            if ans14.upper() == tener_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", tener_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('tener'))
        elif tener_question == 8:
            ans14 = input("(Ellos) \n")
            if ans14.upper() == tener_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", tener_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('tener'))
        else:
            ans14 = input("(Ellas) \n")
            if ans14.upper() == tener_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", tener_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('tener'))
    print("Current Score: ", score)


def traducir():
    global score
    for x in range(1):
        traducir_question = random.randint(0, 9)
        if traducir_question == 0:
            ans15 = input("(Yo) \n")
            if ans15.upper() == traducir_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", traducir_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('traducir'))
        elif traducir_question == 1:
            ans15 = input("(Tú) \n")
            if ans15.upper() == traducir_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", traducir_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('traducir'))
        elif traducir_question == 2:
            ans15 = input("(Él) \n")
            if ans15.upper() == traducir_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", traducir_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('traducir'))
        elif traducir_question == 3:
            ans15 = input("(Ella) \n")
            if ans15.upper() == traducir_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", traducir_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('traducir'))
        elif traducir_question == 4:
            ans15 = input("(Usted) \n")
            if ans15.upper() == traducir_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", traducir_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('traducir'))
        elif traducir_question == 5:
            ans15 = input("(Nosotros) \n")
            if ans15.upper() == traducir_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", traducir_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('traducir'))
        elif traducir_question == 6:
            ans15 = input("(Vosotros) \n")
            if ans15.upper() == traducir_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", traducir_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('traducir'))
        elif traducir_question == 7:
            ans15 = input("(Ustedes) \n")
            if ans15.upper() == traducir_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", traducir_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('traducir'))
        elif traducir_question == 8:
            ans15 = input("(Ellos) \n")
            if ans15.upper() == traducir_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", traducir_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('traducir'))
        else:
            ans15 = input("(Ellas) \n")
            if ans15.upper() == traducir_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", traducir_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('traducir'))
    print("Current Score: ", score)


def traer():
    global score
    for x in range(1):
        traer_question = random.randint(0, 9)
        if traer_question == 0:
            ans16 = input("(Yo) \n")
            if ans16.upper() == traer_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", traer_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('traer'))
        elif traer_question == 1:
            ans16 = input("(Tú) \n")
            if ans16.upper() == traer_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", traer_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('traer'))
        elif traer_question == 2:
            ans16 = input("(Él) \n")
            if ans16.upper() == traer_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", traer_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('traer'))
        elif traer_question == 3:
            ans16 = input("(Ella) \n")
            if ans16.upper() == traer_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", traer_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('traer'))
        elif traer_question == 4:
            ans16 = input("(Usted) \n")
            if ans16.upper() == traer_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", traer_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('traer'))
        elif traer_question == 5:
            ans16 = input("(Nosotros) \n")
            if ans16.upper() == traer_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", traer_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('traer'))
        elif traer_question == 6:
            ans16 = input("(Vosotros) \n")
            if ans16.upper() == traer_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", traer_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('traer'))
        elif traer_question == 7:
            ans16 = input("(Ustedes) \n")
            if ans16.upper() == traer_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", traer_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('traer'))
        elif traer_question == 8:
            ans16 = input("(Ellos) \n")
            if ans16.upper() == traer_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", traer_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('traer'))
        else:
            ans16 = input("(Ellas) \n")
            if ans16.upper() == traer_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", traer_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('traer'))
    print("Current Score: ", score)


def venir():
    global score
    for x in range(1):
        venir_question = random.randint(0, 9)
        if venir_question == 0:
            ans17 = input("(Yo) \n")
            if ans17.upper() == venir_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", venir_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('venir'))
        elif venir_question == 1:
            ans17 = input("(Tú) \n")
            if ans17.upper() == venir_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", venir_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('venir'))
        elif venir_question == 2:
            ans17 = input("(Él) \n")
            if ans17.upper() == venir_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", venir_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('venir'))
        elif venir_question == 3:
            ans17 = input("(Ella) \n")
            if ans17.upper() == venir_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", venir_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('venir'))
        elif venir_question == 4:
            ans17 = input("(Usted) \n")
            if ans17.upper() == venir_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", venir_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('venir'))
        elif venir_question == 5:
            ans17 = input("(Nosotros) \n")
            if ans17.upper() == venir_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", venir_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('venir'))
        elif venir_question == 6:
            ans17 = input("(Vosotros) \n")
            if ans17.upper() == venir_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", venir_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('venir'))
        elif venir_question == 7:
            ans17 = input("(Ustedes) \n")
            if ans17.upper() == venir_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", venir_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('venir'))
        elif venir_question == 8:
            ans17 = input("(Ellos) \n")
            if ans17.upper() == venir_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", venir_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('venir'))
        else:
            ans17 = input("(Ellas) \n")
            if ans17.upper() == venir_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", venir_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('venir'))
    print("Current Score: ", score)


def ver():
    global score
    for x in range(1):
        ver_question = random.randint(0, 9)
        if ver_question == 0:
            ans18 = input("(Yo) \n")
            if ans18.upper() == ver_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", ver_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('ver'))
        elif ver_question == 1:
            ans18 = input("(Tú) \n")
            if ans18.upper() == ver_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", ver_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('ver'))
        elif ver_question == 2:
            ans18 = input("(Él) \n")
            if ans18.upper() == ver_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", ver_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('ver'))
        elif ver_question == 3:
            ans18 = input("(Ella) \n")
            if ans18.upper() == ver_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", ver_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('ver'))
        elif ver_question == 4:
            ans18 = input("(Usted) \n")
            if ans18.upper() == ver_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", ver_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('ver'))
        elif ver_question == 5:
            ans18 = input("(Nosotros) \n")
            if ans18.upper() == ver_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", ver_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('ver'))
        elif ver_question == 6:
            ans18 = input("(Vosotros) \n")
            if ans18.upper() == ver_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", ver_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('ver'))
        elif ver_question == 7:
            ans18 = input("(Ustedes) \n")
            if ans18.upper() == ver_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", ver_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('ver'))
        elif ver_question == 8:
            ans18 = input("(Ellos) \n")
            if ans18.upper() == ver_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", ver_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('ver'))
        else:
            ans18 = input("(Ellas) \n")
            if ans18.upper() == ver_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", ver_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('ver'))
    print("Current Score: ", score)


# ---------------------Definitions of Stem Changes------------------------
def dormir():
    global score
    for x in range(1):
        dormir_question = random.randint(0, 9)
        if dormir_question == 0:
            ans19 = input("(Yo) \n")
            if ans19.upper() == dormir_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", dormir_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('dormir'))
        elif dormir_question == 1:
            ans19 = input("(Tú) \n")
            if ans19.upper() == dormir_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", dormir_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('dormir'))
        elif dormir_question == 2:
            ans19 = input("(Él) \n")
            if ans19.upper() == dormir_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", dormir_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('dormir'))
        elif dormir_question == 3:
            ans19 = input("(Ella) \n")
            if ans19.upper() == dormir_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", dormir_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('dormir'))
        elif dormir_question == 4:
            ans19 = input("(Usted) \n")
            if ans19.upper() == dormir_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", dormir_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('dormir'))
        elif dormir_question == 5:
            ans19 = input("(Nosotros) \n")
            if ans19.upper() == dormir_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", dormir_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('dormir'))
        elif dormir_question == 6:
            ans19 = input("(Vosotros) \n")
            if ans19.upper() == dormir_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", dormir_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('dormir'))
        elif dormir_question == 7:
            ans19 = input("(Ustedes) \n")
            if ans19.upper() == dormir_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", dormir_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('dormir'))
        elif dormir_question == 8:
            ans19 = input("(Ellos) \n")
            if ans19.upper() == dormir_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", dormir_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('dormir'))
        else:
            ans19 = input("(Ellas) \n")
            if ans19.upper() == dormir_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", dormir_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('dormir'))
    print("Current Score: ", score)


def morir():
    global score
    for x in range(1):
        morir_question = random.randint(0, 9)
        if morir_question == 0:
            ans20 = input("(Yo) \n")
            if ans20.upper() == morir_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", morir_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('morir'))
        elif morir_question == 1:
            ans20 = input("(Tú) \n")
            if ans20.upper() == morir_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", morir_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('morir'))
        elif morir_question == 2:
            ans20 = input("(Él) \n")
            if ans20.upper() == morir_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", morir_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('morir'))
        elif morir_question == 3:
            ans20 = input("(Ella) \n")
            if ans20.upper() == morir_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", morir_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('morir'))
        elif morir_question == 4:
            ans20 = input("(Usted) \n")
            if ans20.upper() == morir_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", morir_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('morir'))
        elif morir_question == 5:
            ans20 = input("(Nosotros) \n")
            if ans20.upper() == morir_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", morir_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('morir'))
        elif morir_question == 6:
            ans20 = input("(Vosotros) \n")
            if ans20.upper() == morir_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", morir_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('morir'))
        elif morir_question == 7:
            ans20 = input("(Ustedes) \n")
            if ans20.upper() == morir_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", morir_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('morir'))
        elif morir_question == 8:
            ans20 = input("(Ellos) \n")
            if ans20.upper() == morir_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", morir_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('morir'))
        else:
            ans20 = input("(Ellas) \n")
            if ans20.upper() == morir_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", morir_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('morir'))
    print("Current Score: ", score)


def pedir():
    global score
    for x in range(1):
        pedir_question = random.randint(0, 9)
        if pedir_question == 0:
            ans21 = input("(Yo) \n")
            if ans21.upper() == pedir_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", pedir_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('pedir'))
        elif pedir_question == 1:
            ans21 = input("(Tú) \n")
            if ans21.upper() == pedir_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", pedir_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('pedir'))
        elif pedir_question == 2:
            ans21 = input("(Él) \n")
            if ans21.upper() == pedir_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", pedir_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('pedir'))
        elif pedir_question == 3:
            ans21 = input("(Ella) \n")
            if ans21.upper() == pedir_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", pedir_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('pedir'))
        elif pedir_question == 4:
            ans21 = input("(Usted) \n")
            if ans21.upper() == pedir_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", pedir_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('pedir'))
        elif pedir_question == 5:
            ans21 = input("(Nosotros) \n")
            if ans21.upper() == pedir_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", pedir_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('pedir'))
        elif pedir_question == 6:
            ans21 = input("(Vosotros) \n")
            if ans21.upper() == pedir_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", pedir_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('pedir'))
        elif pedir_question == 7:
            ans21 = input("(Ustedes) \n")
            if ans21.upper() == pedir_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", pedir_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('pedir'))
        elif pedir_question == 8:
            ans21 = input("(Ellos) \n")
            if ans21.upper() == pedir_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", pedir_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('pedir'))
        else:
            ans21 = input("(Ellas) \n")
            if ans21.upper() == pedir_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", pedir_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('pedir'))
    print("Current Score: ", score)


def preferir():
    global score
    for x in range(1):
        preferir_question = random.randint(0, 9)
        if preferir_question == 0:
            ans22 = input("(Yo) \n")
            if ans22.upper() == preferir_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", preferir_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('preferir'))
        elif preferir_question == 1:
            ans22 = input("(Tú) \n")
            if ans22.upper() == preferir_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", preferir_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('preferir'))
        elif preferir_question == 2:
            ans22 = input("(Él) \n")
            if ans22.upper() == preferir_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", preferir_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('preferir'))
        elif preferir_question == 3:
            ans22 = input("(Ella) \n")
            if ans22.upper() == preferir_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", preferir_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('preferir'))
        elif preferir_question == 4:
            ans22 = input("(Usted) \n")
            if ans22.upper() == preferir_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", preferir_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('preferir'))
        elif preferir_question == 5:
            ans22 = input("(Nosotros) \n")
            if ans22.upper() == preferir_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", preferir_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('preferir'))
        elif preferir_question == 6:
            ans22 = input("(Vosotros) \n")
            if ans22.upper() == preferir_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", preferir_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('preferir'))
        elif preferir_question == 7:
            ans22 = input("(Ustedes) \n")
            if ans22.upper() == preferir_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", preferir_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('preferir'))
        elif preferir_question == 8:
            ans22 = input("(Ellos) \n")
            if ans22.upper() == preferir_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", preferir_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('preferir'))
        else:
            ans22 = input("(Ellas) \n")
            if ans22.upper() == preferir_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", preferir_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('preferir'))
    print("Current Score: ", score)


def seguir():
    global score
    for x in range(1):
        seguir_question = random.randint(0, 9)
        if seguir_question == 0:
            ans23 = input("(Yo) \n")
            if ans23.upper() == seguir_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", seguir_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('preferir'))
        elif seguir_question == 1:
            ans23 = input("(Tú) \n")
            if ans23.upper() == seguir_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", seguir_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('preferir'))
        elif seguir_question == 2:
            ans23 = input("(Él) \n")
            if ans23.upper() == seguir_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", seguir_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('preferir'))
        elif seguir_question == 3:
            ans23 = input("(Ella) \n")
            if ans23.upper() == seguir_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", seguir_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('preferir'))
        elif seguir_question == 4:
            ans23 = input("(Usted) \n")
            if ans23.upper() == seguir_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", seguir_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('preferir'))
        elif seguir_question == 5:
            ans23 = input("(Nosotros) \n")
            if ans23.upper() == seguir_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", seguir_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('preferir'))
        elif seguir_question == 6:
            ans23 = input("(Vosotros) \n")
            if ans23.upper() == seguir_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", seguir_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('preferir'))
        elif seguir_question == 7:
            ans23 = input("(Ustedes) \n")
            if ans23.upper() == seguir_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", seguir_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('preferir'))
        elif seguir_question == 8:
            ans23 = input("(Ellos) \n")
            if ans23.upper() == seguir_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", seguir_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('preferir'))
        else:
            ans23 = input("(Ellas) \n")
            if ans23.upper() == seguir_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", seguir_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('preferir'))
    print("Current Score: ", score)


def sentir():
    global score
    for x in range(1):
        sentir_question = random.randint(0, 9)
        if sentir_question == 0:
            ans24 = input("(Yo) \n")
            if ans24.upper() == sentir_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", sentir_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('sentir'))
        elif sentir_question == 1:
            ans24 = input("(Tú) \n")
            if ans24.upper() == sentir_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", sentir_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('sentir'))
        elif sentir_question == 2:
            ans24 = input("(Él) \n")
            if ans24.upper() == sentir_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", sentir_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('sentir'))
        elif sentir_question == 3:
            ans24 = input("(Ella) \n")
            if ans24.upper() == sentir_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", sentir_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('sentir'))
        elif sentir_question == 4:
            ans24 = input("(Usted) \n")
            if ans24.upper() == sentir_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", sentir_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('sentir'))
        elif sentir_question == 5:
            ans24 = input("(Nosotros) \n")
            if ans24.upper() == sentir_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", sentir_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('sentir'))
        elif sentir_question == 6:
            ans24 = input("(Vosotros) \n")
            if ans24.upper() == sentir_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", sentir_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('sentir'))
        elif sentir_question == 7:
            ans24 = input("(Ustedes) \n")
            if ans24.upper() == sentir_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", sentir_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('sentir'))
        elif sentir_question == 8:
            ans24 = input("(Ellos) \n")
            if ans24.upper() == sentir_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", sentir_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('sentir'))
        else:
            ans24 = input("(Ellas) \n")
            if ans24.upper() == sentir_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", sentir_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('sentir'))
    print("Current Score: ", score)


def caer():
    global score
    for x in range(1):
        caer_question = random.randint(0, 9)
        if caer_question == 0:
            ans25 = input("(Yo) \n")
            if ans25.upper() == caer_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", caer_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('caer'))
        elif caer_question == 1:
            ans25 = input("(Tú) \n")
            if ans25.upper() == caer_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", caer_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('caer'))
        elif caer_question == 2:
            ans25 = input("(Él) \n")
            if ans25.upper() == caer_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", caer_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('caer'))
        elif caer_question == 3:
            ans25 = input("(Ella) \n")
            if ans25.upper() == caer_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", caer_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('caer'))
        elif caer_question == 4:
            ans25 = input("(Usted) \n")
            if ans25.upper() == caer_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", caer_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('caer'))
        elif caer_question == 5:
            ans25 = input("(Nosotros) \n")
            if ans25.upper() == caer_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", caer_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('caer'))
        elif caer_question == 6:
            ans25 = input("(Vosotros) \n")
            if ans25.upper() == caer_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", caer_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('caer'))
        elif caer_question == 7:
            ans25 = input("(Ustedes) \n")
            if ans25.upper() == caer_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", caer_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('caer'))
        elif caer_question == 8:
            ans25 = input("(Ellos) \n")
            if ans25.upper() == caer_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", caer_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('caer'))
        else:
            ans25 = input("(Ellas) \n")
            if ans25.upper() == caer_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", caer_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('caer'))
    print("Current Score: ", score)


def creer():
    global score
    for x in range(1):
        creer_question = random.randint(0, 9)
        if creer_question == 0:
            ans26 = input("(Yo) \n")
            if ans26.upper() == creer_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", creer_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('creer'))
        elif creer_question == 1:
            ans26 = input("(Tú) \n")
            if ans26.upper() == creer_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", creer_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('creer'))
        elif creer_question == 2:
            ans26 = input("(Él) \n")
            if ans26.upper() == creer_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", creer_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('creer'))
        elif creer_question == 3:
            ans26 = input("(Ella) \n")
            if ans26.upper() == creer_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", creer_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('creer'))
        elif creer_question == 4:
            ans26 = input("(Usted) \n")
            if ans26.upper() == creer_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", creer_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('creer'))
        elif creer_question == 5:
            ans26 = input("(Nosotros) \n")
            if ans26.upper() == creer_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", creer_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('creer'))
        elif creer_question == 6:
            ans26 = input("(Vosotros) \n")
            if ans26.upper() == creer_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", creer_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('creer'))
        elif creer_question == 7:
            ans26 = input("(Ustedes) \n")
            if ans26.upper() == creer_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", creer_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('creer'))
        elif creer_question == 8:
            ans26 = input("(Ellos) \n")
            if ans26.upper() == creer_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", creer_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('creer'))
        else:
            ans26 = input("(Ellas) \n")
            if ans26.upper() == creer_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", creer_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('creer'))
    print("Current Score: ", score)


def leer():
    global score
    for x in range(1):
        leer_question = random.randint(0, 9)
        if leer_question == 0:
            ans38 = input("(Yo) \n")
            if ans38.upper() == leer_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", leer_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('leer'))
        elif leer_question == 1:
            ans38 = input("(Tú) \n")
            if ans38.upper() == leer_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", leer_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('leer'))
        elif leer_question == 2:
            ans38 = input("(Él) \n")
            if ans38.upper() == leer_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", leer_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('leer'))
        elif leer_question == 3:
            ans38 = input("(Ella) \n")
            if ans38.upper() == leer_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", leer_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('leer'))
        elif leer_question == 4:
            ans38 = input("(Usted) \n")
            if ans38.upper() == leer_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", leer_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('leer'))
        elif leer_question == 5:
            ans38 = input("(Nosotros) \n")
            if ans38.upper() == leer_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", leer_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('leer'))
        elif leer_question == 6:
            ans38 = input("(Vosotros) \n")
            if ans38.upper() == leer_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", leer_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('leer'))
        elif leer_question == 7:
            ans38 = input("(Ustedes) \n")
            if ans38.upper() == leer_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", leer_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('leer'))
        elif leer_question == 8:
            ans38 = input("(Ellos) \n")
            if ans38.upper() == leer_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", leer_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('leer'))
        else:
            ans38 = input("(Ellas) \n")
            if ans38.upper() == leer_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", leer_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('leer'))
        print("Current Score: ", score)


def oir():
    global score
    for x in range(1):
        oir_question = random.randint(0, 9)
        if oir_question == 0:
            ans27 = input("(Yo) \n")
            if ans27.upper() == oir_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", oir_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('oir'))
        elif oir_question == 1:
            ans27 = input("(Tú) \n")
            if ans27.upper() == oir_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", oir_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('oir'))
        elif oir_question == 2:
            ans27 = input("(Él) \n")
            if ans27.upper() == oir_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", oir_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('oir'))
        elif oir_question == 3:
            ans27 = input("(Ella) \n")
            if ans27.upper() == oir_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", oir_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('oir'))
        elif oir_question == 4:
            ans27 = input("(Usted) \n")
            if ans27.upper() == oir_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", oir_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('oir'))
        elif oir_question == 5:
            ans27 = input("(Nosotros) \n")
            if ans27.upper() == oir_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", oir_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('oir'))
        elif oir_question == 6:
            ans27 = input("(Vosotros) \n")
            if ans27.upper() == oir_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", oir_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('oir'))
        elif oir_question == 7:
            ans27 = input("(Ustedes) \n")
            if ans27.upper() == oir_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", oir_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('oir'))
        elif oir_question == 8:
            ans27 = input("(Ellos) \n")
            if ans27.upper() == oir_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", oir_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('oir'))
        else:
            ans27 = input("(Ellas) \n")
            if ans27.upper() == oir_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", oir_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('oir'))
    print("Current Score: ", score)


def destruir():
    global score
    for x in range(1):
        destruir_question = random.randint(0, 9)
        if destruir_question == 0:
            ans28 = input("(Yo) \n")
            if ans28.upper() == destruir_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", destruir_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('destruir'))
        elif destruir_question == 1:
            ans28 = input("(Tú) \n")
            if ans28.upper() == destruir_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", destruir_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('destruir'))
        elif destruir_question == 2:
            ans28 = input("(Él) \n")
            if ans28.upper() == destruir_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", destruir_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('destruir'))
        elif destruir_question == 3:
            ans28 = input("(Ella) \n")
            if ans28.upper() == destruir_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", destruir_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('destruir'))
        elif destruir_question == 4:
            ans28 = input("(Usted) \n")
            if ans28.upper() == destruir_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", destruir_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('destruir'))
        elif destruir_question == 5:
            ans28 = input("(Nosotros) \n")
            if ans28.upper() == destruir_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", destruir_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('destruir'))
        elif destruir_question == 6:
            ans28 = input("(Vosotros) \n")
            if ans28.upper() == destruir_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", destruir_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('destruir'))
        elif destruir_question == 7:
            ans28 = input("(Ustedes) \n")
            if ans28.upper() == destruir_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", destruir_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('destruir'))
        elif destruir_question == 8:
            ans28 = input("(Ellos) \n")
            if ans28.upper() == destruir_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", destruir_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('destruir'))
        else:
            ans28 = input("(Ellas) \n")
            if ans28.upper() == destruir_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", destruir_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('destruir'))
    print("Current Score: ", score)


# ---------------------Definitions of Car,Gar, and Zar Verbs

def buscar():
    global score
    for x in range(1):
        buscar_question = random.randint(0, 9)
        if buscar_question == 0:
            ans29 = input("(Yo) \n")
            if ans29.upper() == buscar_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", buscar_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('buscar'))
        elif buscar_question == 1:
            ans29 = input("(Tú) \n")
            if ans29.upper() == buscar_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", buscar_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('buscar'))
        elif buscar_question == 2:
            ans29 = input("(Él) \n")
            if ans29.upper() == buscar_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", buscar_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('buscar'))
        elif buscar_question == 3:
            ans29 = input("(Ella) \n")
            if ans29.upper() == buscar_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", buscar_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('buscar'))
        elif buscar_question == 4:
            ans29 = input("(Usted) \n")
            if ans29.upper() == buscar_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", buscar_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('buscar'))
        elif buscar_question == 5:
            ans29 = input("(Nosotros) \n")
            if ans29.upper() == buscar_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", buscar_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('buscar'))
        elif buscar_question == 6:
            ans29 = input("(Vosotros) \n")
            if ans29.upper() == buscar_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", buscar_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('buscar'))
        elif buscar_question == 7:
            ans29 = input("(Ustedes) \n")
            if ans29.upper() == buscar_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", buscar_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('buscar'))
        elif buscar_question == 8:
            ans29 = input("(Ellos) \n")
            if ans29.upper() == buscar_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", buscar_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('buscar'))
        else:
            ans29 = input("(Ellas) \n")
            if ans29.upper() == buscar_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", buscar_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('buscar'))
        print("Current Score: ", score)


def sacar():
    global score
    for x in range(1):
        sacar_question = random.randint(0, 9)
        if sacar_question == 0:
            ans30 = input("(Yo) \n")
            if ans30.upper() == sacar_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", sacar_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('sacar'))
        elif sacar_question == 1:
            ans30 = input("(Tú) \n")
            if ans30.upper() == sacar_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", sacar_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('sacar'))
        elif sacar_question == 2:
            ans30 = input("(Él) \n")
            if ans30.upper() == sacar_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", sacar_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('sacar'))
        elif sacar_question == 3:
            ans30 = input("(Ella) \n")
            if ans30.upper() == sacar_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", sacar_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('sacar'))
        elif sacar_question == 4:
            ans30 = input("(Usted) \n")
            if ans30.upper() == sacar_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", sacar_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('andsacarar'))
        elif sacar_question == 5:
            ans30 = input("(Nosotros) \n")
            if ans30.upper() == sacar_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", sacar_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('sacar'))
        elif sacar_question == 6:
            ans30 = input("(Vosotros) \n")
            if ans30.upper() == sacar_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", sacar_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('sacar'))
        elif sacar_question == 7:
            ans30 = input("(Ustedes) \n")
            if ans30.upper() == sacar_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", sacar_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('sacar'))
        elif sacar_question == 8:
            ans30 = input("(Ellos) \n")
            if ans30.upper() == sacar_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", sacar_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('sacar'))
        else:
            ans30 = input("(Ellas) \n")
            if ans30.upper() == sacar_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", sacar_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('sacar'))
        print("Current Score: ", score)


def tocar():
    global score
    for x in range(1):
        tocar_question = random.randint(0, 9)
        if tocar_question == 0:
            ans31 = input("(Yo) \n")
            if ans31.upper() == tocar_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", tocar_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('tocar'))
        elif tocar_question == 1:
            ans31 = input("(Tú) \n")
            if ans31.upper() == tocar_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", tocar_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('tocar'))
        elif tocar_question == 2:
            ans31 = input("(Él) \n")
            if ans31.upper() == tocar_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", tocar_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('tocar'))
        elif tocar_question == 3:
            ans31 = input("(Ella) \n")
            if ans31.upper() == tocar_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", tocar_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('tocar'))
        elif tocar_question == 4:
            ans31 = input("(Usted) \n")
            if ans31.upper() == tocar_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", tocar_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('tocar'))
        elif tocar_question == 5:
            ans31 = input("(Nosotros) \n")
            if ans31.upper() == tocar_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", tocar_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('tocar'))
        elif tocar_question == 6:
            ans31 = input("(Vosotros) \n")
            if ans31.upper() == tocar_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", tocar_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('tocar'))
        elif tocar_question == 7:
            ans31 = input("(Ustedes) \n")
            if ans31.upper() == tocar_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", tocar_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('tocar'))
        elif tocar_question == 8:
            ans31 = input("(Ellos) \n")
            if ans31.upper() == tocar_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", tocar_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('tocar'))
        else:
            ans31 = input("(Ellas) \n")
            if ans31.upper() == tocar_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", tocar_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('tocar'))
        print("Current Score: ", score)


def jugar():
    global score
    for x in range(1):
        jugar_question = random.randint(0, 9)
        if jugar_question == 0:
            ans32 = input("(Yo) \n")
            if ans32.upper() == jugar_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", jugar_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('jugar'))
        elif jugar_question == 1:
            ans32 = input("(Tú) \n")
            if ans32.upper() == jugar_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", jugar_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('jugar'))
        elif jugar_question == 2:
            ans32 = input("(Él) \n")
            if ans32.upper() == jugar_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", jugar_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('jugar'))
        elif jugar_question == 3:
            ans32 = input("(Ella) \n")
            if ans32.upper() == jugar_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", jugar_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('jugar'))
        elif jugar_question == 4:
            ans32 = input("(Usted) \n")
            if ans32.upper() == jugar_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", jugar_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('jugar'))
        elif jugar_question == 5:
            ans32 = input("(Nosotros) \n")
            if ans32.upper() == jugar_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", jugar_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('jugar'))
        elif jugar_question == 6:
            ans32 = input("(Vosotros) \n")
            if ans32.upper() == jugar_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", jugar_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('jugar'))
        elif jugar_question == 7:
            ans32 = input("(Ustedes) \n")
            if ans32.upper() == jugar_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", jugar_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('jugar'))
        elif jugar_question == 8:
            ans32 = input("(Ellos) \n")
            if ans32.upper() == jugar_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", jugar_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('jugar'))
        else:
            ans32 = input("(Ellas) \n")
            if ans32.upper() == jugar_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", jugar_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('jugar'))
        print("Current Score: ", score)


def llegar():
    global score
    for x in range(1):
        llegar_question = random.randint(0, 9)
        if llegar_question == 0:
            ans33 = input("(Yo) \n")
            if ans33.upper() == llegar_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", llegar_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('llegar'))
        elif llegar_question == 1:
            ans33 = input("(Tú) \n")
            if ans33.upper() == llegar_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", llegar_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('llegar'))
        elif llegar_question == 2:
            ans33 = input("(Él) \n")
            if ans33.upper() == llegar_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", llegar_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('llegar'))
        elif llegar_question == 3:
            ans33 = input("(Ella) \n")
            if ans33.upper() == llegar_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", llegar_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('llegar'))
        elif llegar_question == 4:
            ans33 = input("(Usted) \n")
            if ans33.upper() == llegar_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", llegar_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('llegar'))
        elif llegar_question == 5:
            ans33 = input("(Nosotros) \n")
            if ans33.upper() == llegar_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", llegar_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('llegar'))
        elif llegar_question == 6:
            ans33 = input("(Vosotros) \n")
            if ans33.upper() == llegar_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", llegar_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('llegar'))
        elif llegar_question == 7:
            ans33 = input("(Ustedes) \n")
            if ans33.upper() == llegar_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", llegar_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('llegar'))
        elif llegar_question == 8:
            ans33 = input("(Ellos) \n")
            if ans33.upper() == llegar_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", llegar_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('llegar'))
        else:
            ans33 = input("(Ellas) \n")
            if ans33.upper() == llegar_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", llegar_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('llegar'))
        print("Current Score: ", score)


def pagar():
    global score
    for x in range(1):
        pagar_question = random.randint(0, 9)
        if pagar_question == 0:
            ans34 = input("(Yo) \n")
            if ans34.upper() == pagar_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", pagar_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('pagar'))
        elif pagar_question == 1:
            ans34 = input("(Tú) \n")
            if ans34.upper() == pagar_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", pagar_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('pagar'))
        elif pagar_question == 2:
            ans34 = input("(Él) \n")
            if ans34.upper() == pagar_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", pagar_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('pagar'))
        elif pagar_question == 3:
            ans34 = input("(Ella) \n")
            if ans34.upper() == pagar_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", pagar_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('pagar'))
        elif pagar_question == 4:
            ans34 = input("(Usted) \n")
            if ans34.upper() == pagar_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", pagar_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('pagar'))
        elif pagar_question == 5:
            ans34 = input("(Nosotros) \n")
            if ans34.upper() == pagar_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", pagar_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('pagar'))
        elif pagar_question == 6:
            ans34 = input("(Vosotros) \n")
            if ans34.upper() == pagar_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", pagar_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('pagar'))
        elif pagar_question == 7:
            ans34 = input("(Ustedes) \n")
            if ans34.upper() == pagar_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", pagar_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('pagar'))
        elif pagar_question == 8:
            ans34 = input("(Ellos) \n")
            if ans34.upper() == pagar_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", pagar_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('pagar'))
        else:
            ans34 = input("(Ellas) \n")
            if ans34.upper() == pagar_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", pagar_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('pagar'))
        print("Current Score: ", score)


def almorzar():
    global score
    for x in range(1):
        almorzar_question = random.randint(0, 9)
        if almorzar_question == 0:
            ans35 = input("(Yo) \n")
            if ans35.upper() == almorzar_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", almorzar_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('almorzar'))
        elif almorzar_question == 1:
            ans35 = input("(Tú) \n")
            if ans35.upper() == almorzar_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", almorzar_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('almorzar'))
        elif almorzar_question == 2:
            ans35 = input("(Él) \n")
            if ans35.upper() == almorzar_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", almorzar_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('almorzar'))
        elif almorzar_question == 3:
            ans35 = input("(Ella) \n")
            if ans35.upper() == almorzar_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", almorzar_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('almorzar'))
        elif almorzar_question == 4:
            ans35 = input("(Usted) \n")
            if ans35.upper() == almorzar_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", almorzar_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('almorzar'))
        elif almorzar_question == 5:
            ans35 = input("(Nosotros) \n")
            if ans35.upper() == almorzar_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", almorzar_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('almorzar'))
        elif almorzar_question == 6:
            ans35 = input("(Vosotros) \n")
            if ans35.upper() == almorzar_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", almorzar_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('almorzar'))
        elif almorzar_question == 7:
            ans35 = input("(Ustedes) \n")
            if ans35.upper() == almorzar_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", almorzar_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('almorzar'))
        elif almorzar_question == 8:
            ans35 = input("(Ellos) \n")
            if ans35.upper() == almorzar_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", almorzar_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('almorzar'))
        else:
            ans35 = input("(Ellas) \n")
            if ans35.upper() == almorzar_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", almorzar_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('almorzar'))
        print("Current Score: ", score)


def empezar():
    global score
    for x in range(1):
        empezar_question = random.randint(0, 9)
        if empezar_question == 0:
            ans36 = input("(Yo) \n")
            if ans36.upper() == empezar_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", empezar_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('empezar'))
        elif empezar_question == 1:
            ans36 = input("(Tú) \n")
            if ans36.upper() == empezar_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", empezar_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('empezar'))
        elif empezar_question == 2:
            ans36 = input("(Él) \n")
            if ans36.upper() == empezar_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", empezar_conj_words["(Él)"])
            webbrowser.open_new(url + '/{}'.format('empezar'))
        elif empezar_question == 3:
            ans36 = input("(Ella) \n")
            if ans36.upper() == empezar_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", empezar_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('empezar'))
        elif empezar_question == 4:
            ans36 = input("(Usted) \n")
            if ans36.upper() == empezar_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", empezar_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('empezar'))
        elif empezar_question == 5:
            ans36 = input("(Nosotros) \n")
            if ans36.upper() == empezar_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", empezar_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('empezar'))
        elif empezar_question == 6:
            ans36 = input("(Vosotros) \n")
            if ans36.upper() == empezar_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", empezar_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('empezar'))
        elif empezar_question == 7:
            ans36 = input("(Ustedes) \n")
            if ans36.upper() == empezar_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", empezar_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('empezar'))
        elif empezar_question == 8:
            ans36 = input("(Ellos) \n")
            if ans36.upper() == empezar_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", empezar_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('empezar'))
        else:
            ans36 = input("(Ellas) \n")
            if ans36.upper() == empezar_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", empezar_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('empezar'))
        print("Current Score: ", score)


def organizar():
    global score
    for x in range(1):
        organizar_question = random.randint(0, 9)
        if organizar_question == 0:
            ans37 = input("(Yo) \n")
            if ans37.upper() == organizar_conj_words["(Yo)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", organizar_conj_words["(Yo)"])
                webbrowser.open_new(url + '/{}'.format('organizar'))
        elif organizar_question == 1:
            ans37 = input("(Tú) \n")
            if ans37.upper() == organizar_conj_words["(Tú)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", organizar_conj_words["(Tú)"])
                webbrowser.open_new(url + '/{}'.format('organizar'))
        elif organizar_question == 2:
            ans37 = input("(Él) \n")
            if ans37.upper() == organizar_conj_words["(Él)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", organizar_conj_words["(Él)"])
                webbrowser.open_new(url + '/{}'.format('organizar'))
        elif organizar_question == 3:
            ans37 = input("(Ella) \n")
            if ans37.upper() == organizar_conj_words["(Ella)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", organizar_conj_words["(Ella)"])
                webbrowser.open_new(url + '/{}'.format('organizar'))
        elif organizar_question == 4:
            ans37 = input("(Usted) \n")
            if ans37.upper() == organizar_conj_words["(Usted)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", organizar_conj_words["(Usted)"])
                webbrowser.open_new(url + '/{}'.format('organizar'))
        elif organizar_question == 5:
            ans37 = input("(Nosotros) \n")
            if ans37.upper() == organizar_conj_words["(Nosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", organizar_conj_words["(Nosotros)"])
                webbrowser.open_new(url + '/{}'.format('organizar'))
        elif organizar_question == 6:
            ans37 = input("(Vosotros) \n")
            if ans37.upper() == organizar_conj_words["(Vosotros)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", organizar_conj_words["(Vosotros)"])
                webbrowser.open_new(url + '/{}'.format('organizar'))
        elif organizar_question == 7:
            ans37 = input("(Ustedes) \n")
            if ans37.upper() == organizar_conj_words["(Ustedes)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", organizar_conj_words["(Ustedes)"])
                webbrowser.open_new(url + '/{}'.format('organizar'))
        elif organizar_question == 8:
            ans37 = input("(Ellos) \n")
            if ans37.upper() == organizar_conj_words["(Ellos)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", organizar_conj_words["(Ellos)"])
                webbrowser.open_new(url + '/{}'.format('organizar'))
        else:
            ans37 = input("(Ellas) \n")
            if ans37.upper() == organizar_conj_words["(Ellas)"]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", organizar_conj_words["(Ellas)"])
                webbrowser.open_new(url + '/{}'.format('organizar'))
        print("Current Score: ", score)


# ---------------------Definition of Signals-----------------------------

def signalQuiz():
    global score
    for x in range(1):
        signal_question = random.randint(0, len(signals))
        if signal_question == 0:
            ans38 = input("at (number)\n")
            if ans38.lower() == signals.get("at (number) "):
                print("That is correct \n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", signals.get("at (number) "))
        elif signal_question == 1:
            ans38 = input("to the (verb) [ex. upon arrival] \n")
            if ans38.lower() == signals.get("to the (verb) [ex. upon arrival] "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", signals.get("to the (verb) [ex. upon arrival] "))
        elif signal_question == 2:
            ans38 = input("last night \n")
            if ans38.lower() == signals.get("last night "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", signals.get("last night "))
        elif signal_question == 3:
            ans38 = input("the day before yesterday \n")
            if ans38.lower() == signals.get("the day before yesterday "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", signals.get("the day before yesterday "))
        elif signal_question == 4:
            ans38 = input("yesterday \n")
            if ans38.lower() == signals.get("yesterday "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", signals.get("yesterday "))
        elif signal_question == 5:
            ans38 = input("when \n")
            if ans38.lower() == signals.get("when "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", signals.get("when "))
        elif signal_question == 6:
            ans38 = input("fast \n")
            if ans38.lower() == signals.get("fast "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", signals.get("fast "))
        elif signal_question == 7:
            ans38 = input("suddenly \n")
            if ans38.lower() == signals["suddenly "]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", signals.get("suddenly "))
        elif signal_question == 8:
            ans38 = input("on the last day \n")
            if ans38.lower() == signals.get("on the last day "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", signals.get("on the last day "))
        elif signal_question == 9:
            ans38 = input("the (past) state \n")
            if ans38.lower() == signals.get("the (past) state "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", signals.get("the (past) state "))
        elif signal_question == 10:
            ans38 = input("last year \n")
            if ans38.lower() == signals.get("last year "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", signals.get("last year "))
        elif signal_question == 11:
            ans38 = input("the next day \n")
            if ans38.lower() == signals.get("the next day "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", signals.get("the next day "))
        elif signal_question == 12:
            ans38 = input("immediately \n")
            if ans38.lower() == signals.get("immediately "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", signals.get("immediately "))
        elif signal_question == 13:
            ans38 = input("then \n")
            if ans38.lower() == signals.get("then "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", signals.get("then "))
        elif signal_question == 14:
            ans38 = input("this morning \n")
            if ans38.lower() == signals.get("this morning "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", signals.get("this morning "))
        elif signal_question == 15:
            ans38 = input("this afternoon \n")
            if ans38.lower() == signals.get("this afternoon "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", signals.get("this afternoon "))
        elif signal_question == 16:
            ans38 = input("finally \n")
            if ans38.lower() == signals.get("finally "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", signals.get("finally "))
        elif signal_question == 17:
            ans38 = input("later \n")
            if ans38.lower() == signals.get("later "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", signals.get("later "))
        elif signal_question == 18:
            ans38 = input("to start with \n")
            if ans38.lower() == signals.get("to start with "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", signals.get("to start with "))
        elif signal_question == 19:
            ans38 = input("therefore \n")
            if ans38.lower() == signals.get("therefore "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", signals.get("therefore "))
        elif signal_question == 20:
            ans38 = input("in the morning \n")
            if ans38.lower() == signals.get("in the morning "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", signals.get("in the morning "))
        elif signal_question == 21:
            ans38 = input("in the evening \n")
            if ans38.lower() == signals.get("in the evening "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", signals.get("in the evening "))
        elif signal_question == 22:
            ans38 = input("in the afternoon \n")
            if ans38.lower() == signals.get("in the afternoon "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", signals.get("in the afternoon "))
        elif signal_question == 23:
            ans38 = input("soon \n")
            if ans38.lower() == signals.get("soon "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", signals.get("soon "))
        elif signal_question == 24:
            ans38 = input("one day \n")
            if ans38.lower() == signals.get("one day "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", signals.get("one day "))
        elif signal_question == 25:
            ans38 = input("once \n")
            if ans38.lower() == signals.get("once "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", signals.get("once "))
        elif signal_question == 26:
            ans38 = input("always \n")
            if ans38.lower() == signals.get("always "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", signals.get("always "))
        elif signal_question == 27:
            ans38 = input("so many times \n")
            if ans38.lower() == signals.get("so many times "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", signals.get("so many times "))
        elif signal_question == 28:
            ans38 = input("every week \n")
            if ans38.lower() == signals.get("every week "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", signals.get("every week "))
        elif signal_question == 29:
            ans38 = input("all the time \n")
            if ans38.lower() == signals.get("all the time "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", signals.get("all the time "))
        elif signal_question == 30:
            ans38 = input("every day \n")
            if ans38.lower() == signals.get("every day "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", signals.get("every day "))
        elif signal_question == 31:
            ans38 = input(signals.get("several times"))
            if ans38.lower() == signals.get("several times"):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", signals.get("several times"))
        elif signal_question == 32:
            ans38 = input("at once\n")
            if ans38.lower() == signals.get("at once "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", signals.get("at once "))
        else:
            print("There is an error in the code under signalQuiz() \n")
        print("Current Score: ", score)

def imperfectSignalQuiz():
    global score
    for x in range(1):
        signal_question = random.randint(0, len(imperfect_signals))
        if signal_question == 0:
            ans38 = input("often \n")
            if ans38.lower() == imperfect_signals.get("often "):
                print("That is correct \n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", imperfect_signals.get("often "))
        elif signal_question == 1:
            ans38 = input("sometimes \n")
            if ans38.lower() == imperfect_signals.get("sometimes "):
                print("That is correct\n")
                score
                score += 1
            else:
              print("That is incorrect. The correct answer is ", imperfect_signals.get("sometimes "))
        elif signal_question == 2:
            ans38 = input("other times \n")
            if ans38.lower() == imperfect_signals.get("other times "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", imperfect_signals.get("other times "))
        elif signal_question == 3:
            ans38 = input("each year \n")
            if ans38.lower() == imperfect_signals.get("each year "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", imperfect_signals.get("each year "))
        elif signal_question == 4:
            ans38 = input("cada día \n")
            if ans38.lower() == imperfect_signals.get("cada día "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", imperfect_signals.get("cada día "))
        elif signal_question == 5:
            ans38 = input("cada semana \n")
            if ans38.lower() == imperfect_signals.get("cada semana "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", imperfect_signals.get("cada semana "))
        elif signal_question == 6:
            ans38 = input("con frecuencia \n")
            if ans38.lower() == imperfect_signals.get("con frecuencia "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", imperfect_signals.get("con frecuencia "))
        elif signal_question == 7:
            ans38 = input("de costumbre \n")
            if ans38.lower() == imperfect_signals["de costumbre "]:
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", imperfect_signals.get("de costumbre "))
        elif signal_question == 8:
            ans38 = input("de vez de cuando \n")
            if ans38.lower() == imperfect_signals.get("de vez de cuando "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", imperfect_signals.get("de vez de cuando "))
        elif signal_question == 9:
            ans38 = input("durante \n")
            if ans38.lower() == imperfect_signals.get("durante "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", imperfect_signals.get("durante "))
        elif signal_question == 10:
            ans38 = input("en aquella época \n")
            if ans38.lower() == imperfect_signals.get("en aquella época "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", imperfect_signals.get("en aquella época "))
        elif signal_question == 11:
            ans38 = input("frecuentemente \n")
            if ans38.lower() == imperfect_signals.get("frecuentemente "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", imperfect_signals.get("frecuentemente "))
        elif signal_question == 12:
            ans38 = input("generalmente \n")
            if ans38.lower() == imperfect_signals.get("generalmente "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", imperfect_signals.get("generalmente "))
        elif signal_question == 13:
            ans38 = input("mientras \n")
            if ans38.lower() == imperfect_signals.get("mientras "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", imperfect_signals.get("mientras "))
        elif signal_question == 14:
            ans38 = input("muchas veces \n")
            if ans38.lower() == imperfect_signals.get("muchas veces "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", imperfect_signals.get("muchas veces "))
        elif signal_question == 15:
            ans38 = input("nunca \n")
            if ans38.lower() == imperfect_signals.get("nunca "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", imperfect_signals.get("nunca "))
        elif signal_question == 16:
            ans38 = input("mucho \n")
            if ans38.lower() == imperfect_signals.get("mucho "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", imperfect_signals.get("mucho "))
        elif signal_question == 17:
            ans38 = input("por lo general \n")
            if ans38.lower() == imperfect_signals.get("por lo general "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", imperfect_signals.get("por lo general "))
        elif signal_question == 18:
            ans38 = input("por un rato \n")
            if ans38.lower() == imperfect_signals.get("por un rato "):
                print("That is correct\n")
                score
                score += 1
            else:
                print("That is incorrect. The correct answer is ", imperfect_signals.get("por un rato "))
        else:
            print("There is an error in the code under imperfectSignalQuiz() \n")
        print("Current Score: ", score)# ---------------------Vocabulary of Imperfect Verbs----------------------
andar_conj_words = {
    "(Yo)": "ANDUVE",
    "(Tú)": "ANDUVISTE",
    "(Él)": "ANDUVO",
    "(Ella)": "ANDUVO",
    "(Usted)": "ANDUVO",
    "(Nosotros)": "ANDUVIMOS",
    "(Vosotros)": "ANDUVISTEIS",
    "(Ustedes)": "ANDUVIERON",
    "(Ellos)": "ANDUVIERON",
    "(Ellas)": "ANDUVIERON"
}

caber_conj_words = {
    "(Yo)": "CUPE",
    "(Tú)": "CUPISTE",
    "(Él)": "CUPO",
    "(Ella)": "CUPO",
    "(Usted)": "CUPO",
    "(Nosotros)": "CUPIMOS",
    "(Vosotros)": "CUPISTEIS",
    "(Ustedes)": "CUPIERON",
    "(Ellos)": "CUPIERON",
    "(Ellas)": "CUPIERON"
}

conducir_conj_words = {
    "(Yo)": "CONDUJE",
    "(Tú)": "CONDUJISTE",
    "(Él)": "CONDUJO",
    "(Ella)": "CONDUJO",
    "(Usted)": "CONDUJO",
    "(Nosotros)": "CONDUJIMOS",
    "(Vosotros)": "CONDUJISTEIS",
    "(Ustedes)": "CONDUJERON",
    "(Ellos)": "CONDUJERON",
    "(Ellas)": "CONDUJERON"
}

dar_conj_words = {
    "(Yo)": "DI",
    "(Tú)": "DISTE",
    "(Él)": "DIO",
    "(Ella)": "DIO",
    "(Usted)": "DIO",
    "(Nosotros)": "DIMOS",
    "(Vosotros)": "DISTEIS",
    "(Ustedes)": "DIERON",
    "(Ellos)": "DIERON",
    "(Ellas)": "DIERON"
}

decir_conj_words = {
    "(Yo)": "DIJE",
    "(Tú)": "DIJISTE",
    "(Él)": "DIJO",
    "(Ella)": "DIJO",
    "(Usted)": "DIJO",
    "(Nosotros)": "DIJIMOS",
    "(Vosotros)": "DIJISTEIS",
    "(Ustedes)": "DIJERON",
    "(Ellos)": "DIJERON",
    "(Ellas)": "DIJERON"
}

estar_conj_words = {
    "(Yo)": "ESTUVE",
    "(Tú)": "ESTUVISTE",
    "(Él)": "ESTUVO",
    "(Ella)": "ESTUVO",
    "(Usted)": "ESTUVO",
    "(Nosotros)": "ESTUVIMOS",
    "(Vosotros)": "ESTUVISTEIS",
    "(Ustedes)": "ESTUVIERON",
    "(Ellos)": "ESTUVIERON",
    "(Ellas)": "ESTUVIERON"
}

hacer_conj_words = {
    "(Yo)": "HICE",
    "(Tú)": "HICISTE",
    "(Él)": "HIZO",
    "(Ella)": "HIZO",
    "(Usted)": "HIZO",
    "(Nosotros)": "HICIMOS",
    "(Vosotros)": "HICISTEIS",
    "(Ustedes)": "HICIERON",
    "(Ellos)": "HICIERON",
    "(Ellas)": "HICIERON"
}

ir_conj_words = {
    "(Yo)": "FUI",
    "(Tú)": "FUISTE",
    "(Él)": "FUE",
    "(Ella)": "FUE",
    "(Usted)": "FUE",
    "(Nosotros)": "FUIMOS",
    "(Vosotros)": "FUISTEIS",
    "(Ustedes)": "FUERON",
    "(Ellos)": "FUERON",
    "(Ellas)": "FUERON"
}

poder_conj_words = {
    "(Yo)": "PUDE",
    "(Tú)": "PUDISTE",
    "(Él)": "PUDO",
    "(Ella)": "PUDO",
    "(Usted)": "PUDO",
    "(Nosotros)": "PUDIMOS",
    "(Vosotros)": "PUDISTEIS",
    "(Ustedes)": "PUDIERON",
    "(Ellos)": "PUDIERON",
    "(Ellas)": "PUDIERON"
}

poner_conj_words = {
    "(Yo)": "PUSE",
    "(Tú)": "PUSISTE",
    "(Él)": "PUSO",
    "(Ella)": "PUSO",
    "(Usted)": "PUSO",
    "(Nosotros)": "PUSIMOS",
    "(Vosotros)": "PUSISTEIS",
    "(Ustedes)": "PUSIERON",
    "(Ellos)": "PUSIERON",
    "(Ellas)": "PUSIERON"
}

querer_conj_words = {
    "(Yo)": "QUISE",
    "(Tú)": "QUISISTE",
    "(Él)": "QUISO",
    "(Ella)": "QUISO",
    "(Usted)": "QUISO",
    "(Nosotros)": "QUISIMOS",
    "(Vosotros)": "QUISISTEIS",
    "(Ustedes)": "QUISIERON",
    "(Ellos)": "QUISIERON",
    "(Ellas)": "QUISIERON"
}

saber_conj_words = {
    "(Yo)": "SUPE",
    "(Tú)": "SUPISTE",
    "(Él)": "SUPO",
    "(Ella)": "SUPO",
    "(Usted)": "SUPO",
    "(Nosotros)": "SUPIMOS",
    "(Vosotros)": "SUPISTEIS",
    "(Ustedes)": "SUPIERON",
    "(Ellos)": "SUPIERON",
    "(Ellas)": "SUPIERON"
}

ser_conj_words = {
    "(Yo)": "FUI",
    "(Tú)": "FUISTE",
    "(Él)": "FUE",
    "(Ella)": "FUE",
    "(Usted)": "FUE",
    "(Nosotros)": "FUIMOS",
    "(Vosotros)": "FUISTEIS",
    "(Ustedes)": "FUERON",
    "(Ellos)": "FUERON",
    "(Ellas)": "FUERON"
}

tener_conj_words = {
    "(Yo)": "TUVE",
    "(Tú)": "TUVISTE",
    "(Él)": "TUVO",
    "(Ella)": "TUVO",
    "(Usted)": "TUVO",
    "(Nosotros)": "TUVIMOS",
    "(Vosotros)": "TUVISTEIS",
    "(Ustedes)": "TUVIERON",
    "(Ellos)": "TUVIERON",
    "(Ellas)": "TUVIERON"
}

traducir_conj_words = {
    "(Yo)": "TRADUJE",
    "(Tú)": "TRADUJISTE",
    "(Él)": "TRADUJO",
    "(Ella)": "TRADUJO",
    "(Usted)": "TRADUJO",
    "(Nosotros)": "TRADUJIMOS",
    "(Vosotros)": "TRADUJISTEIS",
    "(Ustedes)": "TRADUJERON",
    "(Ellos)": "TRADUJERON",
    "(Ellas)": "TRADUJERON"
}

traer_conj_words = {
    "(Yo)": "TRAJE",
    "(Tú)": "TRAJISTE",
    "(Él)": "TRAJO",
    "(Ella)": "TRAJO",
    "(Usted)": "TRAJO",
    "(Nosotros)": "TRAJIMOS",
    "(Vosotros)": "TRAJISTEIS",
    "(Ustedes)": "TRAJERON",
    "(Ellos)": "TRAJERON",
    "(Ellas)": "TRAJERON"
}

venir_conj_words = {
    "(Yo)": "VINE",
    "(Tú)": "VINISTE",
    "(Él)": "VINO",
    "(Ella)": "VINO",
    "(Usted)": "VINO",
    "(Nosotros)": "VINIMOS",
    "(Vosotros)": "VINISTEIS",
    "(Ustedes)": "VINIERON",
    "(Ellos)": "VINIERON",
    "(Ellas)": "VINIERON"
}

ver_conj_words = {
    "(Yo)": "VI",
    "(Tú)": "VISTE",
    "(Él)": "VIO",
    "(Ella)": "VIO",
    "(Usted)": "VIO",
    "(Nosotros)": "VIMOS",
    "(Vosotros)": "VISTEIS",
    "(Ustedes)": "VIERON",
    "(Ellos)": "VIERON",
    "(Ellas)": "VIERON"
}

# ----------------------Stem Changes--------------------
dormir_conj_words = {
    "(Yo)": "DORMÍ",
    "(Tú)": "DORMISTE",
    "(Él)": "DURMIÓ",
    "(Ella)": "DURMIÓ",
    "(Usted)": "DURMIÓ",
    "(Nosotros)": "DORMIMOS",
    "(Vosotros)": "DORMISTEIS",
    "(Ustedes)": "DURMIERON",
    "(Ellos)": "DURMIERON",
    "(Ellas)": "DURMIERON"
}

morir_conj_words = {
    "(Yo)": "MORÍ",
    "(Tú)": "MORISTE",
    "(Él)": "MURIÓ",
    "(Ella)": "MURIÓ",
    "(Usted)": "MURIÓ",
    "(Nosotros)": "MORIMOS",
    "(Vosotros)": "MORISTEIS",
    "(Ustedes)": "MURIERON",
    "(Ellos)": "MURIERON",
    "(Ellas)": "MURIERON"
}

pedir_conj_words = {
    "(Yo)": "PEDÍ",
    "(Tú)": "PEDISTE",
    "(Él)": "PIDIÓ",
    "(Ella)": "PIDIÓ",
    "(Usted)": "PIDIÓ",
    "(Nosotros)": "PEDIMOS",
    "(Vosotros)": "PEDISTEIS",
    "(Ustedes)": "PIDIERON",
    "(Ellos)": "PIDIERON",
    "(Ellas)": "PIDIERON"
}

preferir_conj_words = {
    "(Yo)": "PREFERÍ",
    "(Tú)": "PREFERISTE",
    "(Él)": "PREFIRIÓ",
    "(Ella)": "PREFIRIÓ",
    "(Usted)": "PREFIRIÓ",
    "(Nosotros)": "PREFERIMOS",
    "(Vosotros)": "PREFERISTEIS",
    "(Ustedes)": "PREFIRIERON",
    "(Ellos)": "PREFIRIERON",
    "(Ellas)": "PREFIRIERON"
}

seguir_conj_words = {
    "(Yo)": "SEGUÍ",
    "(Tú)": "SEGUISTE",
    "(Él)": "SIGUIÓ",
    "(Ella)": "SIGUIÓ",
    "(Usted)": "SIGUIÓ",
    "(Nosotros)": "SEGUIMOS",
    "(Vosotros)": "SEGUISTEIS",
    "(Ustedes)": "SIGUIERON",
    "(Ellos)": "SIGUIERON",
    "(Ellas)": "SIGUIERON"
}

sentir_conj_words = {
    "(Yo)": "SENTÍ",
    "(Tú)": "SENTISTE",
    "(Él)": "SINTIÓ",
    "(Ella)": "SINTIÓ",
    "(Usted)": "SINTIÓ",
    "(Nosotros)": "SENTIMOS",
    "(Vosotros)": "SENTISTEIS",
    "(Ustedes)": "SINTIERON",
    "(Ellos)": "SINTIERON",
    "(Ellas)": "SINTIERON"
}

caer_conj_words = {
    "(Yo)": "CAÍ",
    "(Tú)": "CAÍSTE",
    "(Él)": "CAYÓ",
    "(Ella)": "CAYÓ",
    "(Usted)": "CAYÓ",
    "(Nosotros)": "CAÍMOS",
    "(Vosotros)": "CAÍSTEIS",
    "(Ustedes)": "CAYERON",
    "(Ellos)": "CAYERON",
    "(Ellas)": "CAYERON"
}

creer_conj_words = {
    "(Yo)": "CREÍ",
    "(Tú)": "CREÍSTE",
    "(Él)": "CREYÓ",
    "(Ella)": "CREYÓ",
    "(Usted)": "CREYÓ",
    "(Nosotros)": "CREÍMOS",
    "(Vosotros)": "CREÍSTEIS",
    "(Ustedes)": "CREYERON",
    "(Ellos)": "CREYERON",
    "(Ellas)": "CREYERON"
}

leer_conj_words = {
    "(Yo)": "LEÍ",
    "(Tú)": "LEÍSTE",
    "(Él)": "LEYÓ",
    "(Ella)": "LEYÓ",
    "(Usted)": "LEYÓ",
    "(Nosotros)": "LEÍMOS",
    "(Vosotros)": "LEÍSTEIS",
    "(Ustedes)": "LEYERON",
    "(Ellos)": "LEYERON",
    "(Ellas)": "LEYERON"
}

oir_conj_words = {
    "(Yo)": "OÍ",
    "(Tú)": "OÍSTE",
    "(Él)": "OYÓ",
    "(Ella)": "OYÓ",
    "(Usted)": "OYÓ",
    "(Nosotros)": "OÍMOS",
    "(Vosotros)": "OÍSTEIS",
    "(Ustedes)": "OYERON",
    "(Ellos)": "OYERON",
    "(Ellas)": "OYERON"
}

destruir_conj_words = {
    "(Yo)": "DESTRUÍ",
    "(Tú)": "DESTRUISTE",
    "(Él)": "DESTRUYÓ",
    "(Ella)": "DESTRUYÓ",
    "(Usted)": "DESTRUYÓ",
    "(Nosotros)": "DESTRUIMOS",
    "(Vosotros)": "DESTRUISTEIS",
    "(Ustedes)": "DESTRUYERON",
    "(Ellos)": "DESTRUYERON",
    "(Ellas)": "DESTRUYERON"
}

# ----------------------Vocabulary of Car,Gar,Zar Verbs------------------
buscar_conj_words = {
    "(Yo)": "BUSQUÉ",
    "(Tú)": "BUSCASTE",
    "(Él)": "BUSCÓ",
    "(Ella)": "BUSCÓ",
    "(Usted)": "BUSCÓ",
    "(Nosotros)": "BUSCAMOS",
    "(Vosotros)": "BUSCASTEIS",
    "(Ustedes)": "BUSCARON",
    "(Ellos)": "BUSCARON",
    "(Ellas)": "BUSCARON"
}

sacar_conj_words = {
    "(Yo)": "SAQUÉ",
    "(Tú)": "SACASTE",
    "(Él)": "SACÓ",
    "(Ella)": "SACÓ",
    "(Usted)": "SACÓ",
    "(Nosotros)": "SACAMOS",
    "(Vosotros)": "SACASTEIS",
    "(Ustedes)": "SACARON",
    "(Ellos)": "SACARON",
    "(Ellas)": "SACARON"
}

tocar_conj_words = {
    "(Yo)": "TOQUÉ",
    "(Tú)": "TOCASTE",
    "(Él)": "TOCÓ",
    "(Ella)": "TOCÓ",
    "(Usted)": "TOCÓ",
    "(Nosotros)": "TOCAMOS",
    "(Vosotros)": "TOCASTEIS",
    "(Ustedes)": "TOCARON",
    "(Ellos)": "TOCARON",
    "(Ellas)": "TOCARON"
}

jugar_conj_words = {
    "(Yo)": "JUGUÉ",
    "(Tú)": "JUGASTE",
    "(Él)": "JUGÓ",
    "(Ella)": "JUGÓ",
    "(Usted)": "JUGÓ",
    "(Nosotros)": "JUGAMOS",
    "(Vosotros)": "JUGASTEIS",
    "(Ustedes)": "JUGARON",
    "(Ellos)": "JUGARON",
    "(Ellas)": "JUGARON"
}

llegar_conj_words = {
    "(Yo)": "LLEGUÉ",
    "(Tú)": "LLEGASTE",
    "(Él)": "LLEGÓ",
    "(Ella)": "LLEGÓ",
    "(Usted)": "LLEGÓ",
    "(Nosotros)": "LLEGAMOS",
    "(Vosotros)": "LLEGASTEIS",
    "(Ustedes)": "LLEGARON",
    "(Ellos)": "LLEGARON",
    "(Ellas)": "LLEGARON"
}

pagar_conj_words = {
    "(Yo)": "PAGUÉ",
    "(Tú)": "PAGASTE",
    "(Él)": "PAGÓ",
    "(Ella)": "PAGÓ",
    "(Usted)": "PAGÓ",
    "(Nosotros)": "PAGAMOS",
    "(Vosotros)": "PAGASTEIS",
    "(Ustedes)": "PAGARON",
    "(Ellos)": "PAGARON",
    "(Ellas)": "PAGARON"
}

almorzar_conj_words = {
    "(Yo)": "ALMORCÉ",
    "(Tú)": "ALMORZASTE",
    "(Él)": "ALMORZÓ",
    "(Ella)": "ALMORZÓ",
    "(Usted)": "ALMORZÓ",
    "(Nosotros)": "ALMORZAMOS",
    "(Vosotros)": "ALMORZASTEIS",
    "(Ustedes)": "ALMORZARON",
    "(Ellos)": "ALMORZARON",
    "(Ellas)": "ALMORZARON"
}

empezar_conj_words = {
    "(Yo)": "EMPECÉ",
    "(Tú)": "EMPEZASTE",
    "(Él)": "EMPEZÓ",
    "(Ella)": "EMPEZÓ",
    "(Usted)": "EMPEZÓ",
    "(Nosotros)": "EMPEZAMOS",
    "(Vosotros)": "EMPEZASTEIS",
    "(Ustedes)": "EMPEZARON",
    "(Ellos)": "EMPEZARON",
    "(Ellas)": "EMPEZARON"
}

organizar_conj_words = {
    "(Yo)": "ORGANICÉ",
    "(Tú)": "ORGANIZASTE",
    "(Él)": "ORGANIZÓ",
    "(Ella)": "ORGANIZÓ",
    "(Usted)": "ORGANIZÓ",
    "(Nosotros)": "ORGANIZAMOS",
    "(Vosotros)": "ORGANIZASTEIS",
    "(Ustedes)": "ORGANIZARON",
    "(Ellos)": "ORGANIZARON",
    "(Ellas)": "ORGANIZARON"
}

# ----------------------The Preterite is used for:---------------------
preterite_uses = ["Specific actions or events completed in the past.", "Isolated actions that happened once",
                "Narrating a series of completed actions or events.",
                "Interrupting an action that was already happening.",
                "Preterite of 'Hay' = HUBO (There was, there were)"]

# -----------------------Signals----------------------------------------
signals = {
    "at (number) ": "a las (número)",
    "to the (verb) [ex. upon arrival] ": "al (verbo) [ex. al llegar]",
    "last night ": "anoche",
    "the day before yesterday ": "anteayer",
    "yesterday ": "ayer",
    "when ": "cuando",
    "fast ": "de prisa",
    "suddenly ": "de repente",
    "on the last day ": "el (día) pasado",
    "the (past) state ": "el (estación) pasado",
    "last year ": "el año pasado",
    "the next day ": "el día siguiente",
    "at once ": "en seguida",
    "then ": "entonces",
    "this morning ": "esta mañana",
    "this afternoon ": "esta tarde",
    "finally ": "finalmente",
    "immediately ": "inmediatamente",
    "later ": "luego",
    "to start with ": "para empezar",
    "therefore ": "por eso",
    "finally ": "por fin",
    "in the morning ": "por la mañana",
    "in the evening ": "por la noche",
    "in the afternoon ": "por la tarde",
    "soon ": "pronto",
    "one day ": "un día",
    "once ": "una vez",
    "always ": "siempre",
    "so many times ": "tantas veces",
    "every week ": "todas las semanas",
    "all the time ": "todo el tiempo",
    "every day ": "todos los días",
    "several times": "varias veces",
}

imperfect_signals = {
"often ": "a menudo",
"sometimes ": "a veces",
"other times ": "algunas veces",
"each year ": "cada año",
"cada día ": "each day",
"cada semana": "each week",
"con frecuencia ": "frequently",
"de costumbre ": "as usual",
"de vez en cuando": " from time to time",
"durante ": "during",
"en aquella época ": "at that time",
"frecuentemente ": "frequently",
"generalmente ": "generally",
"mientras ": "while",
"muchas veces ": "many times",
"mucho ": "a lot",
"nunca ": "never",
"por lo general ": "generally",
"por un rato ": "for awhile",
}
# -----------------------Housekeeping---------------------------------
def stop():
    dec = input("Click [ENTER] to continue or any other key to stop \n")
    if dec != "":
        print("\n")
        sys.exit()


# ----------------------Practice Code-------------------
def main():
    print("Para practicar para la prueba, yo hice esta programma computadora\n")
    print("***Only the preterite verb quiz is done\n")
    selection = input("(1) Pretérito o (2) Imperfecto \n")
    if selection == "1":
        preterite_selection = input("Sus opciones son (1) verbos irregulares, (2) Stem Changers,  (3) -CAR, -GAR, -ZAR, (4) Cuándo debe usar un verbo pretérito, y (5) señales \n")
        if preterite_selection == "1":
            irregular_list = ["Andar (to walk)", "Caber (to fit)", "Conducir (to drive)", "Dar (to give)",
                                "Decir (to tell)", "Estar (to be)", "Hacer (to do/make)", "Ir (to go)",
                                "Poder (to be able to)", "Poner (to put)", "Querer (to want)", "Saber(to know)", "Ser(to be)",
                                "Tener (to have)", "Traducir (to translate)", "Traer (to bring)", "Venir (to come)",
                                "verb(to see)"]
            print("This category is Irregular Verbs\n")
            rand_word = [x for x in range(17)]
            np.random.shuffle(rand_word)
            for i in rand_word:
                question_loc = rand_word[i]
                question = irregular_list[question_loc]
                if question_loc == 0:
                    print("Your irregular word is andar \n")
                    andar()
                elif question_loc == 1:
                    print("Your irregular word is caber \n")
                    caber()
                elif question_loc == 2:
                    print("Your irregular word is conducir \n")
                    conducir()
                elif question_loc == 3:
                    print("Your irregular verb is dar \n")
                    dar()
                elif question_loc == 4:
                    print("Your irregular verb is decir \n")
                    decir()
                elif question_loc == 5:
                    print("Your irregular verb is estar \n")
                    estar()
                elif question_loc == 6:
                    print("Your irregular verb is hacer \n")
                    hacer()
                elif question_loc == 7:
                    print("Your irregular verb is ir \n")
                    ir()
                elif question_loc == 8:
                    print("Your irregular verb is poder \n")
                    poder()
                elif question_loc == 9:
                    print("Your irregular verb is poner \n")
                    poner()
                elif question_loc == 10:
                    print("Your irregular verb is querer \n")
                    querer()
                elif question_loc == 11:
                    print("Your irregular verb is saber \n")
                    saber()
                elif question_loc == 12:
                    print("Your irregular verb is ser \n")
                    ser()
                elif question_loc == 13:
                    print("Your irregular verb is tener \n")
                    tener()
                elif question_loc == 14:
                    print("Your irregular verb is traducir \n")
                    traducir()
                elif question_loc == 15:
                    print("Your irregular verb is traer \n")
                    traer()
                elif question_loc == 16:
                    print("Your irregular verb is venir \n")
                    venir()
                elif question_loc == 17:
                    print("Your irregular verb is verb\n")
                    ver()
                else:
                    ("question_loc is out of the range between 0-17. Check for any errors in code\n")
                stop()
        elif preterite_selection == "2":
            print("This category is Stem Changers \n")
            print("Some things that you should know about stem changers are the following: \n")
            stem_changers_init = input(
                "Verbs that end in -ir and goes through a stem-change (boot verbs) are the only verbs that go through a stem change in the preterite tense. The changes are [e to i] and [o to u]. For verbs that end in [aer, eer, oír, oer, or uir], there is a special spelling change. In the third person forms, the [i becomes a y] (ex. yó, yeron). The remaining forms gain written accent over the letter i, except for [uir] verbs, where there are no irregular accents. Verbs that end in [guir] do not follow this pattern. (Click enter once you are done reading this) \n")
            if stem_changers_init == "":
                stem_changers_list = ["Dormir (to sleep)", "Morir (to die)", "Pedir (to ask for)", "Preferir (to prefer)",
                                        "Seguir (to follow)", "Sentir (to feel)", "Caer (to fall)", "Creer (to think)",
                                        "Leer (to read)", "Oir (to hear)", "Destruir (to destroy)"]
                print("This category is Stem Changers\n")
                stem_changer_rand_word = [x for x in range(11)]
                np.random.shuffle(stem_changer_rand_word)
                for i in stem_changer_rand_word:
                    stem_changer_question_loc = stem_changer_rand_word[i]
                    if stem_changer_question_loc == 0:
                        print("Your irregular word is dormir \n")
                        dormir()
                    elif stem_changer_question_loc == 1:
                        print("Your irregular word is morir \n")
                        morir()
                    elif stem_changer_question_loc == 2:
                        print("Your irregular word is pedir \n")
                        pedir()
                    elif stem_changer_question_loc == 3:
                        print("Your irregular verb is preferir \n")
                        preferir()
                    elif stem_changer_question_loc == 4:
                        print("Your irregular verb is seguir \n")
                        seguir()
                    elif stem_changer_question_loc == 5:
                        print("Your irregular verb is sentir \n")
                        sentir()
                    elif stem_changer_question_loc == 6:
                        print("Your irregular verb is caer \n")
                        caer()
                    elif stem_changer_question_loc == 7:
                        print("Your irregular verb is creer \n")
                        creer()
                    elif stem_changer_question_loc == 8:
                        print("Your irregular verb is leer \n")
                        leer()
                    elif stem_changer_question_loc == 9:
                        print("Your irregular verb is oir \n")
                        oir()
                    elif stem_changer_question_loc == 10:
                        print("Your irregular verb is destruir \n")
                        destruir()
                    else:
                        ("stem_changer_question_loc is out of the range between 0-17. Check for any errors in code\n")
                    stop()
                else:
                    print(
                        "Foreign characters other than [ENTER] have been detected or you have completed your study session!\n")
        elif preterite_selection == "4":
            while True:
                rand_rule = [x for x in range(4)]
                np.random.shuffle(rand_rule)
                for i in rand_rule:
                    print(preterite_uses[i])
                    inputVal = input("[SPACE] for continue\n")
                    if inputVal == "":
                        score += 1
                        print("Current Score: ", score)
                        stop()
        elif preterite_selection == "3":
            cgz_irregular_list = cgz_irregular_list = ["Buscar (to search)","Sacar (to take)","Tocar (to play [ex. instrument])", "Jugar (to play [ex. sports])","Llegar (to arrive)","Pagar (to pay)", "Almorzar (to eat lunch)", "Empezar (To start)","Organizar (to organize)"]
            print("This category is Irregular Verbs\n")
            cgz_rand_word = [x for x in range(9)]
            np.random.shuffle(cgz_rand_word)
            for i in cgz_rand_word:
                cgz_question_loc = cgz_rand_word[i]
                cgz_question = cgz_irregular_list[cgz_question_loc]
                if cgz_question_loc == 0:
                    print("Your irregular word is buscar \n")
                    buscar()
                elif cgz_question_loc == 1:
                    print("Your irregular word is sacar \n")
                    sacar()
                elif cgz_question_loc == 2:
                    print("Your irregular word is tocar \n")
                    tocar()
                elif cgz_question_loc == 3:
                    print("Your irregular verb is jugar \n")
                    jugar()
                elif cgz_question_loc == 4:
                    print("Your irregular verb is llegar \n")
                    llegar()
                elif cgz_question_loc == 5:
                    print("Your irregular verb is pagar \n")
                    pagar()
                elif cgz_question_loc == 6:
                    print("Your irregular verb is almorzar \n")
                    almorzar()
                elif cgz_question_loc == 7:
                    print("Your irregular verb is empezar \n")
                    empezar()
                elif cgz_question_loc == 8:
                    print("Your irregular verb is organizar \n")
                    organizar()
                else:
                    ("question_loc is out of the range between 0-9. Check for any errors in code\n")
                stop()
        elif preterite_selection == "5":
            while True:
                signalQuiz()
                stop()
    elif selection == "2":
        solution = input("(1) Signals for imperfect verbs")
        if solution == '1':
            while True:
                imperfectSignalQuiz()
                stop()
        else:
            print("Invalid selection\n")
            sys.exit()
main()
