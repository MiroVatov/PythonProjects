from project.Coaches.coach import Coach
from project.Players.defender import Defender
from project.Players.forward import Forward
from project.Players.goalkeeper import Goalkeeper
from project.Players.midfielder import Midfielder
from project.Teams.base_team import BaseTeam


peter_schmeichel = Goalkeeper(name="Peter Schmeichel", height=197, weight= 105, salary=650_000, contract_expiry_date="20/July/2022", stamina=80, transfer_fee=2_000_000, handling=95, jumping=90, reflexes=90)
gary_neville = Defender(name="Gary Nevile", height=173, weight=73, salary=800_000, contract_expiry_date="20/July/2022", stamina=100, transfer_fee=2_000_000, heading=50, pace=90, positioning=88, tackling=90)
phil_neville = Defender(name="Phil Nevile", height=175, weight=76, salary=600_000, contract_expiry_date="20/July/2022", stamina=100, transfer_fee=2_500_000, heading=50, pace=90, positioning=88, tackling=90)
jap_stam = Defender(name="Jap Stam", height=195, weight=98, salary=1_200_000, contract_expiry_date="20/July/2022", stamina=850, transfer_fee=2_600_00, heading=95, pace=80, positioning=88, tackling=85)
wes_brown = Defender(name="Wes Brown", height=181, weight=80, salary=800_000, contract_expiry_date="20/July/2022", stamina=95, transfer_fee=3_000_000, heading=85, pace=90, positioning=87, tackling=85)
roy_keane = Midfielder(name="Roy Keane", height=181, weight=85, salary=1_500_000, contract_expiry_date="20/July/2022", stamina=100, transfer_fee=5_000_000, agression=100, creativity=82, pace=85, passing=86, shooting=80)
paul_scholes = Midfielder(name="Paul Scholes", height=181, weight=82, salary=1_500_000, contract_expiry_date="20/July/2022", stamina=90, transfer_fee=7_500_000, agression=95, creativity=95, pace=85, passing=95, shooting=88)
ryan_giggs = Midfielder(name="Ryan Giggs", height=178, weight=77, salary=1_300_000, contract_expiry_date="20/July/2022", stamina=95, transfer_fee=8_000_000, agression=75, creativity=95, pace=90, passing=95, shooting=88)
david_beckham = Midfielder(name="David Beckham", height=181, weight=82, salary=1_500_000, contract_expiry_date="20/July/2022", stamina=90, transfer_fee=98_500_000, agression=85, creativity=95, pace=80, passing=100, shooting=88)
dwight_yorke = Forward(name="Dwight Yorke", height=184, weight=81, salary=1_800_00, contract_expiry_date="20/July/2022", stamina=85, transfer_fee=10_000_000, speed=88, technique=82, goalscoring=88, heading=88)
andy_cole = Forward(name="Andy Cole", height=186, weight=84, salary=1_800_00, contract_expiry_date="20/July/2022", stamina=90, transfer_fee=9_500_000, speed=88, technique=82, goalscoring=88, heading=88)

# TODO -> create free agents players pool

man_utd_slot = [peter_schmeichel, gary_neville, phil_neville, wes_brown, jap_stam, roy_keane, ryan_giggs, david_beckham, paul_scholes, dwight_yorke, andy_cole]
man_utd = BaseTeam(name="Manchester United", city="Manchester", stadium="Old Traford", stadium_capacity=80_000, chairman="Glazer's Family", finances=100_000_000, nationality="England")
for player in man_utd_slot:
    man_utd.add_player(player)

