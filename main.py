from flask import Flask

app = Flask(__name__)


@app.route('/')
def name():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def describe():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    words = ["Человечество вырастает из детства.",
             "Человечеству мала одна планета.",
             "Мы сделаем обитаемыми безжизненные пока планеты.",
             "И начнем с Марса!",
             "Присоединяйся!"]
    return "<br>".join(words)

@app.route('/image_mars')
def image():
    return """<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/mars.png" alt="здесь должна была быть картинка, но не нашлась">
                    <h3>Вот она какая, красная планета</h3>
                  </body>
                </html>"""

@app.route('/promotion_image')
def promotion_image():
    words = ["Человечество вырастает из детства.",
             "Человечеству мала одна планета.",
             "Мы сделаем обитаемыми безжизненные пока планеты.",
             "И начнем с Марса!",
             "Присоединяйся!"]
    return """<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" href="static/css/style.css" >
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/mars.png" alt="здесь должна была быть картинка, но не нашлась">
                    <h3>Вот она какая, красная планета</h3>
                    <div class="alert alert-primary" role="alert">
                    <br> "Человечество вырастает из детства."
                    </div>
                    <div class="alert alert-primary" role="alert">
                    <br> "Человечеству мала одна планета."
                    </div>
                    <div class="alert alert-primary" role="alert">
                    <br> "Мы сделаем обитаемыми безжизненные пока планеты."
                    </div>
                    <div class="alert alert-primary" role="alert">
                    <br> "И начнем с Марса!"
                    </div>
                    <div class="alert alert-primary" role="alert">
                    <br> "Присоединяйся!"
                    </div>
                  </body>
                </html>"""


@app.route("/choice/<planet_name>")
def plan_name(planet_name):
    return f"""<!doctype html>
                    <html lang="ru">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Мое предложение: {planet_name}</h1>
                        <h3>Эта планета является идеальным туристическим маршрутом</h3>
                        <div class="alert alert-primary" role="alert">
                        <br> На ней много необходимых ресурсов
                        </div>
                        <div class="alert alert-primary" role="alert">
                        <br> На ней есть вода и атмосфера
                        </div>
                        <div class="alert alert-primary" role="alert">
                        <br> На ней есть небольшое магнитное поле
                        </div>
                        <div class="alert alert-primary" role="alert">
                        <br> Наконец она просто красива!
                        </div>
                        <div class="alert alert-primary" role="alert">
                        <br> Присоединяйся!
                        </div>
                      </body>
                    </html>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f"""<!doctype html>
                    <html lang="ru">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Результаты отбора</h1>
                        <h3>Претендент на участие в миссии, {nickname}:</h3>
                        <div class="alert alert-primary" role="alert">
                            <br> Поздравляем, Ваш рейтинг после {level} этапа отбора:
                        </div>
                        <h3>составляет {rating}!</h3>
                        <div class="alert alert-primary" role="alert">
                        <br> Желаем удачи!
                        </div>
                      </body>
                    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
