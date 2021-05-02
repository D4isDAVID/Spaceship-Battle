from pygame.time import Clock
from entity.player import PlayerEntity
from entity.bullet import BulletEntity


class Lobby:
    PLAYER_MAX = 16
    MAX_PLAYERS = 8

    def __init__(self):
        self.entity_count = 0
        self.entities = {}
    
    def update(self):
        ids = []
        for eid, entity in self.entities.items():
            entity.update()
            if isinstance(entity, BulletEntity):
                for oid, other in self.entities.items():
                    if entity != other:
                        d = entity.get_distance(other)
                        if d != -1:
                            if d < entity.radius+other.radius:
                                if eid not in ids:
                                    ids.append(eid)
                                if isinstance(other, PlayerEntity):
                                    if other.alive == True:
                                        other.alive = False
                                        other.score -= 1
                                        entity.entity.score += 1
                                elif isinstance(other, BulletEntity):
                                    if oid not in ids:
                                        ids.append(oid)
                if entity.is_out_of_bounds():
                    if eid not in ids:
                        ids.append(eid)
        if ids:
            for eid in ids:
                self.entities.pop(eid)

    def main(self):
        clock = Clock()
        print('Lobby Running')

        while True:
            clock.tick(144)
            self.update()
