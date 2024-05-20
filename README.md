# Ler_Pdf
Para extração de informações de aquivo pdf em Python e extrair as mesmas em txt, para depois realizar analises.

Para ler um arquivo PDF que contém tabelas, dividir por página e salvar as informações em arquivos TXT separados, você pode usar uma biblioteca PyMuPDF(também conhecida como fitz) para lidar com PDFs e uma biblioteca pandaspara manipulação de dados, especialmente se precisar lidar com tabelas.


Instalação de bibliotecas com permissão
Para rodar o script, você precisa instalar as bibliotecas PyMuPDFe pandas. Você pode convidá-los usando o pip:

pip install pymupdf pandas


Explicação do script

Importações: Importa as bibliotecas possíveis.

Função extract_and_save_text:

Abra o arquivo PDF usando fitz.open.

Cria o diretório de saída se ele não existir.

Itera por cada página no PDF, extrai o texto e salva em um arquivo TXT separado.

Variáveis ​​de caminho: Define o caminho do PDF e o diretório de saída.

Chamada da função: Chama a função extract_and_save_textcom os caminhos fornecidos.

Esse script vai criar arquivos TXT sem diretório especificado, cada um contendo o texto de uma página do PDF. Se o PDF contém tabelas em formato de texto, essas tabelas serão extraídas no formato de texto bruto. Para um processamento mais sofisticado de tabelas (por exemplo, se precisar de conversor de tabelas em DataFrames do pandas), seria necessário um processamento adicional usando bibliotecas como pdfplumberou camelot-py.
