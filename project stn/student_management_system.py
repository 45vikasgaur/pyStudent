"""
Student Information Management System
Python + Tkinter + SQLite
-----------------------------------
Features:
- Add, view, update, delete, and search students
- SQLite database created automatically
- Form validation and duplicate roll-number protection
- Export records to CSV
- No third-party packages required

Run:
    python student_management_system.py
"""

import csv
import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime

DB_FILE = "students.db"

FIELDS = [
    ("roll_no", "Roll Number"),
    ("name", "Full Name"),
    ("dob", "Date of Birth (DD-MM-YYYY)"),
    ("gender", "Gender"),
    ("department", "Department"),
    ("course", "Course"),
    ("semester", "Class / Semester"),
    ("admission_year", "Admission Year"),
    ("email", "Email"),
    ("phone", "Phone Number"),
    ("cgpa", "CGPA / Percentage"),
    ("address", "Address"),
    ("status", "Status"),
    ("notes", "Notes"),
]

TABLE_COLUMNS = [
    "roll_no", "name", "gender", "course", "department",
    "semester", "phone", "email", "cgpa", "status"
]

TABLE_HEADINGS = {
    "roll_no": "Roll No", "name": "Name", "gender": "Gender",
    "course": "Course", "department": "Department", "semester": "Semester",
    "phone": "Phone", "email": "Email", "cgpa": "CGPA", "status": "Status"
}


class StudentDatabase:
    def __init__(self, filename=DB_FILE):
        self.connection = sqlite3.connect(filename)
        self.connection.row_factory = sqlite3.Row
        self.connection.execute("""
            CREATE TABLE IF NOT EXISTS students (
                roll_no TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                dob TEXT DEFAULT '',
                gender TEXT DEFAULT '',
                department TEXT DEFAULT '',
                course TEXT DEFAULT '',
                semester TEXT NOT NULL,
                admission_year TEXT DEFAULT '',
                email TEXT DEFAULT '',
                phone TEXT DEFAULT '',
                cgpa TEXT DEFAULT '',
                address TEXT DEFAULT '',
                status TEXT NOT NULL DEFAULT 'Active',
                notes TEXT DEFAULT '',
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        """)
        self.connection.commit()

    def add(self, data):
        now = datetime.now().isoformat(timespec="seconds")
        keys = [field[0] for field in FIELDS]
        values = [data.get(key, "").strip() for key in keys]
        placeholders = ", ".join("?" for _ in range(len(keys) + 2))
        query = (
            f"INSERT INTO students ({', '.join(keys)}, created_at, updated_at) "
            f"VALUES ({placeholders})"
        )
        self.connection.execute(query, values + [now, now])
        self.connection.commit()

    def update(self, original_roll, data):
        keys = [field[0] for field in FIELDS]
        update_keys = keys[1:]
        now = datetime.now().isoformat(timespec="seconds")
        assignments = ", ".join(f"{key} = ?" for key in update_keys)
        values = [data.get(key, "").strip() for key in update_keys]
        self.connection.execute(
            f"UPDATE students SET {assignments}, updated_at = ? WHERE roll_no = ?",
            values + [now, original_roll]
        )
        self.connection.commit()

    def delete(self, roll_no):
        self.connection.execute(
            "DELETE FROM students WHERE roll_no = ?", (roll_no,)
        )
        self.connection.commit()

    def get(self, roll_no):
        return self.connection.execute(
            "SELECT * FROM students WHERE roll_no = ?", (roll_no,)
        ).fetchone()

    def search(self, term=""):
        if term.strip():
            pattern = f"%{term.strip()}%"
            return self.connection.execute("""
                SELECT * FROM students
                WHERE roll_no LIKE ? OR name LIKE ? OR email LIKE ?
                   OR phone LIKE ? OR course LIKE ? OR department LIKE ?
                ORDER BY name COLLATE NOCASE
            """, (pattern, pattern, pattern, pattern, pattern, pattern)).fetchall()
        return self.connection.execute(
            "SELECT * FROM students ORDER BY name COLLATE NOCASE"
        ).fetchall()

    def count(self):
        return self.connection.execute(
            "SELECT COUNT(*) FROM students"
        ).fetchone()[0]

    def close(self):
        self.connection.close()


