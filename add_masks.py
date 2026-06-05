import os

def add_imask():
    files = [
        r"c:\Users\Administrator\Desktop\Chaplin-TCC\templates\shared\base.html",
        r"c:\Users\Administrator\Desktop\Chaplin-TCC\templates\shared\base_dashboard.html"
    ]
    
    mask_script = """
    <!-- IMask.js -->
    <script src="https://unpkg.com/imask"></script>
    <script>
        document.addEventListener("DOMContentLoaded", function () {
            document.querySelectorAll('.mask-cep').forEach(function (el) {
                IMask(el, { mask: '00000-000' });
            });
            document.querySelectorAll('.mask-cpf').forEach(function (el) {
                IMask(el, { mask: '000.000.000-00' });
            });
            document.querySelectorAll('.mask-cnpj').forEach(function (el) {
                IMask(el, { mask: '00.000.000/0000-00' });
            });
            document.querySelectorAll('.mask-phone').forEach(function (el) {
                IMask(el, {
                    mask: [
                        { mask: '(00) 0000-0000' },
                        { mask: '(00) 00000-0000' }
                    ]
                });
            });
        });
    </script>
    """
    
    for filepath in files:
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            if "unpkg.com/imask" not in content:
                content = content.replace('</body>', mask_script + '\n</body>')
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Added IMask to {filepath}")

if __name__ == "__main__":
    add_imask()
