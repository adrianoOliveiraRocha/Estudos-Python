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

	@staticmethod
	def init():
		import sqlite3
		try:
			conn = sqlite3.connect('/home/adriano/python/pygit/en-phrases/db/ep.db')
			c = conn.cursor()
			c.execute("update phrase set checked=0")
			conn.commit()
			conn.close()
			
		except Exception as e:
			print(e)

            
	@staticmethod
	def getAllPhrases():
		try:
			import sqlite3
			conn = sqlite3.connect('/home/adriano/python/pygit/en-phrases/db/ep.db')      
			c = conn.cursor()
			c.execute("""select * from phrase""")
			rows = c.fetchall() 
			conn.commit()
			conn.close()
			return [None, rows]
		except Exception as e:
			print(e)
			return [False, e]

	@staticmethod
	def getOnePhrase():
		try:
			import sqlite3
			conn = sqlite3.connect('/home/adriano/python/pygit/en-phrases/db/ep.db')      
			c = conn.cursor()
			c.execute("""
             	select rowid, phrase  
             	from phrase 
              	where checked=0
               	order by rowid asc limit 1""")
			phrase = c.fetchone() 
			print(phrase[1])
			if phrase[1] is None:
				raise Exception("You don't have a phrase")
			conn.commit()
			conn.close()
			return [None, phrase]
		except Exception as e:
			return [False, e]

	@staticmethod
	def markAsChecked(id):
		try:
			import sqlite3
			conn = sqlite3.connect('/home/adriano/python/pygit/en-phrases/db/ep.db')
			c = conn.cursor()
			c.execute("""update phrase set checked = 1
             	where rowid = {}""".format(id))
			conn.commit()
			conn.close()
		except Exception as e:
			print(e)

 
		