import math

# Coordenadas geográficas da China
china_lat = 35.8617
china_lon = 104.1954

# Coordenadas geográficas do Brasil
brasil_lat = -14.2401
brasil_lon = -53.1805

# Função para calcular a distância entre dois pontos no globo
def distancia(lat1, lon1, lat2, lon2):
    # Convertendo graus para radianos
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Calculando a distância
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad
    a = math.sin(dlat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    R = 6371  # Raio da Terra em km
    distancia = R * c

    return distancia

# Calculando a distância entre a China e o Brasil
distancia_china_brasil = distancia(china_lat, china_lon, brasil_lat, brasil_lon)

print(f"A distância entre a China e o Brasil é de aproximadamente {distancia_china_brasil:.2f} km")