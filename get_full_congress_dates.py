import json
from datetime import datetime, date

with open("congress-begin-end-dates.json", "r") as ofile:
	json_data = json.loads(ofile.read())
ofile.close()



# puts data into keys based on congress
congresses = {}

for item in json_data:
	try:
		congresses[item["Congress"]].append(item)
	except:
		congresses[item["Congress"]] = [item]
	
congress_dates = []


new_century = True

# adds full years to dates after 1900

for key, val in congresses.items():
	for item in val:
		d = {}
		for date_type in ["Adjourn Date", "Begin Date"]:
			date_split = item[date_type].split("/")
			print(item[date_type])
			try:
				if date_split[2][0] == "9":
					new_century = False
			except:
				pass
			if new_century == True:
				year_prefix = "20"
			else:
				year_prefix = "19"
			try:
				item[date_type] = date_split[0] + "/" + date_split[1]  + "/" + year_prefix + date_split[2]
			except:
				pass
		print(item)


		# adjourn_split = item["Adjourn Date"].split("/")
		# begin_split = item["Begin Date"].split("/")
		# if new_century == True:
		# 	item["Adjourn Date"] =  adjourn_split[0] + "/" + adjourn_split[1] + "20" + adjourn_split[2]
		# 	item["Begin Date"] =  adjourn_split[0] + "/" + adjourn_split[1] + "20" + adjourn_split[2]
		# print(item["Adjourn Date"])
		# print(item["Begin Date"])





for key, val in congresses.items():
	# iterate through items in value and figure out if bigger than max or smaller than min date, then if so store as a variable
	d = {}
	d["congress"] = key
	d["begin_date"] = ""
	d["end_date"] = ""
	for item in val:
		d["begin_date"]
		if d["begin_date"] == []:
			d["begin_date"] = item["Begin Date"]
			d["end_date"] = item["Adjourn Date"]
		else:
			# print(item["Adjourn Date"])
			try:
				begin_date = datetime.strptime(item["Begin Date"], "%m/%d/%Y")
			except:
				begin_date = datetime.strptime(item["Begin Date"], "%b %d, %Y")
			try:
				end_date = datetime.strptime(item["Adjourn Date"], "%m/%d/%Y")
			except:
				try:
					end_date = datetime.strptime(item["Adjourn Date"], "%b %d, %Y")
				except:
					pass
			# print(begin_date)
			# try:
			# 	print(end_date)
			# except:
			# 	print("No end date")
			# print()




		# print(item["Begin Date"])
	congress_dates.append(d)