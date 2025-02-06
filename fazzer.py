import requests

def main():
    file_name = input('Файл с ссылками (адрес относительный):\t')
    url = input('URL для поиска:\t')  # здесь записываете url сайта, на котором будете искать директории
    extensions = input('Введите расширения файлов через запятую (например, .txt,.php):\t').split(',')

    links = []

    # загружаем все ссылки из файла
    with open(file_name, 'rt') as f:
        links = f.readlines()
    
    # Закрываем файл после чтения
    f.close()

    # если ссылок нет, то мы завершаем работу программы
    if len(links) == 0:
        print('Нет ссылок для проверки')
        return

    found_files = []

    for link in links:
        # убираем знак переноса строки в конце каждой ссылки
        link = link.strip()
        
        for link in extensions:
            full_link = f'{url}{link}'  # формируем полную ссылку

            try:
                response = requests.get(full_link)  # получаем ответ от запроса

                if response.status_code != 404:  # если вернувшийся ответ не содержит код 404
                    print(f'{full_link} - существует')  # выводим ссылки, которые нам удалось найти
                    found_files.append(full_link)  # добавляем найденную ссылку в список

            except requests.exceptions.RequestException as e:
                print(f'Ошибка при запросе {full_link}: {e}')

    # записываем найденные файлы в file.txt
    output_file = open('file.txt', 'wt')  # открываем файл для записи
    for found_file in found_files:
        output_file.write(found_file + '\n')

    output_file.close()  # закрываем файл после записи

    print(f'Найденные файлы записаны в file.txt')

if __name__ == "__main__":
    main()
