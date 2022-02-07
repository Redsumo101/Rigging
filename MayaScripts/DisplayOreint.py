import maya.cmds as cmds
def display_joint_orient():
    sels = cmds.ls(sl=True)
    
    for sel in sels:
        if cmds.nodeType(sel) == 'joint':
            if cmds.getAttr('%s.displayLocalAxis' % sel):
                cmds.setAttr('%s.displayLocalAxis' % sel, 0)
                cmds.setAttr('%s.jointOrientX' % sel, keyable = False, channelBox = False)
                cmds.setAttr('%s.jointOrientY' % sel, keyable = False, channelBox = False)
                cmds.setAttr('%s.jointOrientZ' % sel, keyable = False, channelBox = False)
                
            else:
                cmds.setAttr('%s.displayLocalAxis' % sel, 1)
                cmds.setAttr('%s.jointOrientX' % sel, keyable = True)
                cmds.setAttr('%s.jointOrientY' % sel, keyable = True)
                cmds.setAttr('%s.jointOrientZ' % sel, keyable = True)
display_joint_orient()