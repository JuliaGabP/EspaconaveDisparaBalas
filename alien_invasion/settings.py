class Settings:
    """Classe para armazenar as configurações do Jogo Invasão Alienígena"""
    def __init__(self):
        """Inicializa as configurações do jogo"""
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
		
        # Configurações da espaçonave
        self.ship_speed = 1.5
        self.ship_limit = 3
        
        # Configurações do projétil
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        # Configurações do alienígena
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        
        # A rapidez com que o jogo acelera
        self.speedup_scale = 1.1
        
        # Com que rapidez os valores dos pontos alienígenas aumentam
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Inicializa as configurações que mudam ao longo do jogo"""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0
        self.fleet_direction = 1
        self.alien_points = 50
	    
    def increase_speed(self):
        """Aumenta as configurações de velocidade e valores dos pontos alienígenas"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
	    
    def set_difficulty(self, level):
        """Define os parâmetros iniciais de acordo com o nível de dificuldade"""
        if level == "easy":
            self.ship_speed = 1.5
            self.bullet_speed = 2.5
            self.alien_speed = 0.8
            self.speedup_scale = 1.05
        
        elif level == "medium":
            self.ship_speed = 1.8
            self.bullet_speed = 3.0
            self.alien_speed = 1.2
            self.speedup_scale = 1.1
    
        elif level == "hard":
            self.ship_speed = 2.2
            self.bullet_speed = 3.5
            self.alien_speed = 1.6
            self.speedup_scale = 1.15
    
        self.fleet_direction = 1
