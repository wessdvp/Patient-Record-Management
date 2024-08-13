# importing dependencies
import tkinter as tk
from tkinter import messagebox

# class definition
class PatientManager:
    def __init__(self, root):
        # list to store patient records
        self.patients = []
        # dictionary to temporarily hold data for current patient
        self.patient_data = {}
        # tracking field currently being filled out
        self.field_index = 0
        # tuples: prompt string + key
        self.fields = [
            ("Enter patient name:", "Name"),
            ("Enter patient age:", "Age"),
            ("Enter patient gender (M/F):", "Gender"),
            ("Enter medical history:", "Medical History")
        ]
        # the main window settings
        self.root = root
        self.root.title("Patient Record Management")
        self.root.geometry("400x300")  # Adjust window size as needed

        # main screen elements
        self.addpatient_button = tk.Button(root, text="Add Patient", command=self.add_patient)
        self.addpatient_button.pack(pady=10)

        self.retpatient_button = tk.Button(root, text="Retrieve Patient", command=self.retrieve_patient)
        self.retpatient_button.pack(pady=10)

        self.view_list_button = tk.Button(root, text="View Patient List", command=self.create_patient_list_window)
        self.view_list_button.pack(pady=10)

        # this block uses the len function to calculate total patients and show the number
        self.total_patients_label = tk.Label(root, text=f"Total Patients: {len(self.patients)}")
        self.total_patients_label.pack(pady=10)

        # Input field elements (initially hidden)
        self.field_label = tk.Label(root, text="")
        self.entry_field = tk.Entry(root)
        self.next_button = tk.Button(root, text="Next", command=self.next_button_click)

    def add_patient(self):
        # hide the main menu widgets
        self.clear_main_menu_widgets()
        self.field_index = 0
        self.patient_data = {}
        self.show_next_field()

    # checks if there are more fields to display.
    # if there are, it shows the current field's prompt
    # and input box.
    def show_next_field(self):
        if self.field_index < len(self.fields):
            self.field_label.config(text=self.fields[self.field_index][0])
            self.entry_field.delete(0, tk.END)
            self.field_label.pack(pady=10)
            self.entry_field.pack(pady=10)
            self.next_button.pack(pady=10)
        else:
            self.patient_data[self.fields[self.field_index - 1][1]] = self.entry_field.get()
            self.patients.append(self.patient_data.copy())
            messagebox.showinfo("Success", f"Patient {self.patient_data['Name']} added successfully.")
            self.update_total_patients_label()
            self.reset_to_main_menu()

    # gets the current field’s value
    # from the input box and validates it.
    def next_button_click(self):
        if self.field_index < len(self.fields):
            current_field_name = self.fields[self.field_index][1]
            current_value = self.entry_field.get().strip()

            if current_field_name == "Gender" and current_value not in ["M", "F"]:
                messagebox.showerror("Error", "Please enter 'M' for Male or 'F' for Female.")
            else:
                self.patient_data[current_field_name] = current_value
                self.field_index += 1
                if self.field_index < len(self.fields):
                    self.show_next_field()
                else:
                    # Add patient and return to main menu
                    self.patient_data[self.fields[self.field_index - 1][1]] = self.entry_field.get()
                    self.patients.append(self.patient_data.copy())
                    messagebox.showinfo("Success", f"Patient {self.patient_data['Name']} added successfully.")
                    self.update_total_patients_label()
                    self.reset_to_main_menu()

    # updates the label displaying the total number of patients
    # by recalculating the length of the self.patients list.
    def update_total_patients_label(self):
        self.total_patients_label.config(text=f"Total Patients: {len(self.patients)}")

    # clears all temp stuff and goes back to main
    def reset_to_main_menu(self):
        # Clear the temporary widgets and show the main menu buttons
        self.field_label.pack_forget()
        self.entry_field.pack_forget()
        self.next_button.pack_forget()
        self.addpatient_button.pack(pady=10)
        self.retpatient_button.pack(pady=10)
        self.view_list_button.pack(pady=10)
        self.total_patients_label.pack(pady=10)

    # destroys any temp widgets that are not needed
    def clear_temp_widgets(self):
        # Clear widgets related to specific operations
        if hasattr(self, 'search_label'):
            self.search_label.pack_forget()
            self.search_entry.pack_forget()
            self.search_button.pack_forget()
            del self.search_label
            del self.search_entry
            del self.search_button

        if hasattr(self, 'info_window'):
            self.info_window.destroy()
            del self.info_window

        if hasattr(self, 'list_window'):
            self.list_window.destroy()
            del self.list_window

        if hasattr(self, 'info_label'):
            self.info_label.pack_forget()
            del self.info_label

        if hasattr(self, 'return_button'):
            self.return_button.pack_forget()
            del self.return_button

    # search function
    def retrieve_patient(self):
        self.clear_main_menu_widgets()

        self.search_label = tk.Label(self.root, text="Enter patient name to search:")
        self.search_entry = tk.Entry(self.root)
        self.search_button = tk.Button(self.root, text="Search", command=self.search_patient)

        self.search_label.pack(pady=10)
        self.search_entry.pack(pady=10)
        self.search_button.pack(pady=10)

    def search_patient(self):
        search_name = self.search_entry.get().strip().lower()
        found_patient = next((patient for patient in self.patients if patient["Name"].lower() == search_name), None)

        if found_patient:
            self.show_patient_info(found_patient)
        else:
            messagebox.showerror("Error", "This patient doesn't exist.")

    # show patient info list thing
    def show_patient_info(self, patient):
        self.clear_main_menu_widgets()

        self.info_window = tk.Toplevel(self.root)
        self.info_window.title("Patient Information")
        self.info_window.geometry("300x200")

        info_text = (f"Name: {patient['Name']}\n"
                     f"Age: {patient['Age']}\n"
                     f"Gender: {patient['Gender']}\n"
                     f"Medical History: {patient['Medical History']}")

        self.info_label = tk.Label(self.info_window, text=info_text, padx=10, pady=10)
        self.info_label.pack()

        self.return_button = tk.Button(self.info_window, text="← Return to Main Menu", command=self.return_to_main_menu)
        self.return_button.pack(pady=10, anchor="w", padx=10)

