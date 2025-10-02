class Solution:
    def checkStatus(self, a, b, flag):
       
        

        condition_1 = (
           ((a>=0)^(b>=0)) and (not flag)
        )


        condition_2= (
            (a<0) and (b<0) and flag
        )

        return condition_1 or condition_2
