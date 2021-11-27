#
"""                                                                           
        +=================================================================\ 
        |\    \\\\\\\  \\     \\  \\\\\\\  \\            \\     \\\\\\     \    
        | \    \\       \\     \\  \\       \\          \\  \\   \\    \\   \   
        |  \    \\\\\\\  \\     \\  \\       \\         \\\\\\\\  \\\\\\     \  
        |   \         \\  \\     \\  \\       \\        \\     \\  \\  \\     \ 
        |    \   \\\\\\\\  \\\\\\\\\  \\\\\\\  \\\\\\\\  \\     \\  \\    \\   \    
        +     \=================================================================\   
"""
import re


class Docu_set:
    # Basic property
    file_address = ""
    #file_name = ""
    raw = ""


    def __init__(self,addr):
        self.file_address = addr
    
    def opener(self):
        #TODO:get raw
        with open(self.file_address):
            pass
        self.raw = ""
        pass
        yield self.raw    
    
    def extractor(self):
        p1 = re.compile(r"\d+\s*人")
        #p2 = re.compile()
        p3 = re.compile(r"(\d+)(?#序号)\s+(\S+)(?#姓名)\s+(\S+)(?#性别)\s+(\d+[年\.\s]\d+[月\.\s]\d*[日]*)(?#申请入党日期)\s+(\S+)(?#职务)\s+(\d+\s*[/／]\s*\d+)(?#投票详情)\s+(\S)(?#投票结果)")

        r1 = re.findall(p1,self.raw) #List
        #r2    
        r3 = re.findall(p3,self.raw)# Return tuples in a list
        
        
        #====================================  1
        toll = []    
        for element in r1:
            toll.append(eval(element[:-1]))
        self.dict_Toll = {
                "团员总数":toll[0],
                "党员":toll[1],
                "预备党员":toll[2],
                "非团员":toll[3],
                "已上交入党申请书":toll[4],
                "应出席":toll[5],
                "实出席":toll[6],
                "请假":toll[7]
                }
        yield self.dict_Toll
        #=====================================  2




        #=====================================  3
        self.poll_Info = []
        for tup in r3:
            dict = {
            "姓名":tup[1],
            "性别":tup[2],
            "申请入党日期":tup[3],
            "职务":tup[4],
            "投票详情":tup[5],
            "投票结果":[6]
                    }
            self.poll_Info.append(dict)
        yield self.poll_Info

    def checker():
        #TODO:
        pass
    
    