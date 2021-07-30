function calculate_difference(generalistas, medicosDeFamilia, ponto, upper, lower, ocorrencias, y, z){

    const proporcaoInicialGeneralistas = 0.66
    const proporcaoInicialMedicosDeFamilia = parseFloat((1 - proporcaoInicialGeneralistas).toFixed(2))
    

    const pontoPAF = ((proporcaoInicialGeneralistas * 1) + (proporcaoInicialMedicosDeFamilia * ponto)) - ((generalistas * 1) + (medicosDeFamilia * ponto)) /
    ((proporcaoInicialGeneralistas * 1) + (proporcaoInicialMedicosDeFamilia * ponto))

  const upperPAF = (proporcaoInicialGeneralistas * 1 + proporcaoInicialMedicosDeFamilia * upper) - (generalistas * 1 + medicosDeFamilia * upper) /
    (proporcaoInicialGeneralistas * 1 + proporcaoInicialMedicosDeFamilia * upper)

  const lowerPAF = (proporcaoInicialGeneralistas * 1 + proporcaoInicialMedicosDeFamilia * lower) - (generalistas * 1 + medicosDeFamilia * lower) /
    (proporcaoInicialGeneralistas * 1 + proporcaoInicialMedicosDeFamilia * lower)


  const popPontoPAF = Math.round((z * y * pontoPAF / 100).toFixed(4), 0)
  const popLowerPAF = Math.round((z * y * lowerPAF / 100).toFixed(4), 0)
  const popUpperPAF = Math.round((z * y * upperPAF / 100).toFixed(4), 0)

  const diferenca = ((ocorrencias + popPontoPAF) / ocorrencias * 100).toFixed(1)
  const intervaloLower = ocorrencias + popLowerPAF
  const intervaloUpper = ocorrencias + popUpperPAF

  return [diferenca, intervaloLower, intervaloUpper]
}