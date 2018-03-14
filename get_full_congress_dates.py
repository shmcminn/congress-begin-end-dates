import json
from datetime import datetime, date

with open("congress-begin-end-dates.json", "r") as ofile:
	json_data = json.loads(ofile.read())
ofile.close()
	
congress_dates = []



# puts data into keys based on congress
congresses = {}

for item in json_data:
	try:
		congresses[item["Congress"]].append(item)
	except:
		congresses[item["Congress"]] = [item]




# adds full years to dates after 1900

new_century = True

for key, val in congresses.items():
	for item in val:
		d = {}
		for date_type in ["Adjourn Date", "Begin Date"]:
			date_split = item[date_type].split("/")
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


for key, val in congresses.items():
	# iterate through items in value and figure out if bigger than max or smaller than min date, then if so store as a variable
	d = {}
	d["congress"] = key
	d["begin_date"] = ""
	d["end_date"] = ""
	for item in val:
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
				end_date = ""
				pass

		if d["begin_date"] == "":
			d["begin_date"] = begin_date
		elif begin_date < d["begin_date"]:
			d["begin_date"] = begin_date	

		if d["end_date"] == "" and type(end_date) != str:
  			d["end_date"] = end_date
		elif end_date > d["end_date"]:
			d["end_date"] = end_date

	if key == max(list(congresses.keys())):
		d["end_date"] = ""


	congress_dates.append(d)

for item in congress_dates:
	print(item)