from spectrum_processor import SpectrumImageProcessor

def main():
    s = SpectrumImageProcessor()
    while True:
        print("\n==== MENU ====")
        print("1 - Selecionar Imagem da Pasta")
        print("2 - Transformação Linear")
        print("3 - Transformação Não-Linear")
        print("4 - Equalização de Histograma")
        print("5 - Análise de Histograma")
        print("6 - Visualização Comparativa")
        print("7 - Gerar Relatório")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            s.upload_image()
        elif opcao == "2":
            s.linear_transformations()
        elif opcao == "3":
            s.nonlinear_transformations()
        elif opcao == "4":
            s.histogram_equalization()
        elif opcao == "5":
            s.analyze_histogram()
        elif opcao == "6":
            s.comparative_visualization()
        elif opcao == "7":
            s.generate_report()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
