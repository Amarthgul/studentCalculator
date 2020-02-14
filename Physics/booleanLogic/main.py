
class clause():
    def __init__(self):
        self.__variableOne = None;
        self.__variableTwo = None;
        self.__variableOneNeg = False; 
        self.__variableTwoNeg = False;
        self.__operator = None;
        self.value = [self.__variableOneNeg, self.__variableOne, 
                      self.__operator, 
                      self.__variableTwoNeg, self.__variableTwo];
        self.truth = True;

    def setOperator(self, ope):
        self.__operator = ope;

    def setVOne(self, vOne):
        self.__variableOne = vOne;

    def setVTwo(self, vTwo):
        self.__variableTwo = vTwo;

    def setVOneNeg(self, negate):
        assert negate == True or False, "Negation can either be true or false";
        self.__variableOneNeg = negate;

    def setVTwoNeg(self, negate):
        assert negate == True or False, "Negation can either be true or false";
        self.__variableTwoNeg = negate;



class proposition():
    def __init__(self, inputStr = '(Q and R) or P'):
        # you can add rules into these notation sets to better suit your source
        self.__specialCharacterSet = '''¬∧∨⟹⇒⟺⇔'''; #useless
        self.__primeNotations = ["'", "`"];
        self.__notNotations = ['¬', '~', '!', 'not'];
        self.__andNotations = ['∧', '&', '&&', 'and'];
        self.__orNotations = ['∨', '|', '+',  '||', 'or'];
        self.__thenNotations = ['⟹', '⇒', '=>', '->', '==>', '-->', 'then'];
        self.__eqvltNotations = ['⟺', '⇔', '=', '=='];
        self.__rawProposition = inputStr;
        self.__spiltedProposition = [];
        self.__value = clause();
        self.__listOfVariables = [];

    #================================================================
    @property
    def __notationSet(self):
        notationSet = []
        for set in [self.__notNotations, self.__andNotations, self.__orNotations,
                    self.__thenNotations, self.__eqvltNotations]:
            notationSet.extend(set);
        return notationSet;

    def clear(self):
        self.__value = clause();
        self.__rawProposition = '';
        self.__listOfVariables = [];
        self.__spiltedProposition = [];

    def setProposition(self, inputStr):
        '''inputStr: the proposition to be analysed'''
        assert len(inputStr), "Fucking retarded, it's empty!"
        self.__rawProposition = inputStr;

    def getProposition(self):
        return self.__rawProposition;

    def getListOfVariables(self):
        return self.__listOfVariables;

    def getDevOptions(self):
        '''Options for developers to inspect result without using debugger since python debugging is shitty'''
        result = [];
        result.append(self.__spiltedProposition);
        result.append(self.__listOfVariables);
        return result;

    #================================================================
    def __regulating(self):

        # fixing self.__listOfVariables
        self.__listOfVariables = list(set(self.__listOfVariables));

        # fixing self.__spiltedProposition
        newProList = [];
        preIsVar = False;
        preVar = None;

        for i in range(len(self.__spiltedProposition)):
            current = self.__spiltedProposition[i];
            # is a variable 
            if (current in self.__listOfVariables):
                if (newProList[-1] == ')'):
                    newProList.append('and');
                if (preIsVar):
                    newProList.append('and');
                preIsVar = True;
                preVar = current;
                newProList.append(current);
            # is a prime notation
            elif (current == 'prime'):
                print('got prime')
                if (i > 0 and preIsVar):
                    newProList[-1:] = ['not'];
                    newProList.append(preVar);
                    preIsVar = True;
            else:
                newProList.append(current)
                preIsVar = False;

        self.__spiltedProposition = newProList

    def spiltProposition(self):
        assert len(self.__rawProposition), "Nothing to analyse."

        text = self.__rawProposition;

        while (len(text)):
            print(len(text))
            # length 4 character
            if (len(text) >= 4):
                current = text[0 : 4]
                if (current == 'then'):
                    self.__spiltedProposition.append('then')
                    text = text[4:];
            # length 3 character
            if (len(text) >= 3):
                current = text[0 : 3]
                if (current in ['==>', '-->']):
                    self.__spiltedProposition.append('then')
                    text = text[3:];
                elif (current == 'not'):
                    self.__spiltedProposition.append('not')
                    text = text[3:];
                elif (current == 'and'):
                    self.__spiltedProposition.append('and')
                    text = text[3:];
            # length 2 character
            if (len(text) >= 2):
                current = text[0 : 2]
                if (current == '||'):
                    self.__spiltedProposition.append('or')
                    text = text[2:];
                elif (current == '&&'):
                    self.__spiltedProposition.append('and')
                    text = text[2:];
                elif (current in ['->', '=>']):
                    self.__spiltedProposition.append('then')
                    text = text[2:];
                elif (current == '=='):
                    self.__spiltedProposition.append('equals')
                    text = text[2:];
            # length 1 character
            if(len(text)):
                if (text[0] in self.__notNotations):
                    self.__spiltedProposition.append('not')
                    text = text[1:];
                elif (text[0] in self.__andNotations):
                    self.__spiltedProposition.append('and')
                    text = text[1:];
                elif (text[0] in self.__orNotations):
                    self.__spiltedProposition.append('or')
                    text = text[1:];
                elif (text[0] in self.__thenNotations):
                    self.__spiltedProposition.append('then')
                    text = text[1:];
                elif (text[0] in self.__eqvltNotations):
                    self.__spiltedProposition.append('equals')
                    text = text[1:];
                elif (text[0] in self.__primeNotations):
                    self.__spiltedProposition.append('prime')
                    text = text[1:];
                elif (text[0] == ' '):
                    text = text[1:];
                elif (text[0] in '([{'):
                    self.__spiltedProposition.append('(')
                    text = text[1:];
                elif (text[0] in ')]}'):
                    self.__spiltedProposition.append(')')
                    text = text[1:];
                else:
                    self.__spiltedProposition.append(text[0].upper())
                    self.__listOfVariables.append(text[0].upper());
                    text = text[1:];

        self.__regulating();

    #================================================================
    def parse(self):
        assert len(__spiltedProposition), "Need something to work with. Try call spiltProposition() first"
        
        newClause = clause();

        return newClause;

    #================================================================
    def getResult(self):
        
        self.spiltProposition();
        #self.__value = self.parse();



def truthTable():
    tt = proposition("(A'B + C)A");
    tt.getResult();
    print(tt.getDevOptions())


#================================================================
'''==========================================================='''
def main():
    truthTable();

if __name__ == "__main__":
    main()
