import os
import glob
              #função
def remover_arquivos_json(diretorio):
    arquivos_json = glob.glob(os.path.join(diretorio, "*.json"))

    for arquivo in arquivos_json:
        try:
            os.remove(arquivo)
            print(f"Removido: {arquivo}")
        except Exception as e:
            print(f"Erro ao remover {arquivo}: {e}")

# Como usar
remover_arquivos_json("input/jason/resultados")
