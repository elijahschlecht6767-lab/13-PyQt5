class LeetSpeaker:
    leet_table={
            "A":("4", "@"),
            "B":("8", "|3"),
            "C":("(", "<"),
            "D":("|)", "[)"),
            "E":("3", "€"),
            "F":("|=", "ph"),
            "G":("6", "9"),
            "H":("|-|", "#"),
            "I":("1", "!"),
            "J":("_|", "_/"),
            "K":("|<", "|{"),
            "L":("1", "|_"),
            "M":("//\\", "|/|"),
            "N":("||", "//"),
            "O":("0", "()"),
            "P":("|*", "|o"),
            "Q":("0_", "(,)"),
            "R":("|2", "12"),
            "S":("5", "$"),
            "T":("7", "+"),
            "U":("|_|", "(_)"),
            "V":("/", "|"),
            "W":("//", "vv"),
            "X":("><", "}{"),
            "Y":("`/", "j"),
            "Z":("2", "7_")
    }


    @staticmethod
    def translate(text:str, index:int):
        if index==1:
            pass
        elif index==0:
            pass
        elif index!=0 and index!=1 and index>1 and (index%2)==0:
            index=0
        elif index<0:
            raise ValueError("integer required for leet conversion")
        else:
            index=1
        
        #text=text.strip().upper()
        bypass=[]
        for i in range(len(text)):
            if text[i] in LeetSpeaker.leet_table:
                bypass.append(LeetSpeaker.leet_table[text[i]][index])
            else:
                bypass.append(text[i])
        
        new_string=""
        for i in range(len(bypass)):
            new_string+=bypass[i]
        
        print(new_string)


def main():
    while True:
        #try:
        string=str(input("Enter raw/ unchanged text: ")).strip().upper()
        integer=int(input("Enter either 0 or 1 (bypass method): "))
        print(LeetSpeaker.translate(string, integer))
        break
        #except:
            #print("Please try again, ensure that only numbers are used for the bypass method")
    print("bypassed message printed successfully")


if __name__=="__main__":
    main()
