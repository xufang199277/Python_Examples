#!/usr/bin/python
# _*_ coding: utf-8 _*_
# Function: 使用PyQt4模块画界面-查看窗口位置信息
# Author: xufang

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class Geometry(QDialog):

    def __init__(self,parent=None):
        super(Geometry,self).__init__(parent)
        self.setWindowTitle("Geometry")
        Label1=QLabel("x0:")
        Label2=QLabel("y0:")
        Label3=QLabel("frameGeometry():")
        Label4=QLabel("pos():")
        Label5=QLabel("geometry():")
        Label6=QLabel("width():")
        Label7=QLabel("height():")
        Label8=QLabel("rect():")
        Label9=QLabel("size():")
        self.xLabel=QLabel()
        self.yLabel=QLabel()
        self.frameGeoLabel=QLabel()
        self.posLabel=QLabel()
        self.geoLabel=QLabel()
        self.widthLabel=QLabel()
        self.heightLabel=QLabel()
        self.rectLabel=QLabel()
        self.sizeLabel=QLabel()

        layout=QGridLayout()
        layout.addWidget(Label1,0,0)
        layout.addWidget(self.xLabel,0,1)
        layout.addWidget(Label2,1,0)
        layout.addWidget(self.yLabel,1,1)
        layout.addWidget(Label3,2,0)
        layout.addWidget(self.frameGeoLabel,2,1)
        layout.addWidget(Label4,3,0)
        layout.addWidget(self.posLabel,3,1)
        layout.addWidget(Label5,4,0)
        layout.addWidget(self.geoLabel,4,1)
        layout.addWidget(Label6,5,0)
        layout.addWidget(self.widthLabel,5,1)
        layout.addWidget(Label7,6,0)
        layout.addWidget(self.heightLabel,6,1)
        layout.addWidget(Label8,7,0)
        layout.addWidget(self.rectLabel,7,1)
        layout.addWidget(Label9,8,0)
        layout.addWidget(self.sizeLabel,8,1)
        self.setLayout(layout)
        self.updateLabel()

    def moveEvent(self,event):
        self.updateLabel()

    def resizeEvent(self,event):
        self.updateLabel()

    def updateLabel(self):
        temp=QString()
        self.xLabel.setText(temp.setNum(self.x()))
        self.yLabel.setText(temp.setNum(self.y()))
        self.frameGeoLabel.setText(temp.setNum(self.frameGeometry().x())+","+
                                    temp.setNum(self.frameGeometry().y())+","+
                                    temp.setNum(self.frameGeometry().width())+","+
                                    temp.setNum(self.frameGeometry().height()))
        self.posLabel.setText(temp.setNum(self.pos().x())+","+
                            temp.setNum(self.pos().y()))
        self.geoLabel.setText(temp.setNum(self.geometry().x())+","+
                             temp.setNum(self.geometry().y())+","+
                             temp.setNum(self.geometry().width())+","+
                             temp.setNum(self.geometry().height()))
        self.widthLabel.setText(temp.setNum(self.width()))
        self.heightLabel.setText(temp.setNum(self.height()))
        self.rectLabel.setText(temp.setNum(self.rect().x())+","+
                                temp.setNum(self.rect().y())+","+
                                temp.setNum(self.rect().width())+","+
	                            temp.setNum(self.rect().height()))

        self.sizeLabel.setText(temp.setNum(self.size().width())+","+
                               temp.setNum(self.size().height()))
app=QApplication(sys.argv)
form=Geometry()
form.show()
app.exec_()


