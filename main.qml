import QtQuick 2.5
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4
import QtQuick.Layouts 1.2
import Qt.labs.folderlistmodel 1.0
import QtQuick.XmlListModel 2.0
import Qt.labs.folderlistmodel 2.1


ApplicationWindow {
    visible: true
    width: 612
    height: 620
    title: qsTr("Магазин")
    color: "#f5f5f5"

    menuBar: MenuBar {
        Menu {
            title: "File"
            MenuItem { text: "Open..."
                        shortcut: "Ctrl+O"
                        onTriggered: {
                                fileDialog.selectExisting = true
                                fileDialog.open()
                                        }
                        }

            MenuItem { text: "Close"
                        shortcut: "Ctrl+W"
                        onTriggered:  Qt.quit()
                        }
            MenuItem { text: "Save"
                        shortcut: "Ctrl+S"
                        }

            MenuItem { text: "Save as..."
                        shortcut: "Shift+Ctrl+S"
                            onTriggered: {
                                fileDialog.selectExisting = false
                                fileDialog.open()
                                        }
                        }
            }

        Menu {
            title: "Edit"
            MenuItem { text: "Cut"
                        shortcut: "Ctrl+X"
                        onTriggered:  activeFocusItem.cut()
                        }
            MenuItem { text: "Copy"
                        shortcut: "Ctrl+C"
                        onTriggered:  activeFocusItem.copy()
                        }
            MenuItem { text: "Paste"
                        shortcut: "Ctrl+V"
                        onTriggered:  activeFocusItem.paste()
                        }

        }
    }

TabView {
        id: tabView
        anchors.top: parent.top
        anchors.topMargin: 0
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.bottom: parent.bottom


        Tab {
            id: tab1
            title: qsTr("Client")
            GridLayout  {
                Rectangle   {
                    width: 602
                    height: 150
                    anchors.top: parent.top
                    anchors.topMargin: 5
                    anchors.horizontalCenter: parent.horizontalCenter

                ListModel {
                    dynamicRoles: true
                }


            TableView {
            id: FullName
            anchors.margins: 0
            anchors.fill: parent
            model: dataModel


        TableViewColumn {
            width: 150
            title: "surname"
            role: "surname"
            }
        TableViewColumn {
            width: 150
            title: "Address"
            role: "client_attributes"
            }
        TableViewColumn {
            width: 150
            title: "Phone"
            role: "filePhone"
            }
        TableViewColumn {
            width: 150
            title: "Email"
            role: "gui"
            }
            }
        }
            }}

        Tab {
            id: tab2
            title: qsTr("Product")
            Text{
            anchors.fill: parent
            text:  obj.text
                }

        }
        Tab {
            id: tab3
            title: qsTr("Sale")
        }

    }
}



