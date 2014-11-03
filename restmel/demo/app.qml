/* Demo application for creating a cube in Maya through Flask from QML

Usage:
    1. Start server
    2. Start QML application
    3. Create Cube

Requirements:
    Qt 5.3

*/


import QtQuick 2.3
import QtQuick.Controls 1.2
import QtQuick.Window 2.2


ApplicationWindow {
    id: app
    title: "Cube Creator"
    width: 140
    height: 190
    minimumWidth: 140
    minimumHeight: 190
    modality: Qt.WindowModal

    Component.onCompleted: {
        // Center window (for non-Windows platforms)
        app.x = (Screen.width - app.width) / 2
        app.y = (Screen.height - app.height) / 2
    }

    /**
    * Close window after delivery of message
    */
    Timer {
        id: timer
        interval: 500
        running: false
        repeat: false
        onTriggered: Qt.quit();
    }

    /**
    * Cube creator function
    *
    * This function is called whenever the user either
    * presses the button, or hits enter in the inputbox.
    */
    function create () {
        var xhr = new XMLHttpRequest(),
            data = {
                "command": "cmds.polyCube",
                "kwargs": {
                    "name": name.text
                }
            };

        xhr.open("POST", "http://127.0.0.1:6000/command");
        xhr.send(JSON.stringify(data));

        app.visible = false;
        timer.running = true;
    }

    /**
    * Container for window elements
    */
    Item {
        width: 140
        height: parent.height
        anchors.horizontalCenter: parent.horizontalCenter

        /**
        * An arbitrary image of a cube, downloaded from the internets
        */
        Image {
            id: image
            source: "http://img2.wikia.nocookie.net/__cb20120601000828/creepypasta/images/4/40/Coloriage-cube.jpg"
            sourceSize.width: parent.width

            Text {
                id: text
                text: image.status == Image.Ready ? "" : "Loading.."
                font.family: "Verdana"
                font.pointSize: 12
            }
        }

        /**
        * Input box for user to enter a name of the resulting cube
        */
        TextField {
            id: name
            width: parent.width
            placeholderText: "Name of cube.."
            anchors.bottom: button.top
            focus: true
            onAccepted: create();
        }

        /**
        * Master button, this creates the cube, using the
        * name specified in the input box.
        */
        Button {
            id: button
            width: parent.width
            text: "Create"
            anchors.bottom: parent.bottom

            onClicked: create();
                
        }
    }
}
