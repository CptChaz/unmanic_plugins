import logging

logger = logging.getLogger(__name__)

def on_library_management_item_completed(*args, **kwargs):
    logger.info("Library management item completed successfully.")
    # Your plugin logic here

def on_task_completed(*args, **kwargs):
    logger.info("Task completed successfully.")
    # Your task completion logic here

