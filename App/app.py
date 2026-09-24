import tkinter as tk
from tkinter import ttk
import sys
import os


# ============================================================
# PROJECT PATH
# ============================================================

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.append(PROJECT_ROOT)

from Frontend.parser import parse_file


# ============================================================
# COLORS
# ============================================================

BG = "#0d1117"
PANEL = "#161b22"
PANEL_LIGHT = "#21262d"
BORDER = "#30363d"

TEXT = "#e6edf3"
TEXT_DIM = "#8b949e"

GREEN = "#3fb950"
GREEN_DARK = "#238636"

BLUE = "#58a6ff"
PURPLE = "#bc8cff"
ORANGE = "#d29922"
RED = "#f85149"
CYAN = "#39d0d8"

EDITOR_BG = "#0d1117"
CONSOLE_BG = "#090c10"


# ============================================================
# FONTS
# ============================================================

FONT_UI = ("Segoe UI", 10)
FONT_UI_BOLD = ("Segoe UI", 10, "bold")
FONT_TITLE = ("Segoe UI", 18, "bold")
FONT_CODE = ("Consolas", 11)
FONT_CODE_SMALL = ("Consolas", 10)


# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()

root.title("NEO Iot-DSL")
root.geometry("1400x850")
root.minsize(1100, 700)
root.configure(bg=BG)


# ============================================================
# STATE
# ============================================================

current_file = None
tree_paths = {}


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def set_status(message, color=TEXT_DIM):
    status_text.set(message)
    status_indicator.configure(
        text="● READY",
        foreground=color
    )


