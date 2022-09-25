import function_work_html_ratio
def main():
    for i in range(1,5):  # для каждой звезды
        print('Ищем отзывы для звезды '+str(i))
        function_work_html_ratio.function_work_html_ratio(i)


if __name__=='__main__':
    main()