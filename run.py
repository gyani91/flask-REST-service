from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_marshmallow import Marshmallow
from config import DevelopmentConfig, TestingConfig, ProductionConfig
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from sqlalchemy import Column, Integer, String
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

    ma = Marshmallow(app)

    api = Api(app)

    return app, manager, ma, api, db


config_type_ = os.environ["CONFIG_TYPE"]
app, manager, ma, api, db = create_app(config_type=config_type_)

class Document(db.Model):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String, nullable=False)
    summary = Column(String)

    def __repr__(self):
        return '<Document %s>' % self.uuid

class DocumentSchema(ma.Schema):
    class Meta:
        fields = ("id", "text")
        model = Document

class SummarySchema(ma.Schema):
    class Meta:
        fields = ("id", "summary")
        model = Document


document_schema = DocumentSchema()
summary_schema = SummarySchema()


class DocumentListResource(Resource):
    def post(self):
        new_document = Document(
            text=request.json['text'],
            summary=request.json['text'],
        )
        db.session.add(new_document)
        db.session.commit()
        return new_document.id

class DocumentResource(Resource):
    def get(self, document_id):
        document = Document.query.get_or_404(document_id)
        return document_schema.dump(document)

    def patch(self, post_id):
        document = Document.query.get_or_404(post_id)

        if 'text' in request.json:
            document.text = request.json['text']
        if 'summary' in request.json:
            document.summary = request.json['summary']

        db.session.commit()
        return document_schema.dump(document)

    def delete(self, post_id):
        document = Document.query.get_or_404(post_id)
        db.session.delete(document)
        db.session.commit()
        return '', 204

class SummaryResource(Resource):
    def get(self, document_id):
        document = Document.query.get_or_404(document_id)
        return summary_schema.dump(document)


api.add_resource(DocumentListResource, '/documents')
api.add_resource(DocumentResource, '/documents/<int:document_id>')
api.add_resource(SummaryResource, '/summary/<int:document_id>')


@app.route("/")
def test():
    return "test"


@app.route('/greet')
def say_hello():
    return 'Hello from Server'


if __name__ == "__main__":
    manager.run()
