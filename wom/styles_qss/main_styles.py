title_label = "color: White;"\
              "font-size: 12pt;"\
              "font-family: Roboto;"


button_del = "QPushButton {\
                  background-color: rgba(112, 38, 50, 190);\
                  font-size: 9pt;\
                  color: White;\
                  border: None;\
              }\
              \
              QPushButton::hover {\
                  background-color: rgba(112, 38, 50, 255);\
                  border: 2px solid rgba(145, 47, 64, 255);\
              }\
              \
              QPushButton::pressed {\
                  background-color: rgba(145, 47, 64, 255);\
                  border: 1px solid rgba(255, 255, 255, 255);\
              }\
              \
              QPushButton::disabled {\
                  background-color: #EEEEEE;\
                  border: 1px solid rgba(112, 38, 50, 255);\
              }"


progress = "QProgressBar::chunk {\
                    background-color: rgba(112, 38, 50, 190);\
            }"


lineEdit_style = "QLineEdit {\
                      background-color: #EEEEEE;\
                      color: #13242B;\
                      border: 1px solid #326273;\
                      font-weight: bold;\
                      font-size: 11pt;\
                  }"


lineEdit_style_error = """
    QLineEdit {
        background-color: rgba(112, 38, 50, 40);
        color: #EEEEEE;
        border: 1px solid rgba(112, 38, 50, 190);
        font-weight: bold;
        font-size: 11pt;
    }"""


label_style_b20 = "QLabel {\
                       color: White;\
                       background-color: rgba(145, 47, 64, 255);\
                       border-style:solid;\
                       border-width: 1px;\
                       border-color: White;\
                   }"

label_style_diabet = "QLabel {\
                         color: #EEEEEE;\
                         background-color: rgba(50, 98, 115, 255);\
                         border-style:solid;\
                         border-width: 1px;\
                         border-color: rgba(92, 158, 173, 255);\
                     }"

label_style_dis = "QLabel {\
                       color: #EEEEEE;\
                       background-color: rgba(112, 38, 50, 255);\
                       border-style:solid;\
                       border-width: 1px;\
                       border-color: rgba(145, 47, 64, 255);\
                   }"


label_style_act = "QLabel {\
                       color: White;\
                       background-color: rgba(92, 158, 173, 200);\
                       border-style:solid;\
                       border-width: 1px;\
                       border-color: rgba(92, 158, 173, 255);\
                   }"


label_style_ln = "QLabel {\
                      color: #EEEEEE;\
                      background-color: rgba(92, 158, 173, 200);\
                      border-style:solid;\
                      border-width: 1px;\
                      border-color: rgba(145, 47, 64, 255);\
                  }"


style_true_button = "QPushButton {\
                         background-color: rgba(50, 98, 115, 255);\
                         font-size: 14pt;\
                         color: White;\
                         border: None;\
                         }\
                         \
                     QPushButton::hover {\
                         background-color: rgba(92, 158, 173, 255);\
                         border: 1px solid rgba(255, 255, 255, 255);\
                         }\
                         \
                     QPushButton::pressed {\
                         color: rgba(0, 0, 0, 255)\
                         background-color: rgba(255, 255, 255, 255);\
                         border: 1px solid rgba(50, 98, 115, 255);\
                         }\
                         \
                     QPushButton::disabled {\
                         background-color: #EEEEEE;\
                         border: 1px solid rgba(50, 98, 115, 255);\
                         }"


progress_style_own = "QProgressBar::chunk {\
                          background-color: rgba(112, 38, 50, 190);\
                      }"


progress_style_other = "QProgressBar::chunk {\
                            background-color: rgba(50, 98, 115, 190);\
                        }"


button_own = "QPushButton {\
                  background-color: rgba(112, 38, 50, 190);\
                  font-size: 9pt;\
                  color: White;\
                  border: None;\
              }\
              \
              QPushButton::hover {\
                  background-color: rgba(112, 38, 50, 255);\
                  border: 2px solid rgba(145, 47, 64, 255);\
              }\
              \
              QPushButton::pressed {\
                  background-color: rgba(145, 47, 64, 255);\
                  border: 1px solid rgba(255, 255, 255, 255);\
              }\
              \
              QPushButton::disabled {\
                  background-color: #EEEEEE;\
                  border: 1px solid rgba(112, 38, 50, 255);\
              }"


button_other = "QPushButton {\
                    background-color: rgba(50, 98, 115, 190);\
                    font-size: 9pt;\
                    color: White;\
                    border: None;\
                }\
                \
                QPushButton::hover {\
                    background-color: rgba(50, 98, 115, 255);\
                    border: 2px solid rgba(92, 158, 173, 255);\
                }\
                \
                QPushButton::pressed {\
                    background-color: rgba(92, 158, 173, 255);\
                    border: 1px solid rgba(255, 255, 255, 255);\
                }\
                \
                QPushButton::disabled {\
                    background-color: #EEEEEE;\
                    border: 1px solid rgba(50, 98, 115, 190);\
                }"


pTE_main = "QPlainTextEdit {\
                 background-color: #EEEEEE;\
                 color: #13242B;\
                 border: 1px solid #326273;\
                 font-weight: bold;\
                 font-size: 11pt;\
             }"


pTE_drugs = "QPlainTextEdit {\
                 background-color: #EEEEEE;\
                 color: #13242B;\
                 border: 1px solid #326273;\
                 font-weight: bold;\
                 font-size: 9pt;\
             }"


check_main = "QCheckBox {\
                  color: White;\
                  border: none;\
                  background-color: none;\
                  padding-left: 5px;\
              }\
              QCheckBox:checked {\
                  color: #702632;\
              }\
              QCheckBox:disabled {\
                  color: #EEEEEE;\
              }\
              QCheckBox::indicator:checked {\
                  border-style:solid;\
                  border-width: 1px;\
                  border-color: #702632;\
                  color: #FFFFFF;\
                  background-color: #702632;\
              }\
              QCheckBox::indicator:!checked {\
                  border-style:solid;\
                  border-width: 1px;\
                  border-color: #702632;\
                  color: #FFFFFF;\
                  background-color: none;\
              }\
              QCheckBox::indicator:disabled {\
                  border-style:solid;\
                  border-width: 1px;\
                  border-color: #EEEEEE;\
                  color: #FFFFFF;\
                  background-color: transparent;\
              }"
