idDict = dict()

def solution(record):
    answer = []
    logList = []
    for e in record:
        dataList = e.split(" ")
        if dataList[0] == "Leave":
            logList.append([dataList[1], "님이 나갔습니다."])
        elif dataList[0] == "Enter":
            idDict[dataList[1]] = dataList[2]
            logList.append([data[1], "님이 들어왔습니다."])
        elif dataList[0] == "Change":
            idDict[dataList[1]] = dataList[2]

    print(logList)
    # 저장은 id + 나갔 or 들어 로 log를 저장한 후, idDict과 logList를 이용해서 answer로 출력 시 id->nickname
    for log in logList:
        answer.append(idDict[log[0]] + log[1])
    return answer

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict["brand"] = "Change"
print(thisdict)
