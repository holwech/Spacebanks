class User:
	def __init__(self,userid,funding_permission):
		self.userid = userid
		self.funding_permission = funding_permission
		self.fundings = []

	def add_funding(self,funding):
		self.fundings.append(funding)

class Funding:
	def __init__(self,status,time_ack,time_expired,funding_type,funding_id):
		self.status = status
		self.time_ack = time_ack
		self.time_expired = time_expired #self.add_time(time_ack,funding_type.duration)
		self.funding_type = funding_type
		self.funding_id = funding_id

	def add_time(self,time,add_time):
		#return time+add_time
		return 1

class Funding_type:
	def __init__(self,name,amount,permission_type,duration):
		self.name = name
		self.amount = amount
		self.permission_type = permission_type
		self.duration = duration # in days