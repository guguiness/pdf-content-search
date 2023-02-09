import PyPDF2
import os

class PdfContentSearch:

    @staticmethod
    def search_pdf(folder, search_key):
        found_files = []
        for filename in os.listdir(folder):
            if filename.endswith(".pdf"):
                pdf_file = os.path.join(folder, filename)
                with open(pdf_file, 'rb') as file:
                    pdf_reader = PyPDF2.PdfReader(file)
                    pages = pdf_reader.pages
                    for i, page in enumerate(pages):
                        text = page.extract_text()
                        if search_key in text[:]:
                            found_files.append(filename)
                            break
        if found_files:
            print(f"A chave '{search_key}' foi encontrada nos arquivos:")
            for filename in found_files:
                print(f"- {filename}")
        else:
            print(f"A chave '{search_key}' não foi encontrada em nenhum arquivo.")

pasta = input('Qual o caminho absoluto da pasta onde os arquivos se encontram? Digite: ')
chave = input('Qual o termo que deseja buscar nos arquivos? Digite: ')
PdfContentSearch.search_pdf(pasta, chave)