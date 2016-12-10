from maya import cmds
import operatorCheck as oc
import findAttributes as fa
reload(oc)
reload(fa)

'''  Script Cannon  '''

'''
    This program will help you not only generate, but apply an expression to any number of objects simultaneously.
    It was designed to work similar to the Expression Editor, but with added functionality for large groups of objects,
    and additional tools for building scripts using a GUI.
        Still in production:

        Add built in functions, or function assembly tools, like:
            Sin wave built in patterns
            Linear patterns
            Transformation drop-downs and value fields

        Set up graphical interface for previewing animation curves.

        Fix formatting and insertion point errors, as well as scripts for adding variables and decision making strings.
            For example:
                float $testNumber;
                int $otherNumber;
                firstObject.ty = $otherNumber * sin($testNumer);
                if($testNumber > 0){
                    secondObject.ty = firstObject.ty;
                }

    Version 1.3
    Written by:
        Adam Benson
        AdamBenson.vfx@gmail.com

'''

'''  UI  '''

def ScriptCannonUI():

    if cmds.window('scriptCannonWindow', q=True, exists=True):
        cmds.deleteUI('scriptCannonWindow')
    cmds.window('scriptCannonWindow', t='Script Cannon v1.3', ret=True, rtf=True, bgc=(1.0,0.4,0.0), width=600, height=810)
    
    #setup scroll window
    cmds.scrollLayout('scrollSettings', width=600, height=810, vst=16)
    #set up main column
    cmds.rowColumnLayout(nc=1, rs=[1, 10])

    #Set up top two columns for the driver and targets and their respective attributes.
    cmds.rowColumnLayout('objectsCollection', nc=2, cs=[1,15], rs=[1,5])
    cmds.columnLayout()
    cmds.text('Script Name', align='right')
    blastCount = 1

    #check for other blast scripts in the scene
    firedCheck = False
    while firedCheck == False:
        try:
            checkShot = cmds.select('blastScript%i' % blastCount)
            print checkShot
            blastCount += 1
        except ValueError:
            firedCheck = True


    cmds.textField('scriptName', tx='blastScript%i' % blastCount, width=200)
    cmds.setParent('..')
    cmds.paneLayout()
    cmds.image(image='ScriptCannon_Logo_v01.png')
    cmds.setParent('..')


    #set up the target and attributes column
    cmds.rowColumnLayout('targetNames', nc=1)
    cmds.text('Script Targets', align='left')
    cmds.scrollField('targetList', nl=1, en=False, width=265, height=50)
    cmds.button('setTargets', c='setSelection("targets")', rs=True, bgc=[1.0, 0.75, 0.25], ann='When more than one object is selected, only attributes that all objects share will be listed.')
    #close target aquisition column
    cmds.setParent('..')

    #set up three columns for the driver selection box
    cmds.rowColumnLayout('driverName', numberOfColumns=1)
    cmds.text('Script Driver', align='left')
    cmds.textField('setDriver', width=260)
    cmds.button('setCurrent', c='setSelection("driver")', bgc=[1.0, 0.75, 0.25])
    #close the driver selection box columns in order to add separator
    cmds.setParent('..')
    #close top row columns
    cmds.setParent('..')

    #set up middle separator
    cmds.rowColumnLayout(nc=1)
    cmds.separator()
    #Close Separator
    cmds.setParent('..')

    #setup two columns for respective attributes
    cmds.rowColumnLayout('collectedAttributes', nc=2, cw=[1, 285])
    cmds.text('Target Attributes')
    cmds.text('Driver Attributes')
    #Dummy layout for making buttons deletable as a block
    cmds.rowColumnLayout('targetDummy', nc=1)

    '''  Here is where we will later create another dynamic layout - targetAttributes '''
    '''  Buttons will then go inside '''

    #close dummy layout
    cmds.setParent('..')


    #Dummy Layout for making buttons deletable as a block
    cmds.rowColumnLayout('driverDummy', nc=1)

    '''  Here is where we will later dynamically create another layout - driverAttributes '''
    '''  Within this will be placed buttons '''

    #close dummy layout.
    cmds.setParent('..')

    #close attributes collection
    cmds.setParent('..')

    cmds.text('Operators')
    #set up single fat block for all of the operator buttons
    cmds.rowColumnLayout('operators', nc=8)

    cmds.button('plus', l='+', rs=True, bgc=[1.0, 0.75, 0.25], width=70, height=20, c='operatorAction("+")')
    cmds.button('minus', l='-', rs=True, bgc=[1.0, 0.75, 0.25], width=70, height=20, c='operatorAction("-")')
    cmds.button('multiply', l='*', rs=True, bgc=[1.0, 0.75, 0.25], width=70, height=20, c='operatorAction("*")')
    cmds.button('divide', l='/', rs=True, bgc=[1.0, 0.75, 0.25], width=70, height=20, c='operatorAction("/")')

    cmds.button('lessThan', l='<', rs=True, bgc=[1.0, 0.75, 0.25], width=70, height=20, c='operatorAction("<")')
    cmds.button('greaterThan', l='>', rs=True, bgc=[1.0, 0.75, 0.25], width=70, height=20, c='operatorAction(">")')
    cmds.button('lessThanEqual', l='<=', rs=True, bgc=[1.0, 0.75, 0.25], width=70, height=20, c='operatorAction("<=")')
    cmds.button('greaterThanEqual', l='>=', rs=True, bgc=[1.0, 0.75, 0.25], width=70, height=20, c='operatorAction(">=")')

    cmds.button('e', l='e', rs=True, bgc=[1.0, 0.75, 0.25], width=70, height=20, c='operatorAction("2.71828182846")')
    cmds.button('pi', l='pi', rs=True, bgc=[1.0, 0.75, 0.25], width=70, height=20, c='operatorAction("3.14159265359")')
    cmds.button('theta', l='theta', rs=True, bgc=[1.0, 0.75, 0.25], width=70, height=20, c='operatorAction("6.28318530718")')
    cmds.button('equal', l='=', rs=True, bgc=[1.0, 0.75, 0.25], width=70, height=20, c='operatorAction("=")')

    cmds.button('sin', l='sin()', rs=True, bgc=[1.0, 0.75, 0.25], width=70, height=20, c='operatorAction("sin(")')
    cmds.button('cos', l='cos()', rs=True, bgc=[1.0, 0.75, 0.25], width=70, height=20, c='operatorAction("cos(")')
    cmds.button('tan', l='tan()', rs=True, bgc=[1.0, 0.75, 0.25], width=70, height=20, c='operatorAction("tan(")')
    cmds.button('x2', l='X^2', rs=True, bgc=[1.0, 0.75, 0.25], width=70, height=20, c='operatorAction("sqr(")')

    cmds.button('pow', l='X^y', rs=True, bgc=[1.0, 0.75, 0.25], width=70, height=20, c='operatorAction("**")')
    cmds.button('abs', l='abs()', rs=True, bgc=[1.0, 0.75, 0.25], width=70, height=20, c='operatorAction("abs(")')
    cmds.button('log', l='log()', rs=True, bgc=[1.0, 0.75, 0.25], width=70, height=20, c='operatorAction("log(")')
    cmds.button('ln', l='LN()', rs=True, bgc=[1.0, 0.75, 0.25], width=70, height=20, c='operatorAction("ln(")')

    cmds.button('not', l='NOT!', rs=True, bgc=[1.0, 0.75, 0.25], width=70, height=20, c='operatorAction("!")')
    cmds.button('and', l='AND', rs=True, bgc=[1.0, 0.75, 0.25], width=70, height=20, c='operatorAction("&&")')
    cmds.button('or', l='OR', rs=True, bgc=[1.0, 0.75, 0.25], width=70, height=20, c='operatorAction("||")')
    cmds.button('close', l=')', rs=True, bgc=[1.0, 0.75, 0.25], width=70, height=20, c='operatorAction(")")')

    #close operator block
    cmds.setParent('..')

    #setup modifiers
    cmds.rowColumnLayout('modifiers', nc=2)

    cmds.radioButtonGrp('velocity', l='Muzzle Velocity', labelArray2=['frame', 'time'], numberOfRadioButtons=2, select=2)
    cmds.button('addVelocity', l='Add', c='operatorAction("TIME")')
    cmds.radioButtonGrp('offsetRando', l='Cannon Offset   ', labelArray2=['incriment', 'random'], numberOfRadioButtons=2, select=1, cc='offsetChange()')
    #this camera offset, $sCannonOffset, gets it's assigned value when the script is run.  The variable is for the MEL side. 
    #This needs to be adjusted for the new system of building scripts.
    cmds.textFieldButtonGrp('addOffset', bl='Add', bc='operatorAction("$sCannonOffset")', tx=1, cw=[1, 25])

    #close modifiers
    cmds.setParent('..')

    #Set up prebuilt functions
    cmds.rowColumnLayout('preloadedAmmo', nc=5, cw=[1,140])
    
    cmds.iconTextRadioCollection('preloadedAmmoCollection')
    cmds.text('Preloaded Ammo')
    cmds.iconTextRadioButton(st='iconOnly', i1='wave.png', l='wave', bgc=[1.0, 0.75, 0.25])
    cmds.iconTextRadioButton(st='iconOnly', i1='triangle.png', l='triangle', bgc=[1.0, 0.75, 0.25])
    cmds.iconTextRadioButton(st='iconOnly', i1='sawtooth.png', l='sawtooth', bgc=[1.0, 0.75, 0.25])
    cmds.iconTextRadioButton(st='iconOnly', i1='clear.png', l='clear', bgc=[1.0, 0.75, 0.25])


    #close prebuilt functions
    cmds.setParent('..')

    cmds.button('reset', l='Reload Cannon', c='reloadCannon()', bgc=[1.0, 0.75, 0.25])

    #setup script block
    cmds.rowColumnLayout('scriptExpressions', nc=1)
    cmds.text('Script Ammo', align='left')
    cmds.scrollField('cannonAmmo', nl=1, width=575, height=100, cc='checkAmmo()', ec='checkAmmo()', kpc='checkAmmo()', ip=0)
    #close script Block
    cmds.setParent("..")

    #set up script graph
    cmds.frameLayout(l='Script Trajectory', height=150, width=450)
    if cmds.animCurveEditor('showAnimCurve', ex=True):
        cmds.deleteUI('showAnimCurve')
    cmds.animCurveEditor('showAnimCurve', sr='on', sb=True, ru='interactive', dtg='Expression Curve')
    #close script graph
    cmds.setParent('..')

    #set up button bars
    cmds.rowColumnLayout(nc=2, width=500, cs=[2, 100], cal=[2, 'center'])
    cmds.button('Preview', l='Preview Graph', rs=True, bgc=[1.0, 0.75, 0.25], width=200, height=50)
    cmds.button('Fire', l='Fire!', rs=True, bgc=[1.0, 0.75, 0.25], width=200, height=50, c='fireCannon()')
    #close button bars
    cmds.setParent('..')

    #close main column
    cmds.setParent('..')

    cmds.showWindow('scriptCannonWindow')


