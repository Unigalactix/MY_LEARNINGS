import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text() + '\n'
    return text

pdf_path = 'AI Engineer/ai-engineer.pdf'
output_path = 'AI Engineer/ai-engineer.txt'

text = extract_text_from_pdf(pdf_path)

with open(output_path, 'w') as output_file:
    output_file.write(text)

print(f"Text extracted and saved to {output_path}")
