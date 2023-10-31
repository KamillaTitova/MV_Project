from flask import Flask, render_template, send_from_directory
from folders.selectfolders import blueprint_folders
from sqlalchemy import create_engine

app = Flask(__name__)


app.register_blueprint(blueprint_folders, url_prefix='/folders')

#with open('datta_files/dbconfig.json', 'r') as f:
#    db_config = json.load(f)
#app.config['dbconfig'] = db_config

@app.route("/")
# @app.route("/folders")
def start():
    return render_template('main.html')


@app.route('/public/<path:path>')
def send_report(path):
    return send_from_directory('public', path)


@app.route("/query/")
def get_query_list():
    # зедсь должно быть получение списка экземпляров класса SQLquery
    return """
    <ul>
        <li><a href="/query/1">запрос 1</a></li>
        <li><a href="/query/2">запрос 2</a></li>
    </ul>
    """


@app.route("/query/<id>")
def get_query(id):
    # здесь должно быть полчение модели классс SQLqury и вывод ее в пользователя
    return f"query {id}; вернуться в листинг. <a href=\"/query\">тыц</a>"

if __name__ == '__main__':
    app.run(debug=True)