import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageDraw

class FloorPlanGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Floor Plan Generator")

        # Create a frame to contain all elements
        self.frame = ttk.Frame(root, padding="20")
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
        floor_plan_image = self.generate_floor_plan_image(area)

        # Display the image
        floor_plan_image.show()
        
    def generate_floor_plan_image(self, area):
        # Create a white image with dimensions based on user input
        #image = Image.new("RGB", (int(width), int(height)), "white")
        additional_info = self.text_additional_info.get("1.0", tk.END).strip()
        if(additional_info=="double bedroom"):
            if(area>=1 and area<=900):
                image = Image.open(r"C:\pic\picture.jpeg.jpg") 
            elif(area>950 and area<=1000):
                image = Image.open(r"C:\pic\doublebedroom1000.jpg") 
            elif(area>1000 and area<=1300):
                image = Image.open(r"C:\pic\DB1300.jpg") 
            elif(area>1300 and area<=1350):
                image = Image.open(r"C:\pic\db1350.jpg") 
            elif(area>900 and area<=950):
                image = Image.open(r"C:\pic\DB950.jpg") 
            elif(area>1900):
                image = Image.open(r"C:\pic\DB2000.jpg") 
            elif(area>1700 and area<=1900):
                image = Image.open(r"C:\pic\DB1900.jpg") 
            elif(area>1350 and area<=1400):
                image = Image.open(r"C:\pic\DB1400.jpg") 
            elif(area>1400 and area<=1700):
                image = Image.open(r"C:\pic\DB1700.jpg") 
                
            
        if(additional_info=="function hall"):
            if(area==5000):
                image=Image.open(r"C:\pic\FH5000.jpg")
            elif(area==4500):
                image=Image.open(r"C:\pic\FH4500.jpg")
            elif(area>=1 and area<=3000):
                image=Image.open(r"C:\pic\FH3000.jpg")
            elif(area>3000 and area<=3500):
                image=Image.open(r"C:\pic\FH3500.jpg")
            elif(area==5500):
                image=Image.open(r"C:\pic\FH5500.jpg")
            else:
                image=Image.open(r"C:\pic\FHD.jpg")
                
                
        if(additional_info=="single bedroom"):
            if(area>700 and area<=800):
                image=Image.open(r"C:\pic\SB800.jpg")
            elif(area>=1 and area<=650):
                image=Image.open(r"C:\pic\SB650.jpg")
            elif(area>650 and area<=700):
                image=Image.open(r"C:\pic\SB700.jpg")
            elif(area>800 and area<=850):
                image=Image.open(r"C:\pic\SB850.jpg")
            elif(area>850):
                image=Image.open(r"C:\pic\SB1850.jpg")
        
        
        if(additional_info=="theatre"):
            if(area>900 and area<=1000):
                image=Image.open(r"C:\pic\TH1000.jpg")
            elif(area>2000 and area<=2500):
                image=Image.open(r"C:\pic\TH2500.jpg")
            elif(area>=1 and area<=800):
                image=Image.open(r"C:\pic\TH800.jpg")
            elif(area>850 and area<=900):
                image=Image.open(r"C:\pic\TH900.jpg")
            elif(area>1000 and area<=1500):
                image=Image.open(r"C:\pic\TH1500.jpg")
            elif(area>2500 and area<=3000):
                image=Image.open(r"C:\pic\TH3000.jpg")
            elif(area>3000):
                image=Image.open(r"C:\pic\TH3500.jpg")
            elif(area>1500 and area<=2000):
                image=Image.open(r"C:\pic\TH2000.jpg")
            elif(area>800 and area<=850):
                image=Image.open(r"C:\pic\TH850.jpg")
            
        
        if(additional_info=="triple bedroom"):
            if(area>1200 and area<=1500):
                image=Image.open(r"C:\pic\TB1500.jpg")
            elif(area>1700 and area<=1800):
                image=Image.open(r"C:\pic\TB1800.jpg")
            elif(area>1950):
                image=Image.open(r"C:\pic\TB2000.jpg")
            elif(area>=1 and area<=1200):
                image=Image.open(r"C:\pic\TB1200.jpg")
            elif(area>1500 and area<=1600):
                image=Image.open(r"C:\pic\TB1600.jpg")
            elif(area>1800 and area<=1850):
                image=Image.open(r"C:\pic\TB1850.jpg")
            elif(area>1850 and area<=1950):
                image=Image.open(r"C:\pic\TB1950.jpg")
            elif(area>1600 and area<=1700):
                image=Image.open(r"C:\pic\TB1700.jpg")
        
        if(additional_info=="office"):
            if(area>1800 and area<=2000):
                image=Image.open(r"C:\pic\OF2000.jpg")
            elif(area>2000 and area<=2500):
                image=Image.open(r"C:\pic\OF2500.jpg")
            elif(area>=1 and area<=1600):
                image=Image.open(r"C:\pic\OF1600.jpg")
            elif(area>2500 and area<=2700):
                image=Image.open(r"C:\pic\OF2700.jpg")
            elif(area>2700 and area<=4000):
                image=Image.open(r"C:\pic\OF4000.jpg")
            elif(area>=4000):
                image=Image.open(r"C:\pic\OF4500.jpg")
            elif(area>1600 and area<=1800):
                image=Image.open(r"C:\pic\OF1800.jpg")
        
        
        if(additional_info=="restaurant"):
            if(area>=1 and area<=1500):
                image=Image.open(r"C:\pic\RT1500.jpg")
            elif(area>1500 and area<=2000):
                image=Image.open(r"C:\pic\RT2000.jpg")
            elif(area>2000 and area<=2500):
                image=Image.open(r"C:\pic\RT2500.jpg")
            elif(area>2500 and area<=3000):
                image=Image.open(r"C:\pic\RT3000.jpg")
            elif(area>3000 and area<=3500):
                image=Image.open(r"C:\pic\RT3500.jpg")
            elif(area>=3500):
                image=Image.open(r"C:\pic\RT4000.jpg")
        draw = ImageDraw.Draw(image)

        return image
 
if __name__ == "__main__":
    root = tk.Tk()
    app = FloorPlanGeneratorApp(root)
    root.mainloop()