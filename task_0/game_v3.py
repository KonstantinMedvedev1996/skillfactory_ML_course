"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 1
    predict_number_low =1 # нижняя граница предсказания
    predict_number_high = 101 # верхняя граница
    predict_number = int((predict_number_high-predict_number_low)/2) #загаданное число


    while number != predict_number:
        count+=1
        if number > predict_number:
            predict_number_low = predict_number
            predict_number = int((predict_number_high-predict_number_low)/2+predict_number_low)
        elif number < predict_number:
            predict_number_high = predict_number
            predict_number = int((predict_number_high-predict_number_low)/2+predict_number_low)
    return count
            


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за : {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
