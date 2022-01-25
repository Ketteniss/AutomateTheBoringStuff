def commaCode(listValue):
    
    if not type(listValue) == list:
        return 0
    if len(listValue) == 0:
        print('')
        return ''
    resultString = str(listValue[0])
    for item in listValue[1:]:
        resultString = resultString + ', ' + str(item)
    resultString = resultString[:resultString.index(listValue[-1])] + 'and ' + resultString[resultString.index(listValue[-1]):]
    print(resultString)
    return resultString
    
commaCode(['apples', 'bananas', 'tofu', 'cats'])