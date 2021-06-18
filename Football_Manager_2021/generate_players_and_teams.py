from project.Coaches.coach import Coach
from project.Players.goalkeeper import Goalkeeper
from project.Players.defender import Defender
from project.Players.midfielder import Midfielder
from project.Players.forward import Forward
from project.Teams.base_team import BaseTeam


class GeneratePlayersAndTeams:

    generated_teams = []

    def __init__(self):

        self.peter_schmeichel = Goalkeeper(name="Peter Schmeichel", height=197, weight=105, salary=650_000,
                                      contract_expiry_date="20/July/2022", stamina=8, transfer_fee=2_000_000, handling=9, jumping=9, reflexes=9)
        self.gary_neville = Defender(name="Gary Nevile", height=173, weight=73, salary=800_000,
                                contract_expiry_date="20/July/2022", stamina=10, transfer_fee=2_000_000, heading=10, pace=9, positioning=9, tackling=9)
        self.phil_neville = Defender(name="Phil Nevile", height=175, weight=76, salary=600_000,
                                contract_expiry_date="20/July/2022", stamina=10, transfer_fee=2_500_000, heading=10, pace=9,
                                positioning=9, tackling=9)
        self.jap_stam = Defender(name="Jap Stam", height=195, weight=98, salary=1_200_000, contract_expiry_date="20/July/2022",
                            stamina=8, transfer_fee=2_600_00, heading=9, pace=10, positioning=9, tackling=8)
        self.wes_brown = Defender(name="Wes Brown", height=181, weight=80, salary=800_000, contract_expiry_date="20/July/2022",
                             stamina=9, transfer_fee=3_000_000, heading=8, pace=9, positioning=8, tackling=8)
        self.roy_keane = Midfielder(name="Roy Keane", height=181, weight=85, salary=1_500_000,
                               contract_expiry_date="20/July/2022", stamina=10, transfer_fee=5_000_000, agression=8,
                               creativity=8, pace=8, passing=8, shooting=8)
        self.paul_scholes = Midfielder(name="Paul Scholes", height=181, weight=82, salary=1_500_000,
                                  contract_expiry_date="20/July/2022", stamina=9, transfer_fee=7_500_000, agression=9,
                                  creativity=9, pace=8, passing=9, shooting=8)
        self.ryan_giggs = Midfielder(name="Ryan Giggs", height=178, weight=77, salary=1_300_000,
                                contract_expiry_date="20/July/2022", stamina=9, transfer_fee=8_000_000, agression=10,
                                creativity=9, pace=9, passing=9, shooting=8)
        self.david_beckham = Midfielder(name="David Beckham", height=181, weight=82, salary=1_500_000,
                                   contract_expiry_date="20/July/2022", stamina=9, transfer_fee=98_500_000, agression=8,
                                   creativity=9, pace=8, passing=10, shooting=8)
        self.dwight_yorke = Forward(name="Dwight Yorke", height=184, weight=81, salary=1_800_00,
                               contract_expiry_date="20/July/2022", stamina=8, transfer_fee=10_000_000, speed=10,
                               technique=8, goalscoring=9, heading=10)
        self.andy_cole = Forward(name="Andy Cole", height=186, weight=84, salary=1_800_00, contract_expiry_date="20/July/2022",
                            stamina=9, transfer_fee=9_500_000, speed=10, technique=10, goalscoring=10, heading=10)

        self.man_utd = BaseTeam(name="Manchester United", city="Manchester", stadium="Old Traford", stadium_capacity=80_000,
                           chairman="Glazer's Family", finances=100_000_000, nationality="England")
        self.man_utd_players = [self.peter_schmeichel, self.gary_neville, self.phil_neville, self.wes_brown, self.jap_stam, self.roy_keane, self.ryan_giggs,
                            self.david_beckham, self.paul_scholes, self.dwight_yorke, self.andy_cole]

        self.man_utd = self.add_players_to_club(self.man_utd_players, self.man_utd)

        self.sir_alex_ferguson = Coach(name="Alex Ferguson", nationality="scottish", age=80, salary=5_000_000, experience=10, mentality="attacking", coaching_ability=9, formation="4-4-2")
        self.man_utd.coach = self.sir_alex_ferguson

        self.gk_team2 = Goalkeeper(name="Nelson Dida", height=194, weight=95, salary=4_650_000,
                              contract_expiry_date="20/July/2022", stamina=9, transfer_fee=3_000_000, handling=10,
                              jumping=9, reflexes=9)
        self.df1_team2 = Defender(name="Paolo Maldini", height=186, weight=87, salary=5_800_000,
                             contract_expiry_date="20/July/2022", stamina=10, transfer_fee=12_000_000, heading=9, pace=9,
                             positioning=10, tackling=10)
        self.df2_team2 = Defender(name="Cafu", height=181, weight=77, salary=4_600_000, contract_expiry_date="20/July/2022",
                             stamina=10, transfer_fee=6_500_000, heading=6, pace=9, positioning=9, tackling=9)
        self.df3_team2 = Defender(name="Alessandro Nesta", height=185, weight=80, salary=5_200_000,
                             contract_expiry_date="20/July/2022", stamina=9, transfer_fee=12_600_00, heading=9, pace=9,
                             positioning=9, tackling=10)
        self.df4_team2 = Defender(name="Franco Baresi", height=185, weight=80, salary=3_800_000,
                             contract_expiry_date="20/July/2022", stamina=9, transfer_fee=13_000_000, heading=10, pace=9,
                             positioning=8, tackling=9)
        self.mf1_team2 = Midfielder(name="Gennaro Gatuso", height=177, weight=80, salary=4_500_000,
                               contract_expiry_date="20/July/2022", stamina=10, transfer_fee=5_000_000, agression=9,
                               creativity=9, pace=10, passing=9, shooting=8)
        self.mf2_team2 = Midfielder(name="Andrea Pirlo", height=181, weight=82, salary=5_500_000,
                               contract_expiry_date="20/July/2022", stamina=8, transfer_fee=9_500_000, agression=10,
                               creativity=9, pace=8, passing=8, shooting=9)
        self.mf3_team2 = Midfielder(name="Dejan Savjcevic", height=178, weight=77, salary=7_300_000,
                               contract_expiry_date="20/July/2022", stamina=9, transfer_fee=8_000_000, agression=10,
                               creativity=9, pace=9, passing=9, shooting=9)
        self.mf4_team2 = Midfielder(name="Ricardo Kaka", height=183, weight=82, salary=10_000_000,
                               contract_expiry_date="20/July/2022", stamina=9, transfer_fee=10_500_000, agression=10,
                               creativity=9, pace=9, passing=10, shooting=9)
        self.fw1_team2 = Forward(name="Filippo Inzaghi", height=181, weight=75, salary=6_800_00,
                            contract_expiry_date="20/July/2022", stamina=8, transfer_fee=8_000_000, speed=8, technique=8,
                            goalscoring=9, heading=9)
        self.fw2_team2 = Forward(name="Andriy Schevchenko", height=186, weight=81, salary=9_800_00,
                            contract_expiry_date="20/July/2022", stamina=8, transfer_fee=10_500_000, speed=9, technique=9,
                            goalscoring=9, heading=9)

        self.milan = BaseTeam(name="AC MILAN", city="Milano", stadium="San Siro", stadium_capacity=85_000,
                         chairman="Silvio Berlusconi", finances=105_000_000, nationality="Italy")

        self.milan_players = [self.gk_team2, self.df1_team2, self.df2_team2, self.df3_team2, self.df4_team2, self.mf1_team2, self.mf2_team2, self.mf3_team2, self.mf4_team2,
                          self.fw1_team2, self.fw2_team2]

        self.milan = self.add_players_to_club(self.milan_players, self.milan)

        self.carlo_ancelotti = Coach(name="Carlo Ancelotti", nationality="italian", age=63, salary=7_000_000, experience=10,
                                mentality="balanced", coaching_ability=9, formation="4-1-4-1")
        self.milan.coach = self.carlo_ancelotti

        self.gk_team3 = Goalkeeper(name="Viktor Valdez", height=182, weight=86, salary=4_650_000,
                              contract_expiry_date="20/July/2022", stamina=9, transfer_fee=7_000_000, handling=9, jumping=9,
                              reflexes=9)
        self.df1_team3 = Defender(name="Eric Abidal", height=180, weight=77, salary=5_800_000,
                             contract_expiry_date="20/July/2022", stamina=10, transfer_fee=6_000_000, heading=8, pace=9,
                             positioning=8, tackling=9)
        self.df2_team3 = Defender(name="Dani Alves", height=176, weight=73, salary=5_800_000,
                             contract_expiry_date="20/July/2022", stamina=10, transfer_fee=12_000_000, heading=7, pace=9,
                             positioning=9, tackling=9)
        self.df3_team3 = Defender(name="Carles Puyol", height=188, weight=87, salary=5_800_000,
                             contract_expiry_date="20/July/2022", stamina=9, transfer_fee=10_000_000, heading=9, pace=8,
                             positioning=9, tackling=9)
        self.df4_team3 = Defender(name="Gerard Pique", height=194, weight=88, salary=5_800_000,
                             contract_expiry_date="20/July/2022", stamina=10, transfer_fee=11_000_000, heading=9, pace=9,
                             positioning=9, tackling=9)
        self.mf1_team3 = Midfielder(name="Xavi Hernandez", height=170, weight=70, salary=10_300_000,
                               contract_expiry_date="20/July/2022", stamina=9, transfer_fee=12_000_000, agression=7,
                               creativity=10, pace=8, passing=10, shooting=9)
        self.mf2_team3 = Midfielder(name="Andres Iniesta", height=175, weight=73, salary=9_300_000,
                               contract_expiry_date="20/July/2022", stamina=9, transfer_fee=13_000_000, agression=8,
                               creativity=10, pace=9, passing=10, shooting=8)
        self.mf3_team3 = Midfielder(name="Hristo Stoichkov", height=178, weight=75, salary=8_300_000,
                               contract_expiry_date="20/July/2022", stamina=9, transfer_fee=9_000_000, agression=9,
                               creativity=9, pace=9, passing=9, shooting=9)
        self.mf4_team3 = Midfielder(name="Lionel Messi", height=170, weight=72, salary=15_000_000,
                               contract_expiry_date="20/July/2022", stamina=9, transfer_fee=98_000_000, agression=8,
                               creativity=10, pace=10, passing=10, shooting=10)
        self.fw1_team3 = Forward(name="Samuel Eto'o", height=186, weight=81, salary=9_800_00,
                            contract_expiry_date="20/July/2022", stamina=9, transfer_fee=10_500_000, speed=9, technique=9,
                            goalscoring=9, heading=8)
        self.fw2_team3 = Forward(name="David Villa", height=183, weight=81, salary=9_800_00, contract_expiry_date="20/July/2022",
                            stamina=8, transfer_fee=10_500_000, speed=8, technique=9, goalscoring=9, heading=8)

        self.barca = BaseTeam(name="FC Barcelona", city="Barcelona", stadium="Camp Nou", stadium_capacity=120_000,
                         chairman="Joan Laporta", finances=120_000_000, nationality="Spain")
        self.barca_players = [self.gk_team3, self.df1_team3, self.df2_team3, self.df3_team3, self.df4_team3, self.mf1_team3, self.mf2_team3, self.mf3_team3, self.mf4_team3,
                          self.fw1_team3, self.fw2_team3]

        self.barca = self.add_players_to_club(self.barca_players, self.barca)

        self.pep_guardiola = Coach(name="Josep Guardiola", nationality="spanish", age=50, salary=10_000_000, experience=7,
                              mentality="attacking", coaching_ability=9,
                              formation="4-3-3")  # "4-1-4-1", "4-2-4", "3-4-3"
        self.barca.coach = self.pep_guardiola

        self.gk_team4 = Goalkeeper(name="Iker Casillas", height=185, weight=86, salary=7_650_000,
                              contract_expiry_date="20/July/2022", stamina=9, transfer_fee=7_000_000, handling=9, jumping=9,
                              reflexes=9)
        self.df1_team4 = Defender(name="Alvaro Arbeloa", height=185, weight=83, salary=5_800_000,
                             contract_expiry_date="20/July/2022", stamina=10, transfer_fee=6_000_000, heading=8, pace=9,
                             positioning=8, tackling=9)
        self.df2_team4 = Defender(name="Marcelo", height=176, weight=73, salary=5_800_000, contract_expiry_date="20/July/2022",
                             stamina=10, transfer_fee=12_000_000, heading=10, pace=9, positioning=9, tackling=9)
        self.df3_team4 = Defender(name="Sergio Ramos", height=188, weight=87, salary=7_800_000,
                             contract_expiry_date="20/July/2022", stamina=10, transfer_fee=10_000_000, heading=9, pace=9,
                             positioning=9, tackling=9)
        self.df4_team4 = Defender(name="Pepe", height=187, weight=88, salary=5_800_000, contract_expiry_date="20/July/2022",
                             stamina=10, transfer_fee=11_000_000, heading=9, pace=9, positioning=9, tackling=9)
        self.mf1_team4 = Midfielder(name="Xabi Alonso", height=180, weight=78, salary=10_300_000,
                               contract_expiry_date="20/July/2022", stamina=9, transfer_fee=12_000_000, agression=10,
                               creativity=9, pace=8, passing=9, shooting=9)
        self.mf2_team4 = Midfielder(name="Sami Khedira", height=188, weight=85, salary=9_300_000,
                               contract_expiry_date="20/July/2022", stamina=9, transfer_fee=13_000_000, agression=9,
                               creativity=8, pace=8, passing=8, shooting=8)
        self.mf3_team4 = Midfielder(name="Mesut Ozil", height=178, weight=75, salary=10_300_000,
                               contract_expiry_date="20/July/2022", stamina=9, transfer_fee=11_000_000, agression=10,
                               creativity=10, pace=8, passing=9, shooting=8)
        self.mf4_team4 = Midfielder(name="Angel DiMaria", height=177, weight=72, salary=12_000_000,
                               contract_expiry_date="20/July/2022", stamina=9, transfer_fee=10_000_000, agression=8,
                               creativity=9, pace=9, passing=9, shooting=9)
        self.fw1_team4 = Forward(name="Cristiano Ronaldo", height=186, weight=81, salary=14_800_00,
                            contract_expiry_date="20/July/2022", stamina=10, transfer_fee=97_500_000, speed=10, technique=9,
                            goalscoring=9, heading=9)
        self.fw2_team4 = Forward(name="Karim Benzema", height=188, weight=81, salary=10_800_00,
                            contract_expiry_date="20/July/2022", stamina=9, transfer_fee=18_500_000, speed=8, technique=9,
                            goalscoring=9, heading=9)

        self.real_madrid = BaseTeam(name="Real Madrid", city="Madrid", stadium="Santiago Bernabeu", stadium_capacity=78_000,
                               chairman="Florentino Perez", finances=200_000_000, nationality="Spain")
        self.real_madrid_players = [self.gk_team4, self.df1_team4, self.df2_team4, self.df3_team4, self.df4_team4, self.mf1_team4, self.mf2_team4, self.mf3_team4, self.mf4_team4,
                          self.fw1_team4, self.fw2_team4]
        self.real_madrid = self.add_players_to_club(self.real_madrid_players, self.real_madrid)

        self.jose_mourinho = Coach(name="Jose Mourinho", nationality="portuguese", age=60, salary=9_000_000, experience=8,
                                   mentality="defensive", coaching_ability=8, formation="4-1-4-1")

        self.real_madrid.coach = self.jose_mourinho

        self.gk_team5 = Goalkeeper(name="Gianluigi Buffon", height=182, weight=86, salary=4_650_000,
                                   contract_expiry_date="20/July/2022", stamina=9, transfer_fee=7_000_000, handling=9,
                                   jumping=9,
                                   reflexes=9)
        self.df1_team5 = Defender(name="Luigi Sartor", height=180, weight=77, salary=5_800_000,
                                  contract_expiry_date="20/July/2022", stamina=10, transfer_fee=6_000_000, heading=8,
                                  pace=9,
                                  positioning=8, tackling=9)
        self.df2_team5 = Defender(name="Antonio Benarrivo", height=176, weight=73, salary=5_800_000,
                                  contract_expiry_date="20/July/2022", stamina=10, transfer_fee=12_000_000, heading=7,
                                  pace=9,
                                  positioning=9, tackling=9)
        self.df3_team5 = Defender(name="Luigi Apolloni", height=188, weight=87, salary=5_800_000,
                                  contract_expiry_date="20/July/2022", stamina=9, transfer_fee=10_000_000, heading=9,
                                  pace=8,
                                  positioning=9, tackling=9)
        self.df4_team5 = Defender(name="Saliou Lassissi", height=194, weight=88, salary=5_800_000,
                                  contract_expiry_date="20/July/2022", stamina=10, transfer_fee=11_000_000, heading=9,
                                  pace=9,
                                  positioning=9, tackling=9)
        self.mf1_team5 = Midfielder(name="Diego Fuser", height=170, weight=70, salary=10_300_000,
                                    contract_expiry_date="20/July/2022", stamina=9, transfer_fee=12_000_000,
                                    agression=7,
                                    creativity=10, pace=8, passing=10, shooting=9)
        self.mf2_team5 = Midfielder(name="Dino Baggio", height=175, weight=73, salary=9_300_000,
                                    contract_expiry_date="20/July/2022", stamina=9, transfer_fee=13_000_000,
                                    agression=8,
                                    creativity=10, pace=9, passing=10, shooting=8)
        self.mf3_team5 = Midfielder(name="Hernán Crespo", height=178, weight=75, salary=8_300_000,
                                    contract_expiry_date="20/July/2022", stamina=9, transfer_fee=9_000_000, agression=9,
                                    creativity=9, pace=9, passing=9, shooting=9)
        self.mf4_team5 = Midfielder(name="Ariel Ortega", height=170, weight=72, salary=15_000_000,
                                    contract_expiry_date="20/July/2022", stamina=9, transfer_fee=98_000_000,
                                    agression=8,
                                    creativity=10, pace=10, passing=10, shooting=10)
        self.fw1_team5 = Forward(name="Márcio Amoroso", height=186, weight=81, salary=9_800_00,
                                 contract_expiry_date="20/July/2022", stamina=9, transfer_fee=10_500_000, speed=9, technique=9,
                                 goalscoring=9, heading=8)
        self.fw2_team5 = Forward(name="Mario Stanić", height=183, weight=81, salary=9_800_00,
                                 contract_expiry_date="20/July/2022",
                                 stamina=8, transfer_fee=10_500_000, speed=8, technique=9, goalscoring=9, heading=8)
        self.parma = BaseTeam(name="AS Parma", city="Parma", stadium="Ennio Tardini", stadium_capacity=34_000,
                               chairman="Calisto Tanzi", finances=100_000_000, nationality="Italy")

        self.parma_players = [self.gk_team5, self.df1_team5, self.df2_team5, self.df3_team5, self.df4_team5, self.mf1_team5, self.mf2_team5,
                              self.mf3_team5, self.mf4_team5, self.fw1_team5, self.fw2_team5]

        self.parma = self.add_players_to_club(self.parma_players, self.parma)

        self.nevio_scala = Coach(name="Nevio Scala", nationality="italian", age=56, salary=7_000_000, experience=9,
                                 mentality="attacking", coaching_ability=9, formation="4-3-3")
        self.parma.coach = self.nevio_scala

        self.oliver_kahn = Goalkeeper(name="Oliver Kahn", height=193, weight=92, salary=6_000_000,
                                 contract_expiry_date="20/July/2022", stamina=10, transfer_fee=8_000_000, handling=9,
                                 jumping=10, reflexes=9)
        self.lucio = Defender(name="Lucio", height=190, weight=87, salary=7_800_000, contract_expiry_date="20/July/2022",
                         stamina=95, transfer_fee=10_000_000, heading=9, pace=8, positioning=9, tackling=9)
        self.virgil = Defender(name="Virgil Van Dyke", height=194, weight=87, salary=11_800_000,
                          contract_expiry_date="20/July/2022", stamina=9, transfer_fee=10_000_000, heading=9, pace=9, positioning=9, tackling=9)
        self.clarence_seedorf = Midfielder(name="Clarence Seedorf", height=178, weight=75, salary=10_000_000,
                                      contract_expiry_date="20/July/2022", stamina=9, transfer_fee=10_000_000,
                                      agression=9, creativity=9, pace=9, passing=9, shooting=9)
        self.zinedine_zidane = Midfielder(name="Zinedine Zidane", height=183, weight=76, salary=12_000_000,
                                     contract_expiry_date="20/July/2022", stamina=8, transfer_fee=12_000_000,
                                     agression=9, creativity=10, pace=8, passing=9, shooting=9)
        self.ronaldihno = Midfielder(name="Ronaldihno", height=183, weight=76, salary=12_000_000,
                                contract_expiry_date="20/July/2022", stamina=8, transfer_fee=12_000_000, agression=9,
                                creativity=10, pace=8, passing=9, shooting=9)
        self.zola = Midfielder(name="Zola", height=183, weight=76, salary=12_000_000,
                          contract_expiry_date="20/July/2022", stamina=8, transfer_fee=12_000_000, agression=9,
                          creativity=10, pace=8, passing=9, shooting=9)
        self.maradona = Midfielder(name="Maradona", height=183, weight=76, salary=12_000_000,
                              contract_expiry_date="20/July/2022", stamina=8, transfer_fee=12_000_000, agression=9,
                              creativity=10, pace=8, passing=9, shooting=9)
        self.gabriel_batistuta = Forward(name="Gabriel Batistuta", height=188, weight=83, salary=10_800_00,
                                    contract_expiry_date="20/July/2022", stamina=9, transfer_fee=18_500_000, speed=8,
                                    technique=9, goalscoring=10, heading=9)
        self.ronaldo = Forward(name="Ronaldo", height=183, weight=81, salary=13_800_00, contract_expiry_date="20/July/2022",
                          stamina=9, transfer_fee=18_500_000, speed=9, technique=9, goalscoring=9, heading=8)
        self.mbappe = Forward(name="Ronaldo", height=183, weight=81, salary=13_800_00, contract_expiry_date="20/July/2022",
                         stamina=9, transfer_fee=18_500_000, speed=9, technique=9, goalscoring=9, heading=8)

        self.free_agents_slot1 = [self.oliver_kahn, self.lucio, self.virgil, self.clarence_seedorf, self.zinedine_zidane, self.ronaldihno, self.zola, self.maradona,
                             self.gabriel_batistuta, self.ronaldihno, self.mbappe]

        self.goerge_weah = Forward(name="George Weah", height=183, weight=81, salary=13_800_00, contract_expiry_date="20/July/2022",
                         stamina=9, transfer_fee=18_500_000, speed=9, technique=9, goalscoring=9, heading=8)

        self.dennis_bergkamp = Forward(name="Dennis Bergkamp", height=183, weight=81, salary=13_800_00, contract_expiry_date="20/July/2022",
                         stamina=9, transfer_fee=18_500_000, speed=9, technique=9, goalscoring=9, heading=8)

        self.lotar_matthaus = Forward(name="Lotar Matthaus", height=183, weight=81, salary=13_800_00, contract_expiry_date="20/July/2022",
                         stamina=9, transfer_fee=18_500_000, speed=9, technique=9, goalscoring=9, heading=8)

        self.trifon_ivanov = Defender(name="Trifon Ivanov", height=190, weight=87, salary=7_800_000,
                              contract_expiry_date="20/July/2022",
                              stamina=95, transfer_fee=10_000_000, heading=9, pace=8, positioning=9, tackling=9)

        self.franz_beckenbauer = Defender(name="Franz Beckenbauer", height=190, weight=87, salary=7_800_000,
                                      contract_expiry_date="20/July/2022",
                                      stamina=95, transfer_fee=10_000_000, heading=9, pace=8, positioning=9, tackling=9)

        self.zico = Midfielder(name="Zico", height=183, weight=76, salary=12_000_000,
                                          contract_expiry_date="20/July/2022", stamina=8, transfer_fee=12_000_000,
                                          agression=9, creativity=10, pace=8, passing=9, shooting=9)

        self.petar_jekov = Forward(name="Petar Jekov", height=183, weight=81, salary=13_800_00,
                                       contract_expiry_date="20/July/2022",
                                       stamina=9, transfer_fee=18_500_000, speed=9, technique=9, goalscoring=9, heading=8)
        self.emil_kostadinov = Forward(name="Emil Kostadinov", height=183, weight=81, salary=13_800_00,
                                       contract_expiry_date="20/July/2022",
                                       stamina=9, transfer_fee=18_500_000, speed=9, technique=9, goalscoring=9, heading=8)

        self.krasi_balakov = Midfielder(name="Krasimir Balakov", height=183, weight=76, salary=12_000_000,
                               contract_expiry_date="20/July/2022", stamina=8, transfer_fee=12_000_000,
                               agression=9, creativity=10, pace=8, passing=9, shooting=9)

        self.frank_lampard = Midfielder(name="Frank Lampard", height=183, weight=76, salary=12_000_000,
                               contract_expiry_date="20/July/2022", stamina=8, transfer_fee=12_000_000,
                               agression=9, creativity=10, pace=8, passing=9, shooting=9)

        self.lev_yashin = Goalkeeper(name="Lev Yashin", height=193, weight=92, salary=6_000_000,
                                      contract_expiry_date="20/July/2022", stamina=10, transfer_fee=8_000_000,
                                      handling=9,
                                      jumping=10, reflexes=9)

        self.david_de_gea = Goalkeeper(name="David De Gea", height=193, weight=92, salary=6_000_000,
                                      contract_expiry_date="20/July/2022", stamina=10, transfer_fee=8_000_000,
                                      handling=9,
                                      jumping=10, reflexes=9)

        self.free_agents_slot = [self.goerge_weah, self.dennis_bergkamp, self.lotar_matthaus, self.trifon_ivanov, self.franz_beckenbauer,
                                 self.zico, self.emil_kostadinov, self.krasi_balakov, self.frank_lampard, self.lev_yashin, self.david_de_gea, self.petar_jekov]  # TODO create 11 free agent players and add them into this list

        self.fc_juventus = BaseTeam(name="Juventus", city="Torino", stadium="Dele Alpi", stadium_capacity=71_000,
                               chairman="FIAT", finances=130_000_000, nationality="Italy")

        self.antonio_conte = Coach(name="Antonio Conte", nationality="italian", age=50, salary=10_000_000, experience=7,
                              mentality="attacking", coaching_ability=9, formation="4-3-3")

        self.fc_juventus_players = [self.oliver_kahn, self.lucio, self.virgil, self.clarence_seedorf, self.zinedine_zidane, self.ronaldihno, self.zola, self.maradona,
                             self.gabriel_batistuta, self.ronaldihno, self.mbappe]

        self.fc_juventus = self.add_players_to_club(self.fc_juventus_players, self.fc_juventus)
        self.fc_juventus.coach = self.antonio_conte

        self.inter = BaseTeam(name="Inter Milano", city="Milano", stadium="San Siro", stadium_capacity=85_000,
                         chairman="Massimo Morati", finances=120_000_000, nationality="Italy")
        self.helenio_herrera = Coach(name="Helenio Herera", nationality="argentinian", age=60, salary=6_000_000,
                                experience=10, mentality="defensive", coaching_ability=9, formation="4-5-1")
        self.inter_players = [self.oliver_kahn, self.lucio, self.virgil, self.clarence_seedorf, self.zinedine_zidane, self.ronaldihno, self.zola, self.maradona,
                             self.gabriel_batistuta, self.ronaldihno, self.mbappe]

        self.inter = self.add_players_to_club(self.inter_players, self.inter)

        self.inter.coach = self.helenio_herrera

        self.bayern_munich = BaseTeam(name="Bayern Munich", city="Munich", stadium="Allianz Arena", stadium_capacity=69_000,
                                 chairman="Oliver Kahn", finances=110_000_000, nationality="Germany")
        self.trapatoni = Coach(name="Giovanni Trapatoni", nationality="italian", age=60, salary=6_000_000, experience=10,
                          mentality="balanced", coaching_ability=9, formation="4-4-2")

        self.bayern_munich_players = [self.oliver_kahn, self.lucio, self.virgil, self.clarence_seedorf, self.zinedine_zidane, self.ronaldihno, self.zola, self.maradona,
                             self.gabriel_batistuta, self.ronaldihno, self.mbappe]
        self.bayern_munich = self.add_players_to_club(self.bayern_munich_players, self.bayern_munich)
        self.bayern_munich.coach = self.trapatoni

        self.liverpool = BaseTeam(name="Liverpool", city="Liverpool", stadium="Anfiled Road", stadium_capacity=67_000,
                             chairman="Gteven Gerrard", finances=130_000_000, nationality="England")
        self.klopp = Coach(name="Jurgen Klopp", nationality="german", age=52, salary=8_000_000, experience=8,
                      mentality="attacking", coaching_ability=9, formation="4-3-3")

        self.liverpool_players = [self.oliver_kahn, self.lucio, self.virgil, self.clarence_seedorf, self.zinedine_zidane, self.ronaldihno, self.zola, self.maradona,
                             self.gabriel_batistuta, self.ronaldihno, self.mbappe]

        self.liverpool = self.add_players_to_club(self.liverpool_players, self.liverpool)

        self.liverpool.coach = self.klopp

        self.atletico_madrid = BaseTeam(name="Atletico Madrid", city="Madrid", stadium="Wanda Metrolopitano", stadium_capacity=72_000,
                             chairman="Enrique Cerezo", finances=130_000_000, nationality="Spain")
        self.diego_simeone = Coach(name="Diego Simeone", nationality="argentinian", age=50, salary=10_000_000, experience=8, mentality="defensive", coaching_ability=8, formation="4-3-3")

        self.atletico_madrid_players = [self.oliver_kahn, self.lucio, self.virgil, self.clarence_seedorf, self.zinedine_zidane, self.ronaldihno, self.zola, self.maradona,
                             self.gabriel_batistuta, self.ronaldihno, self.mbappe]
        self.atletico_madrid = self.add_players_to_club(self.atletico_madrid_players, self.atletico_madrid)
        self.atletico_madrid.coach = self.diego_simeone

        self.borussia_dortmund = BaseTeam(name="Borussia Dortmund", city="Dortmund", stadium="Westfalenstadion", stadium_capacity=83_000,
                             chairman="Reinhard Rauball", finances=180_000_000, nationality="Germany")

        self.thomas_tuchel = Coach(name="Thomas Tuchel", nationality="german", age=49, salary=10_000_000, experience=8, mentality="balanced", coaching_ability=9, formation="4-3-3")

        self.borussia_dortmund_players = [self.oliver_kahn, self.lucio, self.virgil, self.clarence_seedorf, self.zinedine_zidane, self.ronaldihno, self.zola, self.maradona,
                             self.gabriel_batistuta, self.ronaldihno, self.mbappe]
        self.borussia_dortmund = self.add_players_to_club(self.borussia_dortmund_players, self.borussia_dortmund)

        self.borussia_dortmund.coach = self.thomas_tuchel

        self.ajax_amsterdam = BaseTeam(name="Football Club Ajax", city="Amsterdam", stadium="Johan Cruyff Arena", stadium_capacity=55_000,
                             chairman="Frank Eijken", finances=120_000_000, nationality="Netherland")

        self.rinus_michels = Coach(name="Rhinus Michels", nationality="dutch", age=72, salary=5_000_000, experience=10, mentality="attacking", coaching_ability=10, formation="4-2-4")

        self.ajax_amsterdam_players = [self.oliver_kahn, self.lucio, self.virgil, self.clarence_seedorf, self.zinedine_zidane, self.ronaldihno, self.zola, self.maradona,
                             self.gabriel_batistuta, self.ronaldihno, self.mbappe]
        self.ajax_amsterdam = self.add_players_to_club(self.ajax_amsterdam_players, self.ajax_amsterdam)
        self.ajax_amsterdam.coach = self.rinus_michels

        self.glasgow_rangers = BaseTeam(name="Rangers Football Club", city="Glasgow", stadium="Aibrox", stadium_capacity=52_000,
                             chairman="Douglas Park", finances=120_000_000, nationality="Scotland")

        self.glasgow_rangers_players = [self.oliver_kahn, self.lucio, self.virgil, self.clarence_seedorf, self.zinedine_zidane, self.ronaldihno, self.zola, self.maradona,
                             self.gabriel_batistuta, self.ronaldihno, self.mbappe]
        self.glasgow_rangers = self.add_players_to_club(self.glasgow_rangers_players, self.glasgow_rangers)

        self.willie_wadel = Coach(name="Willie Waddell", nationality="scotish", age=62, salary=5_000_000, experience=9, mentality="attacking", coaching_ability=9, formation="4-4-2")

        self.glasgow_rangers.coach = self.willie_wadel

        self.dinamo_kiev = BaseTeam(name="Dynamo Kyiv", city="Kyiv", stadium="Olimpiyskiy", stadium_capacity=70_000,
                             chairman="Ihor Surkis", finances=120_000_000, nationality="Ukraine")

        self.valeriy_lobanovskyi = Coach(name="Valeriy Lobanovskyi,", nationality="ukrainian", age=62, salary=5_000_000, experience=10, mentality="balanced", coaching_ability=10, formation="4-4-2")

        self.dinamo_kiev_players = [self.oliver_kahn, self.lucio, self.virgil, self.clarence_seedorf, self.zinedine_zidane, self.ronaldihno, self.zola, self.maradona,
                             self.gabriel_batistuta, self.ronaldihno, self.mbappe]

        self.dinamo_kiev = self.add_players_to_club(self.dinamo_kiev_players, self.dinamo_kiev)
        self.dinamo_kiev.coach = self.valeriy_lobanovskyi

        self.arsenal = BaseTeam(name="The Arsenal Football Club", city="London", stadium="Highbury Ground", stadium_capacity=38_000,
                             chairman="Kronke Sports", finances=190_000_000, nationality="England")

        self.arsene_wenger = Coach(name="Arsene Wenger,", nationality="french", age=62, salary=9_000_000, experience=10, mentality="attacking", coaching_ability=10, formation="4-4-2")

        self.arsenal_players = [self.oliver_kahn, self.lucio, self.virgil, self.clarence_seedorf, self.zinedine_zidane, self.ronaldihno, self.zola, self.maradona,
                             self.gabriel_batistuta, self.ronaldihno, self.mbappe]
        self.arsenal = self.add_players_to_club(self.arsenal_players, self.arsenal)

        self.arsenal.coach = self.arsene_wenger

        self.man_city = BaseTeam(name="Manchester City", city="Manchester", stadium="Stadium of Light", stadium_capacity=66_000,
                             chairman="Muhamad al Parichko", finances=500_000_000, nationality="England")
        self.mauricio_pochetino = Coach(name="Mouricio Pochetino", nationality="argentine", age=42, salary=9_000_000, experience=8, mentality="balanced", coaching_ability=9, formation="4-4-2")

        self.man_city_players = [self.oliver_kahn, self.lucio, self.virgil, self.clarence_seedorf, self.zinedine_zidane, self.ronaldihno, self.zola, self.maradona,
                             self.gabriel_batistuta, self.ronaldihno, self.mbappe]
        self.man_city = self.add_players_to_club(self.man_city_players, self.man_city)

        self.man_city.coach = self.mauricio_pochetino

        self.paris_saint_germain = BaseTeam(name="Paris Saint Germain", city="Paris", stadium="Parc de Prences", stadium_capacity=50_000,
                             chairman="Muhamad Al Faied", finances=490_000_000, nationality="France")

        self.laurent_blank = Coach(name="Lauernt Blank", nationality="french", age=52, salary=9_000_000, experience=9, mentality="balanced", coaching_ability=9, formation="4-4-2")

        self.paris_saint_germain_players = [self.oliver_kahn, self.lucio, self.virgil, self.clarence_seedorf, self.zinedine_zidane, self.ronaldihno, self.zola, self.maradona,
                             self.gabriel_batistuta, self.ronaldihno, self.mbappe]
        self.paris_saint_germain = self.add_players_to_club(self.paris_saint_germain_players, self.paris_saint_germain)
        self.paris_saint_germain.coach = self.laurent_blank

        self.cska_sofia = BaseTeam(name="CSKA Sofia 1948", city="Sofia", stadium="Bulgarska Armia", stadium_capacity=26_000,
                             chairman="Miro Vatov", finances=100_000_000, nationality="Bulgaria")

        self.dimitar_penev = Coach(name="Dimitar Penev", nationality="bulgarian", age=72, salary=3_000_000, experience=10, mentality="balanced", coaching_ability=10, formation="4-4-2")

        self.cska_sofia_players = [self.oliver_kahn, self.lucio, self.virgil, self.clarence_seedorf, self.zinedine_zidane, self.ronaldihno, self.zola, self.maradona,
                             self.gabriel_batistuta, self.ronaldihno, self.mbappe]
        self.cska_sofia = self.add_players_to_club(self.cska_sofia_players, self.cska_sofia)

        self.cska_sofia.coach = self.dimitar_penev

        self.botev_vratsa = BaseTeam(name="PFC Botev Vratsa", city="Vratsa", stadium="Hristo Botev", stadium_capacity=28_000,
                             chairman="Miro Vatov", finances=100_000_000, nationality="Bulgaria")

        self.sasho_angelov = Coach(name="Sasho Angelov", nationality="bulgarian", age=62, salary=3_000_000, experience=10, mentality="balanced", coaching_ability=10, formation="4-4-2")

        self.botev_vratsa_players = [self.oliver_kahn, self.lucio, self.virgil, self.clarence_seedorf, self.zinedine_zidane, self.ronaldihno, self.zola, self.maradona,
                             self.gabriel_batistuta, self.ronaldihno, self.mbappe]
        self.botev_vratsa = self.add_players_to_club(self.botev_vratsa_players, self.botev_vratsa)
        self.botev_vratsa.coach = self.sasho_angelov

        "------------------------------------------------------------------------------------------------------------------------"

        self.coaches = [self.sir_alex_ferguson, self.jose_mourinho, self.carlo_ancelotti, self.pep_guardiola, self.nevio_scala,
                        self.antonio_conte, self.diego_simeone, self.thomas_tuchel, self.rinus_michels, self.willie_wadel,
                        self.arsene_wenger, self.mauricio_pochetino, self.dimitar_penev, self.sasho_angelov, self.laurent_blank]

        """"
                    [self.man_utd_games, self.milan_games, self.barca_games, self.real_madrid_games, self.atletico_madrid_games,
                             self.parma_games, self.juventus_games, self.borussia_dortmund_games, self.ajax_games, self.glasgow_rangers_games,
                             self.arsenal_games, self.man_city_games, self.paris_saint_germain_games, self.cska_games, self.botev_vratsa_games, self.liverpool]
        """

        self.teams = [self.man_utd, self.milan, self.barca, self.real_madrid, self.atletico_madrid,  self.parma, self.fc_juventus,
                      self.borussia_dortmund, self.ajax_amsterdam, self.glasgow_rangers, self.arsenal, self.man_city,
                      self.paris_saint_germain, self.cska_sofia, self.botev_vratsa, self.liverpool]

        self.champions_league_teams = [self.man_utd, self.milan, self.barca, self.real_madrid, self.atletico_madrid, self.fc_juventus,
                      self.borussia_dortmund, self.liverpool, self.arsenal, self.man_city,  self.paris_saint_germain, self.bayern_munich, self.dinamo_kiev, self.inter]

        GeneratePlayersAndTeams.generated_teams = [self.man_utd, self.milan, self.barca, self.real_madrid, self.atletico_madrid, self.parma, self.fc_juventus,
                    self.borussia_dortmund, self.ajax_amsterdam, self.glasgow_rangers, self.arsenal,
                    self.man_city, self.paris_saint_germain, self.cska_sofia, self.botev_vratsa, self.liverpool]

    def print_teams(self):
        data = []
        for team in self.teams:
            data.append(team.name)
        return '\n'.join(data)

    @staticmethod
    def add_players_to_club(players_slot, club):
        for player in players_slot:
            club.add_player(player)
        return club
