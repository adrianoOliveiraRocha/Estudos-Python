class Phrase:
	def __init__(self, phrase):
		self.phrase = phrase
	
	def save(self):
		import sqlite3
		try:
			conn = sqlite3.connect('/home/adriano/python/pygit/en-phrases/db/ep.db')
			c = conn.cursor()
			c.execute("""INSERT INTO phrase (phrase) 
             values('{}')""".format(self.phrase))
			conn.commit()
			conn.close()
			return True
		except Exception as e:
			print(e)
			return False
		