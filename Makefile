start:
	poetry run app

install:
	poetry install

convert_all:
	convert_common_ui_to_py
	convert_omr_ui_to_py
	convert_bta_ui_to_py

convert_common:
	poetry run pyside6-uic wom/GUI/UI/common/User_main_menu.ui > wom/GUI/PY/common/User_main_menu.py
	poetry run pyside6-uic wom/GUI/UI/common/Registration.ui > wom/GUI/PY/common/Registration.py
	poetry run pyside6-uic wom/GUI/UI/common/Login.ui > wom/GUI/PY/common/Login.py
	poetry run pyside6-uic wom/GUI/UI/common/drugs_dictionary.ui > wom/GUI/PY/common/drugs_dictionary.py
	poetry run pyside6-uic wom/GUI/UI/common/load_arch_data.ui > wom/GUI/PY/common/load_arch_data.py
	poetry run pyside6-uic wom/GUI/UI/common/PatientPassportData.ui > wom/GUI/PY/common/PatientPassportData.py
	poetry run pyside6-uic wom/GUI/UI/common/AddRelative.ui > wom/GUI/PY/common/AddRelative.py
	poetry run pyside6-uic wom/GUI/UI/common/StObj_admition.ui > wom/GUI/PY/common/StObj_admition.py
	poetry run pyside6-uic wom/GUI/UI/common/StObj_discharge.ui > wom/GUI/PY/common/StObj_discharge.py
	poetry run pyside6-uic wom/GUI/UI/common/St_Neurology.ui > wom/GUI/PY/common/St_Neurology.py
	poetry run pyside6-uic wom/GUI/UI/common/Diagnosis.ui > wom/GUI/PY/common/Diagnosis.py
	poetry run pyside6-uic wom/GUI/UI/common/Discharge_details.ui > wom/GUI/PY/common/Discharge_details.py
	poetry run pyside6-uic wom/GUI/UI/common/icf.ui > wom/GUI/PY/common/Icf.py
	poetry run pyside6-uic wom/GUI/UI/common/Laboratory_data.ui > wom/GUI/PY/common/Laboratory_data.py
	poetry run pyside6-uic wom/GUI/UI/common/Almanac.ui > wom/GUI/PY/common/Almanac.py
	poetry run pyside6-uic wom/GUI/UI/common/Entry.ui > wom/GUI/PY/common/Entry.py

convert_omr:
	poetry run pyside6-uic wom/GUI/UI/omr/omr_MainMenu.ui > wom/GUI/PY/omr/omr_MainMenu.py
	poetry run pyside6-uic wom/GUI/UI/omr/omr_PatientCard.ui > wom/GUI/PY/omr/omr_PatientCard.py
	poetry run pyside6-uic wom/GUI/UI/omr/omr_AddNewPatient.ui > wom/GUI/PY/omr/omr_AddNewPatient.py
	poetry run pyside6-uic wom/GUI/UI/omr/omr_Appointments.ui > wom/GUI/PY/omr/omr_Appointments.py
	poetry run pyside6-uic wom/GUI/UI/omr/omr_MDRK.ui > wom/GUI/PY/omr/omr_MDRK.py
	poetry run pyside6-uic wom/GUI/UI/omr/omr_Dynamic.ui > wom/GUI/PY/omr/omr_Dynamic.py

convert_bta:
	poetry run pyside6-uic wom/GUI/UI/bta/bta_AddNewPatient.ui > wom/GUI/PY/bta/bta_AddNewPatient.py
	poetry run pyside6-uic wom/GUI/UI/bta/bta_MainMenu.ui > wom/GUI/PY/bta/bta_MainMenu.py
	poetry run pyside6-uic wom/GUI/UI/bta/bta_PatientCard.ui > wom/GUI/PY/bta/bta_PatientCard.py
	poetry run pyside6-uic wom/GUI/UI/bta/bta_Protocol.ui > wom/GUI/PY/bta/bta_Protocol.py

convert_res:
	poetry run pyside6-rcc wom/GUI/UI/res_main.qrc -o res_main_rc.py
