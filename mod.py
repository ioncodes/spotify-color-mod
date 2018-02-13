import os

for root, dirs, files in os.walk("Apps/"):
	for file in files:
		if file.endswith(".css"):
			path = os.path.join(root, file)
			print("Editing %s" % path)
			with open(path, "r+") as f:
				data = f.read()
				data = data.replace('#1ed760', '#E91E63') # sidebar, ...
				data = data.replace('#1db954', '#D81B60') # links, ...
				data = data.replace('#18ac4d', '#C2185B') # ??? (prob controls, slider, etc)
				data = data.replace('#1cd85e', '#E91E63') # btn #1
				data = data.replace('#179443', '#C2185B') # btn #1 active
				data = data.replace('#1df369', '#F06292') # not active, ...?
				data = data.replace('#87dc5a', '#C2185B') # ??? strange green
				f.seek(0)
				f.write(data)
				f.truncate()
