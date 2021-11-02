#   This file is part of Item List.

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

from os import path
import locale
import json

class Language:
    def Get():
        # Parsing settings file
        with open("settings.json", "r", encoding="UTF-8") as settingsfile:
            settings = json.load(settingsfile)

        # Checking language and language file then loading the file
        if settings["language"] == "System":
            system_language = locale.getdefaultlocale()[0]

            if path.isfile("langs/{}.json".format(system_language)):
                with open("langs/{}.json".format(system_language), "r", encoding="UTF-8") as langfile:
                    language = json.load(langfile)
            else:
                print("[Warning] {}.json language file is missing, using en_US instead.".format(system_language))

                with open("langs/en_US.json", "r", encoding="UTF-8") as langfile:
                    language = json.load(langfile)
        else:
            if path.isfile("langs/{}.json".format(settings["language"])):
                with open("langs/{}.json".format(settings["language"]), "r", encoding="UTF-8") as langfile:
                    language = json.load(langfile)
            else:
                print("[Warning] {}.json language file is missing, using en_US instead.".format(settings["language"]))
                
                with open("langs/en_US.json", "r", encoding="UTF-8") as langfile:
                    language = json.load(langfile)

        return language
