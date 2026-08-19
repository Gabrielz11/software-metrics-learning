"""Módulo educacional para cálculo de Pontos de Caso de Uso (UCP - Use Case Points).

Implementa a metodologia desenvolvida por Gustav Karner (1993) contendo:
- UAW (Unadjusted Actor Weight)
- UUCW (Unadjusted Use Case Weight)
- UUCP (Unadjusted Use Case Points)
- TCF (Technical Complexity Factor - T1 a T13)
- ECF (Environmental Complexity Factor - E1 a E8)
- Cálculo total de UCP e estimativa de esforço em horas.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List


class ActorComplexity(Enum):
    SIMPLE = 1  # API / sistema via interface definida
    AVERAGE = 2  # Protocolo interativo ou interface em linha de comando / arquivo
    COMPLEX = 3  # Usuário humano via interface gráfica (GUI)


class UseCaseComplexity(Enum):
    SIMPLE = 5  # 1 a 3 transações
    AVERAGE = 10  # 4 a 7 transações
    COMPLEX = 15  # 8 ou mais transações


# Fatores Técnicos T1-T13 com seus respectivos pesos padrão Karner
TECHNICAL_FACTOR_WEIGHTS: Dict[str, float] = {
    "T1": 2.0,  # Sistema Distribuído
    "T2": 1.0,  # Desempenho / Tempo de Resposta
    "T3": 1.0,  # Eficiência do Usuário Final
    "T4": 1.0,  # Processamento Interno Complexo
    "T5": 1.0,  # Reutilização de Código
    "T6": 0.5,  # Facilidade de Instalação
    "T7": 0.5,  # Facilidade de Uso
    "T8": 2.0,  # Portabilidade
    "T9": 1.0,  # Facilidade de Mudança
    "T10": 1.0,  # Concorrência
    "T11": 1.0,  # Recursos de Segurança Especiais
    "T12": 1.0,  # Acesso Direto a Terceiros
    "T13": 1.0,  # Treinamento Especial do Usuário
}

# Fatores Ambientais E1-E8 com seus respectivos pesos padrão Karner
ENVIRONMENTAL_FACTOR_WEIGHTS: Dict[str, float] = {
    "E1": 1.5,  # Familiaridade com o processo de desenvolvimento
    "E2": 0.5,  # Experiência com a aplicação / domínio
    "E3": 1.0,  # Experiência em Orientação a Objetos
    "E4": 0.5,  # Capacidade do Analista Principal
    "E5": 1.0,  # Motivação da Equipe
    "E6": 2.0,  # Estabilidade de Requisitos
    "E7": -1.0,  # Trabalhadores em Tempo Parcial
    "E8": -1.0,  # Linguagem de Programação Difícil
}


@dataclass
class Actor:
    name: str
    complexity: ActorComplexity

    @property
    def weight(self) -> int:
        return self.complexity.value


@dataclass
class UseCase:
    name: str
    complexity: UseCaseComplexity

    @property
    def weight(self) -> int:
        return self.complexity.value


class UseCasePointCalculator:
    """Calculadora de Use Case Points (UCP)."""

    def __init__(self):
        self.actors: List[Actor] = []
        self.use_cases: List[UseCase] = []
        # Avaliações padrão (0 a 5). Se não informadas, assume-se 3 (neutro)
        self.technical_ratings: Dict[str, int] = {key: 3 for key in TECHNICAL_FACTOR_WEIGHTS}
        self.environmental_ratings: Dict[str, int] = {
            key: 3 for key in ENVIRONMENTAL_FACTOR_WEIGHTS
        }

    def add_actor(self, name: str, complexity: ActorComplexity) -> Actor:
        actor = Actor(name, complexity)
        self.actors.append(actor)
        return actor

    def add_use_case(self, name: str, complexity: UseCaseComplexity) -> UseCase:
        uc = UseCase(name, complexity)
        self.use_cases.append(uc)
        return uc

    def set_technical_rating(self, factor_code: str, rating: int) -> None:
        """Define o valor de um fator técnico (T1 a T13) entre 0 e 5."""
        if factor_code not in TECHNICAL_FACTOR_WEIGHTS:
            raise ValueError(f"Fator técnico inválido: {factor_code}. Use T1 a T13.")
        if not (0 <= rating <= 5):
            raise ValueError("O rating do fator técnico deve estar entre 0 e 5.")
        self.technical_ratings[factor_code] = rating

    def set_environmental_rating(self, factor_code: str, rating: int) -> None:
        """Define o valor de um fator ambiental (E1 a E8) entre 0 e 5."""
        if factor_code not in ENVIRONMENTAL_FACTOR_WEIGHTS:
            raise ValueError(f"Fator ambiental inválido: {factor_code}. Use E1 a E8.")
        if not (0 <= rating <= 5):
            raise ValueError("O rating do fator ambiental deve estar entre 0 e 5.")
        self.environmental_ratings[factor_code] = rating

    def calculate_uaw(self) -> int:
        """Calcula o UAW (Unadjusted Actor Weight)."""
        return sum(actor.weight for actor in self.actors)

    def calculate_uucw(self) -> int:
        """Calcula o UUCW (Unadjusted Use Case Weight)."""
        return sum(uc.weight for uc in self.use_cases)

    def calculate_uucp(self) -> int:
        """Calcula o UUCP (Unadjusted Use Case Points). UUCP = UAW + UUCW."""
        return self.calculate_uaw() + self.calculate_uucw()

    def calculate_tcf(self) -> float:
        """Calcula o TCF (Technical Complexity Factor). TCF = 0.6 + (0.01 * TFactor)."""
        tf_sum = sum(
            TECHNICAL_FACTOR_WEIGHTS[code] * rating
            for code, rating in self.technical_ratings.items()
        )
        return 0.6 + (0.01 * tf_sum)

    def calculate_ecf(self) -> float:
        """Calcula o ECF (Environmental Complexity Factor). ECF = 1.4 + (-0.03 * EFactor)."""
        ef_sum = sum(
            ENVIRONMENTAL_FACTOR_WEIGHTS[code] * rating
            for code, rating in self.environmental_ratings.items()
        )
        return 1.4 + (-0.03 * ef_sum)

    def calculate_ucp(self) -> float:
        """Calcula o valor final de UCP = UUCP * TCF * ECF."""
        return self.calculate_uucp() * self.calculate_tcf() * self.calculate_ecf()

    def estimate_effort_hours(self, productivity_factor: float = 20.0) -> float:
        """Calcula a estimativa de esforço em horas (padrão Karner = 20 horas por UCP)."""
        if productivity_factor <= 0:
            raise ValueError("O fator de produtividade deve ser maior que zero.")
        return self.calculate_ucp() * productivity_factor

    def summary(self, productivity_factor: float = 20.0) -> dict:
        return {
            "uaw": self.calculate_uaw(),
            "uucw": self.calculate_uucw(),
            "uucp": self.calculate_uucp(),
            "tcf": round(self.calculate_tcf(), 4),
            "ecf": round(self.calculate_ecf(), 4),
            "ucp": round(self.calculate_ucp(), 2),
            "estimated_effort_hours": round(self.estimate_effort_hours(productivity_factor), 2),
        }
