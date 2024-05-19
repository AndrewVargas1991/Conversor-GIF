# pip install moviepy
from moviepy.editor import VideoFileClip

arquivo = input('Selecione o arquivo de video: ').replace('"', '')
clip = VideoFileClip(arquivo)
clip.write_gif('arquivo.gif', fps=5)

input('\nConversão concluída com sucesso!\nAperte ENTER par sair...')