'''  Select the Driver Object '''

'''  Check line ends -  Check Ammo '''
'''  Currently, this def doesn't do anything.  It's intention is to check for end of line ; statements. '''

def checkAmmo():
    ammo = cmds.scrollField('cannonAmmo', q=True, tx=True)
    clipLoad = ammo.endswith('\n')
    bulletTest = ammo.endswith(';\n')
    if clipLoad == True and bulletTest == False:
        print ammo, clipLoad # This should be a replacement string

'''  End check lines ends '''

'''  Reload Cannon '''
'''  Resets the script cannon '''

def reloadCannon():
    cmds.scrollField('cannonAmmo', e=True, tx="")
    cmds.scrollField('targetList', e=True, tx='')
    cmds.textField('setDriver', e=True, tx='')
    if cmds.rowColumnLayout('targetAttributes', ex=True):
        cmds.deleteUI('targetAttributes')
    if cmds.rowColumnLayout('driverAttributes', ex=True):
        cmds.deleteUI('driverAttributes')
    blastCount = 1
    #check for other blastScripts in the scene
    firedCheck = False
    while firedCheck == False:
        try:
            checkShot = cmds.select('blastScript%i' % blastCount)
            blastCount += 1
        except ValueError:
            firedCheck = True
    cmds.textField('scriptName', e=True, tx='blastScript%i' % blastCount)

