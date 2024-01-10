import os
from box.exceptions import BoxValueError 
import yaml #

from src.textSummarizer.logging import logger
from ensure import ensure_annotations 
from box import ConfigBox 
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    '''
    reads yaml file and return
    Args:
    path_to_yaml(str) : path like input
    
    Raises:
    ValueError:if yaml file is empty
    e:empty file
    
    Returns:
    ConfigBox:ConfigBox Type
    '''
    
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml:{path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml File is empty")
    except Exception as e:
        raise e
    
@ensure_annotations   
def create_directories(path_to_directories:list,verbose=True):
    """
    create list of directories
    
    Args:
    Path_to_directories(list) :list of path of directories
    ignore_log(bool,optional): ignore if multiple dirs is to be created.Default to false
    """
    
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Created Directory:{path}")
            
@ensure_annotations
def get_size(path:Path) -> str:
    """
    get size in KB
    
    ARGS:path(Path): path of the file
    
    Returns:
    str:size in KB
    """
    
    Size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{Size_in_kb} KB"