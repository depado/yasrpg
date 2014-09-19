from pytmx import tmxloader
from pygame import surface, Rect

class TiledRenderer(object):
    """
    Simple way to render a tiled map
    """

    def __init__(self, filename):
        self.tiledmap = tmxloader.load_pygame(filename, pixelalpha=True)
        self.boxcollider = []
        self.alphacollider = []

    def terrain_render(self, surface):
        tw = self.tiledmap.tilewidth
        th = self.tiledmap.tileheight
        gt = self.tiledmap.get_tile_image

        for y in range(0, self.tiledmap.height):
            for x in range(0, self.tiledmap.width):
                tile = gt(x, y, 0)
                if tile: surface.blit(tile, (x*tw, y*th))

    def over_terrain_render(self, surface):
        tw = self.tiledmap.tilewidth
        th = self.tiledmap.tileheight
        gt = self.tiledmap.get_tile_image

        for y in range(0, self.tiledmap.height):
            for x in range(0, self.tiledmap.width):
                tile = gt(x, y, 1)
                if tile: surface.blit(tile, (x*tw, y*th))

    def under_char_render(self, surface):
        tw = self.tiledmap.tilewidth
        th = self.tiledmap.tileheight
        gt = self.tiledmap.get_tile_image

        for y in range(0, self.tiledmap.height):
            for x in range(0, self.tiledmap.width):
                tile = gt(x, y, 2)
                if tile: 
                    surface.blit(tile, (x*tw, y*th))
                    self.boxcollider.append(Rect(x*tw, y*th, tw, th))

    def over_char_render(self, surface):
        tw = self.tiledmap.tilewidth
        th = self.tiledmap.tileheight
        gt = self.tiledmap.get_tile_image

        for y in range(0, self.tiledmap.height):
            for x in range(0, self.tiledmap.width):
                tile = gt(x, y, 3)
                if tile: surface.blit(tile, (x*tw, y*th))
