"""Módulo educacional para Análise de Pontos de Função (APF / FPA) segundo o método IFPUG.

Este módulo implementa a contagem de Pontos de Função Não Ajustados (PFNA)
com base em Funções de Dados (ALI e AIE) e Funções de Transação (EE, SE e CE),
utilizando as matrizes padrão de complexidade do IFPUG.
"""

from dataclasses import dataclass
from enum import Enum
from typing import List


class Complexity(Enum):
    LOW = "Baixa"
    AVERAGE = "Média"
    HIGH = "Alta"


class DataFunctionType(Enum):
    ALI = "Arquivo Lógico Interno"
    AIE = "Arquivo de Interface Externa"


class TransactionType(Enum):
    EE = "Entrada Externa"
    SE = "Saída Externa"
    CE = "Consulta Externa"


# Tabela de Pesos IFPUG para Funções de Dados e Transacionais
WEIGHT_TABLE = {
    DataFunctionType.ALI: {
        Complexity.LOW: 7,
        Complexity.AVERAGE: 10,
        Complexity.HIGH: 15,
    },
    DataFunctionType.AIE: {
        Complexity.LOW: 5,
        Complexity.AVERAGE: 7,
        Complexity.HIGH: 10,
    },
    TransactionType.EE: {Complexity.LOW: 3, Complexity.AVERAGE: 4, Complexity.HIGH: 6},
    TransactionType.SE: {Complexity.LOW: 4, Complexity.AVERAGE: 5, Complexity.HIGH: 7},
    TransactionType.CE: {Complexity.LOW: 3, Complexity.AVERAGE: 4, Complexity.HIGH: 6},
}


def get_data_function_complexity(ret: int, det: int) -> Complexity:
    """Determina a complexidade funcional de um ALI ou AIE com base em RETs e DETs."""
    if ret < 1 or det < 1:
        raise ValueError("RET e DET devem ser números inteiros maiores ou iguais a 1.")

    if ret == 1:
        if 1 <= det <= 50:
            return Complexity.LOW
        else:  # det >= 51
            return Complexity.AVERAGE
    elif 2 <= ret <= 5:
        if 1 <= det <= 19:
            return Complexity.LOW
        elif 20 <= det <= 50:
            return Complexity.AVERAGE
        else:  # det >= 51
            return Complexity.HIGH
    else:  # ret >= 6
        if 1 <= det <= 19:
            return Complexity.AVERAGE
        else:  # det >= 20
            return Complexity.HIGH


def get_ee_complexity(ftr: int, det: int) -> Complexity:
    """Determina a complexidade de uma Entrada Externa (EE) com base em FTRs e DETs."""
    if ftr < 0 or det < 1:
        raise ValueError("FTR deve ser >= 0 e DET deve ser >= 1.")

    if ftr <= 1:
        if 1 <= det <= 15:
            return Complexity.LOW
        else:  # det >= 16
            return Complexity.AVERAGE
    elif ftr == 2:
        if 1 <= det <= 4:
            return Complexity.LOW
        elif 5 <= det <= 15:
            return Complexity.AVERAGE
        else:  # det >= 16
            return Complexity.HIGH
    else:  # ftr >= 3
        if 1 <= det <= 4:
            return Complexity.AVERAGE
        else:  # det >= 5
            return Complexity.HIGH


def get_se_ce_complexity(ftr: int, det: int) -> Complexity:
    """Determina a complexidade de uma Saída Externa (SE) ou Consulta Externa (CE)."""
    if ftr < 0 or det < 1:
        raise ValueError("FTR deve ser >= 0 e DET deve ser >= 1.")

    if ftr <= 1:
        if 1 <= det <= 19:
            return Complexity.LOW
        else:  # det >= 20
            return Complexity.AVERAGE
    elif 2 <= ftr <= 3:
        if 1 <= det <= 5:
            return Complexity.LOW
        elif 6 <= det <= 19:
            return Complexity.AVERAGE
        else:  # det >= 20
            return Complexity.HIGH
    else:  # ftr >= 4
        if 1 <= det <= 5:
            return Complexity.AVERAGE
        else:  # det >= 6
            return Complexity.HIGH


@dataclass
class DataFunction:
    name: str
    function_type: DataFunctionType
    ret: int
    det: int

    @property
    def complexity(self) -> Complexity:
        return get_data_function_complexity(self.ret, self.det)

    @property
    def unadjusted_points(self) -> int:
        return WEIGHT_TABLE[self.function_type][self.complexity]


@dataclass
class TransactionalFunction:
    name: str
    transaction_type: TransactionType
    ftr: int
    det: int

    @property
    def complexity(self) -> Complexity:
        if self.transaction_type == TransactionType.EE:
            return get_ee_complexity(self.ftr, self.det)
        else:
            return get_se_ce_complexity(self.ftr, self.det)

    @property
    def unadjusted_points(self) -> int:
        return WEIGHT_TABLE[self.transaction_type][self.complexity]


class FunctionPointCalculator:
    """Calculadora educacional de Análise de Pontos de Função."""

    def __init__(self):
        self.data_functions: List[DataFunction] = []
        self.transactional_functions: List[TransactionalFunction] = []

    def add_data_function(
        self, name: str, function_type: DataFunctionType, ret: int, det: int
    ) -> DataFunction:
        df = DataFunction(name, function_type, ret, det)
        self.data_functions.append(df)
        return df

    def add_transactional_function(
        self, name: str, transaction_type: TransactionType, ftr: int, det: int
    ) -> TransactionalFunction:
        tf = TransactionalFunction(name, transaction_type, ftr, det)
        self.transactional_functions.append(tf)
        return tf

    def calculate_total_unadjusted_points(self) -> int:
        data_points = sum(df.unadjusted_points for df in self.data_functions)
        trans_points = sum(tf.unadjusted_points for tf in self.transactional_functions)
        return data_points + trans_points

    def summary(self) -> dict:
        return {
            "total_data_functions": len(self.data_functions),
            "data_function_points": sum(df.unadjusted_points for df in self.data_functions),
            "total_transactional_functions": len(self.transactional_functions),
            "transactional_function_points": sum(
                tf.unadjusted_points for tf in self.transactional_functions
            ),
            "total_unadjusted_function_points": self.calculate_total_unadjusted_points(),
        }