# """
# A PyQT4 dialog to confirm and set options for auto-tag
# """
#
# """
# Copyright 2012-2014  Anthony Beville
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# """
#
# from PyQt4 import QtCore, QtGui, uic
# from settings import ComicTaggerSettings
# from settingswindow import SettingsWindow
# from filerenamer import FileRenamer
# import os
# import utils
#
#
# class AutoTagStartWindow(QtGui.QDialog):
#     def __init__(self, parent, settings, msg):
#         super(AutoTagStartWindow, self).__init__(parent)
#
#         uic.loadUi(ComicTaggerSettings.getUIFile('autotagstartwindow.ui'), self)
#         self.label.setText(msg)
#
#         self.setWindowFlags(self.windowFlags() &
#                             ~QtCore.Qt.WindowContextHelpButtonHint)
#
#         self.settings = settings
#
#         self.cbxSaveOnLowConfidence.setCheckState(QtCore.Qt.Unchecked)
#         self.cbxDontUseYear.setCheckState(QtCore.Qt.Unchecked)
#         self.cbxAssumeIssueOne.setCheckState(QtCore.Qt.Unchecked)
#         self.cbxIgnoreLeadingDigitsInFilename.setCheckState(QtCore.Qt.Unchecked)
#         self.cbxRemoveAfterSuccess.setCheckState(QtCore.Qt.Unchecked)
#         self.cbxSpecifySearchString.setCheckState(QtCore.Qt.Unchecked)
#         self.leNameLengthMatchTolerance.setText(str(self.settings.id_length_delta_thresh))
#         self.leSearchString.setEnabled(False)
#
#         if self.settings.save_on_low_confidence:
#             self.cbxSaveOnLowConfidence.setCheckState(QtCore.Qt.Checked)
#         if self.settings.dont_use_year_when_identifying:
#             self.cbxDontUseYear.setCheckState(QtCore.Qt.Checked)
#         if self.settings.assume_1_if_no_issue_num:
#             self.cbxAssumeIssueOne.setCheckState(QtCore.Qt.Checked)
#         if self.settings.ignore_leading_numbers_in_filename:
#             self.cbxIgnoreLeadingDigitsInFilename.setCheckState(QtCore.Qt.Checked)
#         if self.settings.remove_archive_after_successful_match:
#             self.cbxRemoveAfterSuccess.setCheckState(QtCore.Qt.Checked)
#         if self.settings.wait_and_retry_on_rate_limit:
#             self.cbxWaitForRateLimit.setCheckState(QtCore.Qt.Checked)
#
#         nlmtTip = (
#             """ <html>The <b>Name Length Match Tolerance</b> is for eliminating automatic
#                 search matches that are too long compared to your series name search. The higher
#                 it is, the more likely to have a good match, but each search will take longer and
#                 use more bandwidth. Too low, and only the very closest lexical matches will be
#                 explored.</html>""")
#
#         self.leNameLengthMatchTolerance.setToolTip(nlmtTip)
#
#         ssTip = (
#             """<html>
#             The <b>series search string</b> specifies the search string to be used for all selected archives.
#             Use this when trying to match archives with hard-to-parse or incorrect filenames.  All archives selected
#             should be from the same series.
#             </html>"""
#         )
#         self.leSearchString.setToolTip(ssTip)
#         self.cbxSpecifySearchString.setToolTip(ssTip)
#
#         validator = QtGui.QIntValidator(0, 99, self)
#         self.leNameLengthMatchTolerance.setValidator(validator)
#
#         self.cbxSpecifySearchString.stateChanged.connect(self.searchStringToggle)
#
#         self.autoSaveOnLow = False
#         self.dontUseYear = False
#         self.assumeIssueOne = False
#         self.ignoreLeadingDigitsInFilename = False
#         self.removeAfterSuccess = False
#         self.waitAndRetryOnRateLimit = False
#         self.searchString = None
#         self.nameLengthMatchTolerance = self.settings.id_length_delta_thresh
#
#     def searchStringToggle(self):
#         enable = self.cbxSpecifySearchString.isChecked()
#         self.leSearchString.setEnabled(enable)
#
#     def accept(self):
#         QtGui.QDialog.accept(self)
#
#         self.autoSaveOnLow = self.cbxSaveOnLowConfidence.isChecked()
#         self.dontUseYear = self.cbxDontUseYear.isChecked()
#         self.assumeIssueOne = self.cbxAssumeIssueOne.isChecked()
#         self.ignoreLeadingDigitsInFilename = self.cbxIgnoreLeadingDigitsInFilename.isChecked()
#         self.removeAfterSuccess = self.cbxRemoveAfterSuccess.isChecked()
#         self.nameLengthMatchTolerance = int(self.leNameLengthMatchTolerance.text())
#         self.waitAndRetryOnRateLimit = self.cbxWaitForRateLimit.isChecked()
#
#         # persist some settings
#         self.settings.save_on_low_confidence = self.autoSaveOnLow
#         self.settings.dont_use_year_when_identifying = self.dontUseYear
#         self.settings.assume_1_if_no_issue_num = self.assumeIssueOne
#         self.settings.ignore_leading_numbers_in_filename = self.ignoreLeadingDigitsInFilename
#         self.settings.remove_archive_after_successful_match = self.removeAfterSuccess
#         self.settings.wait_and_retry_on_rate_limit = self.waitAndRetryOnRateLimit
#
#         if self.cbxSpecifySearchString.isChecked():
#             self.searchString = unicode(self.leSearchString.text())
#             if len(self.searchString) == 0:
#                 self.searchString = None
#
#
