# lista dos pilotos selecionáveis, e as informações apresentadas
infos_pilotos = [
    {"nome": "Jean-Eric Vergne", "equipe": "DS Penske", "vitorias": 10, "titulos": 2, "curiosidades": "Jean-Eric Vergne é o único piloto a vencer duas vezes o campeonato de Fórmula E consecutivamente."},
    {"nome": "Stoffel Vandoorne", "equipe": "DS Penske", "vitorias": 3, "titulos": 1, "curiosidades": "Stoffel Vandoorne venceu o campeonato de Fórmula E na temporada 2021-2022."},
    {"nome": "Lucas di Grassi", "equipe": "Maserati MSG Racing", "vitorias": 12, "titulos": 1, "curiosidades": "Lucas di Grassi é conhecido por ser um dos pilotos mais consistentes da Fórmula E."},
    {"nome": "Edoardo Mortara", "equipe": "Maserati MSG Racing", "vitorias": 4, "titulos": 0, "curiosidades": "Edoardo Mortara é também conhecido por seu sucesso nas corridas de DTM."},
    {"nome": "Sebastien Buemi", "equipe": "Envision Racing", "vitorias": 13, "titulos": 1, "curiosidades": "Sebastien Buemi também compete no Campeonato Mundial de Endurance da FIA."},
    {"nome": "Nick Cassidy", "equipe": "Envision Racing", "vitorias": 2, "titulos": 0, "curiosidades": "Nick Cassidy é um piloto versátil com vitórias em várias categorias, incluindo a Super Formula japonesa."},
    {"nome": "Andre Lotterer", "equipe": "Avalanche Andretti", "vitorias": 4, "titulos": 0, "curiosidades": "Andre Lotterer tem vasta experiência em corridas de endurance, incluindo Le Mans."},
    {"nome": "Jake Dennis", "equipe": "Avalanche Andretti", "vitorias": 2, "titulos": 0, "curiosidades": "Jake Dennis foi um dos estreantes mais impressionantes na Fórmula E, com vitórias em sua primeira temporada."},
    {"nome": "Mitch Evans", "equipe": "Jaguar TCS Racing", "vitorias": 3, "titulos": 0, "curiosidades": "Mitch Evans é o primeiro piloto da Nova Zelândia a vencer uma corrida na Fórmula E."},
    {"nome": "Sam Bird", "equipe": "Jaguar TCS Racing", "vitorias": 11, "titulos": 0, "curiosidades": "Sam Bird é o único piloto a vencer em todas as temporadas da Fórmula E até 2021."},
    {"nome": "Oliver Rowland", "equipe": "Mahindra Racing", "vitorias": 1, "titulos": 0, "curiosidades": "Oliver Rowland foi campeão da World Series em 2015."},
    {"nome": "Alexander Sims", "equipe": "Mahindra Racing", "vitorias": 1, "titulos": 0, "curiosidades": "Alexander Sims é conhecido por sua habilidade tanto em corridas de monopostos quanto de endurance."},
    {"nome": "Maximilian Günther", "equipe": "Nissan Formula E Team", "vitorias": 3, "titulos": 0, "curiosidades": "Maximilian Günther é o piloto mais jovem a vencer uma corrida na Fórmula E."},
    {"nome": "Norman Nato", "equipe": "Nissan Formula E Team", "vitorias": 1, "titulos": 0, "curiosidades": "Norman Nato venceu sua primeira corrida na Fórmula E na temporada 2020-2021."},
    {"nome": "René Rast", "equipe": "NEOM McLaren Formula E Team", "vitorias": 2, "titulos": 0, "curiosidades": "René Rast é tricampeão do DTM e teve uma transição bem-sucedida para a Fórmula E."},
    {"nome": "Jake Hughes", "equipe": "NEOM McLaren Formula E Team", "vitorias": 0, "titulos": 0, "curiosidades": "Jake Hughes é um jovem piloto britânico com um futuro promissor na Fórmula E."},
    {"nome": "Sergio Sette Camara", "equipe": "NIO 333 Racing", "vitorias": 0, "titulos": 0, "curiosidades": "Sergio Sette Camara é um jovem talento brasileiro que também competiu anteriormente na Fórmula 2."},
    {"nome": "Dan Ticktum", "equipe": "NIO 333 Racing", "vitorias": 0, "titulos": 0, "curiosidades": "Dan Ticktum é um piloto britânico conhecido por sua agressividade e seu grande talento."},
    {"nome": "Pascal Wehrlein", "equipe": "TAG Heuer Porsche Formula E Team", "vitorias": 2, "titulos": 0, "curiosidades": "Pascal Wehrlein é ex-piloto de Fórmula 1, tendo competido pela Sauber anteriormente."},
    {"nome": "Antonio Felix da Costa", "equipe": "TAG Heuer Porsche Formula E Team", "vitorias": 7, "titulos": 1, "curiosidades": "Antonio Felix da Costa ganhou seu primeiro título da Fórmula E em 2020."},
    {"nome": "Robin Frijns", "equipe": "ABT CUPRA Formula E Team", "vitorias": 2, "titulos": 0, "curiosidades": "Robin Frijns tem sido um forte competidor tanto na Fórmula E quanto em outras categorias de automobilismo."},
    {"nome": "Nico Müller", "equipe": "ABT CUPRA Formula E Team", "vitorias": 0, "titulos": 0, "curiosidades": "Nico Müller é um piloto suíço conhecido por seu sucesso no DTM."},
    {"nome": "Oliver Turvey", "equipe": "ABT CUPRA Formula E Team", "vitorias": 0, "titulos": 0, "curiosidades": "Oliver Turvey é um dos pilotos mais experientes na Fórmula E, competindo desde a temporada inaugural."},
    {"nome": "Kevin van der Linde", "equipe": "ABT CUPRA Formula E Team", "vitorias": 0, "titulos": 0, "curiosidades": "Kevin van der Linde é um piloto sul-africano que estreou na Fórmula E, e vem apresentando bons resultados."},
    {"nome": "Felipe Massa", "equipe": "Venturi Racing", "vitorias": 0, "titulos": 0, "curiosidades": "Felipe Massa é um ex-piloto de Fórmula 1, ele ficou conhecido mundialmente por suas temporadas na Ferrari."},
]

