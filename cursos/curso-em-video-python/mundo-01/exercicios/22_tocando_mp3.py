NOME_DO_PROGRAMA = "Playando um MP3"
print(f'{"="*10} {NOME_DO_PROGRAMA.upper()} {"="*10}')
# ==========================================

# ------------------------------------------
import pygame

pygame.init()
pygame.mixer.init()

try:
    pygame.mixer.music.load('assets/guanacast-33.mp3')
    pygame.mixer.music.play()
    input("Tocando... Aperte Enter para parar.")
except pygame.error as e:
    print(f"Erro ao tentar tocar: {e}")

















# ------------------------------------------

# ==========================================

# --- RODAPÉ ---
print(f'{"="*40}')










