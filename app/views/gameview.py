from app.views.view import View

class GameView(View):
  def render(self):
    self.graphics.fill((0,0,0))
    y = 0
    x = 0
    offset = 0
    level = self.model
    for byte in level.data:
      if byte == level.WALL:
        self.graphics.draw_rect(x, y, 15, 15, (128,128,128))
      elif byte == level.FIELD:
        self.graphics.draw_rect(x, y, 15, 15, (128,255,128))
      elif byte == level.HEAD:
        self.graphics.draw_rect(x, y, 15, 15, (0,128,0))
      elif byte == level.TAIL:
        self.graphics.draw_rect(x, y, 15, 15, (0,156,0))
      elif byte == level.APPLE:
        self.graphics.draw_rect(x, y, 15, 15, (255,64,0))

      x += 16
      offset += 1
      if offset == level.line_length:
        offset = 0
        x = 0
        y += 16
