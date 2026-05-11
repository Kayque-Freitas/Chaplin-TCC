import zipfile
import xml.etree.ElementTree as ET
import sys

docx_path = sys.argv[1]
output_path = sys.argv[2]

try:
    with zipfile.ZipFile(docx_path) as z:
        tree = ET.XML(z.read('word/document.xml'))
        WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
        texts = [''.join([node.text for node in p.iter(WORD_NAMESPACE + 't') if node.text]) 
                 for p in tree.iter(WORD_NAMESPACE + 'p')]
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(t for t in texts if t))
    print("Success")
except Exception as e:
    print(f"Error: {e}")
