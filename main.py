import function_work_html_ratio
import os
def main():
    for i in range(1,6):
        os.makedirs("dataset/"+str(i)) # для каждой звезды
        print('Ищем отзывы для звезды '+str(i))
        function_work_html_ratio.function_work_html_ratio(i)


if __name__=='__main__':
    main()