# lista das equipes selecionáveis, e as curiosidades delas
infos_equipes = {
    "DS Penske": "Curiosidade: A DS Penske é uma equipe de corrida de Fórmula E formada pela união da DS Automobiles e a Penske Autosport. Conhecida pelo seu sucesso e a sua boa consistência, a equipe possui dois títulos de pilotos e diversas vitórias em campeonatos.",
    "Maserati MSG Racing": "Curiosidade: Maserati MSG Racing é uma equipe de Fórmula E que representa a histórica marca de carros Maserati. A equipe tem se destacado nos últimos anos por seu exelente desempenho, e vem nos mostrando pilotos experientes.",
    "Envision Racing": "Curiosidade: Envision Racing é uma equipe competitiva na Fórmula E, apoiada pela Envision Group, uma empresa bem forte em tecnologia de energia renovável. A equipe é conhecida por sua constante inovação e boa performance.",
    "Avalanche Andretti": "Curiosidade: Avalanche Andretti é uma equipe americana de Fórmula E, parte da Andretti Autosport. A equipe combina a experiência da Andretti em corridas com a tecnologia elétrica de ponta.",
    "Jaguar TCS Racing": "Curiosidade: Jaguar TCS Racing é a equipe de Fórmula E da Jaguar Land Rover, com apoio da Tata Consultancy Services. A equipe é conhecida por sua busca constante por inovação e vitórias.",
    "Mahindra Racing": "Curiosidade: Mahindra Racing é a equipe de Fórmula E da Mahindra Group, um conglomerado indiano. A equipe tem se destacado por seu compromisso com a sustentabilidade e o desempenho competitivo.",
    "Nissan Formula E Team": "Curiosidade: Nissan Formula E Team representa a marca japonesa Nissan na Fórmula E. A equipe é conhecida por sua tecnologia avançada e pilotos talentosos.",
    "NEOM McLaren Formula E Team": "Curiosidade: NEOM McLaren Formula E Team é uma colaboração entre a McLaren e o projeto futurístico NEOM da Arábia Saudita. A equipe se destaca por sua visão inovadora e pilotos de ponta.",
    "NIO 333 Racing": "Curiosidade: NIO 333 Racing é a equipe de Fórmula E da marca chinesa NIO, focada em tecnologia de veículos elétricos. A equipe tem um histórico de desenvolvimento contínuo e competitividade.",
    "TAG Heuer Porsche Formula E Team": "Curiosidade: TAG Heuer Porsche Formula E Team é a equipe da Porsche na Fórmula E, conhecida por sua precisão, velocidade e herança automobilística.",
    "ABT CUPRA Formula E Team": "ABT CUPRA Formula E Team é uma colaboração entre a ABT Sportsline e a CUPRA, trazendo experiência e inovação para a Fórmula E.",
    "Venturi Racing": "Venturi Racing é uma das equipes fundadoras da Fórmula E, conhecida por sua paixão por corridas e compromisso com a mobilidade elétrica.",
}

