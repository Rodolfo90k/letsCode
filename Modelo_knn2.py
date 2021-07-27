class CalculoKnn:


    def calculaDoKnn(self, k, item_no_class, data):
        lista1 = []
        for item_data in data:
            y = []
        
            y.append(self.CD(item_data[2],item_no_class))
            y.append(item_data[1])
            y.append(item_data[2])
            lista1.append(y)

        lista1.sort()
        return self.dP(lista1[:k])
    
    
    
    def CD(self, ValorAntigo, ValorNovo):
        D = 0
        for i in range(len(ValorAntigo)):
            
            D = D + (ValorAntigo[i] - ValorNovo[i])**2
    
        return D**(0.5)
    
    def dP(self, lista1):
        m = 0
        a = 0
        c = 0
        RP = ''
        for perfil in lista1:
            if perfil[1] == 'Moderado':
                m = m + 1
            elif perfil[1] == 'Agressivo':
                a = a + 1
            elif perfil[1] == 'Conservador':
                c = c + 1

        if a > m:
            if a > c:
                RP = 'Agressivo'
        elif m > c:
            RP = 'Moderado'
        else:
            RP = 'Conservador'

        return RP
   
    def classificar_perfil(self , no_class, data, k):
        resultado = dict()
        for item_no_class in no_class:
            item_no_class[1] = self.calculaDoKnn(k, item_no_class[2], data)
            resultado[item_no_class[0]] = item_no_class[1]
        return resultado
        