import os
import sys
import torch
from detect import run
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget, QApplication, QLabel, QFrame
from PyQt5.QtGui import QIcon, QPixmap, QFont, QPalette, QBrush
import _thread
from PyQt5.QtCore import Qt





if torch.cuda.is_available():
    dev = '0'
else:
    dev = 'cpu'
run_dict = {
    'weights': 'kid.pt',
    'source': 0,
    'imgsz': [640, 640],
    'conf_thres': 0.60,
    'iou_thres': 0.40,
    'max_det': 10,
    'device': dev,
    'view_img': False,
    'save_txt': False,
    'save_conf': False,
    'save_crop': False,
    'nosave': False,
    'classes': None,
    'agnostic_nms': False,
    'augment': False,
    'visualize': False,
    'update': False,
    'project': 'runs/detect',
    'name': 'exp',
    'exist_ok': False,
    'line_thickness': 3,
    'hide_labels': False,
    'hide_conf': False,
    'half': False,
}

run_dict_file = {
    'weights': 'kid.pt',
    'source': 'data/images',
    'imgsz': [640, 640],
    'conf_thres': 0.60,
    'iou_thres': 0.40,
    'max_det': 10,
    'device': dev,
    'view_img': False,
    'save_txt': False,
    'save_conf': False,
    'save_crop': False,
    'nosave': False,
    'classes': None,
    'agnostic_nms': False,
    'augment': False,
    'visualize': False,
    'update': False,
    'project': 'runs/detect',
    'name': 'exp',
    'exist_ok': False,
    'line_thickness': 3,
    'hide_labels': False,
    'hide_conf': False,
    'half': False,
}


class WindowClass(QWidget):

    def __init__(self, parent=None):

        super(WindowClass, self).__init__(parent)
        self.setWindowTitle('口罩佩戴检测')
        self.setWindowIcon(QIcon('ico.jpg'))
        self.btn_1 = QPushButton("从摄像头开始")
        self.btn_2 = QPushButton("从文件开始")
        self.btn_3 = QPushButton("显示结果")
        self.btn_4 = QPushButton("退出")

        self.btn_1.setCheckable(True)
        self.btn_1.toggle()

        self.btn_1.clicked.connect(lambda: self.wichBtn(self.btn_1))
        self.btn_2.clicked.connect(lambda: self.wichBtn(self.btn_2))
        self.btn_3.clicked.connect(lambda: self.wichBtn(self.btn_3))
        self.btn_4.clicked.connect(lambda: self.wichBtn(self.btn_4))

        self.resize(300, 300)
        layout = QVBoxLayout()
        layout.addWidget(self.btn_1)
        layout.addWidget(self.btn_2)
        layout.addWidget(self.btn_3)
        layout.addWidget(self.btn_4)

        self.setLayout(layout)

    def wichBtn(self, btn):
        print("点击的按钮是：", btn.text())
        if btn.text() == '退出':
            sys.exit()
        if btn.text() == '从摄像头开始':
            try:
                _thread.start_new_thread(run(**run_dict), ("Thread-1", 2,))
            except:
                print("子进程退出")
        if btn.text() == '显示结果':
            path = os.getcwd() + r'\runs\detect'
            os.system("start explorer %s" % path)
        if btn.text() == '从文件开始':
            run(**run_dict_file)

# class WindowClass(QWidget):
#     def __init__(self, parent=None):
#         super(WindowClass, self).__init__(parent)
#
#         # 设置窗口标题和图标
#         self.setWindowTitle("口罩佩戴检测系统")
#         self.setWindowIcon(QIcon("ico.jpg"))
#
#         # 设置整体样式
#         self.setStyleSheet("background-color: #2C3E50; color: white;")
#
#         # 初始化组件
#         self.title_label = QLabel("口罩佩戴检测系统")
#         self.title_label.setAlignment(Qt.AlignCenter)
#         self.title_label.setFont(QFont("华文黑体", 26, QFont.Bold))
#         self.title_label.setStyleSheet("color: #1ABC9C; margin-bottom: 20px;")
#
#         self.subtitle_label = QLabel("请选择操作")
#         self.subtitle_label.setAlignment(Qt.AlignCenter)
#         self.subtitle_label.setFont(QFont("微软雅黑", 14))
#         self.subtitle_label.setStyleSheet("color: #ECF0F1; margin-bottom: 30px;")
#
#         self.btn_camera = QPushButton("从摄像头检测")
#         self.btn_file = QPushButton("从文件检测")
#         self.btn_result = QPushButton("查看检测结果")
#         self.btn_exit = QPushButton("退出系统")
#
#         # 设置按钮样式
#         self._style_buttons([self.btn_camera, self.btn_file, self.btn_result, self.btn_exit])
#
#         # 绑定按钮点击事件
#         self.btn_camera.clicked.connect(lambda: self.whichBtn(self.btn_camera))
#         self.btn_file.clicked.connect(lambda: self.whichBtn(self.btn_file))
#         self.btn_result.clicked.connect(lambda: self.whichBtn(self.btn_result))
#         self.btn_exit.clicked.connect(lambda: self.whichBtn(self.btn_exit))
#
#         # 设置布局
#         self._setup_layout()
#
#     def _style_buttons(self, buttons):
#         """设置按钮样式"""
#         button_style = """
#         QPushButton {
#             font-size: 18px;
#             font-family: '微软雅黑';
#             font-weight: bold;
#             color: white;
#             background-color: #3498DB;
#             border: none;
#             border-radius: 12px;
#             padding: 14px 20px;
#             margin: 8px;
#         }
#         QPushButton:hover {
#             background-color: #2980B9;
#         }
#         QPushButton:pressed {
#             background-color: #1F618D;
#         }
#         """
#         for btn in buttons:
#             btn.setStyleSheet(button_style)
#
#     def _setup_layout(self):
#         """设置窗口布局"""
#         layout = QVBoxLayout()
#
#         layout.addWidget(self.title_label)
#         layout.addWidget(self.subtitle_label)
#
#         button_layout = QVBoxLayout()
#         button_layout.addWidget(self.btn_camera)
#         button_layout.addWidget(self.btn_file)
#         button_layout.addWidget(self.btn_result)
#         button_layout.addWidget(self.btn_exit)
#
#         layout.addLayout(button_layout)
#         layout.setContentsMargins(40, 40, 40, 40)
#         layout.setSpacing(20)
#
#         self.setLayout(layout)
#
#     def whichBtn(self, btn):
#         print(f"点击的按钮是：{btn.text()}")
#         if btn.text() == "退出系统":
#             sys.exit()
#         elif btn.text() == "从摄像头检测":
#             try:
#                 _thread.start_new_thread(run(**run_dict), ("Thread-1", 2,))
#             except:
#                 print("启动线程失败")
#         elif btn.text() == "查看检测结果":
#             path = os.getcwd() + r'\\runs\\detect'
#             os.system("start explorer %s" % path)
#         elif btn.text() == "从文件检测":
#             run(**run_dict_file)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WindowClass()
    #win.resize(500, 400)
    win.show()
    sys.exit(app.exec_())
