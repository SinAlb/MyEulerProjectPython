def KUniqueCharacters(strParam):
    k = int(strParam[0])
    strParam = list(strParam)
    strParam = strParam[1:]
    strParam1 = strParam
    maxuniqcollab = ""

    for item in strParam:
        uniqletters = item
        uniqcollab = item
        strParam1 = strParam1[1:]

        for item1 in strParam1:
            if len(uniqletters) <= k:
                if item1 in uniqletters:
                    uniqcollab += str(item1)
                else:
                    uniqletters += str(item1)

                    if len(uniqletters) <= k:
                        uniqcollab += str(item1)

        if len(uniqcollab) > len(maxuniqcollab):
            maxuniqcollab = uniqcollab

    return maxuniqcollab


# keep this function call here
print(KUniqueCharacters(input()))


def HTMLElements(strParam):
    tags = {
        "b": "1",
        "div": "2",
        "em": "3",
        "i": "4",
        "p": "5"
    }
    tags2 = {
        "1": "b",
        "2": "div",
        "3": "em",
        "4": "i",
        "5": "p"
    }
    strParam = list(strParam)
    inttags = ""
    for item in range(len(strParam)):
        if strParam[item] == "<" or strParam[item] == "/":
            strdiv = ''.join(strParam[(item + 1): (item + 4)])
            if "div" in strdiv:
                inttags += "2"
            else:
                for tag in tags:
                    if str(tag) in str(strParam[item: (item + 2)]):
                        inttags += str(tags[tag])
    inttags = list(inttags)
    result = True
    for item in inttags:
        if inttags.count(item) % 2 != 0:
            result = tags2[item]
            break
    return result


print(HTMLElements(input()))
