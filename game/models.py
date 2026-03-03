from django.db import models

class Game(models.Model):
    #players
    player_white = models.CharField(max_length=100, default='white')
    player_black = models.CharField(max_length=100, default='black')
    #game state
    is_draw = models.BooleanField(default=False)
    winner = models.CharField(
        verbose_name='Winner',
        max_length=10,
        choices=[('white', 'White'), ('black', 'Black'), ('draw', 'Draw')],
        null=True,
        blank=True
    )

    board_state = models.CharField(max_length=300)

    #board stat in FEN notation
    def __str__(self):
        return f"Game {self.player_white} vs {self.player_black}"
    

class Move(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='moves')
    player = models.CharField(max_length=100, choices=[('white', 'White'), ('black', 'Black')])
    move = models.CharField(max_length=10)  # e.g., 'e4', 'Nf3'
    timestamp = models.DateTimeField(auto_now_add=True)
    from_square = models.CharField(max_length=2, null=True, blank=True)  # e.g., 'e2'
    to_square = models.CharField(max_length=2, null=True, blank=True)
    piece = models.CharField(max_length=10, null=True, blank=True) 
    
    def __str__(self):
        return f"{self.player} moved {self.move} in {self.game}"