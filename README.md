# 🔐 Reconhecimento Facial para Controle de Acesso a Arquivos

Este projeto é um **protótipo funcional open source** que simula o controle de acesso a arquivos com base em reconhecimento facial. Utiliza uma webcam e a biblioteca DeepFace para verificar se o rosto capturado é autorizado. Quando reconhecido, arquivos são copiados automaticamente de uma pasta "protegida" para uma pasta "desbloqueada".

---

## 💡 Proposta

Oferecer uma base simples e extensível para sistemas de autenticação por reconhecimento facial, com foco didático, para estudantes e desenvolvedores que desejam explorar aplicações de visão computacional e segurança local.

---

## ⚙️ Tecnologias Utilizadas

- [Python 3.10](https://www.python.org/)
- [OpenCV](https://opencv.org/) – Captura e exibição da webcam
- [DeepFace](https://github.com/serengil/deepface) – Reconhecimento facial
- `os` e `shutil` – Manipulação de diretórios e arquivos

---

## 🖼️ Como Funciona

1. A webcam captura imagens continuamente.
2. A cada 3 frames, o sistema compara a imagem com uma foto autorizada.
3. Se o rosto for reconhecido, os arquivos da pasta `protected/` são copiados para `unlocked/`.

---

## 📁 Estrutura de Pastas Esperada

Certifique-se de que seu diretório do projeto contenha:

```
seu_projeto/
├── authorized_faces/
│   └── NOME_IMAGEM_COM_SEU_ROSTO.JPG
├── protected/
│   └── arquivos_a_serem_protegidos.txt
├── unlocked/
│   └── (vazio inicialmente)
├── main.py
```

> **OBS:** A pasta `unlocked/` será criada automaticamente caso não exista.

---

## 🔧 Passo a Passo para Execução

### 1. Clone o repositório (ou baixe os arquivos)

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

Ou instale manualmente:

```bash
pip install opencv-python deepface
```

### 4. Configure sua imagem autorizada

Coloque uma **foto frontal do seu rosto** em `authorized_faces/` e atualize o nome da imagem no código:

```python
AUTHORIZED_IMAGE = "authorized_faces/NOME_IMAGEM_COM_SEU_ROSTO.JPG"
```

### 5. Coloque os arquivos protegidos na pasta `protected/`

Adicione quaisquer arquivos que você deseja "proteger" nessa pasta. Eles serão copiados apenas após o reconhecimento facial.

### 6. Execute o script

```bash
python main.py
```

> Ao rodar, uma janela será aberta com a imagem da webcam. Pressione **ESC** para encerrar o sistema.

---

## 📋 Comportamento Esperado

- Se o rosto **for reconhecido**, a mensagem "Rosto reconhecido!" será exibida e os arquivos serão copiados.
- Se **não for reconhecido**, será exibida a mensagem "Acesso negado".
- Se houver falha na câmera ou verificação, erros serão tratados no console.

---

## 📌 Observações Importantes

- O sistema **não protege pastas de verdade** — é uma **simulação didática** de controle de acesso.
- A verificação é baseada em **semelhança de imagem**, e não usa autenticação criptográfica.
- Ideal para fins **educacionais**, demonstrações ou testes locais.

---

## 📜 Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE). Você é livre para usar, modificar e distribuir com os devidos créditos.

---

## ✨ Possíveis Extensões Futuras

- Criptografar/descriptografar arquivos ao invés de apenas copiar.
- Suporte a múltiplos rostos autorizados.
- Integração com sistemas de login de sistema operacional.

---

## 👨‍💻 Autor

Desenvolvido por Guilherme H. Rodrigues para o projeto de extensão de IA + Segurança da informação da Universidade Presbiteriana Mackenzie, em 2025.  
Sinta-se livre para contribuir, adaptar ou expandir este protótipo!