class Day1:
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

    def findDistance(self, list1, list2) -> int:
        list1.sort()
        list2.sort()
        totalDistance = 0
        for i in range(len(list1)):
            totalDistance += abs(list1[i] - list2[i])
        return totalDistance

    def calculateDistance(self) -> int:
        return self.findDistance(self.leftList, self.rightList)
