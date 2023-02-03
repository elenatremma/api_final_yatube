# API_YaTube_FINAL

<i>Реализация API для моделей приложения Posts проекта YaTube.</i> 

<i><b>Функционал</i></b>
<blockquote>
☑ API реализован для моделей приложения posts: User, Post, Group, Comment, Follow; <br>
☑ Аутентификация пользователей по методу JWT-Authentication через Djoser; <br>
☑ UnSafe  методы доступны  для авторов постов/комментариев, а также для подписчиков на авторов;  <br>
☑ Safe методы доступны  для всех пользователей эндпоинтов posts, groups, comments. <br> 
☑ Доступ к эндпоинту follow предоставляется только аутентифицированным пользователям. <br> 
</blockquote>

<i><b>Технологии</i></b>
<blockquote>
☑ Python 3.7.0 <br> 
☑ Django REST framework
</blockquote>

<i><b>Запуск проекта в dev-режиме:</i></b><br> 
☑ Клонируйте проект с GitHub:</li>
    <blockquote>
      git@github.com:elenatremma/api_final_yatube.git
    </blockquote>  
☑ Создайте и активируйте виртуальное окружение:</li>
    <blockquote>
      python -m venv venv<br> 
      source venv/Scripts/activate 
    </blockquote>  
☑ Установите зависимости из файла requirements.txt (не забудьте предварительно обновить pip!):</li>
    <blockquote>
      pip install -r requirements.txt
    </blockquote>
☑ Создавайте посты, комментарии к ним, подписывайтесь на авторов постов через Postman или другие инструментарии для тестирования API.</li>

<i><b>Просматривайте динамическую документацию бэкэнда вместе с примерами запросов через redoc/swagger (напр., http://127.0.0.1:8000/redoc/)</i></b><br> 
 ![tg_bot](https://user-images.githubusercontent.com/104749444/216548474-a4404f08-c639-4324-85b4-3f5bda43feb1.jpg)


Автор: Елена Трембовельская 
