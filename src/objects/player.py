import game_constants.py
class Player(object):
	def __init__(self, id, name, IPSNode):
		#int
		self.id = id;
		self.IPSNode = IPSNode;
		#string
		self.name = name;

    def portScan(self, start):
        #start is the node to start port scan
