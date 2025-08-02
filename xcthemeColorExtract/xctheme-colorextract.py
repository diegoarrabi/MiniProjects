import json
import os
import uuid
from collections import UserDict
from datetime import datetime
from typing import TypedDict

from bs4 import BeautifulSoup


class ColorData(TypedDict):
	hex: str
	red: float
	green: float
	blue: float
	alpha: float
	tags: list
	createdAt: str
	updatedAt: str
	group: str
	uuid: str
	name: str
	originalName: str


# MARK: - ColorTheme Class
class ColorTheme(UserDict):
	def __init__(self, themepath: str):
		super().__init__()
		self.name = self.__themeName(themepath)
		self.colors = []
		self.uuid = str(uuid.uuid4()).upper()
		self.time = self.getTime()
		self.__extractColors(themepath)
		self.theme_data = self.__makeTheme()

	def printTheme(self):
		themedata = self.theme_data.items()
		for key, value in themedata:
			print(key)

	def getTime(self) -> str:
		return f"{datetime.now().replace(microsecond=0).isoformat()}Z"

	def __themeName(self, path: str) -> str:
		"""
		Checks if file exists and if it is a '.xccolortheme'; throws error if neither
		Returns the name of the file
		"""
		if not os.path.isfile(path):
			raise ValueError(f"{path}\n\tis not a file")
		if not path.endswith(".xccolortheme"):
			raise ValueError(f"{path}\n\tFile must end in '.xccolortheme'")
		themename, _ = os.path.splitext(os.path.basename(path))
		return themename

	# MARK: - extractColors
	def __extractColors(self, path: str):
		with open(path, "r") as openFile:
			content = openFile.read()

		xml_content = BeautifulSoup(content, "xml")
		all_tags = xml_content.find_all("string")

		for tag in all_tags:
			tag_string = tag.get_text()

			if not tag_string[0].isnumeric():
				continue

			key_element = tag.find_previous("key")
			if not key_element:
				continue
			key_string = key_element.get_text()

			# NON SYNTAX COLORS
			nonsyntaxstrings = [
				"SourceText",
				"DVT",
				"Color",
			]

			if nonsyntaxstrings[0] in key_string:
				for substr in nonsyntaxstrings:
					key_string = key_string.replace(substr, "")
				self.__addColor(key_string, tag_string)

			# SYNTAX COLORS
			if "xcode.syntax." in key_string:
				key_string = key_string.replace("xcode.syntax.", "").capitalize()
				self.__addColor(key_string, tag_string)

	# MARK: - addColor

	def __addColor(self, colorname: str, nscolor: str):
		"""
		Convert NSColor RGB components (0 0 1 0) to hex
		"""

		def __intIfOne(number: float):
			if number == 1:
				return int(number)
			return number

		nscolor_split = nscolor.split(" ")
		if len(nscolor_split) == 3:
			nscolor_split.append(1)

		red, green, blue, alpha = map(float, nscolor_split)

		r = int(red * 255)
		g = int(green * 255)
		b = int(blue * 255)
		hex_str = f"{r:02X}{g:02X}{b:02X}"
		time_str = self.getTime()

		color_data: ColorData = {
			"hex": hex_str,
			"red": __intIfOne(red),
			"green": __intIfOne(green),
			"blue": __intIfOne(blue),
			"alpha": __intIfOne(alpha),
			"tags": [],
			"createdAt": time_str,
			"updatedAt": time_str,
			"group": "",
			"uuid": str(uuid.uuid4()).upper(),
			"name": colorname,
			"originalName": colorname,
		}
		self.colors.append(color_data)

	@staticmethod
	def nsColorToHex(nscolor: str) -> str:
		"""
		Convert NSColor RGB components (0 0 1 0) to hex
		"""

		nscolor_split = nscolor.split(" ")
		if len(nscolor_split) == 3:
			nscolor_split.append(1)

		red, green, blue, alpha = map(float, nscolor_split)

		r = int(red * 255)
		g = int(green * 255)
		b = int(blue * 255)
		# a = int(alpha * )
		return f"{r:02X}{g:02X}{b:02X}"

	# MARK: makeTheme
	def __makeTheme(self) -> dict:
		"""
		Constructs Theme dict
		"""
		return {
			"name": self.name,
			"originalName": self.name,
			"createdAt": self.time,
			"updatedAt": self.time,
			"uuid": self.uuid,
			"colors": self.colors,
			"tags": [],
			"isHistory": False,
			"lock": False,
		}

	def to_json(self, filename: str = None, indent: int = 2) -> str:
		"""
		Convert theme data to JSON format

		Args:
		    filename: Optional filename to save JSON to file
		    indent: JSON indentation level for readability

		Returns:
		    JSON string representation of theme data
		"""
		json_string = json.dumps(self.theme_data, indent=indent)

		if filename:
			with open(filename, "w") as f:
				f.write(json_string)
			print(f"Theme saved to: {filename}")

		return json_string

	def save_json(self, savepath: str = None) -> str:
		"""
		Save theme as JSON file with automatic naming

		Args:
		    filename: Optional custom filename

		Returns:
		    Path to saved file
		"""

		# if os.path.isdir(savepath):
		#     safe_name = self.name.replace(" ", "_").replace("(", "").replace(")", "")
		#     filename = f"{safe_name}_theme.palette"
		#     save_path = os.path.join(savepath, filename)
		# else:
		#     exit(print("DIRECTORY PLS"))

		self.to_json(savepath)
		return savepath


# theme_path = "/Users/diegoibarra/Library/Developer/Xcode/UserData/FontAndColorThemes/Presentation (Dark).xccolortheme"
# save_path = os.path.expanduser('~/Downloads')
theme_path = "theme.xccolortheme"
save_path = "generated.palette"

print(ColorTheme.nsColorToHex("0.254416 0.715645 0.269896 1"))
# theme.save_json(save_path)
