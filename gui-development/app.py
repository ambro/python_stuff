import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox


def greet():
    print('Hello. world')


# greet_button = ttk.Button(root, text="Greet", command=greet)
# greet_button.pack(sid="left", fill="x", expand=True)
# quit_button = ttk.Button(root, text="Quit", command=root.destroy)
# quit_button.pack(sid="left", fill="x", expand=True)
#
# user_name = tk.StringVar()
# name_label = ttk.Label(root, text="Name: ")
# name_label.pack(side="left", padx=(0, 10))
# name_entry = ttk.Entry(root, width=15, textvariable=user_name)
# name_entry.pack(side="left")
# name_entry.focus()

# name_label = tk.Label(main, text="Label1", bg="red").pack(side="top", fill="both", expand="True")
# name_label = tk.Label(main, text="Label2", bg="red").pack(side="top", fill="both", expand="True")
#
# name_label = tk.Label(root, text="Label3", bg="green").pack(side="left", fill="both", expand="True")

text_contents = dict()


def check_for_changes():
    tab_widget = get_tab_widget()
    current = get_text_widget(tab_widget)
    content = current.get("1.0", "end-1c")
    name = notebook.tab("current")["text"]

    if hash(content) != text_contents[str(current)]:
        if name[-1] != "*":
            notebook.tab("current", text=name + "*")
    elif name[-1] == "*":
        notebook.tab("current", text=name[:-1])


def get_text_widget(tab_widget):
    text_widget = tab_widget.winfo_children()[0]
    return text_widget


def get_tab_widget():
    return root.nametowidget(notebook.select())


def get_text_widget_content(text_widget):
    return text_widget.get("1.0", "end-1c")


def has_unsaved_content(text_widget):
    content = get_text_widget_content(text_widget)
    return hash(content) != text_contents[str(text_widget)]


def create_file(content="", title="Untitled"):
    container = ttk.Frame(notebook)
    container.pack()

    text_area = tk.Text(container)
    text_area.insert("end", content)
    text_area.pack(side="left", fill="both", expand=True)
    notebook.add(container, text=title)
    notebook.select(container)

    key = str(text_area)
    text_contents[key] = hash(content)

    text_scroll = ttk.Scrollbar(container, orient="vertical", command=text_area.yview)
    text_scroll.pack(side="right", fill="y")
    text_area["yscrollcommand"] = text_scroll.set


def save_file():
    file_path = filedialog.asksaveasfilename()

    try:
        filename = os.path.basename(file_path)
        tab_widget = get_tab_widget()
        text_widget = get_text_widget(tab_widget)
        content = get_text_widget_content(text_widget)

        with open(file_path, "w") as file:
            file.write(content)

    except (AttributeError, FileNotFoundError):
        print("Save operation cancelled")
        return

    notebook.tab("current", text=filename)
    text_contents[str(text_widget)] = hash(content)


def open_file():
    file_path = filedialog.askopenfilename()

    try:
        filename = os.path.basename(file_path)
        with open(file_path, "r") as file:
            content = file.read()

    except (AttributeError, FileNotFoundError):
        print("Open operation cancelled")
        return

    create_file(content, filename)


def confirm_quit():
    unsaved = False

    for tab in notebook.tabs():
        tab_widget = root.nametowidget(tab)
        text_widget = get_text_widget(tab_widget)
        if has_unsaved_content(text_widget):
            unsaved = True
            break

    if not unsaved or confirm_close():
        root.destroy()


def close_current_tab():
    tab_widget = get_tab_widget()
    text_widget = get_text_widget(tab_widget)
    if not has_unsaved_content(text_widget) or confirm_close():
        notebook.forget(tab_widget)

    if len(notebook.tabs()) == 0:
        create_file()


def confirm_close():
    return messagebox.askyesno(
        message="Unsaved changes detected. Sure you wanna close exit?",
        icon="question",
        title="Possible loss of data alert"
    )


def show_about_info():
    messagebox.showinfo(
        title="About",
        message="This is a tribute, oh, to The Greatest Editor in the World"
    )


root = tk.Tk()
root.title('Text editor')
root.option_add("*tearOff", False)

main = ttk.Frame(root)
main.pack(side="left", fill="both", expand=True, padx=1, pady=(4, 0))

menubar = tk.Menu()
root.config(menu=menubar)

file_menu = tk.Menu(menubar)
help_menu = tk.Menu(menubar)
menubar.add_cascade(menu=file_menu, label="File")
menubar.add_cascade(menu=help_menu, label="Help")

file_menu.add_command(label="New", command=create_file, accelerator="Ctrl+N")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+O")
file_menu.add_command(label="Open...", command=open_file, accelerator="Ctrl+S")
file_menu.add_command(label="Close Tab", command=close_current_tab, accelerator="Ctrl+Q")
file_menu.add_command(label="Exit", command=confirm_quit)

help_menu.add_command(label="About", command=show_about_info)

notebook = ttk.Notebook(main)
notebook.pack(fill="both", expand=True)
create_file()

root.bind("<KeyPress>", lambda event: check_for_changes())
root.bind("<Control-n>", lambda event: create_file())
root.bind("<Control-o>", lambda event: open_file())
root.bind("<Control-q>", lambda event: close_current_tab())
root.bind("<Control-s>", lambda event: save_file())

root.mainloop()


