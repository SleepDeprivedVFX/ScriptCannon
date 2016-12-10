''' Operator Check '''

class operatorCheck():
    def __init__(self):
        string = None
    def oCheck(self, ammo):
        wadding = False
        bullets = ['!', '$', '%', '^', '&', '*', '(', '-', '=', '+', '\\', '<', '>', '~', '! ', '$ ', '% ', '^ ', '& ', '* ', '( ', '- ', '= ', '+ ', '\\ ', '< ', '> ', '~ ', '|', '| ', '/', '/ ']
        for bullet in bullets:
            checkAmmo = ammo.endswith('%s' % bullet)
            if checkAmmo == True:
                wadding = True
        if wadding == True:
            return True
        else:
            return False


''' check for any kind of proper modifier / operator '''