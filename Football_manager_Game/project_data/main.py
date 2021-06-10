from project.Coaches.coach import Coach
from project.Players.defender import Defender
from project.Players.forward import Forward
from project.Players.goalkeeper import Goalkeeper
from project.Players.midfielder import Midfielder
from project.Teams.base_team import BaseTeam
from project.tournaments.champions_league import ChampionsLeague


peter_schmeichel = Goalkeeper(name="Peter Schmeichel", height=197, weight= 105, salary=650_000, contract_expiry_date="20/July/2022", stamina=8, transfer_fee=2_000_000, handling=9, jumping=9, reflexes=9)
gary_neville = Defender(name="Gary Nevile", height=173, weight=73, salary=800_000, contract_expiry_date="20/July/2022", stamina=10, transfer_fee=2_000_000, heading=10, pace=9, positioning=9, tackling=9)
phil_neville = Defender(name="Phil Nevile", height=175, weight=76, salary=600_000, contract_expiry_date="20/July/2022", stamina=10, transfer_fee=2_500_000, heading=10, pace=9, positioning=9, tackling=9)
jap_stam = Defender(name="Jap Stam", height=195, weight=98, salary=1_200_000, contract_expiry_date="20/July/2022", stamina=8, transfer_fee=2_600_00, heading=9, pace=10, positioning=9, tackling=8)
wes_brown = Defender(name="Wes Brown", height=181, weight=80, salary=800_000, contract_expiry_date="20/July/2022", stamina=9, transfer_fee=3_000_000, heading=8, pace=9, positioning=8, tackling=8)
roy_keane = Midfielder(name="Roy Keane", height=181, weight=85, salary=1_500_000, contract_expiry_date="20/July/2022", stamina=10, transfer_fee=5_000_000, agression=8, creativity=8, pace=8, passing=8, shooting=8)
paul_scholes = Midfielder(name="Paul Scholes", height=181, weight=82, salary=1_500_000, contract_expiry_date="20/July/2022", stamina=9, transfer_fee=7_500_000, agression=9, creativity=9, pace=8, passing=9, shooting=8)
ryan_giggs = Midfielder(name="Ryan Giggs", height=178, weight=77, salary=1_300_000, contract_expiry_date="20/July/2022", stamina=9, transfer_fee=8_000_000, agression=10, creativity=9, pace=9, passing=9, shooting=8)
david_beckham = Midfielder(name="David Beckham", height=181, weight=82, salary=1_500_000, contract_expiry_date="20/July/2022", stamina=9, transfer_fee=98_500_000, agression=8, creativity=9, pace=8, passing=10, shooting=8)
dwight_yorke = Forward(name="Dwight Yorke", height=184, weight=81, salary=1_800_00, contract_expiry_date="20/July/2022", stamina=8, transfer_fee=10_000_000, speed=10, technique=8, goalscoring=9, heading=10)
andy_cole = Forward(name="Andy Cole", height=186, weight=84, salary=1_800_00, contract_expiry_date="20/July/2022", stamina=9, transfer_fee=9_500_000, speed=10, technique=10, goalscoring=10, heading=10)

# TODO -> create free agents players pool

man_utd_slot = [peter_schmeichel, gary_neville, phil_neville, wes_brown, jap_stam, roy_keane, ryan_giggs, david_beckham, paul_scholes, dwight_yorke, andy_cole]
man_utd = BaseTeam(name="Manchester United", city="Manchester", stadium="Old Traford", stadium_capacity=80_000, chairman="Glazer's Family", finances=100_000_000, nationality="England")
for player in man_utd_slot:
    man_utd.add_player(player)