gk_team2 = Goalkeeper(name="Nelson Dida", height=194, weight= 95, salary=4_650_000, contract_expiry_date="20/July/2022", stamina=90, transfer_fee=3_000_000, handling=95, jumping=90, reflexes=85)
df1_team2 = Defender(name="Paolo Maldini", height=186, weight=87, salary=5_800_000, contract_expiry_date="20/July/2022", stamina=100, transfer_fee=12_000_000, heading=90, pace=90, positioning=95, tackling=100)
df2_team2 = Defender(name="Cafu", height=181, weight=77, salary=4_600_000, contract_expiry_date="20/July/2022", stamina=100, transfer_fee=6_500_000, heading=80, pace=95, positioning=88, tackling=90)
df3_team2 = Defender(name="Alessandro Nesta", height=185, weight=80, salary=5_200_000, contract_expiry_date="20/July/2022", stamina=90, transfer_fee=12_600_00, heading=95, pace=90, positioning=88, tackling=100)
df4_team2 = Defender(name="Franco Baresi", height=185, weight=80, salary=3_800_000, contract_expiry_date="20/July/2022", stamina=90, transfer_fee=13_000_000, heading=85, pace=90, positioning=100, tackling=95)
mf1_team2 = Midfielder(name="Gennaro Gatuso", height=177, weight=80, salary=4_500_000, contract_expiry_date="20/July/2022", stamina=100, transfer_fee=5_000_000, agression=100, creativity=82, pace=85, passing=86, shooting=80)
mf2_team2 = Midfielder(name="Andrea Pirlo", height=181, weight=82, salary=5_500_000, contract_expiry_date="20/July/2022", stamina=86, transfer_fee=9_500_000, agression=80, creativity=100, pace=85, passing=100, shooting=88)
mf3_team2 = Midfielder(name="Dejan Savjcevic", height=178, weight=77, salary=7_300_000, contract_expiry_date="20/July/2022", stamina=90, transfer_fee=8_000_000, agression=75, creativity=95, pace=90, passing=95, shooting=90)
mf4_team2 = Midfielder(name="Ricardo Kaka", height=183, weight=82, salary=10_000_000, contract_expiry_date="20/July/2022", stamina=90, transfer_fee=10_500_000, agression=85, creativity=95, pace=95, passing=100, shooting=90)
fw1_team2 = Forward(name="Filippo Inzaghi", height=181, weight=75, salary=6_800_00, contract_expiry_date="20/July/2022", stamina=80, transfer_fee=8_000_000, speed=85, technique=85, goalscoring=95, heading=88)
fw2_team2 = Forward(name="Andriy Schevchenko", height=186, weight=81, salary=9_800_00, contract_expiry_date="20/July/2022", stamina=86, transfer_fee=10_500_000, speed=88, technique=92, goalscoring=95, heading=92)

players_slot_2 = [gk_team2, df1_team2, df2_team2, df3_team2, df4_team2, mf1_team2, mf2_team2, mf3_team2, mf4_team2, fw1_team2, fw2_team2]
milan = BaseTeam(name="AC MILAN", city="Milano", stadium="San Siro", stadium_capacity=85_000, chairman="Silvio Berlusconi", finances=105_000_000, nationality="Italy")

for player in players_slot_2:
    milan.add_player(player)

gk_team3 = Goalkeeper(name="Viktor Valdez", height=182, weight= 86, salary=4_650_000, contract_expiry_date="20/July/2022", stamina=90, transfer_fee=7_000_000, handling=90, jumping=90, reflexes=90)
df1_team3 = Defender(name="Eric Abidal", height=180, weight=77, salary=5_800_000, contract_expiry_date="20/July/2022", stamina=100, transfer_fee=6_000_000, heading=80, pace=90, positioning=85, tackling=90)
df2_team3 = Defender(name="Dani Alves", height=176, weight=73, salary=5_800_000, contract_expiry_date="20/July/2022", stamina=100, transfer_fee=12_000_000, heading=75, pace=95, positioning=90, tackling=90)
df3_team3 = Defender(name="Carles Puyol", height=188, weight=87, salary=5_800_000, contract_expiry_date="20/July/2022", stamina=90, transfer_fee=10_000_000, heading=95, pace=85, positioning=95, tackling=95)
df4_team3 = Defender(name="Gerard Pique", height=194, weight=88, salary=5_800_000, contract_expiry_date="20/July/2022", stamina=100, transfer_fee=11_000_000, heading=90, pace=90, positioning=90, tackling=90)
mf1_team3 = Midfielder(name="Xavi Hernandez", height=170, weight=70, salary=10_300_000, contract_expiry_date="20/July/2022", stamina=90, transfer_fee=12_000_000, agression=75, creativity=100, pace=85, passing=100, shooting=90)
mf2_team3 = Midfielder(name="Andres Iniesta", height=175, weight=73, salary=9_300_000, contract_expiry_date="20/July/2022", stamina=90, transfer_fee=13_000_000, agression=80, creativity=100, pace=90, passing=100, shooting=80)
mf3_team3 = Midfielder(name="Hristo Stoichkov", height=178, weight=75, salary=8_300_000, contract_expiry_date="20/July/2022", stamina=90, transfer_fee=9_000_000, agression=95, creativity=90, pace=95, passing=95, shooting=95)
mf4_team3 = Midfielder(name="Lionel Messi", height=170, weight=72, salary=15_000_000, contract_expiry_date="20/July/2022", stamina=90, transfer_fee=98_000_000, agression=85, creativity=100, pace=100, passing=100, shooting=100)
fw1_team3 = Forward(name="Samuel Eto'o", height=186, weight=81, salary=9_800_00, contract_expiry_date="20/July/2022", stamina=90, transfer_fee=10_500_000, speed=90, technique=92, goalscoring=95, heading=80)
fw2_team3 = Forward(name="David Villa", height=183, weight=81, salary=9_800_00, contract_expiry_date="20/July/2022", stamina=86, transfer_fee=10_500_000, speed=88, technique=92, goalscoring=95, heading=83)

