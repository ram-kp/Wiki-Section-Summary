import json
if __name__ == '__main__' :

    str = "\nIn 1771, Franciscan friar Jun\u00edpero Serra founded the mission of San Gabriel Arc\u00e1ngel. In 1781, a group of 44 settlers known as \"Los Pobladores\" established El Pueblo de Nuestra Se\u00f1ora la Reina de los \u00c1ngeles, which is now known as Los Angeles. During Mexican rule, Governor P\u00edo Pico made Los Angeles the regional capital. In 1846, during the wider Mexican-American war, US marines occupied the pueblo, resulting in the siege of Los Angeles"
    data = [{
        'Summary':str.strip()
    }]
    print(data)
    with open("abc.json", 'w', encoding='utf-16') as f:
        json.dump(data, f, ensure_ascii=False)
