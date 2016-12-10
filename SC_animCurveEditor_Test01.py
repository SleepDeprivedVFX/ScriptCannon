from maya import cmds

#This was a test to get the animCurveEditor to work.
#BE CAREFUL!  In it's current state this script will FREEZE UP MAYA!!!
#It only takes a minor modification in 'thisSelection' to fix it, but I'm too lazy right now.

def testWindow():
    try:
        cmds.select('testScript', r=True)
        cmds.delete('testScript')
    except ValueError:
        pass
    testScriptNode = cmds.expression(n='testScript', s='sin(time)')
    if cmds.window('testWindow', ex=True):
        cmds.deleteUI('testWindow')
    cmds.window('testWindow')
    cmds.frameLayout('mainFrame', l='AnimationGraph')
    if cmds.selectionConnection('thisConnection', ex=True):
        cmds.deleteUI('thisConnection')
    animCurveFrame = cmds.animCurveEditor(sr='on')
    if cmds.selectionConnection('testScript', ex=True):
        cmds.deleteUI('testScript')
    thisSelection = cmds.selectionConnection('testScript', obj='pSphere1')
    cmds.editor(animCurveFrame, e=True, mainListConnection=thisSelection)
    cmds.showWindow('testWindow')

testWindow()