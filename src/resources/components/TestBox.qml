import QtQuick 2.8
import QtQuick.Layouts 1.3
import QtQuick.Controls 2.2

import components 1.0

Rectangle {
    id: root
    anchors.fill: parent

    Row {
        id: row
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        anchors.top: parent.top
        anchors.topMargin: 10

        spacing: 10
        
        Rectangle {
            id: testListView
            width:(root.width / 5) * 4
            height: root.height - 20
            border.color: "black"
            border.width: 1
            radius: 5

            Column {
                id: column
                anchors.fill: parent
                padding: 2

                spacing: 10

                Rectangle {
                    id: testArea
                    width: parent.width - 5
                    height: (parent.height / 5) * 4 
                    anchors.horizontalCenter: parent.horizontalCenter
                    radius: 5
                    
                    KakaListView {
                        id: listView

                        internalModel: TestorModel

                        //sresultColor: "black"
                    }                   
                }  

                Rectangle {
                    width: testArea.width
                    height: (parent.height / 5) * 1 - 15
                    anchors.horizontalCenter: parent.horizontalCenter
                    radius: 5

                    Text {
                        id: finalResult
                        text: ""
                        font.pointSize: 28
                    }

                }
            }    
        }

        Button {
            text: "Run Test"

            onClicked: {
                manage.runTest('testcases/test2')
            }
        }
    }

    Connections {
        target: TestorModel

        onRowsInserted: {
            listView.rowChanged();
        }
    }

    Connections {
        target: manage

        onFinalResultSig: {
            finalResult.text = final_result;
            finalResult.color = final_result == 'PASS' ? "Green" : "Red";

        }
    }
}