# Plagiarism Checker

## Overview
The **Plagiarism Checker** is a Python-based project that detects the similarity between text files by comparing their content and highlighting matches. This tool is particularly useful for educational institutions, content creators, and professionals to ensure originality and avoid plagiarism.

---

## Features
- **Text Similarity Detection**: Calculates the similarity percentage between two or more documents.
- **Repository Comparison**: Compares a document against a set of files in a repository.
- **Highlight Matches**: Identifies and highlights common phrases or words.
- **Efficient Algorithms**: Uses hashing and Jaccard similarity for accurate results.

---

## Technologies Used

### **Programming Language**:
- Python

### **Libraries**:
- `re`: For text preprocessing.
- `collections.Counter`: For word frequency analysis (optional).
- Built-in Python file handling for reading and processing text files.

### **Data Structures and Algorithms**:
- Hashing: To efficiently compare text shingles.
- Sets: For implementing Jaccard similarity.

---

## Tools Used
- **IDE/Text Editor**: PyCharm, VS Code, or any Python-compatible editor.
- **Version Control**: Git/GitHub for version management.
- **Testing Framework**: Python's built-in `unittest` (optional).
- **Cloud Services** (optional): AWS S3 or Google Drive for managing large repositories.

---

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/havish7728/plagiarism-checker.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd plagiarism-checker
   ```
3. **Install Dependencies** (if any):
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### **Comparing Two Documents**:
1. Place the text files to be compared in the project directory (e.g., `document1.txt` and `document2.txt`).
2. Update the file paths in the script:
   ```python
   file1 = "document1.txt"
   file2 = "document2.txt"
   ```
3. Run the script:
   ```bash
   python plagiarism_checker.py
   ```
4. View the similarity percentage in the output.

### **Comparing with a Repository**:
1. Place all repository files in the project directory (e.g., `doc1.txt`, `doc2.txt`, etc.).
2. Update the repository list in the script:
   ```python
   repository = ["doc1.txt", "doc2.txt", "doc3.txt"]
   ```
3. Run the script and view similarity results for each file in the repository.

### **Highlight Matches**:
- The script can optionally highlight matched words or phrases for visual analysis.

---

## Example Output
### **Terminal Output**:
```
Similarity between document1.txt and document2.txt: 85.67%

Similarity with repository:
doc1.txt: 90.12% similar
doc2.txt: 75.45% similar
doc3.txt: 62.34% similar
```


## Future Enhancements
- **Multilingual Support**: Extend compatibility to non-English text.
- **Advanced NLP Techniques**: Incorporate libraries like `spaCy` or `TF-IDF` for semantic analysis.
- **Database Integration**: Store and compare documents using a database system.
- **Web-Based Interface**: Add a user-friendly UI for broader accessibility.

---


## Contribution
Contributions are welcome! Feel free to fork the repository and submit pull requests for new features or bug fixes.

---

## Contact
For any questions or feedback, please contact:
- **Name**: Havish Gadey
- **GitHub**: [github.com/havish7728](https://github.com/havish7728)
- **Email**: havish7728@gmail.com
