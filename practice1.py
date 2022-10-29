"""
ایمان ترم پیش تی اس درسی شده بود و برای خاص جلوه دادن این درس نمرات را به صورت توصیفی اعلام کرده بود متاسفانه
در پابان ترم متوجه شد که نمی تواند به صورت توصیفی معدل داننشجویان را حساب کند .
دانشجویان هم بسیار عصبانی هستند که نمرات ترم پیسسان هنوز مشحص نشده در نتیجه ایمان
به سراغ شما آمده تا مشکل او را حل کنید!
او میداند که نمرات امتحانات به صورت زیر هستند:

Iman was a lesson before TS and to make this lesson special, he announced the grades in a descriptive manner, unfortunately.
At the end of the semester, he realized that he could not calculate the GPA of the students descriptively.
The students are also very angry that the Pisan semester grades have not yet been determined as a result of Iman
He came to you to solve his problem!
He knows that the exam scores are as follows:

A = 5, b = 4, c = 3, D = 2,  = 1, F = 0
"""

"""
ورودی :
ورودی شامل یک عدد n است گه برابر تعداد امتحانی است گه هر دانشجو شرکت کرده و پس از آن در خط بعد 
اول وزن آن امتحان و سپس بعداز یک فاصله نمره ی آن امتحان آمده است 

Entrance :
The input contains a number n, which is equal to the number of exams that each student took, and then in the next line
First, the weight of that exam and then, after a gap, the score of that exam
"""

"""
خروجی:
شما باید میانگین را به صورت یک کاراکتر بین a تا f جاپ کنید.(برای مثال برای میانگین های بزرگتر از 4 کاراکتر a چاپ می شود.)


Output:
You have to jump the average as a character between a and f. (for example, for averages greater than 4 characters a is printed.)


"""

import  math


def main():
   number =  pares_number_of_scores()
   weight_scores = parse_weight_score(number)
   numeric_score = compute_score(weight_scores)
   result = to_ch(math.ceil(numeric_score))
   return  result


def pares_number_of_scores():
    number = input()
    return int(number)


def parse_weight_score(number):
    weight_scores = []
    for i in range(number):
        weight, score = input().split()
        weight = int(weight)
        weight_scores.append((weight, score))

    return  weight_scores

def compute_score(weight_scores):
    sum_ = 0
    total_weghts = 0
    for weight, score in weight_scores:
        sum_ += weight * to_numeral(score)
        total_weghts += weight
    numeric_score = sum_ / total_weghts
    return  numeric_score


def to_numeral(ch_score):
    scores = {"A":5, "B":4, "C":3, "D":2, "E":1, "F":0}
    return  scores[ch_score]


def to_ch(num_score):
    scores = {5:'A', 4:'B', 3:'C', 2:'D' ,1:'E',  0:'F'}
    return  scores[num_score]



if __name__ == '__main__':
    print(main())
