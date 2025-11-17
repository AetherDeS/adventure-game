# main.py

from entities import *
from items import *
import random

def game_over(player):
    print("\nИгра закончена!")
    if not player.is_alive():
        print("Вы погибли...")
    else:
        print("Вы успешно завершили путешествие.")
    exit()

def encounter_enemy(player, enemy):
    while True:
        action = input(f"Вас атакует {enemy.name}. Что будете делать?\n[A] Атакуйте\n[F] Бежите\n").strip().lower()
        
        if action == 'a':
            player_damage = player.calculate_damage()
            print(f"\nВы атакуете {enemy.name}, наносите {player_damage} урона.")
            enemy.take_damage(player_damage)
            
            if not enemy.is_alive():
                print(f"Победили {enemy.name}. Продолжаете путь.\n")
                break
                
            enemy_damage = enemy.calculate_damage()
            print(f"{enemy.name} контратакует вас, наносит {enemy_damage} урона.")
            player.take_damage(enemy_damage)
            
            if not player.is_alive():
                game_over(player)
        elif action == 'f':
            print("Вы убегаете от боя.")
            break
        else:
            print("Неправильный ввод, попробуйте снова.")

def find_food(player, food_item):
    print(f"Вы нашли {food_item.name}. Хотите съесть?")
    choice = input("[Y] Да / [N] Нет: ").strip().lower()
    if choice == 'y':
        food_item.use(player)
    else:
        print("Вы решили оставить пищу.")

def campfire_event(player):
    print("Вы натолкнулись на костёр и можете отдохнуть тут, восстановив немного здоровья.")
    player.health += 10
    print(f"Здоровье теперь: {player.health}\nПродолжаем путь.")

def play_game():
    player = Player()
    events = [
        lambda p: encounter_enemy(p, Rat()),
        lambda p: encounter_enemy(p, Ent()),
        lambda p: find_food(p, berries),
        lambda p: find_food(p, apples),
        lambda p: find_food(p, poison_mushrooms),
        lambda p: campfire_event(p)
    ]
    
    print("""
Добро пожаловать в Темный Лес!
Цель вашего путешествия - пройти этот мрачный лес и выбраться наружу.
Будьте осторожны: впереди много опасностей...
""")
    
    step_count = 0
    while True:
        event = random.choice(events)
        event(player)
        step_count += 1
        
        print(f"\nШаг №{step_count}: Вы продолжаете идти дальше...\n")

if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        print("\nПутешествие прервано. До встречи!")