'''  End reload '''

''' Operator Action '''
'''  This def is designed to take code snippets from the function buttons, and apply them to the script ammo.  It needs to go in line with future organizations  '''

def operatorAction(oper):
    ammo = cmds.scrollField('cannonAmmo', q=True, tx=True)
    if oper != "TIME":
        newAmmo = '%s %s' % (ammo, oper)
    else:
        velocity = cmds.radioButtonGrp('velocity', q=True, select=True)
        if velocity == 1:
            muzzleVelocity = 'frame'
        else:
            muzzleVelocity = 'time'
        newAmmo = '%s %s' % (ammo, muzzleVelocity)
    cmds.scrollField('cannonAmmo', e=True, tx=newAmmo)

''' End Operator Action '''

'''  The next two functions work together '''
'''  The first one decides which kind of selection is being added, either Driver or Target objects
 The next one, setAttributes, creates the attributes button'''
def setSelection(set):
    selected = cmds.ls(sl=True)
    #set is the choice of either driver or target.  Type gets set to one of these.
    type = set
    listSelected = ""
    if type == 'driver':
        if len(selected) > 1:
            cmds.confirmDialog(m='You can only have one Driver Object')
        elif len(selected) < 1:
            cmds.confirmDialog(m='You must select at least one Driver Object')
        else:
            cmds.textField('setDriver', e=True, tx='%s' % selected[0])
            setAttributes(type, selected)
    else:
        if len(selected) < 1:
            cmds.confirmDialog(m='You must select at least one target Object')
        else:
            for thisObject in selected:
                if listSelected != "":
                    listSelected = "%s\n%s" % (listSelected, thisObject)
                else:
                    listSelected = thisObject
            cmds.scrollField('targetList', e=True, tx=listSelected)
            setAttributes(type, selected)

