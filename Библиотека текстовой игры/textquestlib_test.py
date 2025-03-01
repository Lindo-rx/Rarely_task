# Импортируем библиотеку
from textquestlib import *

# Пример теста для библиотеки

# Создаем игрока и предметы
player = Player("John", 100, 1)
health_potion = Item("Health Potion", "health", 20)
damage_sword = Item("Damage Sword", "damage", 15)

# Добавляем предметы в инвентарь
player.add_item(health_potion)
player.add_item(damage_sword)

# Попытка использования предмета, которого нет в инвентаре
try:
    fake_item = Item("Fake Item", "health", 50)
    player.use_item(fake_item)
except ItemNotFoundError as e:
    print(f"Ошибка: {e}")

# Попытка использования предмета при недостаточном здоровье
try:
    player.health = 0
    player.use_item(health_potion)
except NotEnoughHealthError as e:
    print(f"Ошибка: {e}")

# Создание сцены и выбор действия
scene = Scene("Dungeon", "You're in a dark dungeon.", ["Fight", "Run"])
try:
    scene.choose_option("Rest")  # Неверный выбор
except InvalidOptionError as e:
    print(f"Ошибка: {e}")

# Сражение с врагом
enemy = Enemy("Goblin", 50, 10)
combat = CombatSystem(player, enemy)

# Проводим сражение
try:
    combat.start_battle()
except BattleError as e:
    print(f"Ошибка: {e}")

# Применяем улучшение здоровья
try:
    player.use_item(health_potion)  # Восстановление здоровья
    print(f"{player.name} теперь имеет {player.health} здоровья.")
except ItemNotFoundError as e:
    print(f"Ошибка: {e}")

# Создаем квест и сцены для него
quest = Quest(player, "Rescue the Princess")
scene1 = Scene("Dungeon", "You're in a dark dungeon.", ["Fight", "Run"])
scene2 = Scene("Castle", "You reached the castle.", ["Talk to the Princess", "Leave"])

quest.add_scene(scene1)
quest.add_scene(scene2)

# Начинаем квест
quest.start_game()

# Перемещаемся по сценам
try:
    quest.move_to_scene("Castle")  # Перемещение в замок
    quest.move_to_scene("NonExistentScene")  # Попытка перемещения в несуществующую сцену
except Exception as e:
    print(f"Ошибка при перемещении: {e}")
