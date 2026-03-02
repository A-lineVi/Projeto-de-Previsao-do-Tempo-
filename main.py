import requests

print("✧⁠*∘⁠˚⁠✿˳⁠° Previsão do Tempo ✧⁠*∘⁠˚⁠✿˳⁠°")

#selecionar região
regioes = {
    "zona sul" :{
        "lat": -23.6786,
        "lon": -46.7650 
    },
    'zona norte':{
        'lat': -23.5009,
        'lon': -46.6648
    },
    'zona leste' :{
        'lat': -23.5716,
        'lon': -46.5093
    },
    'zona oeste':{
        'lat' : -23.5701,
        'lon' : -46.7253
    }
}
escolha = str(input("Nos diga qual região você esta!\nDigite uma das opções: zona sul, zona norte, zona leste ou zona oeste:\n"))
cordenada_lat = regioes[escolha]['lat']
cordenada_lon = regioes[escolha]['lon']

#fazer requisição
url = "https://api.open-meteo.com/v1/forecast"
parametros ={
    'latitude': cordenada_lat,
    'longitude': cordenada_lon,
    "current": ["temperature_2m", "surface_pressure", "wind_speed_10m"],
    'timezone': 'America/Sao_Paulo'
}

try:
    response = requests.get(url, params=parametros)
    response.raise_for_status()

    dados = response.json()
    dados_previsao = dados['current']

    print(f"\n✧⁠*∘⁠˚⁠✿˳⁠° Previsão para sua Região ✧⁠*∘⁠˚⁠✿˳⁠°\n")
    print(f"Temperatura de {dados_previsao['temperature_2m']}°C")
    print(f"Pressão barômetrica está em {dados_previsao['surface_pressure']} mbar")
    print(f"O vento esta a {dados_previsao['wind_speed_10m']} km/h!")
    
except Exception as e:
    print(f"Deu Erro faz de novo ae{e}")