from pdf2image import convert_from_path

file_name = f"teaser"
pdf_path = f'./{file_name}.pdf'

if __name__ == "__main__":

    images = convert_from_path(pdf_path, dpi=300)
    image = images[0]
    image.save(f'./{file_name}.png', 'PNG')

