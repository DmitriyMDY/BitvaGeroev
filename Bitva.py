import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = self.attack_power
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона.")
        print(f"У {other.name} осталось {other.health} здоровья.\n")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        print("Начало игры 'Битва героев'!\n")
        while self.player.is_alive() and self.computer.is_alive():
            self.player_turn()
            if not self.computer.is_alive():
                print(f"{self.player.name} победил!")
                break
            self.computer_turn()
            if not self.player.is_alive():
                print(f"{self.computer.name} победил!")
                break

    def player_turn(self):
        self.player.attack(self.computer)

    def computer_turn(self):
        self.computer.attack(self.player)

# Пример использования
if __name__ == "__main__":
    player_hero = Hero(name="Игрок")
    computer_hero = Hero(name="Компьютер")
    game = Game(player=player_hero, computer=computer_hero)
    game.start()
