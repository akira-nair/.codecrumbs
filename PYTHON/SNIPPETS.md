# Snippets
Press command+shift+p and search configure snippets.

## Python
```json
{
	"HEADER_PY": {
    "prefix": "HEADER",
    "body": [
      "#!/usr/bin/env python",
      "# -*- coding: utf-8 -*-",
      "\"\"\"",
      "",
      "Description",
      "",
      "File        :    ${TM_FILENAME}",
      "Author      :    Akira Nair",
      "Contact     :    akira.nair@pennmedicine.upenn.edu",
      "",
      "\"\"\"",
      ""
    ],
    "description": "Python file header"
  	}
}
```

## R
```json
{
	"HEADER_R": {
    "prefix": "header",
    "body": [
      "######################################################",
      "# Description",
      "#----------------------------------------------------#",
      "# File      :  ${TM_FILENAME}",
      "# Author    :  Akira Nair",
      "# Contact   :  akira.nair@pennmedicine.upenn.edu",
      "######################################################",
      ""
    ],
    "description": "Standard file header"
  	}
}
```