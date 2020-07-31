import files
from services import parte

def processarDiretorios(work_dir, model_file = ''):
    #files.arquivosParaImagem(work_dir)
    file_name = parte(work_dir, -1, '\\')
    files.gerar_documento(work_dir, file_name, model_file)
    files.word_to_pdf(work_dir, file_name)