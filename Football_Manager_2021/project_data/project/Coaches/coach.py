class Coach:

    salary_restrictions = range(1_000_000, 10_000_000 + 1)
    age_restriction = range(30, 80 + 1)
    experience_restriction = range(1, 100 + 1)
    mentality_available = ["attacking", "defensive", "counter_attack", "balanced"]
    coaching_ability_restrictions = range(1, 100 + 1)
    formations_available = ["3-4-3", "3-5-2", "3-3-4", "4-4-2", "4-1-4-1", "4-3-3", "4-5-1", "4-2-4", "5-4-1", "5-3-2", "5-2-3"]

    def __init__(self, name: str, nationality: str, age: int, salary: int, experience: int, mentality: str, coaching_ability: int, formation: str):
        self.name = name
        self.nationality = nationality
        self.age = age
        self.salary = salary
        self.experience = experience
        self.mentality = mentality
        self.coaching_ability = coaching_ability
        self.formation = formation
        self.occupied = False
        self.team = None
        self.coach_strength = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Coach name cannot be blank")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value not in Coach.age_restriction:
            raise ValueError(f"Coach age can be between {Coach.age_restriction}")
        self.__age = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value not in Coach.salary_restrictions:
            raise ValueError(f"Coach salary should be between {Coach.salary_restrictions}")
        self.__salary = value

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, value):
        if value not in Coach.experience_restriction:
            raise ValueError(f"Coach experience should be between {Coach.experience_restriction}")
        self.__experience = value

    @property
    def mentality(self):
        return self.__mentality

    @mentality.setter
    def mentality(self, value):
        if value not in Coach.mentality_available:
            raise ValueError(f"Mentality should be from {', '.join(Coach.mentality_available)}")
        self.__mentality = value

    @property
    def coaching_ability(self):
        return self.__coaching_ability

    @coaching_ability.setter
    def coaching_ability(self, value):
        if value not in Coach.coaching_ability_restrictions:
            raise ValueError(f"Coaching ability should be between {Coach.coaching_ability_restrictions}")
        self.__coaching_ability = value

    @property
    def formation(self):
        return self.__formation

    @formation.setter
    def formation(self, value):
        if value not in Coach.formations_available:
            raise ValueError(f"Formations should be chosen from {Coach.formations_available}")
        self.__formation = value

    @property
    def calculate_coach_strength(self):
        coach_strength = self.experience + self.coaching_ability
        if self.mentality == "attacking" and self.formation in ["4-3-3", "3-4-3", "3-3-4", "4-2-4"]:
            coach_strength += 8
        elif self.mentality == "defensive" and self.formation in ["4-5-1", "5-4-1", "5-3-2"]:
            coach_strength += 7
        elif self.mentality == "counter-attack" and self.formation in ["4-1-4-1",  "5-4-1", "5-3-2"]:
            coach_strength += 6
        elif self.mentality == "balanced" and self.formation in ["4-4-2", "5-3-2", "5-2-3", "4-5-1"]:
            coach_strength += 9
        else:
            coach_strength += 4
        return coach_strength

    @property
    def coach_strength_message(self):
        coach_strength = self.calculate_coach_strength
        return f"{self.name} has coach strength {coach_strength}"
