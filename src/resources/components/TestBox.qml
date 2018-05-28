import QtQuick 2.8
import QtQuick.Layouts 1.3
import QtQuick.Controls 2.2

import components 1.0

Rectangle {
    id: root
    anchors.fill: parent

    Row {
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: parent.top
        anchors.topMargin: 30

        spacing: 10
        
        Rectangle {
            id: testListView
            width:(root.width / 5) * 4
            height: root.height - 60
            border.color: "black"
            border.width: 1
            radius: 5

            Rectangle {
                width: parent.width - 5
                height: parent.height - 5
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.verticalCenter: parent.verticalCenter

                KakaListView {
                    id: listView

                    internalModel: TestorModel
                }
            }
        }

        Button {
            text: "Run Test"

            onClicked: {
                manage.runTest('testcases/test1')
            }
        }
    }

    Connections {
        target: TestorModel

        onRowsInserted: {
            listView.rowChanged();
        }
    }
}