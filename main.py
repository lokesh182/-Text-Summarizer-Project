from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.components.data_ingestion import DataIngestion 
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<\n\nX==========X")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME_02 = "Data Validation Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME_02} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME_02} completed <<<<<\n\nX==========X")
except Exception as e:
    logger.exception(e)
    raise e