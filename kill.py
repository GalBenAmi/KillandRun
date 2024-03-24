import tkinter as tk
from tkinter import messagebox

entry = None
listbox = None

def generate_batch_script(program_names):
    script_lines = [
        "@echo off",
        ":: Kill specified programs using taskkill /IM (ignoring errors if the program doesn't exist)"
    ]
    
    for program_name in program_names:
        script_lines.append(f'taskkill /IM "{program_name}" /T /F 2>nul || echo {program_name} not found or already terminated')
    
    script_lines.extend([
        "echo Programs killed successfully.",
        ":: Wait for 3 seconds before closing the window",
        "timeout /t 3 /nobreak >nul"
    ])

    return "\n".join(script_lines)

def generate_script_and_save(program_names):
    script_content = generate_batch_script(program_names)
    with open("kill_programs.bat", "w") as script_file:
        script_file.write(script_content)
    messagebox.showinfo("Script Generated", "Batch script 'kill_programs.bat' generated successfully.")

def add_program():
    global entry
    global listbox
    
    program_name = entry.get()
    if program_name.strip():
        listbox.insert(tk.END, program_name + ".exe")
        entry.delete(0, tk.END)

def remove_program():
    global listbox
    
    selected_index = listbox.curselection()
    if selected_index:
        listbox.delete(selected_index)

def main():
    global entry
    global listbox
    
    window = tk.Tk()
    window.title("Program Termination Script Generator")

    label = tk.Label(window, text="Enter program names (without .exe) and click 'Add':")
    label.pack(pady=5)

    entry = tk.Entry(window, width=30)
    entry.pack(pady=5)

    add_button = tk.Button(window, text="Add", command=add_program)
    add_button.pack(pady=5)

    remove_button = tk.Button(window, text="Remove", command=remove_program)
    remove_button.pack(pady=5)

    listbox = tk.Listbox(window, width=40, height=10)
    listbox.pack(pady=5)

    generate_button = tk.Button(window, text="Generate Script", command=lambda: generate_script_and_save(listbox.get(0, tk.END)))
    generate_button.pack(pady=5)

    window.mainloop()

if __name__ == "__main__":
    main()
