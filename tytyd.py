from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys, json, time

class Start:
	def __init__(self):
		self.PATH = 'C:\Program Files\chromedriver.exe'
		self.browser = webdriver.Chrome(self.PATH)
		self.browser.implicitly_wait(3600)
		self.browser.get('https://colab.research.google.com/notebooks/intro.ipynb')

	def Login(self, email, password):
		elem = self.browser.find_element_by_link_text('Sign in')
		elem.click()
		log_username = self.browser.find_element_by_name('identifier')
		log_username.send_keys(email)
		log_username.send_keys(Keys.ENTER)
		log_pass = self.browser.find_element_by_name('password')
		log_pass.send_keys(password)
		log_pass.send_keys(Keys.ENTER)
		return 'Success Logged in ..'

	def Connect(self, values=None):
		self.con = None
		if self.ReconnectCheck:
			self.con.send_keys(Keys.ENTER)

		self.con = self.browser.find_element_by_xpath("//colab-connect-button")
		if self.con.text == 'Reconnect' or self.con.text == 'Connect':
			self.con.click()
			while True:
				time.sleep(1)
				if 'Connected' in self.con.text:
					return 'Logged In Success :)'
				sys.stdout.write('{}{}\r'.format(self.con.text, ' '*25))
				sys.stdout.flush()
		else:
			return 'Running ..'

	@property
	def Sign_Check(self):
		try:
			elem = self.browser.find_element_by_link_text('Sign in')
			return True
		except:
			return False

	@property
	def ReconnectCheck(self):
		try:
			self.con = self.browser.find_element_by_id('ok')
			return True
		except:
			return False

	def ConCheck(self):
		con = self.browser.find_element_by_xpath('//colab-connect-button')
		return con.text

	def Run(self):
		if self.Sign_Check:
			with open('data.json', 'r') as f:
				data = f.read()
				obj = json.loads(data)
				data = obj['data-sign']
			acc = self.Login(data['email'], data['password'])
			if 'Success' in acc:
				self.browser.get('https://colab.research.google.com/drive/1921HTGy5u7BrNj2ljBzkfc-cmpJeIUPV')
				while True:
					time.sleep(1)
					Check = self.ConCheck()
					if Check != 'Busy':
						sys.stdout.write('{}{}\r'.format(self.Connect(Check), ' '*25))
						sys.stdout.flush()
					else:
						print('Server Already Running')
						sys.exit()
				

	
if __name__ == '__main__':
	Start().Run()
	