class StudentManagementApp:
    BG = "#f2f5fa"
    NAVY = "#17365d"
    BLUE = "#2477e8"
    GREEN = "#159957"
    ORANGE = "#e98b16"
    RED = "#dc3d3d"
    TEXT = "#172b4d"
    WHITE = "#ffffff"

    def __init__(self, root):
        self.root = root
        self.root.title("Student Information Management System")
        self.root.geometry("1450x850")
        self.root.minsize(1100, 700)
        self.root.configure(bg=self.BG)

        self.db = StudentDatabase()
        self.entries = {}
        self.selected_roll = None

        self.configure_styles()
        self.build_layout()
        self.refresh_table()
        self.root.protocol("WM_DELETE_WINDOW", self.close_app)

    def configure_styles(self):
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure("Treeview", font=("Segoe UI", 10), rowheight=30,
                        background="white", fieldbackground="white",
                        foreground=self.TEXT)
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"),
                        background="#e7eef8", foreground=self.NAVY, padding=8)
        style.map("Treeview", background=[("selected", "#cfe2ff")],
                  foreground=[("selected", self.TEXT)])
        style.configure("TCombobox", padding=5, font=("Segoe UI", 10))

    def build_layout(self):
        header = tk.Frame(self.root, bg=self.NAVY, height=76)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(header, text="🎓  Student Information Management System",
                 bg=self.NAVY, fg="white", font=("Segoe UI", 21, "bold")
                 ).pack(side="left", padx=24, pady=18)
        self.total_label = tk.Label(header, text="Total Students: 0",
                                    bg=self.NAVY, fg="white",
                                    font=("Segoe UI", 11))
        self.total_label.pack(side="right", padx=25)

        body = tk.Frame(self.root, bg=self.BG)
        body.pack(fill="both", expand=True, padx=18, pady=16)

        self.build_form(body)
        self.build_records(body)

        footer = tk.Label(self.root,
                          text="Student Management System  •  Python / Tkinter / SQLite",
                          bg=self.BG, fg="#64748b", font=("Segoe UI", 9))
        footer.pack(pady=(0, 8))

    def build_form(self, parent):
        card = tk.Frame(parent, bg=self.WHITE, highlightbackground="#dce4ef",
                        highlightthickness=1)
        card.pack(fill="x", pady=(0, 14))

        tk.Label(card, text="Add / Update Student Information",
                 bg=self.WHITE, fg=self.NAVY,
                 font=("Segoe UI", 15, "bold")).pack(anchor="w", padx=18, pady=(14, 8))

        form = tk.Frame(card, bg=self.WHITE)
        form.pack(fill="x", padx=18, pady=4)

        # Four columns make the form readable on typical laptop screens.
        layout = [
            [("roll_no", "Roll Number"), ("name", "Full Name"),
             ("dob", "Date of Birth (DD-MM-YYYY)"), ("gender", "Gender")],
            [("department", "Department"), ("course", "Course"),
             ("semester", "Class / Semester"), ("admission_year", "Admission Year")],
            [("email", "Email"), ("phone", "Phone Number"),
             ("cgpa", "CGPA / Percentage"), ("status", "Status")],
            [("address", "Address"), ("notes", "Notes")]
        ]

        for col in range(4):
            form.grid_columnconfigure(col, weight=1, uniform="form")

        for row_index, row_fields in enumerate(layout):
            for col_index, (key, label) in enumerate(row_fields):
                cell = tk.Frame(form, bg=self.WHITE)
                cell.grid(row=row_index, column=col_index, sticky="ew",
                          padx=(0 if col_index == 0 else 8, 8), pady=6)
                tk.Label(cell, text=label, bg=self.WHITE, fg=self.TEXT,
                         font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(0, 4))
                if key == "gender":
                    widget = ttk.Combobox(cell, values=["Male", "Female", "Other"],
                                          state="readonly")
                    widget.set("Male")
                elif key == "status":
                    widget = ttk.Combobox(cell, values=["Active", "Inactive", "Graduated"],
                                          state="readonly")
                    widget.set("Active")
                elif key == "course":
                    widget = ttk.Combobox(
                        cell,
                        values=["BCA", "MCA", "B.Tech", "B.Sc", "B.Com", "BA", "MBA", "Other"]
                    )
                    widget.set("BCA")
                elif key == "department":
                    widget = ttk.Combobox(
                        cell,
                        values=["Computer Science", "Information Technology",
                                "Commerce", "Management", "Science", "Arts", "Other"]
                    )
                    widget.set("Computer Science")
                else:
                    widget = tk.Entry(cell, font=("Segoe UI", 10), relief="solid",
                                      bd=1, highlightthickness=0)
                widget.pack(fill="x", ipady=6)
                self.entries[key] = widget

        # Address and notes are regular single-line fields to keep the form compact.
        button_row = tk.Frame(card, bg=self.WHITE)
        button_row.pack(fill="x", padx=18, pady=(10, 16))

        self.make_button(button_row, "＋  Add Student", self.add_student,
                         self.GREEN).pack(side="left", fill="x", expand=True, padx=(0, 7))
        self.make_button(button_row, "↻  Update Selected", self.update_student,
                         self.BLUE).pack(side="left", fill="x", expand=True, padx=7)
        self.make_button(button_row, "✕  Delete Selected", self.delete_student,
                         self.RED).pack(side="left", fill="x", expand=True, padx=7)
        self.make_button(button_row, "Clear Form", self.clear_form,
                         self.ORANGE).pack(side="left", fill="x", expand=True, padx=(7, 0))

    def build_records(self, parent):
        card = tk.Frame(parent, bg=self.WHITE, highlightbackground="#dce4ef",
                        highlightthickness=1)
        card.pack(fill="both", expand=True)

        top = tk.Frame(card, bg=self.WHITE)
        top.pack(fill="x", padx=16, pady=(12, 8))
        tk.Label(top, text="Student Records", bg=self.WHITE, fg=self.NAVY,
                 font=("Segoe UI", 15, "bold")).pack(side="left")

        self.search_var = tk.StringVar()
        search_entry = tk.Entry(top, textvariable=self.search_var,
                                font=("Segoe UI", 10), relief="solid", bd=1, width=32)
        search_entry.pack(side="right", ipady=6, padx=(8, 0))
        search_entry.bind("<Return>", lambda _event: self.refresh_table())
        self.make_button(top, "Search", self.refresh_table, self.BLUE
                         ).pack(side="right", padx=6)
        self.make_button(top, "Export CSV", self.export_csv, self.NAVY
                         ).pack(side="right", padx=6)

        table_frame = tk.Frame(card, bg=self.WHITE)
        table_frame.pack(fill="both", expand=True, padx=14, pady=(0, 14))

        self.table = ttk.Treeview(table_frame, columns=TABLE_COLUMNS,
                                  show="headings", selectmode="browse")
        widths = {
            "roll_no": 80, "name": 150, "gender": 75, "course": 85,
            "department": 150, "semester": 115, "phone": 120,
            "email": 190, "cgpa": 80, "status": 90
        }
        for col in TABLE_COLUMNS:
            self.table.heading(col, text=TABLE_HEADINGS[col])
            self.table.column(col, width=widths[col], minwidth=65, anchor="w")

        y_scroll = ttk.Scrollbar(table_frame, orient="vertical",
                                 command=self.table.yview)
        x_scroll = ttk.Scrollbar(table_frame, orient="horizontal",
                                 command=self.table.xview)
        self.table.configure(yscrollcommand=y_scroll.set,
                             xscrollcommand=x_scroll.set)
        self.table.grid(row=0, column=0, sticky="nsew")
        y_scroll.grid(row=0, column=1, sticky="ns")
        x_scroll.grid(row=1, column=0, sticky="ew")
        table_frame.rowconfigure(0, weight=1)
        table_frame.columnconfigure(0, weight=1)
        self.table.bind("<<TreeviewSelect>>", self.on_select)
        self.table.bind("<Double-1>", self.on_select)

    def make_button(self, parent, text, command, color):
        return tk.Button(parent, text=text, command=command, bg=color, fg="white",
                         activebackground=color, activeforeground="white",
                         relief="flat", cursor="hand2",
                         font=("Segoe UI", 10, "bold"), padx=12, pady=10)

    def get_form_data(self):
        data = {}
        for key, _label in FIELDS:
            widget = self.entries[key]
            data[key] = widget.get().strip()
        return data

    def validate(self, data, updating=False):
        if not data["roll_no"]:
            messagebox.showwarning("Validation", "Roll Number is required.")
            return False
        if not data["name"]:
            messagebox.showwarning("Validation", "Full Name is required.")
            return False
        if not data["semester"]:
            messagebox.showwarning("Validation", "Class / Semester is required.")
            return False
        if data["email"] and ("@" not in data["email"] or "." not in data["email"].split("@")[-1]):
            messagebox.showwarning("Validation", "Enter a valid email address.")
            return False
        if data["cgpa"]:
            try:
                score = float(data["cgpa"])
                if score < 0 or score > 100:
                    messagebox.showwarning(
                        "Validation", "CGPA / Percentage must be between 0 and 100."
                    )
                    return False
            except ValueError:
                messagebox.showwarning("Validation", "CGPA / Percentage must be numeric.")
                return False
        existing = self.db.get(data["roll_no"])
        if existing and not (updating and self.selected_roll == data["roll_no"]):
            messagebox.showwarning(
                "Duplicate Roll Number", "That roll number already exists."
            )
            return False
        return True

    def add_student(self):
        data = self.get_form_data()
        if not self.validate(data):
            return
        try:
            self.db.add(data)
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "A student with that roll number already exists.")
            return
        messagebox.showinfo("Success", "Student record added successfully.")
        self.clear_form()
        self.refresh_table()

    def update_student(self):
        if not self.selected_roll:
            messagebox.showwarning("Select Student", "Select a student record from the table first.")
            return
        data = self.get_form_data()
        if not self.validate(data, updating=True):
            return
        old_roll = self.selected_roll
        if data["roll_no"] != old_roll and self.db.get(data["roll_no"]):
            messagebox.showwarning("Duplicate Roll Number", "That roll number already exists.")
            return
        try:
            # Roll number is the primary key, so changing it is handled as delete + insert
            # inside one transaction to preserve uniqueness.
            if data["roll_no"] != old_roll:
                now = datetime.now().isoformat(timespec="seconds")
                keys = [field[0] for field in FIELDS]
                values = [data.get(key, "").strip() for key in keys]
                self.db.connection.execute("BEGIN")
                self.db.connection.execute(
                    "DELETE FROM students WHERE roll_no = ?", (old_roll,)
                )
                placeholders = ", ".join("?" for _ in range(len(keys) + 2))
                self.db.connection.execute(
                    f"INSERT INTO students ({', '.join(keys)}, created_at, updated_at) "
                    f"VALUES ({placeholders})", values + [now, now]
                )
                self.db.connection.commit()
            else:
                self.db.update(old_roll, data)
        except sqlite3.Error as error:
            self.db.connection.rollback()
            messagebox.showerror("Database Error", str(error))
            return
        messagebox.showinfo("Success", "Student record updated successfully.")
        self.clear_form()
        self.refresh_table()

    def delete_student(self):
        if not self.selected_roll:
            messagebox.showwarning("Select Student", "Select a student record from the table first.")
            return
        if not messagebox.askyesno(
            "Confirm Delete",
            f"Delete the record for roll number {self.selected_roll}?"
        ):
            return
        self.db.delete(self.selected_roll)
        self.clear_form()
        self.refresh_table()
        messagebox.showinfo("Deleted", "Student record deleted.")

    def clear_form(self):
        for key, _label in FIELDS:
            widget = self.entries[key]
            if isinstance(widget, ttk.Combobox):
                if key == "gender":
                    widget.set("Male")
                elif key == "status":
                    widget.set("Active")
                elif key == "course":
                    widget.set("BCA")
                elif key == "department":
                    widget.set("Computer Science")
            else:
                widget.delete(0, tk.END)
        self.selected_roll = None
        for item in self.table.selection():
            self.table.selection_remove(item)

    def on_select(self, _event=None):
        selection = self.table.selection()
        if not selection:
            return
        roll_no = self.table.item(selection[0], "values")[0]
        record = self.db.get(roll_no)
        if not record:
            return
        self.selected_roll = record["roll_no"]
        for key, _label in FIELDS:
            widget = self.entries[key]
            widget_value = record[key] or ""
            if isinstance(widget, ttk.Combobox):
                widget.set(widget_value)
            else:
                widget.delete(0, tk.END)
                widget.insert(0, widget_value)

    def refresh_table(self):
        for item in self.table.get_children():
            self.table.delete(item)
        records = self.db.search(self.search_var.get())
        for record in records:
            self.table.insert(
                "", "end",
                values=[record[col] for col in TABLE_COLUMNS]
            )
        self.total_label.config(text=f"Total Students: {self.db.count()}")

    def export_csv(self):
        records = self.db.search(self.search_var.get())
        if not records:
            messagebox.showinfo("Export", "There are no records to export.")
            return
        filename = filedialog.asksaveasfilename(
            title="Export student records",
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            initialfile="student_records.csv"
        )
        if not filename:
            return
        keys = [field[0] for field in FIELDS]
        try:
            with open(filename, "w", newline="", encoding="utf-8-sig") as file:
                writer = csv.DictWriter(file, fieldnames=keys)
                writer.writeheader()
                for record in records:
                    writer.writerow({key: record[key] for key in keys})
            messagebox.showinfo("Export Complete", f"Records exported to:\n{filename}")
        except OSError as error:
            messagebox.showerror("Export Error", str(error))

    def close_app(self):
        self.db.close()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementApp(root)
    root.mainloop()
