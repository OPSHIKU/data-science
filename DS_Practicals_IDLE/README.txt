DATA SCIENCE PRACTICALS - IDLE VERSION
Karina Bacche - 264447

WHAT IS IN THIS FOLDER
- Practical_01a ... Practical_14 .py : one file per practical (run each on its own)
- ds_practicals_menu.py              : all practicals in one file with a menu
- requirements.txt                   : libraries to install
- DUMMY DATA FILES (so everything runs out of the box):
    Country.csv            -> Practical 1B
    IP_DATA_ALL.csv        -> Practicals 2D, 2E, 2F, 3
    iris1.csv              -> Practical 5 (parallel coordinates)
    hough.jpg              -> Practical 7
    1.png                  -> Practicals 1A, 9, 10, 11
    students_math.csv      -> Practical 14
    student_science.csv    -> Practical 14
    dummy_housing.csv      -> Practical 12 (used only if there is no internet)

HOW TO RUN
1. Install Python from python.org (tick "Add Python to PATH").
2. Open Command Prompt in this folder and run:
       pip install -r requirements.txt
3. Right-click any Practical_XX file -> "Edit with IDLE" -> press F5.
   (or open ds_practicals_menu.py, press F5, and type a number like 1a, 2c, 12)
4. Close each graph window to continue.

NOTES
- Practical 8 downloads NLTK data automatically (needs internet the first time).
- Practical 12 downloads the California housing data (internet); with no
  internet it falls back to dummy_housing.csv.
- To use your own files, just replace the dummy files with yours (same names).
- Files created by the practicals (Image_to_HORUS.csv, HORUS-CSV-Country.csv,
  Retrieve_Router_Location.csv, kde.png, etc.) are saved in this same folder.