gk_team2 = Goalkeeper(name="Nelson Dida", height=194, weight= 95, salary=4_650_000, contract_expiry_date="20/July/2022", stamina=9, transfer_fee=3_000_000, handling=6, jumping=9, reflexes=8)
df1_team2 = Defender(name="Paolo Maldini", height=186, weight=87, salary=5_800_000, contract_expiry_date="20/July/2022", stamina=10, transfer_fee=12_000_000, heading=6, pace=9, positioning=9, tackling=9)
df2_team2 = Defender(name="Cafu", height=181, weight=77, salary=4_600_000, contract_expiry_date="20/July/2022", stamina=10, transfer_fee=6_500_000, heading=6, pace=9, positioning=9, tackling=9)
df3_team2 = Defender(name="Alessandro Nesta", height=185, weight=80, salary=5_200_000, contract_expiry_date="20/July/2022", stamina=9, transfer_fee=12_600_00, heading=6, pace=9, positioning=9, tackling=8)
df4_team2 = Defender(name="Franco Baresi", height=185, weight=80, salary=3_800_000, contract_expiry_date="20/July/2022", stamina=9, transfer_fee=13_000_000, heading=8, pace=9, positioning=8, tackling=9)
mf1_team2 = Midfielder(name="Gennaro Gatuso", height=177, weight=80, salary=4_500_000, contract_expiry_date="20/July/2022", stamina=10, transfer_fee=5_000_000, agression=6, creativity=8, pace=8, passing=9, shooting=8)
mf2_team2 = Midfielder(name="Andrea Pirlo", height=181, weight=82, salary=5_500_000, contract_expiry_date="20/July/2022", stamina=8, transfer_fee=9_500_000, agression=8, creativity=9, pace=8, passing=8, shooting=9)
mf3_team2 = Midfielder(name="Dejan Savjcevic", height=178, weight=77, salary=7_300_000, contract_expiry_date="20/July/2022", stamina=9, transfer_fee=8_000_000, agression=7, creativity=9, pace=9, passing=9, shooting=9)
mf4_team2 = Midfielder(name="Ricardo Kaka", height=183, weight=82, salary=10_000_000, contract_expiry_date="20/July/2022", stamina=9, transfer_fee=10_500_000, agression=8, creativity=9, pace=9, passing=10, shooting=9)
fw1_team2 = Forward(name="Filippo Inzaghi", height=181, weight=75, salary=6_800_00, contract_expiry_date="20/July/2022", stamina=8, transfer_fee=8_000_000, speed=8, technique=8, goalscoring=9, heading=9)
fw2_team2 = Forward(name="Andriy Schevchenko", height=186, weight=81, salary=9_800_00, contract_expiry_date="20/July/2022", stamina=8, transfer_fee=10_500_000, speed=9, technique=9, goalscoring=9, heading=9)

players_slot_2 = [gk_team2, df1_team2, df2_team2, df3_team2, df4_team2, mf1_team2, mf2_team2, mf3_team2, mf4_team2, fw1_team2, fw2_team2]
milan = BaseTeam(name="AC MILAN", city="Milano", stadium="San Siro", stadium_capacity=85_000, chairman="Silvio Berlusconi", finances=105_000_000, nationality="Italy")

for player in players_slot_2:
    milan.add_player(player)

gk_team3 = Goalkeeper(name="Viktor Valdez", height=182, weight= 86, salary=4_650_000, contract_expiry_date="20/July/2022", stamina=9, transfer_fee=7_000_000, handling=9, jumping=9, reflexes=9)
df1_team3 = Defender(name="Eric Abidal", height=180, weight=77, salary=5_800_000, contract_expiry_date="20/July/2022", stamina=10, transfer_fee=6_000_000, heading=8, pace=9, positioning=8, tackling=9)
df2_team3 = Defender(name="Dani Alves", height=176, weight=73, salary=5_800_000, contract_expiry_date="20/July/2022", stamina=10, transfer_fee=12_000_000, heading=7, pace=9, positioning=9, tackling=9)
df3_team3 = Defender(name="Carles Puyol", height=188, weight=87, salary=5_800_000, contract_expiry_date="20/July/2022", stamina=9, transfer_fee=10_000_000, heading=9, pace=8, positioning=9, tackling=9)
df4_team3 = Defender(name="Gerard Pique", height=194, weight=88, salary=5_800_000, contract_expiry_date="20/July/2022", stamina=10, transfer_fee=11_000_000, heading=9, pace=9, positioning=9, tackling=9)
mf1_team3 = Midfielder(name="Xavi Hernandez", height=170, weight=70, salary=10_300_000, contract_expiry_date="20/July/2022", stamina=9, transfer_fee=12_000_000, agression=7, creativity=10, pace=8, passing=10, shooting=9)
mf2_team3 = Midfielder(name="Andres Iniesta", height=175, weight=73, salary=9_300_000, contract_expiry_date="20/July/2022", stamina=9, transfer_fee=13_000_000, agression=8, creativity=10, pace=9, passing=10, shooting=8)
mf3_team3 = Midfielder(name="Hristo Stoichkov", height=178, weight=75, salary=8_300_000, contract_expiry_date="20/July/2022", stamina=9, transfer_fee=9_000_000, agression=9, creativity=9, pace=9, passing=9, shooting=9)
mf4_team3 = Midfielder(name="Lionel Messi", height=170, weight=72, salary=15_000_000, contract_expiry_date="20/July/2022", stamina=9, transfer_fee=98_000_000, agression=8, creativity=10, pace=10, passing=10, shooting=10)
fw1_team3 = Forward(name="Samuel Eto'o", height=186, weight=81, salary=9_800_00, contract_expiry_date="20/July/2022", stamina=9, transfer_fee=10_500_000, speed=9, technique=9, goalscoring=9, heading=8)
fw2_team3 = Forward(name="David Villa", height=183, weight=81, salary=9_800_00, contract_expiry_date="20/July/2022", stamina=8, transfer_fee=10_500_000, speed=8, technique=9, goalscoring=9, heading=8)

