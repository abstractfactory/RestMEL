![][image]

### RestMEL QML

An example of how QML could be used with RestMEL.

### Usage

1. Download and install Qt 5.3
2. Use `shelfbutton.py` in a shelf-button

 > Specifying the absolute path to the qmlscene executable.

3. Launch RestMEL from within Maya

 ```python
 import restmel.server
 restmel.server.start()
 ```
 
4. Run shelfbutton

#### The Program

The following components make up this demo program.

1. A QML interface
2. A Javascript request via XMLHttpRequest

#### QML

The interface features a textbox and asynchronously loaded image, downloaded from the internet upon launch.

Hitting the button, or accepting the input box, transmits a request to a Maya instance running the RestMEL service.

[image]: https://cloud.githubusercontent.com/assets/2152766/4880162/851fdca8-6337-11e4-9be7-f9d4491bb820.gif