class ICC:
    def rules(self):
        print("ICC : International Cricket Rules")
        
class BCCI(ICC):
    def domestic(self):
        print("BCCI: Controls Cricket in India")
    
class IPL(BCCI):
    def league(self):
        print("IPL: Professional T20 League")
        

ipl = IPL()       # Creating object of IPL

ipl.rules()
ipl.domestic()
ipl.league()
