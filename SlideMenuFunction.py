from PyQt5.QtCore import  QPropertyAnimation, QEasingCurve, Qt


def slide_menu_fun(left_menu):
    width = left_menu.width()

    if width == 50:

        newWidth = 160
    else:

        newWidth = 50

    animation = QPropertyAnimation(left_menu, b"maximumWidth")
    animation.setDuration(1000)
    animation.setStartValue(newWidth)
    animation.setEndValue(width)
    animation.setEasingCurve(QEasingCurve.InCurve)
    animation.start()