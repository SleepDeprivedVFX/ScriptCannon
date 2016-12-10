from maya import cmds as rc
'''  Reload Cannon '''

class reloadCannon:
    def reloadCannon():
        rc.scrollField('cannonAmmo', e=True, tx='')
        rc.scrollField('targetList', e=True, tx='')
        rc.textField('setDriver', e=True, tx='')
        if rc.rowColumnLayout('targetAttributes', ex=True):
            rc.deleteUI('targetAttributes')
        if rc.rowColumnLayout('driverAttributes', ex=True):
            rc.deleteUI('driverAttributes')
        blastCount = 1
        firedCheck = False
        while firedCheck == False:
            try:
                checkShot = rc.select('blastScript%i' % blastCount)
                blastCount += 1
            except ValueError:
                firedCheck = True
        rc.textField('scriptName', e=True, tx='blastScript%i' % blastCount)

'''  End reload '''