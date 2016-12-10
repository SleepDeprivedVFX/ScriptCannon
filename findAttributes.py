from maya import cmds as fat

''' This class will find the minimum number of attributes that all objects share '''
class findAttributes:
    def __init__(self):
        selected = 'none'

    def getMinimumAttributes(self, sel):
        selected = sel
        attributesList = []
        for thisObject in selected:
            objAttributes = fat.listAttr(thisObject, k=True)
            if len(attributesList) == 0:
                attributesList = objAttributes
            else:
                currentLength = len(attributesList)
                nextLength = len(objAttributes)
                if currentLength != nextLength:
                    if currentLength > nextLength:
                        #Then I'd have to remove an attribute from the collection
                        #This would have to remove the attribute from the current list
                        for thisAttr in attributesList:
                            try:
                                inNextList = objAttributes.index(thisAttr)
                            except ValueError:
                                attributesList.remove(thisAttr)
                    elif currentLength < nextLength:
                        #Also have to remove an attribute from the collection.
                        #this would have to simply not add the attribute from the next list.  In any case both lists need comparison.
                        for thisAttr in objAttributes:
                            try:
                                isListed = attributesList.index(thisAttr)
                            except ValueError:
                                objAttributes.remove(thisAttr)
        return attributesList
