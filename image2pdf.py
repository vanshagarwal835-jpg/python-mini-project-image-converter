import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

# Function to select images
def select_images():
    global file_paths
    file_paths = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.tiff")]
    )
    if file_paths:
        messagebox.showinfo("Selected", f"{len(file_paths)} images selected.")

# Function to convert selected images to PDF
def convert_to_pdf():
    if not file_paths:
        messagebox.showerror("Error", "No images selected!")
        return

    images = []
    for file in file_paths:
        img = Image.open(file)
        # Convert to RGB if needed
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        images.append(img)

    save_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")],
        title="Save PDF As"
    )

    if save_path:
        try:
            images[0].save(save_path, save_all=True, append_images=images[1:])
            messagebox.showinfo("Success", f"✅ PDF saved successfully at:\n{save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create PDF.\n{e}")

# GUI Setup
root = tk.Tk()
root.title("🖼️ Image to PDF Converter")
root.geometry("350x220")
root.resizable(False, False)
root.config(bg="#f0f0f0")

# Title label
title_label = tk.Label(
    root,
    text="Image to PDF Converter",
    font=("Arial", 16, "bold"),
    bg="#f0f0f0",
    fg="#333"
)
title_label.pack(pady=20)

# Buttons
select_btn = tk.Button(
    root,
    text="Select Images",
    command=select_images,
    width=20,
    height=2,
    bg="#4a90e2",
    fg="white",
    font=("Arial", 10, "bold")
)
select_btn.pack(pady=10)

convert_btn = tk.Button(
    root,
    text="Convert to PDF",
    command=convert_to_pdf,
    width=20,
    height=2,
    bg="#2ecc71",
    fg="white",
    font=("Arial", 10, "bold")
)
convert_btn.pack(pady=10)

# Footer label
footer = tk.Label(
    root,
    text="Made with ❤️ in Python",
    font=("Arial", 9),
    bg="#f0f0f0",
    fg="#777"
)
footer.pack(side="bottom", pady=10)

# Global variable for file paths
file_paths = []

# Run the app
root.mainloop()
