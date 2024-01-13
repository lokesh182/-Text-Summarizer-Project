from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationPipeline

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

STAGE_NAME_03 = "Data Transformation Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME_03} started <<<<<<")
    data_transformation= DataTransformationPipeline()
    data_transformation.main()
    logger.info(f">>>>>> stage {STAGE_NAME_03} completed <<<<<\n\nX==========X")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME_04 = "Model Trainer Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME_04} started <<<<<<")
    model_trainer= ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>> stage {STAGE_NAME_04} completed <<<<<\n\nX==========X")
except Exception as e:
    logger.exception(e)
    raise e