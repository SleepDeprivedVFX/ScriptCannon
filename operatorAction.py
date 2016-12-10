from maya import cmds as oa

''' Operator Action '''

class operatorAction:
    def operatorAction(oper):
        ammo = oa.scrollField('cannonAmmo', q=True, tx=True)
        if oper != "TIME":
            newAmmo = '%s %s' % (ammo, oper)
        else:
            velocity = oa.radioButtonGrp('velocity', q=True, select=True)
            if velocity == 1:
                muzzleVelocity = 'frame'
            else:
                muzzleVelocity = 'time'
            newAmmo = '%s %s' % (ammo, muzzleVelocity)
        oa.scrollField('cannonAmmo', e=True, tx=newAmmo)

''' End Operator Action '''