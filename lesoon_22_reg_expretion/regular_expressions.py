import re


if __name__ == '__main__':

    result = re.search("a", "cat")
    print(type(result))
    print(result)
    print(re.search("b", "cat"))

    print(re.search("[af%#k]", "catk"))
    print(re.findall("[af%#k]", "catk"))

    print(re.search("[a-d]", "cat"))
    print(re.search("[abcd]", "cat"))
    print(re.search("abcd", "cat"))

    print(re.search("[1-9][A-Fa-f]", "9C"))
    print(re.search("[1-9][A-Fa-f]", "7465asfsh9Clajdfgh"))
    print(re.search("[1-9][A-F][a-f]", "9Cf"))
    print(re.search("[1-9][A-Fa-f1-9&%$#]", "9C"))
    print(re.search("[1-9] [@#$%] [a-z]!!!!!!!", "4 # f!!!!!!!"))  # 4 # f
    print(re.search("[1-9] [@#$%] [a-z]!!!!!!!", "gfhgjhjh sd 454 # f!!!!!!!fhfjgk"))
    print(re.search("cats (vs|with|against) dogs", "cats and dogs")) # cats vs dogs # cats with dogs
    print(re.search("cats (vs|with|against) dogs", "cats vs dogs"))

    # + * ?
    #מה שלפני הפלוס יכול להופיע אחד או יותר מפעם אחת
    print(re.search("[1-9]+", "rtey65748536trgfb"))
    print(re.search("[1-9]+", "rtey6trgfb"))
    print(re.search("[1-9]+", "rteytrgfb"))
    print(re.search("[1-9]+", "rt56ey65748536trgfb"))
    print(re.search("[cat]+", "ccctttaatcat"))
    print(re.search("(cat)+", "ccctttaatcat"))
    print(re.search("(cat)+", "ccccacatcattttt"))
    print(re.search("cat+", "catttttt"))
    print(re.search("ca+t+", "catttttt"))
    print(re.search("ca+t+", "caaaaaaatttttt"))
    # חיפוש של פלוס בתוך סטרינג עם סימון מיוחד של(\)לפני הפלוס(+)ס
    print(re.search("\+", "++++"))
    print(re.search("\++", "++++"))
    # מופע אופציונלי של אפס או יותר פעמים*
    # מופע של אפס או אחד פעמים
    print(re.search("(ca*t)", "ct"))
    print(re.search ("(ca)*t", "ct")) #ימצא רק את ה(t)
    # מה שלפני הסימן שאלה יכול להופיע אפס או אחד פעמים?
    print(re.search("ca?t", "cat"))
    print(re.search("ca?t", "ctsssjsj98778sh"))
    print(re.search("(dog|cat)( dog| cat)*", "dog cat dog cat cat dog"))
    # נקודה מסמל תו אחד והוא יכול לסמן את כל הסטרינג ולחפש בו את כל התווים גם תווים מיוחדים...
    print(re.search("[0-9].*[0-9]", "9sjshhd%^^-#?lskd4djdk9")) # ימצא עד הספרה 4 כולל כי הוא אמור להסתיים בספרות בין אפס לתשע
    print(re.search(".*[0-9]$", "dgffdhfhf8"))#תשים כמה תוים שתרצה מכל סוג שהם בגלל סימון הנקודה והכוכבית ושהמשפט יסתיים בספרה בטווח שרשמתי בסוגריים$
    print(re.search(".*[0-9]$", "dgffdhfhf8a"))
    # סימון של מה שאני רוצה שיתחיל הסטרינג^
    print(re.search("^[0-9].*", "7ssfjnjfbv"))#  שזה יתחיל בספרה כי הכובע מחוץ לסוגריים המרובעות
    print(re.search("^[03-9].*", "a7ssfjnjfbv"))
    print(re.search("[^0-9]", "%")) # מה שכתוב בתוך סוגריים מרובעות יהיה הכל חוץ מזה בזכות הכובע בתוך הסוגריים





    # print(re.search("0*[a-c]9+", "cat"))
    # print(re.search("0*[a-c]9+", "c"))
    # print(re.search("0*[a-c]9+", "0000c99999"))
    # print(re.search("0*[a-c]9+", "werwer0000c99999werwer"))



