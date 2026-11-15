
from decimal import Decimal

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def inicio(request: HttpRequest):
    contexto = {
        "titulo": "CANES | Início",
        "descricao": "Bem-vindo ao catálogo CANES!"
    }

    template = "core/index.html"

    return render(request, template, contexto)


def somar():
    resultado = 0

    for a in range(1, 11):
        resultado += a

    return resultado


def calcular_indicadores_catalogo(produtos):
    valor_total_estoque = Decimal("0.00")
    quantidade_total_unidades = 0
    quantidade_indisponiveis = 0
    quantidade_disponiveis = 0

    for item in produtos:
        item["valor_em_estoque"] = item["preco"] * item["estoque"]

        valor_total_estoque += item["valor_em_estoque"]
        quantidade_total_unidades += item["estoque"]

        if item["estoque"] == 0:
            quantidade_indisponiveis += 1
        else:
            quantidade_disponiveis += 1

    quantidade_produtos = len(produtos)

    return {
        "total_produtos": quantidade_produtos,
        "quantidade_produtos": quantidade_produtos,
        "produtos_em_estoque": quantidade_total_unidades,
        "quantidade_total_unidades": quantidade_total_unidades,
        "produtos_esgotados": quantidade_indisponiveis,
        "quantidade_indisponiveis": quantidade_indisponiveis,
        "quantidade_disponiveis": quantidade_disponiveis,
        "valor_total_estoque": valor_total_estoque
    }


def catalogo(request):
    produtos = [
        {"nome": "Teclado", "preco": Decimal("89.90"), "estoque": 5},
        {"nome": "Mouse", "preco": Decimal("49.90"), "estoque": 0},
        {"nome": "Monitor", "preco": Decimal("799.00"), "estoque": 2},
        {"nome": "Notebook", "preco": Decimal("2999.00"), "estoque": 1},
        {"nome": "Cadeira Gamer", "preco": Decimal("499.00"), "estoque": 0},
        {"nome": "Memória DDR5", "preco": Decimal("599.00"), "estoque": 0},
        {"nome": "Placa de Vídeo", "preco": Decimal("899.00"), "estoque": 0},
        {"nome": "Processador", "preco": Decimal("1299.00"), "estoque": 0},
        {"nome": "Gabinete", "preco": Decimal("299.00"), "estoque": 0},
        {"nome": "Fonte de Alimentação", "preco": Decimal("199.00"), "estoque": 0}
    ]

    contexto = {
        "titulo": "Catálogo CANES",
        "produtos": produtos,
        **calcular_indicadores_catalogo(produtos)
    }

    return render(request, "core/catalogo.html", contexto)


def saudacao(request: HttpRequest, nome: str):
    contexto = {
        "nome": nome
    }

    template = "core/saudacao.html"

    return render(request, template, contexto)


def sobre(request):
    return HttpResponse("CANES é um projeto de catálogo web.")


def calcular_indicadores_pedidos(pedidos):
    total_pedidos = 0
    pedidos_pendentes = 0
    pedidos_concluidos = 0
    valor_total = Decimal("0.00")

    for pedido in pedidos:
        pedido["valor_total"] = pedido["preco_unitario"] * pedido["quantidade"]

        total_pedidos += 1
        valor_total += pedido["valor_total"]

        if pedido["situacao"] == "Pendente":
            pedidos_pendentes += 1
        elif pedido["situacao"] == "Concluído":
            pedidos_concluidos += 1

    return {
        "total_pedidos": total_pedidos,
        "pedidos_pendentes": pedidos_pendentes,
        "pedidos_concluidos": pedidos_concluidos,
        "valor_total": valor_total,
        "valor_total_pedidos": valor_total
    }


def pedidos(request: HttpRequest):
    lista_pedidos = [
        {
            "numero": "CAN-001",
            "cliente": "Ana Silva",
            "produto": "Teclado",
            "preco_unitario": Decimal("89.90"),
            "preco": Decimal("89.90"),
            "quantidade": 2,
            "situacao": "Pendente"
        },
        {
            "numero": "CAN-002",
            "cliente": "Bruno Santos",
            "produto": "Mouse",
            "preco_unitario": Decimal("49.90"),
            "preco": Decimal("49.90"),
            "quantidade": 3,
            "situacao": "Concluído"
        },
        {
            "numero": "CAN-003",
            "cliente": "Carla Oliveira",
            "produto": "Monitor",
            "preco_unitario": Decimal("799.00"),
            "preco": Decimal("799.00"),
            "quantidade": 1,
            "situacao": "Pendente"
        },
        {
            "numero": "CAN-004",
            "cliente": "Diego Costa",
            "produto": "Notebook",
            "preco_unitario": Decimal("2999.00"),
            "preco": Decimal("2999.00"),
            "quantidade": 1,
            "situacao": "Concluído"
        },
        {
            "numero": "CAN-005",
            "cliente": "Elisa Souza",
            "produto": "Cadeira Gamer",
            "preco_unitario": Decimal("499.00"),
            "preco": Decimal("499.00"),
            "quantidade": 2,
            "situacao": "Pendente"
        }
    ]

    contexto = {
        "titulo": "Painel de pedidos",
        "descricao": "Acompanhe os pedidos dos clientes, suas situações e os valores de cada compra.",
        "pedidos": lista_pedidos,
        **calcular_indicadores_pedidos(lista_pedidos)
    }

    return render(request, "core/pedidos.html", contexto)
