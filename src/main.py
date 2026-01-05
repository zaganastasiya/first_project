print('Hello from repository!')

# Импорт load_dotenv.
from dotenv import load_dotenv 

# Импорт библиотеки для работы с окружением.
import os  

# Загрузка переменных из .env
load_dotenv(dotenv_path='/Users/anastasiyazagaynova/Desktop/Яндекс Практикум/Data Science/Python_теория/Инструменты разработки/my_project/.env')

def print_author():
    author = os.getenv('AUTHOR')
    print(f"Автор проекта: {author}")

print_author()