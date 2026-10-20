# Task 3: Task Automation with Python Scripts

A versatile **Task Automation Suite** built using Python as part of the **CodeAlpha Python Programming Internship**.

---

## 📌 Project Overview
This project addresses real-world repetitive workflows by automating three distinct tasks specified in the CodeAlpha internship curriculum:
1. **File Management**: Organizing and moving `.jpg` / `.jpeg` files from a source folder into a dedicated destination folder.
2. **Data Extraction**: Extracting all valid email addresses from text files using regular expressions and saving unique results to an output file.
3. **Web Scraping**: Extracting and saving the `<title>` tag of any webpage.

---

## 🛠️ Key Concepts Used
- **`os` & `shutil`**: Directory traversal, path manipulation, directory creation, and moving files.
- **`re` (Regular Expressions)**: Pattern matching for email addresses (`[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+`) and HTML tags (`<title>(.*?)</title>`).
- **`requests` & `urllib.request`**: Sending HTTP GET requests, headers, error handling, and web page content retrieval.
- **File Handling**: Reading text inputs and writing processed output files (`.txt`).

---

## 🚀 How to Run

1. Open your terminal or command prompt.
2. Navigate to this directory:
   ```bash
   cd Task3_Task_Automation
   ```
3. Run the automation script:
   ```bash
   python task_automation.py
   ```

---

## 📋 Interactive Menu Options

```text
=======================================================
      CODEALPHA - TASK AUTOMATION WITH PYTHON
=======================================================
Choose an automation task to run:
  1. Move all .jpg files from a folder to a new folder
  2. Extract all email addresses from a .txt file
  3. Scrape and save the title of a webpage
  4. Run all three automation tasks in sequence
  5. Exit
```

---

## 📂 Included Demo Files
- `sample_text_with_emails.txt`: Pre-built text file with multiple sample email addresses to test Option 2 immediately.
- Automatic demo file generator for Option 1: Creates test dummy `.jpg` files if default folders are selected.
