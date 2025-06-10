# Importa as bibliotecas necessárias
import cv2                    # Para capturar imagem da webcam
import os                     # Para manipulação de diretórios
import shutil                 # Para copiar arquivos entre pastas
from deepface import DeepFace # Para reconhecimento facial com IA

# Define os diretórios usados no sistema
PROTECTED_FOLDER = "protected"       # Pasta com arquivos "protegidos"
UNLOCKED_FOLDER = "unlocked"         # Pasta onde os arquivos são "desbloqueados"
AUTHORIZED_IMAGE = "authorized_faces/NOME_IMAGEM_COM_SEU_ROSTO.JPG"  # Caminho da imagem autorizada

# Inicia a captura de vídeo pela webcam
cap = cv2.VideoCapture(0)
contador = 0  # Contador de quadros capturados

print("Iniciando reconhecimento facial. Pressione ESC para sair.")

# Loop principal do programa: roda até que o usuário pressione ESC
while True:
    ret, frame = cap.read()  # Captura um frame da webcam
    if not ret:
        print("Erro ao acessar a câmera.")
        break  # Encerra caso não consiga capturar a imagem

    # Exibe o frame atual da webcam em uma janela
    cv2.imshow("Reconhecimento Facial", frame)

    # A cada 3 frames, realiza a verificação facial
    if contador % 3 == 0:
        try:
            # Salva o frame atual como imagem temporária
            cv2.imwrite("temp.jpg", frame)

            # Compara a imagem capturada com a imagem autorizada
            result = DeepFace.verify(
                img1_path="temp.jpg",
                img2_path=AUTHORIZED_IMAGE,
                enforce_detection=False  # Evita falha se não detectar rosto claramente
            )

            recognized = result["verified"]  # Resultado da verificação: True ou False

            if recognized:
                print("Rosto reconhecido! Desbloqueando arquivos...")

                # Cria a pasta 'unlocked' caso ela ainda não exista
                if not os.path.exists(UNLOCKED_FOLDER):
                    os.makedirs(UNLOCKED_FOLDER)

                # Copia todos os arquivos da pasta 'protected' para a 'unlocked'
                for file in os.listdir(PROTECTED_FOLDER):
                    src_path = os.path.join(PROTECTED_FOLDER, file)
                    dst_path = os.path.join(UNLOCKED_FOLDER, file)
                    shutil.copy(src_path, dst_path)

                print(f"Arquivos desbloqueados em '{UNLOCKED_FOLDER}/'")

            else:
                # Se o rosto não for reconhecido
                print("Rosto não reconhecido. Acesso negado.")

        except Exception as e:
            # Trata possíveis erros durante a verificação
            print(f"[ERRO] Problema na verificação: {e}")

    contador += 1  # Incrementa o contador de frames

    # Encerra o loop se a tecla ESC (código 27) for pressionada
    if cv2.waitKey(1) & 0xFF == 27:
        print("Encerrando...")
        break

# Libera a câmera e fecha as janelas abertas pelo OpenCV
cap.release()
cv2.destroyAllWindows()
