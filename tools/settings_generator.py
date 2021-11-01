#   This file is part of Item List.

#   Item List is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   Item List is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with Item List.  If not, see <https://www.gnu.org/licenses/>.

import json

settings = {
    "language": "System",
    "theme": "Default"
}

with open("settings.json", "w", encoding="UTF-8") as settingsfile:
    json.dump(settings, settingsfile)