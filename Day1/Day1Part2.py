class Day2:
    def __init__(self):
        self.leftList = []
        self.rightList = []
        self.loadData()

    def loadData(self):
        try:
            with open('../Data/Day1Input.txt', 'r') as file:
                for line in file:
                    splitline = line.split('   ')
                    self.leftList.append(int(splitline[0]))
                    self.rightList.append(int(splitline[1]))
        except FileNotFoundError:
            print("File Not Found")
        except Exception as e:
            print(f"Error loading data: {e}")

    def findSimScore(self,list1,list2) -> int:
        similarity = 0
        list1.sort()
        list2.sort()
        for i in range(len(list1)):
            similarity += list1[i] * list2.count(list1[i])
        return similarity

    def calculateSimScore(self) -> int:
        return self.findSimScore(self.leftList,self.rightList)