players_slot_3 = [gk_team3, df1_team3, df2_team3, df3_team3, df4_team3, mf1_team3, mf2_team3, mf3_team3, mf4_team3, fw1_team3, fw2_team3]
barca = BaseTeam(name="FC Barcelona", city="Barcelona", stadium="Camp Nou", stadium_capacity=120_000, chairman="Joan Laporta", finances=120_000_000, nationality="Spain")
for player in players_slot_3:
    barca.add_player(player)

gk_team4 = Goalkeeper(name="Iker Casillas", height=185, weight= 86, salary=7_650_000, contract_expiry_date="20/July/2022", stamina=9, transfer_fee=7_000_000, handling=9, jumping=9, reflexes=9)
df1_team4 = Defender(name="Alvaro Arbeloa", height=185, weight=83, salary=5_800_000, contract_expiry_date="20/July/2022", stamina=10, transfer_fee=6_000_000, heading=8, pace=9, positioning=8, tackling=9)
df2_team4 = Defender(name="Marcelo", height=176, weight=73, salary=5_800_000, contract_expiry_date="20/July/2022", stamina=10, transfer_fee=12_000_000, heading=10, pace=9, positioning=9, tackling=9)
df3_team4 = Defender(name="Sergio Ramos", height=188, weight=87, salary=7_800_000, contract_expiry_date="20/July/2022", stamina=10, transfer_fee=10_000_000, heading=9, pace=9, positioning=9, tackling=9)
df4_team4 = Defender(name="Pepe", height=187, weight=88, salary=5_800_000, contract_expiry_date="20/July/2022", stamina=10, transfer_fee=11_000_000, heading=9, pace=9, positioning=9, tackling=9)
mf1_team4 = Midfielder(name="Xabi Alonso", height=180, weight=78, salary=10_300_000, contract_expiry_date="20/July/2022", stamina=9, transfer_fee=12_000_000, agression=10, creativity=9, pace=8, passing=9, shooting=9)
mf2_team4 = Midfielder(name="Sami Khedira", height=188, weight=85, salary=9_300_000, contract_expiry_date="20/July/2022", stamina=9, transfer_fee=13_000_000, agression=9, creativity=8, pace=8, passing=8, shooting=8)
mf3_team4 = Midfielder(name="Mesut Ozil", height=178, weight=75, salary=10_300_000, contract_expiry_date="20/July/2022", stamina=9, transfer_fee=11_000_000, agression=10, creativity=10, pace=8, passing=9, shooting=8)
mf4_team4 = Midfielder(name="Angel DiMaria", height=177, weight=72, salary=12_000_000, contract_expiry_date="20/July/2022", stamina=9, transfer_fee=10_000_000, agression=8, creativity=9, pace=9, passing=9, shooting=9)
fw1_team4 = Forward(name="Cristiano Ronaldo", height=186, weight=81, salary=14_800_00, contract_expiry_date="20/July/2022", stamina=10, transfer_fee=97_500_000, speed=10, technique=9, goalscoring=9, heading=9)
fw2_team4 = Forward(name="Karim Benzema", height=188, weight=81, salary=10_800_00, contract_expiry_date="20/July/2022", stamina=9, transfer_fee=18_500_000, speed=8, technique=9, goalscoring=9, heading=9)

real_madrid = BaseTeam(name="Real Madrid", city="Madrid", stadium="Santiago Bernabeu", stadium_capacity=78_000, chairman="Florentino Perez", finances=200_000_000, nationality="Spain")

players_slot_4 = [gk_team4, df1_team4, df2_team4, df3_team4, df4_team4, mf1_team4, mf2_team4, mf3_team4, mf4_team4, fw1_team4, fw2_team4]
for player in players_slot_4:
    real_madrid.add_player(player)

