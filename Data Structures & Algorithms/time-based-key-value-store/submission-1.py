class TimeMap:
    """
    ["tM","set",["a","h",1],"get",["a",1]]
    """

    def __init__(self):
       self.timemap=["TimeMap"]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap.append("set")
        self.timemap.append([key,value,timestamp])
    def get(self, key: str, timestamp: int) -> str:
        n=len(self.timemap)-1
        self.timemap.append("get")
        self.timemap.append([key,timestamp])
        for i in range(n,-1,-1):
            if self.timemap[i] == "set":
               if self.timemap[i+1][0] == key and self.timemap[i+1][2]<=timestamp:
                        return self.timemap[i+1][1]
        return ""
                    
        
        
        
