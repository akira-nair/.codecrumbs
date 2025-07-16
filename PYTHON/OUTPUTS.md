
## Automatic Output Folder
Set an output folder based on datetime.
```python
import os
from datetime import datetime

def create_output_directory(path):
    """
    Create the output directory if it does not exist.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = os.path.join(path, f"NAME_{timestamp}")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir
    
```

## Logging
Logging is just a better version of print, allowing for real-time monitoring of scripts and adjustment of types of messages coming out of the program.

```python
import logging

logging.basicConfig(
    filename=f'path/to/output.log', 
    filemode='w',
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s')
```