# actual patient list window, using a top (new) window
    def create_patient_list_window(self):
        self.clear_main_menu_widgets()

        self.list_window = tk.Toplevel(self.root)
        self.list_window.title("List of Registered Patients")
        self.list_window.geometry("400x300")

        self.list_label = tk.Label(self.list_window, text="List of Registered Patients", font=("Helvetica", 12))
        self.list_label.pack(pady=5, anchor="w", padx=10)

        self.patient_listbox = tk.Listbox(self.list_window, width=50, height=15)
        self.patient_listbox.pack(pady=10)

        for patient in self.patients:
            self.patient_listbox.insert(tk.END, patient["Name"])

        self.patient_listbox.bind("<Double-1>", self.on_patient_listbox_double_click)

        self.return_button = tk.Button(self.list_window, text="←", command=self.return_to_main_menu)
        self.return_button.pack(pady=5, anchor="w", padx=10)

    def on_patient_listbox_double_click(self, event):
        selected_name = self.patient_listbox.get(self.patient_listbox.curselection())
        found_patient = next((patient for patient in self.patients if patient["Name"] == selected_name), None)
        if found_patient:
            self.show_patient_info(found_patient)

    def return_to_main_menu(self):
        self.clear_temp_widgets()
        self.addpatient_button.pack(pady=10)
        self.retpatient_button.pack(pady=10)
        self.view_list_button.pack(pady=10)
        self.total_patients_label.pack(pady=10)

    def clear_main_menu_widgets(self):
        self.addpatient_button.pack_forget()
        self.retpatient_button.pack_forget()
        self.view_list_button.pack_forget()
        self.total_patients_label.pack_forget()


# Create the main window
window = tk.Tk()
app = PatientManager(window)

# Start the Tkinter event loop
window.mainloop()
