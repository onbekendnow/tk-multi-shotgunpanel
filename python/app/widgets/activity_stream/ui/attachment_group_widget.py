# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'attachment_group_widget.ui'
#
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_AttachmentGroupWidget(object):
    def setupUi(self, AttachmentGroupWidget):
        AttachmentGroupWidget.setObjectName("AttachmentGroupWidget")
        AttachmentGroupWidget.resize(345, 182)
        self.verticalLayout = QtGui.QVBoxLayout(AttachmentGroupWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.preview_frame = QtGui.QFrame(AttachmentGroupWidget)
        self.preview_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.preview_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.preview_frame.setObjectName("preview_frame")
        self.preview_layout = QtGui.QGridLayout(self.preview_frame)
        self.preview_layout.setContentsMargins(0, 0, 0, 0)
        self.preview_layout.setSpacing(2)
        self.preview_layout.setObjectName("preview_layout")
        self.verticalLayout.addWidget(self.preview_frame)
        self.attachment_frame = QtGui.QFrame(AttachmentGroupWidget)
        self.attachment_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.attachment_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.attachment_frame.setObjectName("attachment_frame")
        self.attachment_layout = QtGui.QVBoxLayout(self.attachment_frame)
        self.attachment_layout.setContentsMargins(2, 2, 2, 2)
        self.attachment_layout.setObjectName("attachment_layout")
        self.verticalLayout.addWidget(self.attachment_frame)

        self.retranslateUi(AttachmentGroupWidget)
        QtCore.QMetaObject.connectSlotsByName(AttachmentGroupWidget)

    def retranslateUi(self, AttachmentGroupWidget):
        AttachmentGroupWidget.setWindowTitle(QtGui.QApplication.translate("AttachmentGroupWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
from . import resources_rc
