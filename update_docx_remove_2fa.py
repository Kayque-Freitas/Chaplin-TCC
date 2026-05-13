import docx
import sys

def remove_2fa_section(file_path):
    doc = docx.Document(file_path)
    
    # We want to remove the paragraph that mentions "Autenticação de Dois Fatores (2FA) e Verificação de E-mail"
    # To delete a paragraph in python-docx:
    for para in doc.paragraphs:
        if "Autenticação de Dois Fatores (2FA) e Verificação de E-mail" in para.text:
            p = para._element
            p.getparent().remove(p)
            para._p = para._element = None

    doc.save("TCC_CHAPLIN-Corrigido_05-05_Atualizado.docx")
    print("2FA section successfully removed from docx.")

if __name__ == "__main__":
    remove_2fa_section(sys.argv[1])