# função que agrupa os pilotos por equipe
def agrupar_por_equipe(infos_pilotos):
    equipes = {}
    for piloto in infos_pilotos:
        equipe = piloto["equipe"]
        if equipe not in equipes:
            equipes[equipe] = []
        equipes[equipe].append(piloto)
    return equipes

# função que mostra as informações detalhadas de um piloto
def mostrar_informacoes_piloto(piloto):
    info = (
        f"\nNome do Piloto: {piloto['nome']}\n"
        f"Equipe: {piloto['equipe']}\n"
        f"Vitórias do piloto: {piloto['vitorias']}\n"
        f"Títulos Obtidos: {piloto['titulos']}\n"
        f"Curiosidades do piloto: {piloto['curiosidades']}\n"
    )
    print(info)

# permite ao user selecionar um piloto de uma equipe e exibe suas informações
def selecionar_piloto(equipes, nome_equipe):
    infos_pilotos = equipes[nome_equipe]
    while True:
        print(f"\nPilotos da equipe {nome_equipe}:")
        for i, piloto in enumerate(infos_pilotos):
            print(f"{i + 1}. {piloto['nome']}")
        
        entrada = input("Digite o número do piloto (ou 0 para voltar): ")
        if entrada.isdigit():
            indice_piloto = int(entrada) - 1
            if indice_piloto == -1:
                break
            elif 0 <= indice_piloto < len(infos_pilotos):
                mostrar_informacoes_piloto(infos_pilotos[indice_piloto])
                voltar_menu = input("Deseja voltar ao menu principal? (sim/não): ").strip().lower()
                if voltar_menu == "sim":
                    break
                elif voltar_menu == "não":
                    print("Encerrando aplicação...")
                    exit()
                else:
                    print("Opção inválida! Voltando ao menu principal.")
                    break
            else:
                print(f"Comando inválido! Insira um número de 1 a {len(infos_pilotos)}.")
        else:
            print("Comando inválido, escreva o número de um piloto.")

# permite ao user selecionar uma equipe específica e exibe as informações dela
def selecionar_equipe(equipes):
    lista_equipes = list(equipes.keys())
    while True:
        print("\nEquipes disponíveis:")
        for i, equipe in enumerate(lista_equipes):
            print(f"{i + 1}. {equipe}")
        
        entrada = input("Digite o número da equipe (digite 0 para sair): ")
        if entrada.isdigit():
            indice_equipe = int(entrada) - 1
            if indice_equipe == -1:
                print("Encerrando a aplicação...")
                break
            elif 0 <= indice_equipe < len(lista_equipes):
                nome_equipe = lista_equipes[indice_equipe]
                print(f"\nInformações da equipe {nome_equipe}:")
                print(infos_equipes.get(nome_equipe, "Informações não disponíveis."))
                selecionar_piloto(equipes, nome_equipe)
            else:
                print(f"Comando inválido! Insira um número de 1 a {len(lista_equipes)}.")
        else:
            print("Comando inválido, escreva o número de uma equipe (ou selecione seu número!).")

# função da aplicação principal
def tela_principal():
    print("Galeria dos Pilotos de Fórmula E")
    print("="*30)
    
    equipes = agrupar_por_equipe(infos_pilotos)
    selecionar_equipe(equipes)

# inicialização da aplicação
tela_principal()
