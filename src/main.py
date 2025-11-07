from spectrum_processor import SpectrumImageProcessor

def main():
    s = SpectrumImageProcessor()
    imagem_carregada = False

    while True:
        print("\n=====================================")
        print("   🧠 Projeto: Processamento de Imagens")
        print("   Grupo 5 - Transformações Lineares e Não-Lineares")
        print("=====================================")
        print("1 - Selecionar Imagem da Pasta")
        print("2 - Transformação Linear (contraste, brilho, inversão)")
        print("3 - Transformação Não-Linear (logarítmica e gama)")
        print("4 - Equalização de Histograma")
        print("5 - Análise de Histograma")
        print("6 - Visualização Comparativa")
        print("7 - Ajuste Dinâmico de Parâmetros")
        print("8 - Gerar Relatório de Resultados")
        print("0 - Sair")
        print("=====================================")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            s.upload_image()
            imagem_carregada = True
        elif opcao == "2":
            if imagem_carregada:
                s.linear_transformations()
            else:
                print("⚠️  Nenhuma imagem carregada. Use a opção 1 primeiro.")
        elif opcao == "3":
            if imagem_carregada:
                s.nonlinear_transformations()
            else:
                print("⚠️  Nenhuma imagem carregada.")
        elif opcao == "4":
            if imagem_carregada:
                s.histogram_equalization()
            else:
                print("⚠️  Carregue uma imagem antes.")
        elif opcao == "5":
            s.analyze_histogram()
        elif opcao == "6":
            s.comparative_visualization()
        elif opcao == "7":
            if imagem_carregada:
                s.dynamic_parameter_adjustment()
            else:
                print("⚠️  É necessário carregar uma imagem antes.")
        elif opcao == "8":
            s.generate_report()
        elif opcao == "0":
            print("👋 Encerrando o programa...")
            break
        else:
            print("❌ Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
