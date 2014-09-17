from pytmx import tmxloader
from pygame import surface, Rect

class TiledRenderer(object):
    """
    Super simple way to render a tiled map
    """

    def __init__(self, filename):
        self.tiledmap = tmxloader.load_pygame(filename, pixelalpha=True)
        self.boxcollider = []
        self.alphacolider = []

    def terrain_render(self, surface):
        tw = self.tiledmap.tilewidth
        th = self.tiledmap.tileheight
        gt = self.tiledmap.get_tile_image

        for l in range(0, 1):
            for y in range(0, self.tiledmap.height):
                for x in range(0, self.tiledmap.width):
                    tile = gt(x, y, l)
                    if tile: surface.blit(tile, (x*tw, y*th))

    def over_terrain_render(self, surface):
        tw = self.tiledmap.tilewidth
        th = self.tiledmap.tileheight
        gt = self.tiledmap.get_tile_image

        for l in range(1, 2):
            for y in range(0, self.tiledmap.height):
                for x in range(0, self.tiledmap.width):
                    tile = gt(x, y, l)
                    if tile: surface.blit(tile, (x*tw, y*th))

    def under_char_render(self, surface):
        tw = self.tiledmap.tilewidth
        th = self.tiledmap.tileheight
        gt = self.tiledmap.get_tile_image

        for l in range(2, 3):
            for y in range(0, self.tiledmap.height):
                for x in range(0, self.tiledmap.width):
                    tile = gt(x, y, l)
                    if tile: 
                        surface.blit(tile, (x*tw, y*th))
                        self.boxcollider.append(Rect(x*tw, y*th, tw, th))

    def over_char_render(self, surface):
        tw = self.tiledmap.tilewidth
        th = self.tiledmap.tileheight
        gt = self.tiledmap.get_tile_image

        for l in range(3, 4):
            for y in range(0, self.tiledmap.height):
                for x in range(0, self.tiledmap.width):
                    tile = gt(x, y, l)
                    if tile: surface.blit(tile, (x*tw, y*th))
