import flask
import os
import random
import yaml

parameters = dict(
    KITTEN_MIN_WIDTH=200,
    KITTEN_MAX_WIDTH=400,
    KITTEN_MIN_HEIGHT=200,
    KITTEN_MAX_HEIGHT=400,
)

config_file = os.environ.get("KITTEN_CONFIG")
if config_file:
    print("Loading configuration file {}.".format(config_file))
    config = yaml.safe_load(open(config_file))
else:
    print("No configuration file.")
    config = {}

for parameter in parameters:
    if parameter in config:
        print(
            "Parameter {} found in configuration file, value: {}.".format(
                parameter, config[parameter]
            )
        )
        config[parameter] = int(config[parameter])
    else:
        print("Parameter {} not found in configuration file.".format(parameter))
        if parameter in os.environ:
            print(
                "Parameter {} found in environment variables, value: {}.",
                format(parameter, os.environ[parameter]),
            )
            config[parameter] = int(os.environ[parameter])
        else:
            print("Parameter {} not found in environment variables.".format(parameter))
            print("Using default value ({}).".format(parameters[parameter]))
            config[parameter] = parameters[parameter]


app = flask.Flask(__name__)


@app.route("/")
def servekitten():
    w = random.randint(config["KITTEN_MIN_WIDTH"], config["KITTEN_MAX_WIDTH"])
    h = random.randint(config["KITTEN_MIN_HEIGHT"], config["KITTEN_MAX_HEIGHT"])
    img = "https://placekitten.com/{}/{}".format(w, h)
    return '<html><body><img src="{}"></body></html>'.format(img)
