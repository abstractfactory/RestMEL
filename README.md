# RESTMel

A RESTful interface for Maya.

The idea is to facilitate external control of Maya via standard REST commands for tools and user interfaces that operate outside the confines of the Maya GUI; such as Web Applications or QML interfaces.

# Documentation

### Root Endpoint

Issue a GET request to the root endpoint to get a list of available endpoints supported by the API

```bash
GET http://x.x.x.x:port
```

###### Supported endpoints

| Endpoint     | Description
|--------------|--------------
| /node        | GET, POST, PUT and DELETE nodes
| /command     | POST command(s) to execute from within Maya
| /polygon     | GET information about polygonal data

###### Examples

```bash
$ # Retrieve list of all available nodes
$ curl -X GET http://x.x.x.x:port/node
$ # Create a new node
$ curl -X POST http://x.x.x.x:port/node -d "{'type': 'mesh', 'name': 'MyMesh'}"
$ # Execute arbitrary command
$ curl -X POST http://x.x.x.x:port/command -d "{'module': 'cmds', 'command': 'polyCube', 'kwargs': {'name': 'MyMesh'}}"
```


### Client Errors

Errors are returned as JSON with a single "message" field.

```bash
HTTP/1.1 400 Bad Request
 Content-Length: 35

 {"message":"Problems parsing JSON"}
```

### HTTP Verbs

| Verb     | Description      |
|----------|------------------|
| GET      | Used for retrieving resources
| POST     | Used for creating resources, or performing custom actions
| PUT      | Used for replacing resources or collections
| DELETE   | Used for deleting resources
