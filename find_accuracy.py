import os

f=open('/model_files/output.txt')
content=f.read()
accuracy=int(content[-47:-45])
print("Accuracy is ",accuracy)
if accuracy < 80:
	print("Accuracy is less than 80 Running Hyper Parameter File")
	os.system("python3 /model_files/tuning_script.py")
else:
	print("Just got the Accuracy Greater Than 80 [Accuracy :- {}]".format(accuracy))

