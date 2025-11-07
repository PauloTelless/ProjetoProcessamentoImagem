import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt
from datetime import datetime
import json
import os
import warnings
warnings.filterwarnings('ignore')


class SpectrumImageProcessor:
    def __init__(self):
        self.images_history = []
        self.current_image = None
        self.original_image = None
        self.processed_image = None
        self.user_type = "operador"
        print("SPECTRUM - Sistema de Processamento de Imagens")
        print("=" * 60)

    def list_images(self, folder="img"):
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Pasta '{folder}' criada. Adicione imagens para continuar.")
            return []

        imagens = [f for f in os.listdir(folder)
                   if f.lower().endswith(('.jpg', '.png', '.jpeg', '.bmp', '.tiff'))]
        if not imagens:
            print(f"⚠ Nenhuma imagem encontrada na pasta '{folder}'.")
            return []
        print("\nImagens disponíveis:")
        for i, nome in enumerate(imagens, 1):
            print(f"{i} - {nome}")
        return imagens

    def upload_image(self, folder="img"):
        imagens = self.list_images(folder)
        if not imagens:
            return False
        try:
            escolha = int(input("\nDigite o número da imagem desejada: ").strip())
            nome_arquivo = imagens[escolha - 1]
        except (ValueError, IndexError):
            print("❌ Opção inválida.")
            return False

        caminho = os.path.join(folder, nome_arquivo)
        try:
            pil_image = Image.open(caminho).convert("RGB")
            self.original_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
            self.current_image = self.original_image.copy()
            self.processed_image = None
            print(f"✅ Imagem '{nome_arquivo}' carregada com sucesso ({self.original_image.shape})")
            self._log_operation("upload", {"filename": nome_arquivo})
            return True
        except Exception as e:
            print(f"Erro ao carregar imagem: {e}")
            return False

    def linear_transformations(self, brightness=0, contrast=1.0):
        if self.current_image is None:
            print("⚠ Nenhuma imagem carregada!")
            return
        print("\n--- Transformação Linear ---")
        try:
            brightness = float(input("Brilho (-100 a 100): ") or 0)
            contrast = float(input("Contraste (0.1 a 3.0): ") or 1.0)
        except ValueError:
            print("Valores inválidos.")
            return

        brightness = np.clip(brightness, -100, 100)
        contrast = np.clip(contrast, 0.1, 3.0)

        img_float = self.current_image.astype(np.float32)
        transformed = contrast * img_float + brightness
        self.processed_image = np.clip(transformed, 0, 255).astype(np.uint8)

        print("✅ Transformação linear aplicada.")
        self._log_operation("linear_transform", {"brightness": brightness, "contrast": contrast})
        self.analyze_histogram()

    def nonlinear_transformations(self):
        if self.current_image is None:
            print("⚠ Nenhuma imagem carregada!")
            return

        print("\n--- Transformação Não-Linear ---")
        tipo = input("Tipo (gamma/log): ").strip().lower() or "gamma"
        if tipo not in ["gamma", "log"]:
            print("Tipo inválido.")
            return

        gamma = float(input("Gamma (0.1-3.0): ") or 1.0)
        c_log = float(input("Constante Log (>=0.1): ") or 1.0)
        img_normalized = self.current_image.astype(np.float32) / 255.0

        processed = np.power(img_normalized, gamma) if tipo == "gamma" else c_log * np.log1p(img_normalized)
        self.processed_image = np.clip(processed * 255, 0, 255).astype(np.uint8)

        print("✅ Transformação não-linear aplicada.")
        self._log_operation("nonlinear_transform", {"type": tipo, "gamma": gamma, "c_log": c_log})
        self.analyze_histogram()

    def histogram_equalization(self):
        if self.current_image is None:
            print("⚠ Nenhuma imagem carregada!")
            return

        print("\n--- Equalização de Histograma ---")
        metodo = input("Método (global/adaptive): ").strip().lower() or "global"

        if len(self.current_image.shape) == 3:
            ycrcb = cv2.cvtColor(self.current_image, cv2.COLOR_BGR2YCrCb)
            y = ycrcb[:, :, 0]
            y_eq = cv2.createCLAHE(2.0, (8, 8)).apply(y) if metodo == "adaptive" else cv2.equalizeHist(y)
            ycrcb[:, :, 0] = y_eq
            self.processed_image = cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)
        else:
            self.processed_image = cv2.equalizeHist(self.current_image)

        print("✅ Equalização concluída.")
        self._log_operation("histogram_equalization", {"method": metodo})
        self.analyze_histogram()

    def analyze_histogram(self):
        if self.original_image is None:
            print("⚠ Nenhuma imagem carregada!")
            return
        fig, ax = plt.subplots(2, 2, figsize=(12, 8))
        imagens = [self.original_image, self.processed_image]
        titulos = ["Original", "Processada"]

        for i, img in enumerate(imagens):
            if img is not None:
                ax[0, i].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
                ax[0, i].set_title(titulos[i])
                ax[0, i].axis("off")
                for canal, cor in zip(cv2.split(img), ['r', 'g', 'b']):
                    ax[1, i].hist(canal.ravel(), 256, [0, 256], color=cor, alpha=0.5)
                ax[1, i].set_title(f"Histograma {titulos[i]}")
        plt.tight_layout()
        plt.show()

    def comparative_visualization(self):
        if self.original_image is None or self.processed_image is None:
            print("⚠ Execute uma transformação antes.")
            return
        alpha = float(input("Porcentagem da imagem processada (0 a 1): ") or 0.5)
        alpha = np.clip(alpha, 0, 1)
        blended = cv2.addWeighted(self.original_image, 1 - alpha, self.processed_image, alpha, 0)
        plt.imshow(cv2.cvtColor(blended, cv2.COLOR_BGR2RGB))
        plt.title(f"{int(alpha * 100)}% Processada")
        plt.axis("off")
        plt.show()

    def generate_report(self):
        if not self.images_history:
            print("⚠ Nenhuma operação registrada!")
            return
        agora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        os.makedirs("reports", exist_ok=True)
        json_file = os.path.join("reports", f"spectrum_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        tipos = {}
        for op in self.images_history:
            tipos[op["operation"]] = tipos.get(op["operation"], 0) + 1
        report = {
            "sistema": "SPECTRUM - Ferramenta de Análise e Correção de Imagens",
            "data_geracao": agora,
            "total_operacoes": len(self.images_history),
            "tipos_operacao": tipos,
            "operacoes": self.images_history
        }
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"✅ Relatório gerado em '{json_file}'")

    def _log_operation(self, op, params):
        self.images_history.append({
            "operation": op,
            "parameters": params,
            "timestamp": datetime.now().isoformat(),
            "user_type": self.user_type
        })
