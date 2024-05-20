import fitz  # PyMuPDF
import pandas as pd
import os

# Função para extrair texto de cada página e salvar em arquivos TXT
def extract_and_save_text(pdf_path, output_dir):
    # Abrir o arquivo PDF
    pdf_document = fitz.open(pdf_path)
    
    # Verificar se o diretório de saída existe, caso contrário, criá-lo
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Iterar por cada página do PDF
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text = page.get_text("text")
        
        # Nome do arquivo de saída
        output_file_path = os.path.join(output_dir, f"page_{page_num + 1}.txt")
        
        # Salvar o texto extraído em um arquivo TXT
        with open(output_file_path, "w", encoding="utf-8") as output_file:
            output_file.write(text)
        
        print(f"Página {page_num + 1} salva em {output_file_path}")

# Caminho do arquivo PDF e diretório de saída
pdf_path = "caminho/para/seu/arquivo.pdf"
output_dir = "caminho/para/diretorio/de/saida"

# Chamar a função para extrair e salvar texto
extract_and_save_text(pdf_path, output_dir)
