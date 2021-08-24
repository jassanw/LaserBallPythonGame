"""
 This example shows having multiple balls bouncing around the screen at the
 same time. You can hit the space bar to spawn more balls.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
""" 
class A:
    def __init__(self):
        self.OnDeath  = None

    def OnHit(self):
        self.OnDeath()
class B(A):

  
    def __init__(self):
        super().__init__()
        def OnDeath():
            print("BigBallDied")
        self.OnDeath = OnDeath
   



 
def main():
    asdf = B()
    asdf.OnHit()

main()