players_slot_3 = [gk_team3, df1_team3, df2_team3, df3_team3, df4_team3, mf1_team3, mf2_team3, mf3_team3, mf4_team3, fw1_team3, fw2_team3]
barca = BaseTeam(name="FC Barcelona", city="Barcelona", stadium="Camp Nou", stadium_capacity=120_000, chairman="Joan Laporta", finances=120_000_000, nationality="Spain")
for player in players_slot_3:
    barca.add_player(player)

gk_team4 = Goalkeeper(name="Iker Casillas", height=185, weight= 86, salary=7_650_000, contract_expiry_date="20/July/2022", stamina=90, transfer_fee=7_000_000, handling=95, jumping=95, reflexes=95)
df1_team4 = Defender(name="Alvaro Arbeloa", height=185, weight=83, salary=5_800_000, contract_expiry_date="20/July/2022", stamina=100, transfer_fee=6_000_000, heading=80, pace=90, positioning=85, tackling=90)
df2_team4 = Defender(name="Marcelo", height=176, weight=73, salary=5_800_000, contract_expiry_date="20/July/2022", stamina=100, transfer_fee=12_000_000, heading=75, pace=95, positioning=90, tackling=95)
df3_team4 = Defender(name="Sergio Ramos", height=188, weight=87, salary=7_800_000, contract_expiry_date="20/July/2022", stamina=100, transfer_fee=10_000_000, heading=95, pace=95, positioning=95, tackling=95)
df4_team4 = Defender(name="Pepe", height=187, weight=88, salary=5_800_000, contract_expiry_date="20/July/2022", stamina=100, transfer_fee=11_000_000, heading=90, pace=90, positioning=90, tackling=90)
mf1_team4 = Midfielder(name="Xabi Alonso", height=180, weight=78, salary=10_300_000, contract_expiry_date="20/July/2022", stamina=90, transfer_fee=12_000_000, agression=75, creativity=95, pace=85, passing=95, shooting=90)
mf2_team4 = Midfielder(name="Sami Khedira", height=188, weight=85, salary=9_300_000, contract_expiry_date="20/July/2022", stamina=90, transfer_fee=13_000_000, agression=95, creativity=85, pace=85, passing=85, shooting=80)
mf3_team4 = Midfielder(name="Mesut Ozil", height=178, weight=75, salary=10_300_000, contract_expiry_date="20/July/2022", stamina=90, transfer_fee=11_000_000, agression=75, creativity=100, pace=85, passing=95, shooting=85)
mf4_team4 = Midfielder(name="Angel DiMaria", height=177, weight=72, salary=12_000_000, contract_expiry_date="20/July/2022", stamina=90, transfer_fee=10_000_000, agression=85, creativity=90, pace=95, passing=90, shooting=95)
fw1_team4 = Forward(name="Cristiano Ronaldo", height=186, weight=81, salary=14_800_00, contract_expiry_date="20/July/2022", stamina=100, transfer_fee=97_500_000, speed=100, technique=92, goalscoring=95, heading=95)
fw2_team4 = Forward(name="Karim Benzema", height=188, weight=81, salary=10_800_00, contract_expiry_date="20/July/2022", stamina=90, transfer_fee=18_500_000, speed=88, technique=92, goalscoring=90, heading=93)