def setAttributes(type, objs):
    #Again, this is either driver or targets
    attributeCollection = type
    selected = objs
    #this currently takes the attributes from the first object selected.  This needs to be a collection of the minimum attributes of all objects.
    # Might want to send this to another class, like attributeCollection or something like that.  Wouldn't be needed for Driver object.
    if attributeCollection == 'driver':
        getAttributes = cmds.listAttr(selected[0], k=True)
    else:
        collectAttributes = fa.findAttributes()
        getAttributes = collectAttributes.getMinimumAttributes(selected)
    if attributeCollection == 'driver':
        if cmds.rowColumnLayout('driverAttributes', ex=True):
            cmds.deleteUI('driverAttributes')
        cmds.setParent('driverDummy')
        cmds.rowColumnLayout('driverAttributes', nc=3)
        ui = 'd'
    else:
        if cmds.rowColumnLayout('targetAttributes', ex=True):
            cmds.deleteUI('targetAttributes')
        cmds.setParent('targetDummy')
        cmds.rowColumnLayout('targetAttributes', nc=3)
        ui = 't'
    for thisAttribute in getAttributes:
        cmds.button('%s_%s' % (ui, thisAttribute), l='%s' % thisAttribute, bgc=[1.0, 0.75, 0.25], c='buttonActions("%s", "%s")' % (ui, thisAttribute))
        if thisAttribute == 'visibility':
            cmds.text(" ")
            cmds.text(" ")
    cmds.setParent('..')
    selected = None

