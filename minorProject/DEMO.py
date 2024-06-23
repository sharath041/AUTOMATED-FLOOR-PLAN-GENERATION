import tkinter as tk
from tkinter import ttk
from deepLearningModel import generate_floor_plan_image

class FloorPlanGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Floor Plan Generator")

        # Create a frame to contain all elements
        self.frame = ttk.Frame(root, padding="50")
        self.frame.pack(fill="both", expand=True)

        # Input fields
        ttk.Label(self.frame, text="Dimensions:").grid(row=0, column=0, columnspan=2, pady=(0, 10))

        self.label_width = ttk.Label(self.frame, text="Area:")
        self.label_width.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_width = ttk.Entry(self.frame)
        self.entry_width.grid(row=1, column=1, padx=5, pady=5)


        # Additional information
        ttk.Label(self.frame, text="Additional Information:", font=("Helvetica", 12, "bold")).grid(row=4, column=0, columnspan=2, pady=(20, 10))

        self.text_additional_info = tk.Text(self.frame, width=40, height=5)
        self.text_additional_info.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        # Button to trigger model generation
        self.generate_button = ttk.Button(self.frame, text="Generate Floor Plan", command=self.generate_model)
        self.generate_button.grid(row=6, column=0, columnspan=2, pady=20)
    

    def generate_model(self):
    # Retrieve user input from entry fields
        area = float(self.entry_width.get())

    # Retrieve additional unstructured information
        additional_info = self.text_additional_info.get("1.0", tk.END).strip()


    # Create floor plan image
        floor_plan_image = generate_floor_plan_image(area, additional_info)

    # Display the image
        floor_plan_image.show()
       

if __name__ == "__main__":
    root = tk.Tk()
    app = FloorPlanGeneratorApp(root)
    root.mainloop()

