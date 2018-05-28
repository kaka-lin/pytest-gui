from PyQt5.QtCore import Qt, QAbstractListModel, QModelIndex, QVariant, pyqtSlot

class ModelData(object):
    def __init__(self, item, data):
        self._item = item
        self._data = data

    def item(self):
        return self._item

    def data(self):
        return self._data

class Model(QAbstractListModel):
    """ Kaka Model """
    ItemRole = Qt.UserRole + 1
    DataRole = Qt.UserRole + 2

    _roles = { ItemRole: b'item', DataRole: b'data' }

    def __init__(self, parent=None):
        super(Model, self).__init__(parent)

        self._datas = []

    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():
            print("This shouldn't happen")

        return len(self._datas)

    def data(self, index, role=Qt.DisplayRole):
        try:
            model_data = self._datas[index.row()]
        except IndexError:
            return QVariant()

        if role == self.ItemRole:
            return model_data.item()

        if role == self.DataRole:
            return model_data.data()

        return QVariant()

    def roleNames(self):
        return self._roles

    @pyqtSlot(str, str)
    def addData(self, item, data):
        model_data = ModelData(item, data)
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._datas.append(model_data)
        self.endInsertRows()
