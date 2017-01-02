import logging

from flask import current_app, Flask

def createapp(config, debug=False, testing=False, config_overrides=None):
    app = Flask(__name__)
    app.config.from_object(config)

    app.debug  = debug
    app.testing = testing

    if config_overrides:
        app.config.update(config_overrides)


    #Configuring the logging

    if not app.testing:
        logging.basicConfig(level=logging.INFO)

    #Setting up the data model
    with app.app_context():
        model = get_model()
        model.init_app(app)

    # TODO: Configure the  app requests

    # Registering the default root and homepage for the app
    @app.route("/")
    def index():
        return redirect(url_for('autocomplete.show_home'))




    return app

def get_model():
    """
    This model is used to connect and interact with the database in this case
    we have opted to using Google Cloud SQL.. But we can connect it with any
    other cloud storage entity

    They are :
    1. Cloud Datastore
    2. Cloud SQL
    3. Mongo DB
    """

    # TODO Add the handlers for the cloudsql and the datastore
    model_backend = current_app.config['DATA_BACKEND']
    if model_backend == 'cloudsql':
        pass
    elif model_backend == 'datastore':
        pass
    else:
        raise ValueError(
            "No appropriate databackend configured."
            "Please specify cloudsql or datastore"
        )

    return model #TODO remember to add model here and complete the configurations
