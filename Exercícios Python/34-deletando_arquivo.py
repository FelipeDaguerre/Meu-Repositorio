import os
import shutil
fonte = "Teste.txt"


try:
      os.remove(fonte) #deleta um arquivo
      #os.rmdir(fonte)   #deleta um arquivo ou pasta vazia
      #shutil.rmtree(fonte) #deleta arquivos e/ou pastas
    
except FileNotFoundError:
      print("O arquivo não foi encontrado")
except PermissionError:
      print("Você não tem permissão para deletar este arquivo")
except OSError:
      print("Essa pasta contem arquivos") #shutil.rmtree(fonte)

else:
      print(fonte+"foi deletado com sucesso")
