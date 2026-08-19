"""Interface de Linha de Comando (CLI) educacional para a biblioteca software_metrics."""

import argparse
import sys

from software_metrics.defects import calculate_defect_density
from software_metrics.loc import calculate_kloc
from software_metrics.productivity import calculate_productivity


def main():
    parser = argparse.ArgumentParser(
        prog="software-metrics",
        description="Ferramenta educacional de cálculo de Métricas de Software.",
    )
    subparsers = parser.add_subparsers(dest="command", help="Subcomando para o cálculo desejado")

    # Subcomando productivity
    parser_prod = subparsers.add_parser(
        "productivity", help="Calcula a produtividade (Tamanho / Esforço)"
    )
    parser_prod.add_argument(
        "--size", type=float, required=True, help="Tamanho entregue (ex: LOC, PF, UCP)"
    )
    parser_prod.add_argument("--effort", type=float, required=True, help="Esforço gasto em horas")

    # Subcomando defects
    parser_def = subparsers.add_parser(
        "defects", help="Calcula a densidade de defeitos (Defeitos / Tamanho)"
    )
    parser_def.add_argument("--defects", type=float, required=True, help="Quantidade de defeitos")
    parser_def.add_argument("--size", type=float, required=True, help="Tamanho (ex: KLOC, PF)")

    # Subcomando kloc
    parser_kloc = subparsers.add_parser("kloc", help="Converte contagem de LOC em KLOC")
    parser_kloc.add_argument(
        "--loc", type=float, required=True, help="Quantidade de linhas de código (LOC)"
    )

    args = parser.parse_args()

    if args.command == "productivity":
        try:
            prod = calculate_productivity(args.size, args.effort)
            print(f"Produtividade: {prod:.2f} unidades/hora")
        except Exception as e:
            print(f"Erro no cálculo de produtividade: {e}", file=sys.stderr)
            sys.exit(1)

    elif args.command == "defects":
        try:
            density = calculate_defect_density(args.defects, args.size)
            print(f"Densidade de defeitos: {density:.2f} defeitos/unidade")
        except Exception as e:
            print(f"Erro no cálculo de densidade de defeitos: {e}", file=sys.stderr)
            sys.exit(1)

    elif args.command == "kloc":
        try:
            kloc = calculate_kloc(args.loc)
            print(f"KLOC: {kloc:.3f}")
        except Exception as e:
            print(f"Erro na conversão de KLOC: {e}", file=sys.stderr)
            sys.exit(1)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
