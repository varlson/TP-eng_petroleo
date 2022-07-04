def leitor_de_servico(servico):
  servico.update({'tipo_de_servico': input('Entre com tipo de servico: ')})
  servico.update({'metro': float(input('Entre com metro quadrado: '))})


def calculador_de_custo(servico):
  if servico['tipo_de_servico'] == 'P':
    qnt_galao = (servico['metro']/36)
    total_galao = qnt_galao * 45

    custo_de_material = servico['metro'] * 2;
    mao_de_obra = 15*servico['metro']
    custo_total = total_galao + custo_de_material + mao_de_obra
    servico.update({'custo_total': custo_total})
    
  else:
    qnt_galao = (servico['metro']/1.80)
    total_galao = qnt_galao * 32
    
    custo_de_material = servico['metro'] * 5;
    custo_de_material = custo_de_material*0.1+custo_de_material

    mao_de_obra  = servico['metro'] * 40
    custo_total = total_galao + custo_de_material + mao_de_obra
    servico.update({'custo_total': custo_total})


def impressor(servico):
  print(f"Custo de serviço: {servico['custo_total']}")

def main():
  servico = {}
  leitor_de_servico(servico)
  calculador_de_custo(servico)
  impressor(servico)

main()