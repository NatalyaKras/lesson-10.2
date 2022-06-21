from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__, template_folder="pages")



# Открываем Json Файл
with open('candidates.json', encoding='utf-8') as json_file:
    data = json.load(json_file)
    # Выводим тип
print(data)




#step_1
@app.route('/')
def main():
    """
    Шаг 1 - Вывод всех сотрудников
    :return: возвращает всех сотрудников
    """
    return_list = []
    for i in data:

        return_list.append(f'''
      Имя кандидата - {i['name']}<br>
      Позиция кандидата - {i['position']}<br>
      Навыки через запятую - {i['skills']}<br>
           <br>
    ''')


    return ''.join(return_list)


# step_2
@app.route('/candidates/<x>')
def check_for_one(x):
    """
    Шаг 2 - Вывод сотрудника по номеру
    :return: возвращает одного сотрудника
    """
    return_list = []
    x = int(x)
    return_list.append(f'''
      <img src="{data[x]['picture']}"> <br>

      Имя кандидата - {data[x]['name']}<br>
      Позиция кандидата - {data[x]['position']}<br>
      Навыки через запятую - {data[x]['skills']}<br>
        <br>
    ''')

    return ''.join(return_list)

# step_3
@app.route('/skills/<x>')
def check_for_skills(x):
    """
    Шаг 3 - Вывод всех сотрудников по навыкам
    :return: возвращает всех сотрудников с навыками
    """

    return_list = []
    for i in data:

        if x in i['skills'].split(', '):
            return_list.append(f'''
          Имя кандидата - {i['name']}<br>
          Позиция кандидата - {i['position']}<br>
          Навыки через запятую - {i['skills']}<br>
            <br>
            ''')

    return ''.join(return_list)

if __name__ == "__main__":
    app.secret_key = 'key'
    app.run()