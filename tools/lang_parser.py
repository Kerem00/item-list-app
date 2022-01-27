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

import json

lang_en = {
    "columnItem": "Item",
    "columnComment": "Comment",
    "menuFile": "File",
    "menuEdit": "Edit",
    "menuSettings": "Settings",
    "menuHelp": "Help",
    "actionPreferences": "Preferences",
    "actionAbout": "About",
    "actionImport": "Import",
    "actionExport": "Export",
    "actionQuit": "Quit",
    "actionAdd": "Add",
    "actionEdit": "Edit",
    "actionRemove": "Remove",
    "alreadyInDatabase": "Already in database.",
    "emptyText": "File name or comment can't be empty.",
    "selectSomethingToEdit": "Select something to edit.",
    "selectSomethingToRemove": "Select something to remove.",
    "language": "Language",
    "theme": "Theme"
}

lang_tr = {
    "columnItem": "Öğe",
    "columnComment": "Açıklama",
    "menuFile": "Dosya",
    "menuEdit": "Düzenle",
    "menuSettings": "Ayarlar",
    "menuHelp": "Yardım",
    "actionPreferences": "Tercihler",
    "actionAbout": "Hakkında",
    "actionImport": "İçe aktar",
    "actionExport": "Dışa aktar",
    "actionQuit": "Çıkış",
    "actionAdd": "Ekle",
    "actionEdit": "Düzenle",
    "actionRemove": "Kaldır",
    "alreadyInDatabase": "Veritabanında zaten var.",
    "emptyText": "Dosya adı veya açıklama boş bırakılamaz.",
    "selectSomethingToEdit": "Düzenlenecek bir şey seçin.",
    "selectSomethingToRemove": "Kaldırılacak bir şey seçin.",
    "language": "Dil",
    "theme": "Tema"
}

with open("en_US.json", "w", encoding="UTF-8") as langfile: json.dump(lang_en, langfile)
with open("tr_TR.json", "w", encoding="UTF-8") as langfile: json.dump(lang_tr, langfile)