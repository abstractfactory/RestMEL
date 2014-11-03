"""RESTful endpoints available in Maya

/node       (GET, POST)
/command    (POST)

"""

# Standard library
import json

# Dependencies
import flask.ext.restful

# Local library
import wrapper


def loads(data):
    """Load JSON as string instead of unicode objects

    Arguments:
        data (str): String of JSON data

    """

    return convert(json.loads(data))


def convert(input):
    """Cast input to string

    Arguments:
        input (object): Dict, list or unicode object to be converted

    """

    if isinstance(input, dict):
        return dict((convert(k), convert(v)) for k, v in input.iteritems())
    elif isinstance(input, list):
        return [convert(e) for e in input]
    elif isinstance(input, unicode):
        return input.encode("utf-8")
    else:
        return input


class Node(flask.ext.restful.Resource):
    """Node manipulation API"""
    def get(self):
        """List all nodes"""
        return wrapper.cmds.ls()

    def post(self):
        """Create node

        Incoming:
            /node -d {"type": "mesh", **kwargs}
        """

        data_str = flask.request.stream.read()
        data_json = loads(data_str)

        typ = data_json.pop("type", "transform")
        kwargs = data_json  # Remaining arguments are for createNode

        try:
            return wrapper.cmds.createNode(typ, **kwargs)
        except Exception as e:
            return str(e)


class Command(flask.ext.restful.Resource):
    """Run a command via maya.cmds"""
    def post(self):
        data_str = flask.request.stream.read()
        data_json = loads(data_str)

        command = data_json.get("command") or None
        if command is None:
            return {"message": "Must provide a command"}

        try:
            module, attribute = command.split(".")
        except ValueError:
            module, attribute = "cmds", command

        args = data_json.get("args") or list()
        kwargs = data_json.get("kwargs") or dict()

        try:
            _mod = getattr(wrapper, module)
            getattr(_mod, attribute)(*args, **kwargs)
            return {"message": True}
        except Exception as e:
            return {"message": str(e)}