real_madrid = BaseTeam(name="Real Madrid", city="Madrid", stadium="Santiago Bernabeu", stadium_capacity=78_000, chairman="Florentino Perez", finances=200_000_000, nationality="Spain")

players_slot_4 = [gk_team4, df1_team4, df2_team4, df3_team4, df4_team4, mf1_team4, mf2_team4, mf3_team4, mf4_team4, fw1_team4, fw2_team4]
for player in players_slot_4:
    real_madrid.add_player(player)

oliver_kahn = Goalkeeper(name="Oliver Kahn", height=193, weight=92, salary=6_000_000, contract_expiry_date="20/July/2022", stamina=100, transfer_fee=8_000_000, handling=95, jumping=100, reflexes=95)
gigi_buffon = Goalkeeper(name="Gianluigi Buffon", height=193, weight=88, salary=9_000_000, contract_expiry_date="20/July/2022", stamina=90, transfer_fee=12_000_000, handling=95, jumping=95, reflexes=100)
lucio = Defender(name="Lucio", height=190, weight=87, salary=7_800_000, contract_expiry_date="20/July/2022", stamina=95, transfer_fee=10_000_000, heading=90, pace=85, positioning=90, tackling=90)
virgil = Defender(name="Virgil Van Dyke", height=194, weight=87, salary=11_800_000, contract_expiry_date="20/July/2022", stamina=90, transfer_fee=10_000_000, heading=95, pace=90, positioning=95, tackling=90)
clarence_seedorf = Midfielder(name="Clarence Seedorf", height=178, weight=75, salary=10_000_000, contract_expiry_date="20/July/2022", stamina=98, transfer_fee=10_000_000, agression=90, creativity=94, pace=90, passing=94, shooting=90)
zinedine_zidane = Midfielder(name="Zinedine Zidane", height=183, weight=76, salary=12_000_000, contract_expiry_date="20/July/2022", stamina=84, transfer_fee=12_000_000, agression=94, creativity=100, pace=85, passing=96, shooting=95)
gabriel_batistuta = Forward(name="Gabriel Batistuta", height=188, weight=83, salary=10_800_00, contract_expiry_date="20/July/2022", stamina=90, transfer_fee=18_500_000, speed=83, technique=93, goalscoring=100, heading=97)
ronaldo = Forward(name="Ronaldo", height=183, weight=81, salary=13_800_00, contract_expiry_date="20/July/2022", stamina=90, transfer_fee=18_500_000, speed=97, technique=97, goalscoring=97, heading=80)

carlo_ancelotti = Coach(name="Carlo Ancelotti", nationality="italian", age=63, salary=7_000_000, experience=95, mentality="balanced", coaching_ability=95, formation="4-1-4-1")  # "4-5-1", "4-3-3"
sir_alex_ferguson = Coach(name="Alex Ferguson", nationality="scottish", age=80, salary=5_000_000, experience=100, mentality="attacking", coaching_ability=95, formation="4-4-2")  # "4-1-4-1", "4-3-3"
pep_guardiola = Coach(name="Josep Guardiola", nationality="spanish", age=50, salary=10_000_000, experience=75, mentality="attacking", coaching_ability=90, formation="4-3-3")  # "4-1-4-1", "4-2-4", "3-4-3"
jose_mourinho = Coach(name="Jose Mourinho", nationality="portuguese", age=60, salary=9_000_000, experience=85, mentality="defensive", coaching_ability=85, formation="4-1-4-1")  # "4-3-3", "4-5-1", "5-4-1", "5-3-2"

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

print(milan.calculate_team_strength())
print(barca.calculate_team_strength())
print(man_utd.calculate_team_strength())
print(real_madrid.calculate_team_strength())

print()
print(man_utd.show_squad())
print(milan.show_squad())
print(barca.show_squad())
print(real_madrid.show_squad())