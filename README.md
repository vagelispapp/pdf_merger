# 🧾 PDF Merger

A lightweight and user-friendly desktop tool that automatically merges all PDF files in the current folder using a graphical interface — no coding or terminal required.

---

## 🚀 Features

- 📂 Auto-detects all `.pdf` files in the same folder as the executable.
- 📝 Prompts you for a name for the combined PDF.
- 💾 Saves the output in the same directory.
- 🖱️ No terminal window opens — just double-click and go.

---

## 📦 Usage

### 🔧 Step 1: Prepare Your Files

Put the `.exe` file and all your `.pdf` files in the same folder:

### 🖱️ Step 2: Run It

1. Double-click `PDFMerger.exe`.
2. A small window will ask:

   Enter the output file name

3. Type your desired name (e.g., `final_report`) and click OK.
4. The merged file `final_report.pdf` will be created in the same folder.

---

## 🛠️ Built With

- [Python 3](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html) – GUI
- [pypdf](https://pypi.org/project/pypdf/) – PDF merging

## 💡 Notes

- Files are merged in alphabetical order (e.g., `a.pdf`, `b.pdf`, `c.pdf`).
- Ensure no PDFs are open in another program when running the merger.
- If you want to use the source script instead of the `.exe`, install dependencies:

bash
pip install pypdf
