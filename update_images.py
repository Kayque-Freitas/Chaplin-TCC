import os
import shutil
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chaplin_project.settings')
django.setup()

from apps.tasks.models import Task, TaskEvidence

ARTIFACTS_DIR = r"C:\Users\Desktop\.gemini\antigravity-ide\brain\b0df5514-1b0e-4e6a-8587-1cfb32335171"
MEDIA_DIR = r"c:\Users\Desktop\Desktop\projeto\Chaplin-TCC\media\evidences"

if not os.path.exists(MEDIA_DIR):
    os.makedirs(MEDIA_DIR)

image_mapping = {
    6: "task_6_corredor_escuro_1782470767320.png",
    7: "task_7_vazamento_pia_1782470777420.png",
    8: "task_8_rachadura_parede_1782470788255.png",
    9: "task_9_tomada_quebrada_1782470798676.png",
    10: "task_10_filtro_sujo_1782470815031.png",
    11: "task_11_macaneta_nova_1782470825319.png",
    12: "task_12_painel_elevador_1782470834276.png",
    13: "task_13_forro_novo_1782470844392.png",
    14: "task_14_parede_descascando_1782470859567.png",
    15: "task_15_garagem_iluminada_1782470869952.png",
    16: "task_16_canos_manometro_1782470880521.png",
    17: "task_17_rampa_vazia_1782470890242.png",
}

for task_id, image_name in image_mapping.items():
    src_path = os.path.join(ARTIFACTS_DIR, image_name)
    dst_path = os.path.join(MEDIA_DIR, image_name)
    
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)
        print(f"Copied {image_name}")
        
        task = Task.objects.filter(id=task_id).first()
        if task:
            # Delete existing evidence if any
            TaskEvidence.objects.filter(task=task).delete()
            # Create new evidence
            TaskEvidence.objects.create(
                task=task,
                photo=f"evidences/{image_name}",
                description="Imagem gerada recriando a evidência da tarefa"
            )
            print(f"Updated TaskEvidence for Task {task_id}")
    else:
        print(f"Source file not found: {src_path}")
