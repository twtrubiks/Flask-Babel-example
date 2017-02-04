#coding=utf-8
from flask import *
from flask_babel import *

app = Flask(__name__)
app.config.from_pyfile('settings.cfg')
babel = Babel(app)


@babel.localeselector
def get_locale():
    # if a user is logged in, use the locale from the user settings
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    # otherwise try to guess the language from the user accept
    # header the browser transmits.  We support de/fr/en in this
    # example.  The best match wins.
    return request.accept_languages.best_match(['zh', 'en', 'ja'])


@babel.timezoneselector
def get_timezone():
    user = getattr(g, 'user', None)
    if user is not None:
        return user.timezone


@app.route('/')
def index():
    current_language = request.accept_languages.best
    title = gettext("title")
    sub_title = gettext("sub_title")
    translation = gettext("translation")
    country = gettext("country")
    Taiwan = gettext("Taiwan")
    Japan = gettext("japan")
    US = gettext("US")
    test = gettext("<b>我會變亂碼</b>")
    return render_template("index.html", **locals())


if __name__ == '__main__':
    app.run(debug=True)
