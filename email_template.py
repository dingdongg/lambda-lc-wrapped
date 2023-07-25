from jinja2 import Environment, FileSystemLoader, select_autoescape

def load_email():
    jinja_env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=select_autoescape(), 
    )

    template = jinja_env.get_template("email.html.jinja")

    return template