oliver_kahn = Goalkeeper(name="Oliver Kahn", height=193, weight=92, salary=6_000_000, contract_expiry_date="20/July/2022", stamina=10, transfer_fee=8_000_000, handling=9, jumping=10, reflexes=9)
gigi_buffon = Goalkeeper(name="Gianluigi Buffon", height=193, weight=88, salary=9_000_000, contract_expiry_date="20/July/2022", stamina=9, transfer_fee=12_000_000, handling=9, jumping=9, reflexes=10)
lucio = Defender(name="Lucio", height=190, weight=87, salary=7_800_000, contract_expiry_date="20/July/2022", stamina=95, transfer_fee=10_000_000, heading=9, pace=8, positioning=9, tackling=9)
virgil = Defender(name="Virgil Van Dyke", height=194, weight=87, salary=11_800_000, contract_expiry_date="20/July/2022", stamina=9, transfer_fee=10_000_000, heading=9, pace=9, positioning=9, tackling=9)
clarence_seedorf = Midfielder(name="Clarence Seedorf", height=178, weight=75, salary=10_000_000, contract_expiry_date="20/July/2022", stamina=9, transfer_fee=10_000_000, agression=9, creativity=9, pace=9, passing=9, shooting=9)
zinedine_zidane = Midfielder(name="Zinedine Zidane", height=183, weight=76, salary=12_000_000, contract_expiry_date="20/July/2022", stamina=8, transfer_fee=12_000_000, agression=9, creativity=10, pace=8, passing=9, shooting=9)
gabriel_batistuta = Forward(name="Gabriel Batistuta", height=188, weight=83, salary=10_800_00, contract_expiry_date="20/July/2022", stamina=9, transfer_fee=18_500_000, speed=8, technique=9, goalscoring=10, heading=9)
ronaldo = Forward(name="Ronaldo", height=183, weight=81, salary=13_800_00, contract_expiry_date="20/July/2022", stamina=9, transfer_fee=18_500_000, speed=9, technique=9, goalscoring=9, heading=8)

carlo_ancelotti = Coach(name="Carlo Ancelotti", nationality="italian", age=63, salary=7_000_000, experience=9, mentality="balanced", coaching_ability=9, formation="4-1-4-1")  # "4-5-1", "4-3-3"
sir_alex_ferguson = Coach(name="Alex Ferguson", nationality="scottish", age=80, salary=5_000_000, experience=10, mentality="attacking", coaching_ability=9, formation="4-4-2")  # "4-1-4-1", "4-3-3"
pep_guardiola = Coach(name="Josep Guardiola", nationality="spanish", age=50, salary=10_000_000, experience=7, mentality="attacking", coaching_ability=9, formation="4-3-3")  # "4-1-4-1", "4-2-4", "3-4-3"
jose_mourinho = Coach(name="Jose Mourinho", nationality="portuguese", age=60, salary=9_000_000, experience=8, mentality="defensive", coaching_ability=8, formation="4-1-4-1")  # "4-3-3", "4-5-1", "5-4-1", "5-3-2"

print(barca.sign_player_as_free_agent(ronaldo))
print(milan.sign_player_as_free_agent(zinedine_zidane))
# print(man_utd.sign_player_as_free_agent(gabriel_batistuta))
print(real_madrid.sign_player_as_free_agent(ronaldo))
print(milan.buy_player(clarence_seedorf))
print()
print(man_utd.release_player(andy_cole))
print(man_utd.sign_player_as_free_agent(clarence_seedorf))

print(man_utd.sign_coach(sir_alex_ferguson))
print(milan.sign_coach(carlo_ancelotti))
print(barca.sign_coach(pep_guardiola))
print(real_madrid.sign_coach(jose_mourinho))
print(barca.sign_coach(carlo_ancelotti))

print(sir_alex_ferguson.coach_strength_message)
print(carlo_ancelotti.coach_strength_message)
print(pep_guardiola.coach_strength_message)
print(jose_mourinho.coach_strength_message)
print()
print(milan.message_for_team_strength)
print(barca.message_for_team_strength)
print(man_utd.message_for_team_strength)
print(real_madrid.message_for_team_strength)

print()
print(man_utd.show_squad())
print(milan.show_squad())
print(barca.show_squad())
print(real_madrid.show_squad())

champions_league = ChampionsLeague([milan, man_utd, real_madrid, barca], trophy_name="UEFA Champions League", prize_money=25_000_000)
champions_league.draw_teams()
print(champions_league.print_groups_teams())
print(champions_league.play_tournament())


# TODO correct the method -> calculate_team_strength, it should iterete through the whole team and sum the separate players qualities and then the teams and coach sterngth