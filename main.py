import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel, QTextEdit
from PySide6.QtGui import QFont
from pathlib import Path
from check_sequences import check_sequences

def choose_folder():
    folder = QFileDialog.getExistingDirectory(
        window,
        "Select Render Folder"
    )
    if folder:
        folder_label.setText(folder)
        
        results = check_sequences(Path(folder))
        
        if results:
            results_area.setPlainText("\n".join(results))
            
        else:
            results_area.setPlainText("SCAN COMPLETE\n\n"
                                    "No image sequences found in this folder.\n"
                                    "Files should be named like: renderMain.1001.exr")
app = QApplication(sys.argv)
    
window = QWidget()
window.setWindowTitle("Image Sequence Checker")
window.resize(600, 400)

title_label = QLabel("VFX Image Sequence Checker")
title_font = QFont()
title_font.setPointSize(18)
title_font.setBold(True)

title_label.setFont(title_font)

folder_button = QPushButton("Choose Folder")
folder_button.clicked.connect(choose_folder)

folder_label = QLabel("No folder selected")
folder_label.setWordWrap(True)

results_area = QTextEdit()
results_area.setReadOnly(True)
results_area.setPlaceholderText("Please select a folder to check its image sequences.")
layout = QVBoxLayout()
layout.addWidget(title_label)
layout.addWidget(folder_button) 
layout.addWidget(folder_label)
layout.addWidget(results_area)
layout.addStretch()
layout.setContentsMargins(16, 16, 16, 16)
window.setLayout(layout)
window.show()

sys.exit(app.exec())