import speech_recognition
from gtts import gTTS
import playsound
from datetime import datetime
import os
import wikipedia
import time

robot_ear = speech_recognition.Recognizer()
now = datetime.now()

def speak(text):

	tts = gTTS(text=text, lang='vi', tld='com.vn')
	filename = 'voice.mp3'
	tts.save(filename)
	playsound.playsound(filename)	
	# nếu bạn muốn xử dụng mixer
	# mixer.init()
	# mixer.music.load(filename)
	# mixer.music.play()

	# while mixer.music.get_busy():
	# 	time.sleep(0.1)
	# if os.path.exists(filename):

	os.remove(filename)
	print("\n")
def PrintText(text):
	for i in text:
		print(i, end="", flush=True)
		time.sleep(0.04)

while True:
	with speech_recognition.Microphone() as mic:
		robot_ear.adjust_for_ambient_noise(mic)
		PrintText("Robot: Tôi đang nghe")
		audio =robot_ear.record(mic, duration=5)

	try:
		you = robot_ear.recognize_google(audio, language="vi")
	except:
		you = ""

	print("\nYou: " + you)

	PrintText("Robot: ...")
	time.sleep(1)

	if you == "":
		robot_brain = "Tôi không nghe thấy bạn nói gì, hãy thử lại nhé"
		print("\nRobot: " + robot_brain)
		speak(robot_brain)
	elif "ngày" in you or "day" in you:
		robot_brain = now.strftime("Hôm nay là ngày %d tháng %m năm %Y")
		print("\nRobot: " + robot_brain)
		speak(robot_brain)
	elif "giờ" in you or "time" in you:
		robot_brain = now.strftime("%H:%M:%S")
		print("\nRobot: " + robot_brain)
		speak(robot_brain)
	elif "tổng thống Mỹ" in you or "Tổng thống Mỹ" in you:
		robot_brain = "Joe Biden là tổng thống Mỹ"
		print("\nRobot: " + robot_brain)
		speak(robot_brain)
	elif "Goodbye" in you or "bye" in you or "tạm biệt" in you:
		robot_brain = "Bye bye Mai Toàn đẹp trai"
		print("\nRobot: " + robot_brain)
		speak(robot_brain)
		break
	elif "Hello" in you or "Xin chào" in you or "Chào" in you:
		robot_brain = "Xin chào Mai Toàn đẹp trai"
		print("\nRobot: " + robot_brain)
		speak(robot_brain)
	elif "Bạn" in you or "you" in you:
		robot_brain = "Tôi khỏe, còn bạn thì sao"
		print("\nRobot: " + robot_brain)
		speak(robot_brain)
	elif you:
		try:
			wikipedia.set_lang("vi")
			robot_brain = wikipedia.summary(you, sentences=1)
			print("\nRobot: " + robot_brain)
			speak(robot_brain)
		except wikipedia.exceptions.PageError:
			robot_brain = "Tôi không hiểu bạn nói gì, hãy thử lại nhé"
			print("\nRobot: " + robot_brain)
			speak(robot_brain)
		except wikipedia.exceptions.DisambiguationError as e:
			robot_brain = "Có quá nhiều kết quả trùng khớp, hãy cung cấp thông tin cụ thể hơn."
			print("\nRobot: " + robot_brain)
			speak(robot_brain)