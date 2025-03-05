# textquestlib.py

class ItemNotFoundError(Exception):
    """Неверно, попробуй ещё."""
    pass

class InvalidOptionError(Exception):
    """Неверно, попробуй ещё."""
    pass

class NotEnoughHealthError(Exception):
    """Неверно, попробуй ещё."""
    pass

class BattleError(Exception):
    """Неверно, попробуй ещё."""
    pass

# Создание игрока
class Player:
    def __init__(self, name, health, level, inventory):
        self.name = name
        self.health = health
        self.level = level
        self.inventory = inventory

    def add_item(self, item):
        if item not in self.inventory:
            self.inventory.append(item)
        else:
            print('Данный предмет у вас уже имеется.')

    def use_item(self, item):
        if item in self.inventory:
            item.apply_effect(item)
            self.inventory.remove(item)
        else:
            raise ItemNotFoundError("Предмет не найден!")

    def level_up(self):
        if self.level >= 0:
            self.level += 1
        else:
            print('Неправильные параметры!')


# Создание предмета
class Item:
    def __init__(self, name, item_type, effect):
        self.name = name
        self.item_type = item_type
        self.effect = effect


    def apply_effect(self, player):
        if self.item_type == 'health':
            if player.health > 0:
                self.effect += player.health
            else:
                raise NotEnoughHealthError("Недостаточно здоровья!")
        elif self.item_type == 'level_booster':
            self.effect += player.level
        elif self.item_type == 'name_changer':
            player.name = self.effect
        elif self.item_type == 'damage':
            if player.health > 0:
                player.health -= self.effect
            else:
                raise NotEnoughHealthError("Недостаточно здоровья!")


# Создание сцены
class Scene:
    def __init__(self, name, description, options):
        self.name = name
        self.description = description
        self.options = options

    def choose_option(self, option):
        for optional in self.options:
            if option in optional:
                return option
            else:
                raise InvalidOptionError("Неверная опция!")

class Enemy:
    def __init__(self, name, health, attack_damage):
        self.name = name
        self.health = health
        self.attack_damage = attack_damage

    def attack(self, player):
        if player.health > 0:
            player.health -= self.attack_damage
        else:
            raise BattleError("Ошибка в ходе сражения!")

class CombatSystem:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start_battle(self):
        if self.player.health > 0:
            print(f'Сражение {self.player.name} с {self.enemy.name} началось.')
        else:
            raise BattleError("Ошибка в ходе сражения!")
    def end_battle(self):
        print(f'Сражение {self.player.name} с {self.enemy.name} закончилось.')

class Quest:
    def __init__(self, player, quest_name, scenes, current_scene):
        self.player = player
        self.quest_name = quest_name
        self.scenes = scenes
        self.current_scene = current_scene

    def add_scene(self, scene):
        if scene not in self.scenes:
            self.scenes.append(scene)
        else:
            print('Данная ситуация уже есть.')

    def start_game(self):
        print('Игра началась.')

    def move_to_scene(self, scene_name):
        for scene in self.scenes:
            if scene == scene_name:
                scene_name.choose_option()
