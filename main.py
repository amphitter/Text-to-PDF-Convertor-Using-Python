from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def text_to_pdf(input_file, output_file):
    # Create a canvas
    c = canvas.Canvas(output_file, pagesize=letter)

    # Set up fonts
    c.setFont("Helvetica", 12)

    try:
        # Read text from the input file
        with open(input_file, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Error: Input file not found.")
        return

    # Write text to PDF
    y = 750  # Starting y position
    for line in lines:
        c.drawString(50, y, line.strip())
        y -= 15  # Move to the next line

    # Save the PDF
    c.save()
    print("PDF created successfully!")

if __name__ == "__main__":
    input_file = input("Enter the path of the text file: ")
    output_file = input("Enter the desired path for the PDF file: ")
#end of code
    text_to_pdf(input_file, output_file)
