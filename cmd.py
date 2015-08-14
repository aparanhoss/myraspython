class Cmd:
	#Addres to send
	end=None
	#instruction
	cmd=None
	#intruction complemnet if necessary
	comple=None
	
	def __init__(self,end,cmd,*args):
		self.end=end
		self.cmd=cmd
		self.comple=args
	
	def printCmd(self):
		tmp=format(self.end,'02x')+format(self.cmd,'02x')
		for i in self.comple:
			tmp+=format(i,'02x')
		print(tmp)
	def getSize(self):
		return len(self.comple)+6
		

#c=Cmd(0xff,0x30,0x00,0x01)
#c.printCmd()