'''  End Tie together '''

''' start button actions '''
#buttonActions is where the script is built.  This needs to be much more robust.  Needs better script control.
#Needs to get cursor location
#Needs to read each line and look for ';' at the ends
#Needs to recognize the difference between variables and scripts.
#Might need to check for selected text within the scroll Box.  This would be, for instance, to wrap sin() function around a specific text
def buttonActions(dt, type):
    ammo = cmds.scrollField('cannonAmmo', q=True, tx=True)
    driver = cmds.textField('setDriver', q=True, tx=True)
    newAmmo = ""
    if dt == 'd':
        if ammo == "":
            newAmmo = '%s.%s' % (driver, type)
        else:
            #check for a proper mathematical operator between statements.
            #this should also be checking for current cursor location.
            opCheck = oc.operatorCheck()
            checkAmmo = opCheck.oCheck(ammo)
            if checkAmmo == False:
                cmds.confirmDialog(m='Proper scripts must contain valid operators.\nPlese revise your function to be mathematically accurate.')
                newAmmo = ammo
            else:
                #This MIGHT need to be broken into three elements.  Variables, targets and drivers.  Targets are easy though.  Drivers will be the hard part.
                newAmmo = '%s %s.%s' % (ammo, driver, type)
    elif dt=='t':
        if ammo == "":
            newAmmo = '%s = ' % type
        else:
            newAmmo = '%s = %s' % (type, ammo)
    cmds.scrollField('cannonAmmo', e=True, tx=newAmmo)

''' End button Actions '''

'''  Change offset / Randomization '''
#This just changes the value of the randomizer/index field
def offsetChange():
    offsetType = cmds.radioButtonGrp('offsetRando', q=True, select=True)
    if offsetType == 1:
        cmds.textFieldButtonGrp('addOffset', e=True, tx=1)
    else:
        cmds.textFieldButtonGrp('addOffset', e=True, tx=5)


''' End Change Offset / rando '''


''' fire cannon '''

def fireCannon():
    targets = cmds.scrollField('targetList', q=True, tx=True)
    targetList = targets.splitlines()
    ammo = cmds.scrollField('cannonAmmo', q=True, tx=True)
    driver = cmds.textField('setDriver', q=True, tx=True)
    scriptName = cmds.textField('scriptName', q=True, tx=True)
    #These next three statements might need to be moved to ButtonActions.
    #Because, I want to include variables in the script field, and these would be doing just that.
    getOffsetType = cmds.radioButtonGrp('offsetRando', q=True, select=True)
    getOffsetValue = float(cmds.textFieldButtonGrp('addOffset', q=True, tx=True))
    checkOffset = ammo.find('$sCannonOffset')
    for target in targetList:
        if checkOffset > 0:
            checkEnd = ammo.endswith(';')
            checkEndSpace = ammo.endswith('; ')
            if checkEnd > 0 or checkEndSpace > 0:
                addEnd = ''
            else:
                addEnd = ';'
            if getOffsetType == 1:
                newAmmo = 'float $sCannonOffset = %f; %s %s' % (getOffsetValue, ammo, addEnd)
                getOffsetValue += getOffsetValue
            else:
                newAmmo = 'float $sCannonOffset = rand(0, %f); %s %s' % (getOffsetValue, ammo, addEnd)
        else:
            newAmmo=ammo
        cmds.expression(s=newAmmo, o=target, ae=1, uc='all', n=scriptName)
        blastCount = 1
        firedCheck = False
        while firedCheck == False:
            try:
                checkShot = cmds.select('blastScript%i' % blastCount)
                blastCount += 1
            except ValueError:
                firedCheck = True
        cmds.textField('scriptName', e=True, tx='blastScript%i' % blastCount)

''' end fire cannon '''

ScriptCannonUI()