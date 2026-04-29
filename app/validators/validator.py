import re

def validate(output: str) -> str:
    if "Resumo:" not in output:
        raise ValueError("Resposta sem Resumo")

    if "Análise:" not in output:
        raise ValueError("Resposta sem Análise")

    numbers = re.findall(r"\d+", output)
    if len(numbers) < 3:
        raise ValueError("Poucos dados numéricos")

    return output