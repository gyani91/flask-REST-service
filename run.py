from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig, TestingConfig, ProductionConfig
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import os


def create_app(config_type="dev"):
    if config_type == "dev":
        configuration = DevelopmentConfig
        print("Using development config")
    elif config_type == "test":
        configuration = TestingConfig
        print("Using testing config")
    elif config_type == "prod":
        configuration = ProductionConfig
        print("Using production config")
    else:
        raise ValueError("Invalid config type:", config_type)

    app = Flask(__name__)
    app.config.from_object(configuration)
    db = SQLAlchemy(app)

    migrate = Migrate(app, db)
    manager = Manager(app)

    manager.add_command("db", MigrateCommand)

    return app, manager, db


config_type_ = os.environ["CONFIG_TYPE"]
app, manager, db = create_app(config_type=config_type_)


@app.route("/")
def test():
    return "test"


@app.route("/ping", methods=["GET"])
def ping_pong():
    return jsonify({"status": "Epic success", "message": "pong!"})


if __name__ == "__main__":
    manager.run()
