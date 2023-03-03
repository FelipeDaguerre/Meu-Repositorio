# copyfile() = copia conteudo de um arquivo.
# copy() = copyfile() + modo de permissão e o local do arquivo pode ser um diretório
# copy2() = tudo o que copy() faz e com adição de copiar metadados, incluindo a criação do arquivo e horas de modificação 

import shutil

shutil.copyfile('Teste.txt','Copia.txt')  

                # fonte (arquivo a ser copiado) , destino (local onde o arquivo vai ser copiado)