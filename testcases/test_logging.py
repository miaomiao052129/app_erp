import logging
import pytest
logger = logging.getLogger(__name__)
# 设置级别 + 增加输出
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)

student1 = 1
student2 = 3
student3 = student1 + student2

logger.info(student3)