def clear_output():
    output_text.configure(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.configure(state="disabled")


def insert_output(text, tag=None):
    output_text.configure(state="normal")

    if tag:
        output_text.insert(tk.END, text, tag)
    else:
        output_text.insert(tk.END, text)

    output_text.configure(state="disabled")


def update_line_numbers(event=None):
    line_numbers.configure(state="normal")
    line_numbers.delete("1.0", tk.END)

    line_count = int(
        program_text.index("end-1c").split(".")[0]
    )

    numbers = "\n".join(
        str(number)
        for number in range(1, line_count + 1)
    )

    line_numbers.insert("1.0", numbers)
    line_numbers.configure(state="disabled")


# ============================================================
# SYNTAX HIGHLIGHTING
# ============================================================

KEYWORDS = [
    "DEVICE",
    "PIN",
    "LED",
    "TEMP",
    "BUTTON",
    "ON",
    "OFF",
    "WAIT",
    "READ",
    "IF",
    "ELSE",
    "END",
    "LOOP",
]


def highlight_syntax(event=None):

    program_text.tag_remove(
        "keyword",
        "1.0",
        tk.END
    )

    program_text.tag_remove(
        "number",
        "1.0",
        tk.END
    )

    program_text.tag_remove(
        "operator",
        "1.0",
        tk.END
    )

    program_text.tag_remove(
        "comment",
        "1.0",
        tk.END
    )

    # -----------------------------
    # Keywords
    # -----------------------------

    for keyword in KEYWORDS:

        start = "1.0"

        while True:

            position = program_text.search(
                r"\m" + keyword + r"\M",
                start,
                stopindex=tk.END,
                regexp=True
            )

            if not position:
                break

            end = f"{position}+{len(keyword)}c"

            program_text.tag_add(
                "keyword",
                position,
                end
            )

            start = end

    # -----------------------------
    # Numbers
    # -----------------------------

    start = "1.0"

    while True:

        position = program_text.search(
            r"[0-9]+",
            start,
            stopindex=tk.END,
            regexp=True
        )

        if not position:
            break

        line, column = map(
            int,
            position.split(".")
        )

        line_text = program_text.get(
            f"{line}.{column}",
            f"{line}.end"
        )

        number_length = 0

        for character in line_text:
            if character.isdigit():
                number_length += 1
            else:
                break

        if number_length == 0:
            break

        end = f"{position}+{number_length}c"

        program_text.tag_add(
            "number",
            position,
            end
        )

        start = end

    # -----------------------------
    # Operators
    # -----------------------------

    for operator in [">", "<", "=="]:

        start = "1.0"

        while True:

            position = program_text.search(
                operator,
                start,
                stopindex=tk.END
            )

            if not position:
                break

            end = f"{position}+{len(operator)}c"

            program_text.tag_add(
                "operator",
                position,
                end
            )

            start = end

    # -----------------------------
    # Comments
    # -----------------------------

    line_count = int(
        program_text.index("end-1c").split(".")[0]
    )

    for line in range(1, line_count + 1):

        position = program_text.search(
            "#",
            f"{line}.0",
            stopindex=f"{line}.end"
        )

        if position:

            program_text.tag_add(
                "comment",
                position,
                f"{line}.end"
            )


# ============================================================
# LOAD FILE INTO EDITOR
# ============================================================

def load_file(file_path):

    global current_file

    # Only open normal text/source files
    allowed_extensions = {
        ".iot",
        ".g4",
        ".py",
        ".md",
        ".txt",
        ".json",
        ".xml",
    }

    extension = os.path.splitext(file_path)[1].lower()

    if extension not in allowed_extensions:

        set_status(
            "Unsupported file type",
            ORANGE
        )

        return

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            content = file.read()

        program_text.delete(
            "1.0",
            tk.END
        )

        program_text.insert(
            "1.0",
            content
        )

        current_file = file_path

        filename = os.path.basename(file_path)

        file_tab.configure(
            text=f"  ●  {filename}"
        )

        update_line_numbers()
        highlight_syntax()

        set_status(
            f"Opened {filename}",
            GREEN
        )

    except Exception as error:

        set_status(
            f"Could not open file: {error}",
            RED
        )


# ============================================================
# PROJECT EXPLORER
# ============================================================

def populate_folder(parent_id, folder_path):

    try:
        entries = sorted(
            os.listdir(folder_path),
            key=lambda item: (
                not os.path.isdir(
                    os.path.join(folder_path, item)
                ),
                item.lower()
            )
        )

    except PermissionError:
        return

    for name in entries:

        # Ignore Python cache
        if name == "__pycache__":
            continue

        full_path = os.path.join(
            folder_path,
            name
        )

        if os.path.isdir(full_path):

            folder_id = project_tree.insert(
                parent_id,
                "end",
                text=f"📁 {name}",
                open=False
            )

            tree_paths[folder_id] = full_path

            # Add dummy child so the folder can expand
            project_tree.insert(
                folder_id,
                "end",
                text="Loading..."
            )

        else:

            file_id = project_tree.insert(
                parent_id,
                "end",
                text=f"📄 {name}"
            )

            tree_paths[file_id] = full_path


def expand_folder(event=None):

    item_id = project_tree.focus()

    if not item_id:
        return

    path = tree_paths.get(item_id)

    if not path or not os.path.isdir(path):
        return

    children = project_tree.get_children(item_id)

    # Remove placeholder
    for child in children:

        if project_tree.item(child, "text") == "Loading...":

            project_tree.delete(child)

    # Populate only once
    if not project_tree.get_children(item_id):

        populate_folder(
            item_id,
            path
        )


def refresh_project():

    global tree_paths

    tree_paths.clear()

    for item in project_tree.get_children():

        project_tree.delete(item)

    root_id = project_tree.insert(
        "",
        "end",
        text="◆  NEO Iot-DSL",
        open=True
    )

    tree_paths[root_id] = PROJECT_ROOT

    populate_folder(
        root_id,
        PROJECT_ROOT
    )

    set_status(
        "Project explorer refreshed",
        GREEN
    )


def on_project_double_click(event=None):

    item_id = project_tree.focus()

    if not item_id:
        return

    path = tree_paths.get(item_id)

    if not path:
        return

    if os.path.isdir(path):

        expand_folder()

    else:

        load_file(path)


# ============================================================
# COMPILE
# ============================================================

def compile_program():

    program = program_text.get(
        "1.0",
        tk.END
    )

    clear_output()

    status_text.set("Compiling...")

    status_indicator.configure(
        text="● COMPILING",
        foreground=ORANGE
    )

    root.update_idletasks()

    temp_file = os.path.join(
        PROJECT_ROOT,
        "App",
        "temp_program.iot"
    )

    try:

        with open(
            temp_file,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(program)

        tree, errors = parse_file(temp_file)

        # -----------------------------
        # Errors
        # -----------------------------

        if errors:

            status_text.set(
                "Compilation failed"
            )

            status_indicator.configure(
                text="● ERROR",
                foreground=RED
            )

            insert_output(
                "COMPILATION FAILED\n",
                "error_title"
            )

            insert_output(
                "────────────────────────────────────\n\n",
                "separator"
            )

            insert_output(
                f"{len(errors)} syntax error(s) found.\n\n",
                "error"
            )

            for error in errors:

                insert_output(
                    "✗ ",
                    "error"
                )

                insert_output(
                    error + "\n",
                    "error"
                )

            insert_output(
                "\nFix the errors in the editor and compile again.",
                "dim"
            )

            notebook.select(output_frame)

            return

        # -----------------------------
        # Success
        # -----------------------------

        status_text.set(
            "Compilation successful"
        )

        status_indicator.configure(
            text="● READY",
            foreground=GREEN
        )

        insert_output(
            "COMPILATION SUCCESSFUL\n",
            "success_title"
        )

        insert_output(
            "────────────────────────────────────\n\n",
            "separator"
        )

        insert_output(
            "✓ Syntax valid\n",
            "success"
        )

        insert_output(
            "✓ No syntax errors found\n",
            "success"
        )

        insert_output(
            "✓ Parse tree generated\n\n",
            "success"
        )

        insert_output(
            "The IoT program successfully passed "
            "the frontend parser.\n\n",
            "normal"
        )

        parse_tree_text.configure(
            state="normal"
        )

        parse_tree_text.delete(
            "1.0",
            tk.END
        )

        parse_tree_text.insert(
            "1.0",
            tree.toStringTree()
        )

        parse_tree_text.configure(
            state="disabled"
        )

        notebook.select(output_frame)

    except Exception as error:

        status_text.set(
            "Application error"
        )

        status_indicator.configure(
            text="● ERROR",
            foreground=RED
        )

        insert_output(
            "APPLICATION ERROR\n\n",
            "error_title"
        )

        insert_output(
            str(error),
            "error"
        )


# ============================================================
# CLEAR EDITOR
# ============================================================

def clear_editor():

    global current_file

    program_text.delete(
        "1.0",
        tk.END
    )

    current_file = None

    file_tab.configure(
        text="  ●  main.iot"
    )

    clear_output()

    parse_tree_text.configure(
        state="normal"
    )

    parse_tree_text.delete(
        "1.0",
        tk.END
    )

    parse_tree_text.configure(
        state="disabled"
    )

    status_text.set("Ready")

    status_indicator.configure(
        text="● READY",
        foreground=GREEN
    )

    update_line_numbers()
    highlight_syntax()


# ============================================================
# LOAD EXAMPLE
# ============================================================

def load_example():

    example_program = """DEVICE LED PIN 2
DEVICE TEMP PIN 34

READ TEMP

IF TEMP > 30
    LED ON
ELSE
    LED OFF
END

LOOP 3
    LED ON
    WAIT 500
    LED OFF
    WAIT 500
END
"""

    program_text.delete(
        "1.0",
        tk.END
    )

    program_text.insert(
        "1.0",
        example_program
    )

    update_line_numbers()
    highlight_syntax()

    set_status(
        "Example loaded",
        GREEN
    )


# ============================================================
# HEADER
# ============================================================

header = tk.Frame(
    root,
    bg=PANEL,
    height=65
)

header.pack(fill="x")
header.pack_propagate(False)


# Logo

logo_frame = tk.Frame(
    header,
    bg=PANEL
)

logo_frame.pack(
    side="left",
    padx=22
)


logo = tk.Label(
    logo_frame,
    text="◆",
    font=("Segoe UI", 24, "bold"),
    bg=PANEL,
    fg=BLUE
)

logo.pack(
    side="left",
    padx=(0, 10)
)


title_frame = tk.Frame(
    logo_frame,
    bg=PANEL
)

title_frame.pack(
    side="left"
)


title = tk.Label(
    title_frame,
    text="NEO Iot-DSL",
    font=FONT_TITLE,
    bg=PANEL,
    fg=TEXT
)

title.pack(anchor="w")


subtitle = tk.Label(
    title_frame,
    text="Domain-Specific Language for IoT",
    font=("Segoe UI", 9),
    bg=PANEL,
    fg=TEXT_DIM
)

subtitle.pack(anchor="w")


# Header buttons

header_right = tk.Frame(
    header,
    bg=PANEL
)

header_right.pack(
    side="right",
    padx=20
)


status_indicator = tk.Label(
    header_right,
    text="● READY",
    font=FONT_UI_BOLD,
    bg=PANEL,
    fg=GREEN
)

status_indicator.pack(
    side="left",
    padx=15
)


compile_button = tk.Button(
    header_right,
    text="▶  COMPILE",
    font=FONT_UI_BOLD,
    bg=GREEN_DARK,
    fg="white",
    activebackground=GREEN,
    activeforeground="white",
    relief="flat",
    borderwidth=0,
    padx=20,
    pady=8,
    cursor="hand2",
    command=compile_program
)

compile_button.pack(
    side="left",
    padx=5
)


clear_button = tk.Button(
    header_right,
    text="CLEAR",
    font=FONT_UI_BOLD,
    bg=PANEL_LIGHT,
    fg=TEXT,
    activebackground=BORDER,
    activeforeground=TEXT,
    relief="flat",
    borderwidth=0,
    padx=18,
    pady=8,
    cursor="hand2",
    command=clear_editor
)

clear_button.pack(
    side="left",
    padx=5
)


# ============================================================
# MAIN CONTENT
# ============================================================

content = tk.Frame(
    root,
    bg=BG
)

content.pack(
    fill="both",
    expand=True
)


# ============================================================
# PROJECT EXPLORER
# ============================================================

sidebar = tk.Frame(
    content,
    bg=PANEL,
    width=250
)

sidebar.pack(
    side="left",
    fill="y"
)

sidebar.pack_propagate(False)


explorer_header = tk.Frame(
    sidebar,
    bg=PANEL
)

explorer_header.pack(
    fill="x",
    padx=15,
    pady=(15, 8)
)


explorer_title = tk.Label(
    explorer_header,
    text="PROJECT EXPLORER",
    font=("Segoe UI", 9, "bold"),
    bg=PANEL,
    fg=TEXT_DIM
)

explorer_title.pack(
    side="left"
)


refresh_button = tk.Button(
    explorer_header,
    text="↻",
    font=("Segoe UI", 12, "bold"),
    bg=PANEL,
    fg=TEXT_DIM,
    activebackground=PANEL,
    activeforeground=TEXT,
    relief="flat",
    borderwidth=0,
    cursor="hand2",
    command=refresh_project
)

refresh_button.pack(
    side="right"
)


# Treeview style

style = ttk.Style()

style.theme_use("default")

style.configure(
    "Project.Treeview",
    background=PANEL,
    foreground=TEXT,
    fieldbackground=PANEL,
    borderwidth=0,
    font=("Segoe UI", 9),
    rowheight=25
)

style.map(
    "Project.Treeview",
    background=[
        ("selected", "#1f6feb")
    ],
    foreground=[
        ("selected", "white")
    ]
)


tree_frame = tk.Frame(
    sidebar,
    bg=PANEL
)

tree_frame.pack(
    fill="both",
    expand=True,
    padx=10
)


project_tree = ttk.Treeview(
    tree_frame,
    style="Project.Treeview",
    show="tree"
)

project_tree.pack(
    fill="both",
    expand=True
)


project_tree.bind(
    "<Double-1>",
    on_project_double_click
)


# ============================================================
# EDITOR AREA
# ============================================================

editor_area = tk.Frame(
    content,
    bg=EDITOR_BG
)

editor_area.pack(
    side="left",
    fill="both",
    expand=True
)


# Editor tabs

editor_tab_bar = tk.Frame(
    editor_area,
    bg=PANEL_LIGHT,
    height=40
)

editor_tab_bar.pack(fill="x")
editor_tab_bar.pack_propagate(False)


file_tab = tk.Label(
    editor_tab_bar,
    text="  ●  main.iot",
    font=FONT_UI_BOLD,
    bg=EDITOR_BG,
    fg=TEXT,
    padx=15
)

file_tab.pack(
    side="left",
    fill="y"
)


example_button = tk.Button(
    editor_tab_bar,
    text="Load Example",
    font=("Segoe UI", 9),
    bg=PANEL_LIGHT,
    fg=TEXT_DIM,
    activebackground=PANEL_LIGHT,
    activeforeground=TEXT,
    relief="flat",
    borderwidth=0,
    cursor="hand2",
    command=load_example
)

example_button.pack(
    side="right",
    padx=15
)


# Editor container

editor_container = tk.Frame(
    editor_area,
    bg=EDITOR_BG
)

editor_container.pack(
    fill="both",
    expand=True
)


# Line numbers

line_numbers = tk.Text(
    editor_container,
    width=5,
    padx=10,
    pady=15,
    bg=EDITOR_BG,
    fg="#484f58",
    insertbackground=EDITOR_BG,
    font=FONT_CODE,
    relief="flat",
    borderwidth=0,
    state="disabled",
    takefocus=0
)

line_numbers.pack(
    side="left",
    fill="y"
)


# Main editor

program_text = tk.Text(
    editor_container,
    bg=EDITOR_BG,
    fg=TEXT,
    insertbackground=TEXT,
    selectbackground="#264f78",
    selectforeground="white",
    font=FONT_CODE,
    relief="flat",
    borderwidth=0,
    padx=10,
    pady=15,
    undo=True,
    wrap="none"
)

program_text.pack(
    side="left",
    fill="both",
    expand=True
)


editor_scrollbar = ttk.Scrollbar(
    editor_container,
    orient="vertical",
    command=program_text.yview
)

editor_scrollbar.pack(
    side="right",
    fill="y"
)

program_text.configure(
    yscrollcommand=editor_scrollbar.set
)


# Syntax highlighting tags

program_text.tag_configure(
    "keyword",
    foreground=BLUE
)

program_text.tag_configure(
    "number",
    foreground=ORANGE
)

program_text.tag_configure(
    "operator",
    foreground=PURPLE
)

program_text.tag_configure(
    "comment",
    foreground=TEXT_DIM
)


# ============================================================
# DEFAULT EXAMPLE
# ============================================================

example_program = """DEVICE LED PIN 2
DEVICE TEMP PIN 34

READ TEMP

IF TEMP > 30
    LED ON
ELSE
    LED OFF
END

LOOP 3
    LED ON
    WAIT 500
    LED OFF
    WAIT 500
END
"""

program_text.insert(
    "1.0",
    example_program
)


# ============================================================
# EDITOR EVENTS
# ============================================================

program_text.bind(
    "<KeyRelease>",
    lambda event: (
        update_line_numbers(),
        highlight_syntax()
    )
)


# ============================================================
# COMPILER OUTPUT
# ============================================================

output_container = tk.Frame(
    root,
    bg=CONSOLE_BG,
    height=230
)

output_container.pack(
    fill="x"
)

output_container.pack_propagate(False)


notebook = ttk.Notebook(
    output_container
)

notebook.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=(8, 5)
)


# ============================================================
# OUTPUT TAB
# ============================================================

output_frame = tk.Frame(
    notebook,
    bg=CONSOLE_BG
)

notebook.add(
    output_frame,
    text="  COMPILER OUTPUT  "
)


output_text = tk.Text(
    output_frame,
    bg=CONSOLE_BG,
    fg=TEXT,
    font=FONT_CODE_SMALL,
    relief="flat",
    borderwidth=0,
    padx=15,
    pady=10,
    wrap="word",
    state="disabled"
)

output_text.pack(
    fill="both",
    expand=True
)


output_text.tag_configure(
    "success_title",
    foreground=GREEN,
    font=("Consolas", 10, "bold")
)

output_text.tag_configure(
    "success",
    foreground=GREEN
)

output_text.tag_configure(
    "error_title",
    foreground=RED,
    font=("Consolas", 10, "bold")
)

output_text.tag_configure(
    "error",
    foreground=RED
)

output_text.tag_configure(
    "separator",
    foreground=BORDER
)

output_text.tag_configure(
    "dim",
    foreground=TEXT_DIM
)

output_text.tag_configure(
    "normal",
    foreground=TEXT
)


# ============================================================
# PARSE TREE TAB
# ============================================================

parse_tree_frame = tk.Frame(
    notebook,
    bg=CONSOLE_BG
)

notebook.add(
    parse_tree_frame,
    text="  PARSE TREE  "
)


parse_tree_text = tk.Text(
    parse_tree_frame,
    bg=CONSOLE_BG,
    fg=CYAN,
    font=FONT_CODE_SMALL,
    relief="flat",
    borderwidth=0,
    padx=15,
    pady=10,
    wrap="word",
    state="disabled"
)

parse_tree_text.pack(
    fill="both",
    expand=True
)


# ============================================================
# STATUS BAR
# ============================================================

status_bar = tk.Frame(
    root,
    bg=PANEL_LIGHT,
    height=30
)

status_bar.pack(
    fill="x"
)

status_bar.pack_propagate(False)


status_text = tk.StringVar()

status_text.set("Ready")


status_label = tk.Label(
    status_bar,
    textvariable=status_text,
    font=("Segoe UI", 9),
    bg=PANEL_LIGHT,
    fg=TEXT_DIM
)

status_label.pack(
    side="left",
    padx=15
)


status_right = tk.Frame(
    status_bar,
    bg=PANEL_LIGHT
)

status_right.pack(
    side="right",
    padx=15
)


target_label = tk.Label(
    status_right,
    text="ESP32",
    font=("Segoe UI", 9, "bold"),
    bg=PANEL_LIGHT,
    fg=CYAN
)

target_label.pack(
    side="left",
    padx=15
)


parser_label = tk.Label(
    status_right,
    text="ANTLR 4.13.2",
    font=("Segoe UI", 9),
    bg=PANEL_LIGHT,
    fg=TEXT_DIM
)

parser_label.pack(
    side="left",
    padx=15
)


python_label = tk.Label(
    status_right,
    text="Python",
    font=("Segoe UI", 9),
    bg=PANEL_LIGHT,
    fg=TEXT_DIM
)

python_label.pack(
    side="left",
    padx=15
)


# ============================================================
# INITIAL PROJECT TREE
# ============================================================

refresh_project()

update_line_numbers()
highlight_syntax()


# ============================================================
# START APPLICATION
# ============================================================

root.mainloop()